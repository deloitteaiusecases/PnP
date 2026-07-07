"""
rag_pipeline.py — Enterprise RAG Pipeline with Multi-Stage Policy Generation.

Public API (matches app.py imports exactly — do not change signatures):
    ask_question(query)                    → (answer, sources, search_mode)
    generate_policy(user_request)          → (policy_text, sources)
    gap_analysis(current_practices, topic) → (report, sources)
    classify_intent(query)                 → 'qa' | 'generate' | 'gap'

POLICY GENERATION PIPELINE (5 stages):
    Stage 1: Evidence gathering (KB + web)
    Stage 2: Organisational intelligence extraction from KB
    Stage 3: Document plan (outline + regulatory mapping)
    Stage 4: Section-by-section drafting (18 focused LLM calls)
    Stage 5: Assembly into complete document

This produces 25-30 page documents because:
    18 sections × 700 tokens avg = 12,600 tokens output = ~9,450 words = ~30 pages
    vs previous: 1 call × 4,000 tokens = ~10 pages maximum
"""

import os, re, sys, pickle, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

# Generated policy text contains Unicode punctuation (e.g. non-breaking hyphen
# U+2011, en/em dashes, smart quotes). On Windows, stdout defaults to cp1252,
# which cannot encode some of these — so a progress print() carrying that text
# would raise UnicodeEncodeError and abort the whole generation. Force UTF-8 with
# error replacement so logging can never crash the pipeline, on any platform.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import (
    VECTORSTORE_PATH, EMBEDDING_MODEL,
    MODEL_SONNET, MODEL_HAIKU,
    LLM_REASONING_EFFORT, SUPPORT_REASONING_EFFORT,
    TOP_K_RESULTS, ENABLE_WEB_SEARCH, ANTHROPIC_API_KEY,
    SECTION_CONCURRENCY,
)
from prompts import (
    NOT_FOUND_PHRASE,
    KB_QA_PROMPT, KB_TARGETED_EXTRACT_PROMPT, WEB_QA_PROMPT,
    GAP_ANALYSIS_PROMPT,
    INTEL_EXTRACTION_PROMPT,
    PLANNING_PROMPT,
    SECTION_DRAFTING_PROMPT,
    SECTION_GUIDANCE, SECTION_GUIDANCE_MAP,
    POLICY_KEYWORD_LIBRARY,
)

# ── Singletons ────────────────────────────────────────────────────────────────
_embeddings  = None
_vectorstore = None
_all_docs    = []
_bm25        = None

def reset_runtime_caches():
    global _vectorstore, _all_docs, _bm25
    _vectorstore = None
    _all_docs = []
    _bm25 = None

def _get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )
    return _embeddings


def _load_vs() -> bool:
    global _vectorstore, _all_docs, _bm25
    if _vectorstore is not None:
        return True
    p = Path(VECTORSTORE_PATH)
    if not p.exists() or not any(p.iterdir()):
        return False
    try:
        _vectorstore = FAISS.load_local(
            str(p), _get_embeddings(), allow_dangerous_deserialization=True
        )
        pkl = p / "all_docs.pkl"
        if pkl.exists():
            with open(pkl, "rb") as f:
                _all_docs = pickle.load(f)
            from rank_bm25 import BM25Okapi
            _bm25 = BM25Okapi([d.page_content.lower().split() for d in _all_docs])
        return True
    except Exception as e:
        print(f"[rag] VS load error: {e}")
        return False


def _vs_ready():
    return _load_vs()


def warm_up():
    """Eagerly load the embedding model + FAISS/BM25 indexes so the first
    generation doesn't pay the one-time cold-start cost. Safe to call repeatedly
    (the loaders are cached singletons). Called once from app.py at startup."""
    try:
        _get_embeddings()
        _vs_ready()
    except Exception as e:
        print(f"[warmup] skipped: {e}")


# ── Full-document detection & retrieval ───────────────────────────────────────
_FULL_DOC_RE = [
    re.compile(p, re.I) for p in [
        r"\b(full|complete|entire|whole)\s+(policy|procedure|document)\b",
        r"\bshow\s+(the\s+)?[\w\s&/\-]{3,}(policy|procedure)\b",
        r"\bdisplay\s+(the\s+)?[\w\s&/\-]{3,}(policy|procedure)\b",
        r"\bget\s+the\s+[\w\s&/\-]{3,}(policy|procedure)\b",
        r"\bretrieve\s+(the\s+)?[\w\s&/\-]{3,}(policy|procedure)\b",
        r"\bwhat\s+is\s+the\s+[\w\s&/\-]{3,}(policy|procedure)\b",
        r"\bgive\s+(me\s+)?(the\s+)?full\b",
        r"^\s*(the\s+)?[\w\s&/\-]{3,}(policy|procedure)\s*$",
        r"^\s*[\w\s&/\-]{3,}(policy|procedure)\s+please\s*$",
    ]
]
_STOP = {
    "give","show","get","fetch","retrieve","display","provide","send",
    "me","the","a","an","full","complete","entire","whole","please",
    "can","you","what","is","in","for","our","my","your","this","that",
    "all","of","want","need","require",
}


def _is_full_doc_request(q):
    return any(p.search(q) for p in _FULL_DOC_RE)

def _is_explicit_full_doc_request(q: str) -> bool:
    q = q.lower().strip()
    return any(x in q for x in [
        "full policy", "full procedure", "full document",
        "complete policy", "complete procedure", "complete document",
        "entire policy", "entire procedure", "entire document",
        "whole policy", "whole procedure", "whole document",
        "manual", "entire manual","all policies", "all procedures", "all documents",
        "all accounting procedures", "all finance policies","all feedmil procedures",
    ])
   

def _expand_reference_query(query: str) -> str:
    q = query
    ordinals = {
        "first": "1 1st first",
        "second": "2 2nd second",
        "third": "3 3rd third",
        "fourth": "4 4th fourth",
        "fifth": "5 5th fifth",
        "sixth": "6 6th sixth",
        "seventh": "7 7th seventh",
        "eighth": "8 8th eighth",
        "ninth": "9 9th ninth",
        "tenth": "10 10th tenth",
    }
    for word, repl in ordinals.items():
        q = re.sub(rf"\b{word}\b", repl, q, flags=re.I)
    return q

def _is_targeted_subsection_request(query: str) -> bool:
    q = query.lower().strip()

    explicit_full = _is_explicit_full_doc_request(q)
    if explicit_full:
        return False

    has_doc_word = any(x in q for x in [
        "policy", "procedure", "policy statement", "procedures"
    ])

    asks_specific_part = any(re.search(p, q) for p in [
        r"\bpolicy\s+for\b",
        r"\bprocedure\s+for\b",
        r"\bpolicy\s+statement\s+for\b",
        r"\bwhat\s+is\s+the\s+policy\s+for\b",
        r"\bwhat\s+is\s+the\s+procedure\s+for\b",
        r"\bsection\b",
        r"\bclause\b",
        r"\bpoint\b",
        r"\bstep\b",
        r"\bfirst\b", r"\bsecond\b", r"\bthird\b", r"\bfourth\b", r"\bfifth\b",
        r"\b1st\b", r"\b2nd\b", r"\b3rd\b", r"\b4th\b", r"\b5th\b",
        r"\b1\.\b", r"\b2\.\b", r"\b3\.\b", r"\b4\.\b", r"\b5\.\b",
        r"\btable\b", r"\bmatrix\b", r"\braci\b", r"\bkpi\b", r"\bkpis\b",
        r"\bmetric\b", r"\bmetrics\b",
    ])

    # normal policy/procedure targeted asks
    if has_doc_word and asks_specific_part:
        return True

    # title-style policy/procedure asks like "give me information security policy"
    if has_doc_word and re.search(r"\b(give|show|get|fetch|display|provide|send)\s+me\b", q):
        return True

    # KPI / table extraction even without the words policy/procedure
    if asks_specific_part and any(x in q for x in [
        "classification", "data classification", "data quality", "metadata",
        "forecast", "planning", "security", "onboarding"
    ]):
        return True

    return False

def _kws(q):
    return [w for w in re.sub(r"[^\w\s]","",q.lower()).split()
            if w not in _STOP and len(w) > 2]


def _normalize_match_text(text: str) -> str:
    text = re.sub(r"[_\W]+", " ", (text or "").lower())
    return re.sub(r"\s+", " ", text).strip()

def _score_full_doc(query: str, doc) -> float:
    q_norm = _normalize_match_text(query)
    q_words = {
        w for w in q_norm.split()
        if len(w) > 2 and w not in {"policy", "procedure", "document", "the"}
    }

    source = _normalize_match_text(doc.metadata.get("source", ""))
    document_title = _normalize_match_text(doc.metadata.get("document_title", ""))
    document_view = _normalize_match_text(doc.metadata.get("document_view", "full"))
    content_head = _normalize_match_text(doc.page_content[:5000])

    exact_phrase = 0.0
    if q_norm and (q_norm in source or q_norm in document_title or q_norm in content_head):
        exact_phrase += 10.0

    overlap_source = len(q_words & set(source.split()))
    overlap_title = len(q_words & set(document_title.split()))
    overlap_head = len(q_words & set(content_head.split()))

    view_bonus = 0.0
    if "body" in document_view:
        view_bonus += 1.0

    policy_bonus = 0.0
    if "policy" in q_norm and "policy" in content_head:
        policy_bonus += 2.0
    if "procedure" in q_norm and "procedure" in content_head:
        policy_bonus += 2.0

    return exact_phrase + (overlap_source * 1.5) + (overlap_title * 2.0) + (overlap_head * 1.0) + view_bonus + policy_bonus

def _get_full_document(query):
    if not _vs_ready() or not _all_docs:
        return None, []

    ql = query.lower()
    wants_admin = any(x in ql for x in [
        "document control", "revision history", "abbreviations", "acronyms",
        "appendix", "annexure", "annex", "full document", "entire document", "complete document"
    ])

    preferred_view = "full" if wants_admin else "body"

    full_docs = [
        d for d in _all_docs
        if str(d.metadata.get("is_full_document", "false")).lower() == "true"
        and d.metadata.get("document_view", "full").lower() == preferred_view
    ]

    if not full_docs:
        full_docs = [
            d for d in _all_docs
            if str(d.metadata.get("is_full_document", "false")).lower() == "true"
        ]

    if not full_docs:
        return None, []

    ranked = sorted(full_docs, key=lambda d: _score_full_doc(query, d), reverse=True)
    best = ranked[0]
    best_score = _score_full_doc(query, best)

    if best_score < 2.5:
        return None, []

    return best.metadata.get("source", ""), [best]

# ── Hybrid FAISS + BM25 search ────────────────────────────────────────────────

def _normalize_query_with_library(query: str) -> str:
    q = query.lower()

    expanded_terms = set()
    expanded_terms.add(query)

    query_words = q.split()

    for canonical, synonyms in POLICY_KEYWORD_LIBRARY.items():

        # check canonical too
        if canonical.lower() in q:
            expanded_terms.add(canonical)
            expanded_terms.update(synonyms)

        # check every synonym word
        for syn in synonyms:

            syn_words = syn.lower().split()

            # partial keyword matching
            for qw in query_words:
                for sw in syn_words:

                    if qw in sw or sw in qw:
                        expanded_terms.add(canonical)
                        expanded_terms.update(synonyms)

    return " ".join(expanded_terms)

def _search_kb(query, k=TOP_K_RESULTS):
    if not _vs_ready():
        return "", []

    ql = query.lower()

    def allow_doc(doc):
        is_full = str(doc.metadata.get("is_full_document", "false")).lower() == "true"
        if is_full:
            return False

        priority = doc.metadata.get("section_priority", "normal").lower()
        kind = doc.metadata.get("section_kind", "core").lower()

        if priority == "low":
            allow_low = any(x in ql for x in [
                "definition", "definitions", "acronym", "acronyms", "abbreviation",
                "appendix", "appendices", "annex", "form", "document control", "revision history"
            ])
            if not allow_low:
                return False

        if kind == "toc":
            return False

        return True
    normalized_query = _normalize_query_with_library(query)
    faiss_docs = [d for d in _vectorstore.similarity_search(normalized_query, k=k * 3)
                if allow_doc(d)]

    bm25_docs = []
    if _bm25 and _all_docs:
        try:
            scores = _bm25.get_scores(normalized_query.lower().split())
            top_idxs = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k * 5]
            bm25_docs = [_all_docs[i] for i in top_idxs if scores[i] > 0 and allow_doc(_all_docs[i])]
        except Exception:
            pass

    seen, merged = set(), []
    for doc in faiss_docs + bm25_docs:
        uid = (
            doc.metadata.get("source", ""),
            doc.metadata.get("section", ""),
            doc.metadata.get("chunk_name", ""),
            doc.page_content[:120],
        )
        if uid not in seen:
            seen.add(uid)
            merged.append(doc)
        #if len(merged) >= k:
            #break
    merged = _rerank_docs(query, merged)[:k]

    parts, sources = [], []
    for doc in merged:
        src = doc.metadata.get("source", "unknown")
        sec = doc.metadata.get("section", "")
        dept = doc.metadata.get("department", "")
        hdr = f"[Source: {src}"
        if dept:
            hdr += f" | Dept: {dept}"
        if sec:
            hdr += f" | Section: {sec}"
        hdr += "]\n"
        parts.append(hdr + doc.page_content)
        if src not in sources:
            sources.append(src)

    return "\n\n---\n\n".join(parts), sources

def _pick_generation_anchor(user_request: str):
    """
    Pick the closest internal policy/procedure source to anchor generation.
    Returns: (anchor_text, anchor_source)
    """
    if not _vs_ready() or not _all_docs:
        return "", ""

    candidates = []
    q_words = set(re.findall(r"\w+", user_request.lower()))

    for d in _all_docs:
        if str(d.metadata.get("is_full_document", "false")).lower() == "true":
            continue

        source = d.metadata.get("source", "")
        section = d.metadata.get("section", "")
        text = d.page_content[:3000]

        score = 0
        score += len(q_words & set(re.findall(r"\w+", source.lower()))) * 2.0
        score += len(q_words & set(re.findall(r"\w+", section.lower()))) * 2.5
        score += len(q_words & set(re.findall(r"\w+", text.lower()))) * 1.0

        if score > 0:
            candidates.append((score, d))

    if not candidates:
        return "", ""

    candidates.sort(key=lambda x: x[0], reverse=True)
    best = candidates[0][1]
    return best.page_content[:5000], best.metadata.get("source", "")

def _rerank_docs(query: str, docs: list):
    q_words = set(re.findall(r"\w+", query.lower()))

    def score(doc):
        text = doc.page_content.lower()
        src = doc.metadata.get("source", "").lower()
        sec = doc.metadata.get("section", "").lower()

        text_words = set(re.findall(r"\w+", text[:2000]))
        src_words = set(re.findall(r"\w+", src))
        sec_words = set(re.findall(r"\w+", sec))

        overlap_text = len(q_words & text_words)
        overlap_src = len(q_words & src_words)
        overlap_sec = len(q_words & sec_words)

        # section/source overlap gets bonus
        return (overlap_text * 1.0) + (overlap_sec * 2.0) + (overlap_src * 1.5)

    return sorted(docs, key=score, reverse=True)

def _has_ctx(ctx):
    return bool(ctx and len(ctx.strip()) > 50)


def _is_not_found(answer):
    al = answer.lower()
    return any(s in al for s in [
        NOT_FOUND_PHRASE.lower(), "not available in the uploaded",
        "not found in the", "no information", "not covered",
        "cannot find", "does not contain", "no relevant information",
    ])


# ── Web search ────────────────────────────────────────────────────────────────
def _search_web(query):
    """
    Web research via Claude's native server-side web_search tool (replaces Tavily).

    Returns: (web_context, web_sources)
      web_context = Claude's concise, web-grounded summary of the query
      web_sources = list of "Title — URL" labels for UI display
    Degrades gracefully to ("", []) on any error or when disabled.
    """
    if not ENABLE_WEB_SEARCH:
        return "", []

    try:
        client = _get_anthropic()
        resp = client.messages.create(
            model=MODEL_SONNET,
            max_tokens=1800,
            system=("Research the user's query using web search and write a concise, "
                    "factual briefing of the key findings. Prefer authoritative and "
                    "recent sources. Do not speculate beyond what the sources support."),
            messages=[{"role": "user", "content": query}],
            tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 4}],
        )

        text_parts, web_sources = [], []
        for block in resp.content:
            btype = getattr(block, "type", "")
            if btype == "text":
                if getattr(block, "text", "").strip():
                    text_parts.append(block.text.strip())
            elif btype == "web_search_tool_result":
                results = getattr(block, "content", None) or []
                if isinstance(results, list):
                    for r in results:
                        url = (getattr(r, "url", "") or "").strip()
                        title = (getattr(r, "title", "") or "").strip()
                        label = f"{title} — {url}" if title and url else (url or title)
                        if label and label not in web_sources:
                            web_sources.append(label)

        return "\n\n".join(text_parts).strip(), web_sources

    except Exception as e:
        # Falls back cleanly (e.g. web search not enabled on the account) — the KB
        # answer still stands; the app just won't have a web supplement.
        print(f"[web] Claude web search unavailable: {e}")
        return "", []

# ── LLM call ──────────────────────────────────────────────────────────────────
def _strip_answer_metadata(text: str) -> str:
    text = re.sub(r"\n\s*\*\*Applicable Policy Sections:\*\*.*$", "", text, flags=re.S)
    text = re.sub(r"\n\s*Applicable Policy Sections:.*$", "", text, flags=re.S)
    text = re.sub(r"\n\s*\*\*Sources:\*\*.*$", "", text, flags=re.S)
    text = re.sub(r"\n\s*Sources:.*$", "", text, flags=re.S)
    return text.strip()

_anthropic_client = None


def _get_anthropic():
    """Singleton Anthropic client (reads ANTHROPIC_API_KEY from config/.env)."""
    global _anthropic_client
    if _anthropic_client is None:
        import anthropic
        _anthropic_client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY or None)
    return _anthropic_client


def _msg_text(message) -> str:
    """Concatenate the text blocks of an Anthropic message into a plain string."""
    return "".join(b.text for b in message.content if getattr(b, "type", "") == "text").strip()


def _call_llm(system, user, model=None, effort=None, max_tokens=4000, high=False):
    """
    Single chokepoint for every runtime LLM call — now backed by Claude.

    model:  MODEL_SONNET (default, quality tier) or MODEL_HAIKU (light tier).
    effort: "low" | "medium" | "high" — Sonnet only (Claude `output_config.effort`).
            Haiku 4.5 does NOT support effort, so it is ignored for that model.
    Thinking is left OFF (disabled) for speed; effort alone controls depth on Sonnet.

    Always streams (messages.stream + get_final_message) so large max_tokens never
    trips the SDK's non-streaming timeout guard. Returns the response text.
    """
    model = model or MODEL_SONNET
    client = _get_anthropic()

    kwargs = {
        "model": model,
        "max_tokens": max_tokens,
        "system": system,
        "messages": [{"role": "user", "content": user}],
    }
    # Effort + explicit thinking-disabled are Sonnet-tier features. Haiku rejects
    # both, so only attach them for Sonnet.
    if model == MODEL_SONNET:
        kwargs["thinking"] = {"type": "disabled"}
        kwargs["output_config"] = {"effort": (effort or LLM_REASONING_EFFORT)}

    def _run(kw):
        with client.messages.stream(**kw) as stream:
            return _msg_text(stream.get_final_message())

    out = _run(kwargs)

    # Defensive: if a response ever comes back empty, retry once at a lighter setting.
    if not out and model == MODEL_SONNET:
        retry = dict(kwargs)
        retry["output_config"] = {"effort": "low"}
        out = _run(retry)
    return out


def _combine_sources(raw, retrieved):
    combined = list(retrieved)
    for marker in ("Sources Used:", "Sources:", "**Sources:**"):
        if marker in raw:
            for line in raw.split(marker)[-1].splitlines():
                line = line.strip().lstrip("-*•1234567890. **")
                if line and line not in combined:
                    combined.append(line)
            break
    return combined

def _extract_targeted_subsection(query: str):
    search_query = _expand_reference_query(query)
    ql = query.lower()
    if any(x in ql for x in ["kpi", "kpis", "metric", "metrics", "table"]):
        search_query += " KPI KPIs metric metrics table category description threshold target owner frequency"
    ctx, sources = _search_kb(search_query, k=12)

    if not _has_ctx(ctx):
        return None, []

    user_msg = f"""
Context:
{ctx}

User request:
{query}

Return only the requested subsection from the context.
If the user asked for policy only, do not include procedure.
If the user asked for procedure only, do not include policy.
If the user asked for a specific point / clause / step / numbered item, return only that exact requested part.
Preserve wording faithfully and format cleanly in markdown.
"""

    answer = _strip_answer_metadata(
        _call_llm(KB_TARGETED_EXTRACT_PROMPT, user_msg, model=MODEL_HAIKU, max_tokens=8000)
    )

    if _is_not_found(answer):
        return None, []

    return answer, sources

# ══════════════════════════════════════════════════════════════════════════════
# MULTI-STAGE POLICY GENERATION INTERNALS
# ══════════════════════════════════════════════════════════════════════════════

_INTEL_SYSTEM = """You are a document intelligence specialist. Extract structured
organisational facts from policy documents. Be precise. If not found, say "Not found".
Do not invent values."""

_PLANNING_SYSTEM = """You are a Principal Policy Architect at Deloitte Middle East.
Produce precise, actionable document plans for enterprise policy/procedure drafting.
Be specific. Use the organisation's actual terminology."""

_DRAFTING_SYSTEM = """You are a Principal Policy Architect at Deloitte Middle East
with 20 years of experience drafting board-approved policies for regulated organisations.
Write in formal, authoritative, enterprise-grade English.
Every word should justify its presence. No filler. No generic AI language."""

_FINAL_REVIEW_SYSTEM = """You are a Principal Policy Quality Reviewer at Deloitte Middle East.
Refine the draft into a board-ready enterprise policy/procedure.

Keep all substantive content, but improve:
- clarity
- consistency
- professional tone
- section transitions
- duplicate removal
- policy/procedure wording consistency
- removal of awkward AI phrasing

CRITICAL RULES:
- Do not shorten aggressively.
- Do not remove required controls.
- Do not leave unresolved placeholders in the final output.
- Remove any text like: [Industry Standard — validate with management], [TBD], Not found, placeholder notes.
- If an internal governance detail is not supported by KB evidence, rewrite the sentence neutrally instead of guessing.
- Prefer organisation-specific wording from KB over generic consulting language.
- Do not present sectoral frameworks as directly binding unless the draft clearly establishes applicability.
- Convert unsupported approver names, sign-off metadata, document numbers, effective dates, and review dates into neutral controlled-document template wording.
- Remove departments, functions, or governance bodies that appear unrelated to the requested policy topic.
- Preserve explicit user-requested owning department and mandatory support functions even if KB contains different role structures.
"""


def _stage1_extract_org_intel(kb_context: str, anchor_context: str, user_request: str) -> str:
    """Stage 1: Extract org-specific intelligence from KB + closest anchor policy."""
    merged_context = "\n\n=== CLOSEST INTERNAL POLICY ANCHOR ===\n" + (anchor_context or "") + \
                     "\n\n=== BROADER KB CONTEXT ===\n" + (kb_context or "")

    if not _has_ctx(merged_context):
        return "No KB context available."

    prompt = INTEL_EXTRACTION_PROMPT.format(
    user_request=user_request,
    kb_context=merged_context[:9000]
    )
    print("[generate] Stage 1: Extracting organisational intelligence...")
    return _call_llm(_INTEL_SYSTEM, prompt, model=MODEL_SONNET, max_tokens=2500,
                     effort=SUPPORT_REASONING_EFFORT)

def _ensure_minimum_sections(sections: list) -> list:
    """
    Preserve planner-generated section titles.
    Only fill genuinely missing section NUMBERS from the fallback list.
    """
    defaults = {str(d["num"]): d.copy() for d in _default_section_list()}
    merged = {str(s["num"]): s.copy() for s in sections}

    for num, d in defaults.items():
        merged.setdefault(num, d)

    ordered_nums = sorted(int(n) for n in merged.keys())
    out = [merged[str(n)] for n in ordered_nums]

    for i, s in enumerate(out, 1):
        s["num"] = str(i)

    return out

def _stage2_generate_plan(user_request: str, org_intel: str, web_context: str,
                          doc_type: str = None) -> dict:
    """Stage 2: Generate document plan with section outline.

    doc_type: pre-decided 'Policy' | 'Procedure' (from the AI router). When given,
    the planner is told the type up front so it builds the right section set and
    can't hedge to a hybrid 'Policy and Procedure' label.
    """
    prompt = PLANNING_PROMPT.format(
        user_request=user_request,
        org_intel=org_intel,
        web_context=web_context[:3000] if web_context else "No web context available.",
    )
    if doc_type:
        forced = _normalize_doc_type(doc_type)
        prompt = (f"DOCUMENT TYPE (already decided — DO NOT change, DO NOT hedge): {forced}\n"
                  f"Build the {forced} section structure exactly. Set DOCUMENT_TYPE: {forced}.\n\n"
                  + prompt)
    print("[generate] Stage 2: Generating document plan...")
    raw_plan = _call_llm(_PLANNING_SYSTEM, prompt, model=MODEL_SONNET, max_tokens=4000,
                         effort=SUPPORT_REASONING_EFFORT)

    # Parse the plan
    plan = {}
    for line in raw_plan.split("\n"):
        line = line.strip()
        if line.startswith("DOCUMENT_TITLE:"):
            plan["title"] = line.split(":", 1)[1].strip()
        elif line.startswith("DOCUMENT_TYPE:"):
            plan["type"] = line.split(":", 1)[1].strip()
        elif line.startswith("DOCUMENT_NUMBER:"):
            plan["number"] = line.split(":", 1)[1].strip()
        elif line.startswith("DEPARTMENT:"):
            plan["department"] = line.split(":", 1)[1].strip()
        elif line.startswith("DOCUMENT_OWNER:"):
            plan["owner"] = line.split(":", 1)[1].strip()
        elif line.startswith("APPROVAL_AUTHORITY:"):
            plan["approver"] = line.split(":", 1)[1].strip()
        elif line.startswith("PRIMARY_KSA_REGULATIONS:"):
            plan["regulations"] = line.split(":", 1)[1].strip()

    # Parse sections from the plan
    sections = []
    in_sections = False
    for line in raw_plan.split("\n"):
        line = line.strip()
        if line == "SECTIONS:":
            in_sections = True
            continue
        if in_sections:
            if line.startswith("CRITICAL_REQUIREMENTS:") or not line:
                if not line: continue
                in_sections = False
                continue
            # Parse "N. Title | Scope description"
            m = re.match(r"^(\d+)\.\s+(.+?)\s*\|\s*(.+)$", line)
            if m:
                sections.append({
                    "num":   m.group(1),
                    "title": m.group(2).strip(),
                    "scope": m.group(3).strip(),
                })

    # Fallback if parsing failed — use standard section list
    if len(sections) < 8:
        sections = _default_section_list()
    else:
        sections = _ensure_minimum_sections(sections)

    # Force the router's decision if provided; always normalise to strictly
    # POLICY/PROCEDURE so a hybrid label can never propagate downstream.
    plan["type"] = _normalize_doc_type(doc_type or plan.get("type"), default="POLICY")

    if plan["type"] == "POLICY":
        sections = _remove_procedure_sections_for_policy(sections)
    else:  # PROCEDURE — drop policy-only sections (execution-focused output)
        sections = _remove_policy_sections_for_procedure(sections)

    plan["sections"]     = sections
    plan["raw"]          = raw_plan
    plan["user_request"] = user_request
    req_org = _parse_intel(org_intel, "Requested organisation", "Not found")
    req_dept = _parse_intel(org_intel, "Requested primary department", "Not found")
    req_owner = _parse_intel(org_intel, "Requested document owner", "Not found")
    req_approver = _parse_intel(org_intel, "Requested approval authority", "Not found")

    if req_dept.lower() != "not found":
        plan["department"] = req_dept
    if req_owner.lower() != "not found":
        plan["owner"] = req_owner
    if req_approver.lower() != "not found":
        plan["approver"] = req_approver
    if req_org.lower() != "not found":
        plan["title"] = plan.get("title", "").replace("the organisation", req_org).replace("Organisation", req_org)
    plan.setdefault("title",    "Policy Document")
    plan.setdefault("type",     "POLICY")
    plan.setdefault("number",   "To be completed before approval and issue")
    plan.setdefault("department", "Not Found")
    plan.setdefault("owner",    "Not Found")
    plan.setdefault("approver", "Not Found")
    plan.setdefault("regulations", "As applicable per KSA regulatory framework")

    return plan


def _default_section_list():
    """Fallback section list if plan parsing fails."""
    return [
        {"num": "1",  "title": "Document Control and Revision History",        "scope": "Document metadata and revision log"},
        {"num": "2",  "title": "Executive Summary",                            "scope": "Board-level overview of policy purpose and obligations"},
        {"num": "3",  "title": "Purpose and Objectives",                       "scope": "Business rationale, regulatory drivers, measurable objectives"},
        {"num": "4",  "title": "Scope and Applicability",                      "scope": "In-scope entities, exclusions, third-party applicability"},
        {"num": "5",  "title": "Regulatory and Compliance Framework",          "scope": "Applicable KSA laws and international standards"},
        {"num": "6",  "title": "Definitions and Abbreviations",                "scope": "Technical and regulatory terms used in this document"},
        {"num": "7",  "title": "Policy Statements — Governance and Risk",      "scope": "Mandatory governance and risk management policy rules"},
        {"num": "8",  "title": "Policy Statements — Operational Requirements", "scope": "Operational obligations and data management rules"},
        {"num": "9",  "title": "Policy Statements — Data and Third Party",     "scope": "Data handling and outsourcing policy rules"},
        {"num": "10", "title": "Roles, Responsibilities, and RACI Matrix",     "scope": "Governance structure, role matrix, RACI"},
        {"num": "11", "title": "Operational Procedures — Standard Workflow",   "scope": "Step-by-step primary process with SLAs and decision points"},
        {"num": "12", "title": "Operational Procedures — Exceptions and Escalation", "scope": "Exception handling, emergency process, escalation matrix"},
        {"num": "13", "title": "Controls, Approvals, and Authority Matrix",    "scope": "Key controls, approval authorities, segregation of duties"},
        {"num": "14", "title": "Key Performance Indicators and Monitoring",    "scope": "Measurable KPIs with targets, monitoring programme"},
        {"num": "15", "title": "Records Management and Data Retention",        "scope": "Records inventory with retention periods citing KSA regulations"},
        {"num": "16", "title": "Breach, Non-Compliance, and Consequences",     "scope": "Breach classification, reporting obligations, disciplinary action"},
        {"num": "17", "title": "Training, Awareness, and Competency",          "scope": "Training requirements by audience, competency assessment"},
        {"num": "18", "title": "Internal Audit and Policy Review",             "scope": "Audit programme, management actions, review governance"},
        {"num": "19", "title": "Related Documents and Approval Sign-Off",      "scope": "Related policies, regulatory references, approval table"},
    ]

def _remove_procedure_sections_for_policy(sections: list) -> list:
    """
    For POLICY documents, remove workflow/procedure-only sections
    so the output remains policy-first.
    """
    procedure_titles = {
        "Operational Procedures — Standard Workflow",
        "Operational Procedures — Exceptions and Escalation",
    }

    filtered = [s for s in sections if s["title"] not in procedure_titles]

    for i, s in enumerate(filtered, 1):
        s["num"] = str(i)

    return filtered


def _remove_policy_sections_for_procedure(sections: list) -> list:
    """
    For PROCEDURE documents, remove policy-only / governance sections — these state
    obligations, intent, and policy administration rather than execution, and belong
    in the parent policy, not the step-by-step procedure. Matched by title (robust to
    planner wording):
        Executive Summary, Scope & Applicability, Regulatory & Compliance Framework,
        Policy Statements (Governance / Operational / Data & Third Party),
        Breach/Non-Compliance & Consequences, Training/Awareness/Competency,
        Internal Audit & Policy Review, Related Documents & Approval Sign-Off.
    Note: the Word exporter still appends a Revision History + Approval block to every
    document, so dropping the Sign-Off section here does not lose the approval table.
    Execution-focused sections stay: Document Control, Purpose, Definitions, RACI,
    Standard Workflow, Exceptions & Escalation, Controls/Approvals/Authority, KPIs,
    Records Management.
    """
    def _is_policy_only(title: str) -> bool:
        t = (title or "").lower()
        return (
            "executive summary" in t
            or "scope" in t                      # Scope and Applicability
            or "regulatory" in t                 # Regulatory and Compliance Framework
            or "policy statement" in t           # Policy Statements — Governance/Operational/Data
            or "breach" in t or "non-compliance" in t or "consequence" in t
            or "training" in t or "awareness" in t or "competency" in t
            or "audit" in t or "policy review" in t          # Internal Audit and Policy Review
            or "related" in t or "sign-off" in t or "sign off" in t  # Related Docs + Sign-Off
        )

    filtered = [s for s in sections if not _is_policy_only(s["title"])]
    for i, s in enumerate(filtered, 1):
        s["num"] = str(i)
    return filtered


def _guidance_key_for_title(title: str):
    """Map a section title to its SECTION_GUIDANCE key by content, NOT by number.

    Numbers shift when sections are pruned/renumbered, so identifying a section by
    its title is the only stable way to pick the right drafting guidance. Order is
    most-specific-first. Returns None if nothing matches (caller falls back)."""
    t = (title or "").lower()
    if "document control" in t or "revision history" in t:
        return "Document Control"
    if "executive" in t:
        return "Executive Summary"
    if "purpose" in t or "objective" in t:
        return "Purpose and Objectives"
    if "scope" in t or "applicability" in t:
        return "Scope and Applicability"
    if "regulatory" in t or "compliance framework" in t:
        return "Regulatory and Compliance Framework"
    if "definition" in t or "abbreviation" in t:
        return "Definitions and Abbreviations"
    if "policy statement" in t and ("data" in t or "third party" in t):
        return "Policy Statements Data and Third Party"
    if "policy statement" in t and ("operational" in t or "requirement" in t):
        return "Policy Statements Operational"
    if "policy statement" in t:                       # governance/risk or generic
        return "Policy Statements Governance"
    if "raci" in t or "roles" in t or "responsibilit" in t:
        return "Roles and RACI"
    if "workflow" in t:
        return "Operational Procedures Standard"
    if "exception" in t or "escalation" in t:
        return "Operational Procedures Exceptions"
    # 'related / sign-off' before 'approval' — "Related Documents and Approval
    # Sign-Off" must not be captured by the Controls/Approval rule.
    if "related" in t or "sign-off" in t or "sign off" in t:
        return "Governance and Related Docs"
    if "control" in t or "authority" in t or "approval" in t:
        return "Controls and Authority"
    if "kpi" in t or "performance" in t or "monitoring" in t:
        return "KPIs and Monitoring"
    if "records" in t or "retention" in t:
        return "Records Management"
    if "breach" in t or "non-compliance" in t or "consequence" in t:
        return "Breach and Non-Compliance"
    if "training" in t or "awareness" in t or "competency" in t:
        return "Training and Competency"
    if "audit" in t or "policy review" in t:
        return "Internal Audit"
    return None


def _stage3_draft_section(
    section: dict,
    plan: dict,
    org_intel: str,
    web_context: str,
    section_kb: str,
) -> str:
    """Stage 3: Draft one section using focused LLM call."""

    title = section["title"]
    sec_num = str(section.get("num", "")).strip()
    doc_type = str(plan.get("type", "POLICY")).upper()

    # 1) Prefer section-number-based mapping over fuzzy title matching
    if doc_type == "POLICY":
        number_map = {
            "1": "Document Control",
            "2": "Executive Summary",
            "3": "Purpose and Objectives",
            "4": "Scope and Applicability",
            "5": "Regulatory and Compliance Framework",
            "6": "Definitions and Abbreviations",
            "7": "Policy Statements Governance",
            "8": "Policy Statements Operational",
            "9": "Policy Statements Data and Third Party",
            "10": "Roles and RACI",
            "11": "Controls and Authority",
            "12": "KPIs and Monitoring",
            "13": "Records Management",
            "14": "Breach and Non-Compliance",
            "15": "Training and Competency",
            "16": "Internal Audit",
            "17": "Governance and Related Docs",
        }
    else:
        number_map = {
            "1": "Document Control",
            "2": "Executive Summary",
            "3": "Purpose and Objectives",
            "4": "Scope and Applicability",
            "5": "Regulatory and Compliance Framework",
            "6": "Definitions and Abbreviations",
            "7": "Policy Statements Governance",
            "8": "Policy Statements Operational",
            "9": "Policy Statements Data and Third Party",
            "10": "Roles and RACI",
            "11": "Operational Procedures Standard",
            "12": "Operational Procedures Exceptions",
            "13": "Controls and Authority",
            "14": "KPIs and Monitoring",
            "15": "Records Management",
            "16": "Breach and Non-Compliance",
            "17": "Training and Competency",
            "18": "Internal Audit",
            "19": "Governance and Related Docs",
        }

    # Identify the section by its TITLE first (stable across pruning/renumbering),
    # then fall back to the legacy number map for anything the title resolver misses.
    guidance_key = _guidance_key_for_title(title) or number_map.get(sec_num)

    # 2) Only if both fail, try exact/soft title matching against the guidance map
    if not guidance_key:
        for pattern, key in SECTION_GUIDANCE_MAP.items():
            if pattern.lower() in title.lower() or title.lower() in pattern.lower():
                guidance_key = key
                break

    # 3) Narrow fallback matching — remove the over-broad "audit" catch-all
    if not guidance_key:
        tl = title.lower()
        if "document control" in tl or "revision history" in tl:
            guidance_key = "Document Control"
        elif "executive" in tl:
            guidance_key = "Executive Summary"
        elif "purpose" in tl or "objective" in tl:
            guidance_key = "Purpose and Objectives"
        elif "scope" in tl or "applicability" in tl:
            guidance_key = "Scope and Applicability"
        elif "regulatory" in tl or "compliance framework" in tl:
            guidance_key = "Regulatory and Compliance Framework"
        elif "definition" in tl or "abbreviation" in tl:
            guidance_key = "Definitions and Abbreviations"
        elif "raci" in tl or "roles" in tl or "responsibilities" in tl:
            guidance_key = "Roles and RACI"
        elif "workflow" in tl:
            guidance_key = "Operational Procedures Standard"
        elif "exception" in tl or "escalation" in tl:
            guidance_key = "Operational Procedures Exceptions"
        elif "control" in tl or "authority" in tl or "approval" in tl:
            guidance_key = "Controls and Authority"
        elif "kpi" in tl or "performance" in tl or "monitoring" in tl:
            guidance_key = "KPIs and Monitoring"
        elif "records" in tl or "retention" in tl:
            guidance_key = "Records Management"
        elif "breach" in tl or "non-compliance" in tl or "consequence" in tl:
            guidance_key = "Breach and Non-Compliance"
        elif "training" in tl or "awareness" in tl or "competency" in tl:
            guidance_key = "Training and Competency"
        elif "policy review" in tl or "internal audit and policy review" in tl:
            guidance_key = "Internal Audit"
        elif "related" in tl or "sign-off" in tl:
            guidance_key = "Governance and Related Docs"

    specific_guidance = SECTION_GUIDANCE.get(
        guidance_key,
        f"Write a complete, professional section covering: {section['scope']}"
    )
    specific_guidance = specific_guidance.replace("{section_num}", section["num"])
    specific_guidance = specific_guidance.replace("{section_title}", section["title"])
    specific_guidance = specific_guidance.replace("{doc_title}", plan.get("title", "Policy Document"))
    

    # Force domain-native writing behavior for custom section titles
    specific_guidance = (
        f'This section title is "{title}". '
        f'Use subheadings that naturally fit this exact title and this policy domain. '
        f'Do not fall back to generic headings like Governance / Operational / Data unless they genuinely fit this section.\n\n'
        + specific_guidance
    )

    # For a PROCEDURE's standard-workflow section, also emit a Graphviz flowchart of
    # the steps. The frontend renders the ```dot block as a live diagram and the Word
    # exporter renders it to an embedded image (a Visio-style flowchart). Other
    # sections get no diagram.
    # Robust to planner label drift: match procedure-ish types by substring
    # ("PROCEDURE", "SOP") rather than exact equality, so a label like
    # "Standard Operating Procedure" or "Procedure — Storage Forecasting" still triggers.
    _is_proc = ("PROCEDURE" in doc_type) or ("SOP" in doc_type)
    wants_flowchart = _is_proc and (
        guidance_key == "Operational Procedures Standard" or "workflow" in title.lower()
    )
    if wants_flowchart:
        specific_guidance += (
            "\n\nFLOWCHART REQUIREMENT (mandatory for this section):\n"
            "After the written content, add a subheading '### Process Flowchart' and then a\n"
            "Graphviz DOT **horizontal swimlane** diagram of the end-to-end workflow above,\n"
            "inside a fenced code block that starts with ```dot and ends with ```.\n"
            "STRICT DOT RULES (swimlane layout):\n"
            "- Begin with: digraph workflow { rankdir=LR; compound=true; "
            "node [fontname=\"Arial\" fontsize=10]; graph [fontname=\"Arial\"];\n"
            "- ONE swimlane per responsible role. Put each role's steps in a cluster:\n"
            "  subgraph cluster_<role> { label=\"<Role Name>\"; style=filled; color=\"#F2F5FA\"; "
            "fontsize=11; <that role's step nodes> }\n"
            "- Assign every step node to the cluster of the role that performs it (mirror the\n"
            "  Responsible Role column). Flow runs left→right across the lanes in step order.\n"
            "- Process steps: shape=box; decision points: shape=diamond; Start/End: shape=oval.\n"
            "- Sequence the steps with edges S1 -> S2 -> S3 ...; label decision branches on the\n"
            "  edge, e.g. D3 -> S4 [label=\"Proceed\"].\n"
            "- Keep node labels short (max ~6 words, e.g. \"Step 4: Trend analysis\").\n"
            "- Output ONLY valid DOT inside the fence — no prose, no markdown, no comments.\n"
            "- Close every subgraph brace and the graph with a single closing brace."
        )

    # Parse org intel into components
    org_type     = _parse_intel(org_intel, "Org type", "Not found")
    key_roles    = _parse_intel(org_intel, "Key role titles", "Not found")
    gov_bodies   = _parse_intel(org_intel, "Governance bodies", "Not found")
    primary_regs = plan.get("regulations", "As applicable per KSA regulatory framework")
    requested_org = _parse_intel(org_intel, "Requested organisation", "Not found")
    requested_department = _parse_intel(org_intel, "Requested primary department", "Not found")
    requested_owner = _parse_intel(org_intel, "Requested document owner", "Not found")
    requested_approver = _parse_intel(org_intel, "Requested approval authority", "Not found")
    requested_roles = _parse_intel(org_intel, "Requested mandatory roles", "Not found")
    requested_requirements = _parse_intel(org_intel, "Requested mandatory requirements", "Not found")

    prompt = SECTION_DRAFTING_PROMPT.format(
        doc_title=plan.get("title", "Policy Document"),
        doc_type=plan.get("type", "POLICY"),
        doc_number=plan.get("number", "POL-001"),
        org_type=org_type,
        key_roles=key_roles,
        governance_bodies=gov_bodies,
        requested_org=requested_org,
        requested_department=requested_department,
        requested_owner=requested_owner,
        requested_approver=requested_approver,
        requested_roles=requested_roles,
        requested_requirements=requested_requirements,
        primary_regs=primary_regs,
        section_num=sec_num,
        section_title=title,
        section_scope=section["scope"],
        section_kb_context=section_kb[:4500] if section_kb else "No specific KB content for this section.",
        web_context=web_context[:1500] if web_context else "No web context available.",
        section_specific_guidance=specific_guidance,
        user_request=plan.get("user_request", ""),
    )

    # The workflow section also carries a DOT flowchart, so give it extra headroom.
    # Drafting is the quality-critical stage → Sonnet at HIGH effort.
    return _call_llm(_DRAFTING_SYSTEM, prompt, model=MODEL_SONNET, effort=LLM_REASONING_EFFORT,
                     max_tokens=6500 if wants_flowchart else 5000)

def _parse_intel(org_intel: str, key: str, default: str) -> str:
    """Extract a value from the org intel string."""
    for line in org_intel.split("\n"):
        if line.strip().lower().startswith(key.lower() + ":"):
            val = line.split(":", 1)[1].strip()
            if val and val.lower() not in ("not found", "n/a", "unknown"):
                return val
    return default


def _stage4_assemble(sections_content: list, plan: dict) -> str:
    """Stage 4: Assemble all sections into final document."""
    lines = []

    # Document title
    lines.append(f"# {plan.get('title', 'Policy Document')}")
    lines.append("")

    # Stitch all drafted sections
    for content in sections_content:
        if content and content.strip():
            lines.append(content.strip())
            lines.append("")

    return "\n".join(lines)

def _extract_section_headings(text: str) -> list[str]:
    return re.findall(r"(?m)^##\s+\d+\.\s+.+$", text)

def _restore_section_headings(text: str, sections: list) -> str:
    """
    If final review strips markdown hashes from section headings,
    restore them so export/parser still treats them as real sections.
    """
    mapping = {
        f"{s['num']}. {s['title']}".strip().lower(): f"## {s['num']}. {s['title']}"
        for s in sections
    }

    out = []
    for line in text.splitlines():
        stripped = line.strip()
        key = stripped.lower()
        if key in mapping:
            out.append(mapping[key])
        else:
            out.append(line)
    return "\n".join(out)


# ── Procedure workflow flowchart: shield from review + guarantee presence ──────
_DOT_BLOCK_RE = re.compile(r"```(?:dot|graphviz)\s*(.*?)```", re.S | re.I)


def _extract_dot_block(text: str):
    """Return (first_dot_source_or_None, text_with_all_dot_blocks_removed)."""
    blocks = _DOT_BLOCK_RE.findall(text)
    first = blocks[0].strip() if blocks else None
    cleaned = _DOT_BLOCK_RE.sub("", text)
    return first, cleaned


def _clean_dot(dot: str):
    """Normalise a DOT string; return None if it isn't a usable graph."""
    if not dot:
        return None
    d = dot.strip()
    d = re.sub(r"^```(?:dot|graphviz)?", "", d).strip()
    d = re.sub(r"```$", "", d).strip()
    return d if ("digraph" in d or "graph" in d) else None


def _find_workflow_section(plan: dict):
    """(num, title) of the standard-workflow section, else (None, None).

    Robust to planner label drift. A flowchart is warranted whenever the document
    is procedure-ish (type contains PROCEDURE/SOP) OR — the most reliable signal —
    it actually has a section whose title contains 'workflow'. Policies don't carry
    workflow sections, so keying off the section's presence can't mis-fire on them.
    """
    secs = plan.get("sections", [])
    t = str(plan.get("type", "POLICY")).upper()
    is_proc = ("PROCEDURE" in t) or ("SOP" in t)

    wf = next((s for s in secs if "workflow" in s["title"].lower()), None)
    if wf is not None:
        return str(wf["num"]), wf["title"]          # workflow section present → use it
    if is_proc:
        for s in secs:                               # procedure with no 'workflow' title
            if str(s["num"]) == "11":                #   → fall back to the §11 slot
                return "11", s["title"]
    return None, None


def _generate_flowchart_dot(section_text: str) -> str:
    """Dedicated focused call: build a horizontal swimlane Graphviz DOT flowchart
    (lanes grouped by responsible role) from a procedure section's text."""
    sys_p = (
        "You convert a procedure's written workflow into a Graphviz DOT horizontal "
        "swimlane diagram. Output ONLY valid Graphviz DOT — no prose, no markdown "
        "fences, no comments."
    )
    user_p = (
        "Build a HORIZONTAL SWIMLANE flowchart of the workflow steps below — one lane "
        "per responsible role, flow running left to right.\n"
        "RULES:\n"
        '- Start with: digraph workflow { rankdir=LR; compound=true; '
        'node [fontname="Arial" fontsize=10]; graph [fontname="Arial"];\n'
        "- ONE subgraph cluster per responsible role:\n"
        '  subgraph cluster_<role> { label="<Role Name>"; style=filled; color="#F2F5FA"; '
        'fontsize=11; <that role\'s step nodes> }\n'
        "- Put each step in the cluster of the role that performs it (use the Responsible "
        "Role column). Steps flow left to right in order.\n"
        "- Process steps: shape=box; decisions: shape=diamond; start/end: shape=oval.\n"
        '- Sequence with edges S1 -> S2 -> ...; label decision branches, e.g. D -> S [label="Yes"].\n'
        "- Keep labels short (max ~6 words). Close every cluster brace and the graph.\n\n"
        f"WORKFLOW SECTION:\n{section_text[:4000]}"
    )
    raw = _call_llm(sys_p, user_p, model=MODEL_SONNET, max_tokens=1800,
                    effort=SUPPORT_REASONING_EFFORT)
    m = _DOT_BLOCK_RE.search(raw)
    return _clean_dot(m.group(1) if m else raw)


def _insert_flowchart(text: str, sec_num: str, sec_title: str, dot: str) -> str:
    """Append a '### Process Flowchart' + DOT block at the END of the given section."""
    # Drop any now-empty Process Flowchart subheadings so we never double up.
    text = re.sub(r"(?im)^#{2,4}\s*Process Flowchart\s*$\n?", "", text)
    block = f"\n### Process Flowchart\n\n```dot\n{dot}\n```\n"
    lines = text.split("\n")

    head_re = re.compile(rf"^##\s+{re.escape(sec_num)}\.\s", re.I)
    start = next((i for i, ln in enumerate(lines) if head_re.match(ln.strip())), None)
    if start is None:
        start = next((i for i, ln in enumerate(lines)
                      if ln.strip().startswith("##") and sec_title.lower() in ln.lower()), None)
    if start is None:
        return text.rstrip() + "\n" + block

    end = next((j for j in range(start + 1, len(lines))
                if re.match(r"^##\s+\d+\.", lines[j].strip())), len(lines))
    return "\n".join(lines[:end] + [block] + lines[end:])

def _stage5_final_review_safe(complete_document: str, plan: dict) -> str:
    """
    Final review is allowed to polish, but not allowed to drop sections.
    If reviewed output loses sections, fall back to the assembled draft.
    """
    reviewed = _stage5_final_review(complete_document, plan)
    reviewed = _restore_section_headings(reviewed, plan.get("sections", []))

    draft_heads = _extract_section_headings(complete_document)
    reviewed_heads = _extract_section_headings(reviewed)

    if len(reviewed_heads) < len(draft_heads):
        return complete_document

    return reviewed

def _stage5_final_review(complete_document: str, plan: dict) -> str:
    """Final quality pass for enterprise tone and coherence."""
    review_prompt = f"""
Document Title: {plan.get('title', 'Policy Document')}
Document Type: {plan.get('type', 'POLICY')}

Review and improve the following draft so it reads like a polished enterprise-grade
policy/procedure for executive, compliance, legal, and operational review.

Requirements:
- preserve all material obligations and controls
- remove repetition
- improve transitions between sections
- make wording more formal and board-ready
- ensure the document consistently uses the correct term:
  {plan.get('type', 'POLICY')}
- do not add unsupported claims
- do not remove sections
- do not replace explicit user-requested organisation names, departments, or role ownership with unrelated KB-derived roles
- preserve user-requested ownership and operating model where explicitly stated
- remove governance bodies, committee names, and role titles that appear to have leaked from unrelated KB source documents; if not clearly supported, rewrite neutrally
- replace unsupported controlled-document metadata with neutral issuance-template wording rather than invented values
- remove leaked role titles or functions that are not explicitly requested by the user and not clearly supported by KB evidence
- do not state CMA, SAMA, NCA, PDPL, or other frameworks as directly binding unless the user request, section topic, or KB clearly supports applicability
- if a regulator/framework is used only as a benchmark, rewrite the wording to say "where applicable" or "as a best-practice benchmark"
- if a sign-off, approval, review date, document number, or controlled-document field is unsupported, rewrite it as neutral issuance-template wording instead of leaving a fake precise value

ORIGINAL USER REQUEST:
{plan.get('user_request', '')}

DRAFT:
{complete_document}
"""
    return _call_llm(_FINAL_REVIEW_SYSTEM, review_prompt, model=MODEL_SONNET, max_tokens=16000,
                     effort=SUPPORT_REASONING_EFFORT)

# ══════════════════════════════════════════════════════════════════════════════
# CONVERSATIONAL CLARIFICATION (intake) — used by app.py before generate / gap
# ══════════════════════════════════════════════════════════════════════════════
_CLARIFY_SYSTEM = """You are a senior policy & procedure consultant scoping a {kind}
before it is drafted. Your goal is to ask the SINGLE most valuable clarifying question
that will most improve how tailored and accurate the final output is.

Prioritise high-value specifics that are still MISSING from the request and prior answers:
- Organisation / entity name
- Owning department or business function
- Document owner and approval authority
- Jurisdiction / regulatory scope (assume KSA unless the user says otherwise)
- Target audience; in-scope and out-of-scope entities
- Topic-specific specifics a real expert would need for THIS topic
  (e.g. thresholds, triggers, systems, accrual rules, risk tiers)

RULES:
- Output exactly ONE concise question. No preamble, no numbering, no commentary.
- Make it specific to THIS request and adapt to answers already given.
- Never ask about anything already provided in the request or prior answers.
- If the request plus prior answers already contain enough to draft a strong, tailored
  {kind}, reply with exactly: DONE
- Prefer DONE over asking a low-value or redundant question.
"""

_ENRICH_SYSTEM = """You are a policy & procedure scoping specialist. Combine the user's
original request and the clarifying Q&A into ONE detailed, unambiguous specification brief
that will be handed to a drafting pipeline.

RULES:
- Preserve EVERY specific the user provided (organisation, department, owner, approver,
  roles, requirements, scope, jurisdiction, thresholds) verbatim as authoritative constraints.
- Do NOT invent facts, names, numbers, or requirements the user did not provide.
- Where the user deferred or did not answer, write "not specified — use KSA best-practice
  default" instead of guessing a specific value.
- Write a clear drafting brief, not a conversation transcript.
- Keep the user's original intent and topic central.
"""


def _clarify_kind(mode: str) -> str:
    return "compliance gap analysis" if mode == "gap" else "policy/procedure document"


def _format_qa_history(qa_history: list) -> str:
    if not qa_history:
        return "(no questions asked yet)"
    return "\n\n".join(
        f"Q: {qa.get('question', '')}\nA: {qa.get('answer', '')}" for qa in qa_history
    )


def clarify_next_question(mode: str, original_request: str, qa_history: list) -> str:
    """
    Ask the next clarifying question for a generate/gap request.
    Returns the question text, or "" when no further questions are needed (DONE).
    qa_history: list of {"question": str, "answer": str}
    """
    kind = _clarify_kind(mode)
    user_msg = (
        f"REQUEST TO SCOPE ({kind}):\n{original_request}\n\n"
        f"CLARIFYING Q&A SO FAR:\n{_format_qa_history(qa_history)}\n\n"
        "Ask the single most valuable next question, or reply DONE if you have enough."
    )
    resp = _call_llm(_CLARIFY_SYSTEM.format(kind=kind), user_msg, model=MODEL_HAIKU, max_tokens=800).strip()

    cleaned = resp.strip().strip('"').strip()
    if cleaned.upper().startswith("DONE") or cleaned.upper().rstrip(".!").strip() == "DONE":
        return ""
    # strip accidental leading numbering / bullet markers
    cleaned = re.sub(r"^\s*(?:\d+[\.\)]|[-*•])\s*", "", cleaned).strip()
    return cleaned


def build_enriched_request(mode: str, original_request: str, qa_history: list) -> str:
    """
    Synthesize the original request + clarifying Q&A into a single detailed spec brief.
    Falls back to the original request if there were no answers.
    """
    if not qa_history:
        return original_request
    kind = _clarify_kind(mode)
    user_msg = (
        f"DOCUMENT TYPE: {kind}\n\n"
        f"ORIGINAL REQUEST:\n{original_request}\n\n"
        f"CLARIFYING Q&A:\n{_format_qa_history(qa_history)}\n\n"
        "Produce the consolidated specification brief now."
    )
    enriched = _call_llm(_ENRICH_SYSTEM, user_msg, model=MODEL_HAIKU, max_tokens=3000).strip()
    return enriched or original_request


# ══════════════════════════════════════════════════════════════════════════════
# PUBLIC API — imported by app.py
# ══════════════════════════════════════════════════════════════════════════════
def classify_intent(query: str) -> str:
    """Returns 'qa' | 'generate' | 'gap'"""
    q = query.lower().strip()

    # Gap analysis first
    if any(t in q for t in [
        "gap analysis", "gap analyse", "current practice", "current process",
        "we currently", "our current", "compare our", "what are we missing",
        "am i compliant", "are we compliant", "compliance check",
    ]):
        return "gap"

    # Explicit retrieval / ask-for-document should stay QA
    retrieval_patterns = [
        r"\b(give|show|get|fetch|retrieve|display|provide|send)\s+me\b",
        r"\bwhat\s+is\s+the\b",
        r"\b(policy|procedure)\b",
    ]
    if any(re.search(p, q) for p in retrieval_patterns) and not re.search(
        r"\b(create|draft|write|generate|make|prepare|build)\b", q
    ):
        return "qa"

    # Generation should only trigger on WHOLE WORDS, not substrings
    generate_verbs = r"\b(create|draft|write|generate|make|prepare|build)\b"
    doc_terms = r"\b(policy|procedure|standard|sop)\b"

    if re.search(generate_verbs, q) and re.search(doc_terms, q):
        return "generate"

    return "qa"


def _normalize_doc_type(s: str, default: str = "POLICY") -> str:
    """Collapse any free-form type label to strictly 'POLICY' or 'PROCEDURE'.

    Kills hybrid labels like 'Policy and Procedure' that the planner sometimes
    emits — those used to satisfy neither the POLICY nor the PROCEDURE branch and
    left the document mislabelled (no flowchart, wrong section set). When a label
    contains both words, prefer PROCEDURE (the execution-focused intent wins, since
    a hybrid request is almost always 'how do we do X')."""
    s = (s or "").upper()
    has_proc = "PROCEDURE" in s or "SOP" in s or "WORKFLOW" in s
    has_pol  = "POLICY" in s
    if has_proc:
        return "PROCEDURE"
    if has_pol:
        return "POLICY"
    return default.upper()


_CLASSIFY_SYSTEM = """You are an intent router for an enterprise policy & procedure assistant.
Classify the user's request into exactly one INTENT and (when generating) one DOCUMENT_TYPE.

INTENT:
- "generate": the user wants a NEW document written (policy, procedure, process, standard, SOP, manual).
  Verbs like create/draft/write/generate/prepare/build/make, or just naming a document to produce.
- "gap": the user wants their CURRENT practices compared against policy / best practice
  (gap analysis, compliance check, "what are we missing", "are we compliant").
- "qa": the user is ASKING a question or asking to retrieve/show existing content.

DOCUMENT_TYPE (only meaningful when intent = "generate"; otherwise default "policy"):
- "procedure": HOW work is executed — step-by-step workflow, process, SOP, who-does-what,
  sequences, controls in practice. Words like process, procedure, workflow, steps, "how to", SOP.
- "policy": WHAT/WHY — rules, obligations, intent, scope, governing principles, standards.
  Words like policy, rules, standard, governance, obligations.
A request for a "process" is a PROCEDURE. If a request mixes both, choose "procedure" when it is
primarily about execution, otherwise "policy". Never answer "policy and procedure" — pick one."""


def classify_request(query: str, has_practices: bool = False) -> tuple:
    """LLM-based intent + document-type router (replaces brittle keyword matching).

    Returns (intent, doc_type) where intent ∈ {qa, generate, gap} and
    doc_type ∈ {Policy, Procedure}. Uses a fast Haiku call with structured JSON
    output; on ANY failure falls back to the regex `classify_intent` so the app
    never hard-depends on the model for routing.
    """
    # Regex fallback values (used if the model call fails).
    fb_intent = classify_intent(query)
    if has_practices and fb_intent == "qa":
        fb_intent = "gap"
    ql = (query or "").lower()
    fb_type = "Procedure" if (("procedure" in ql or "process" in ql or "workflow" in ql or "sop" in ql)
                              and "policy" not in ql) else "Policy"

    try:
        client = _get_anthropic()
        schema = {
            "type": "object",
            "properties": {
                "intent": {"type": "string", "enum": ["qa", "generate", "gap"]},
                "document_type": {"type": "string", "enum": ["policy", "procedure"]},
            },
            "required": ["intent", "document_type"],
            "additionalProperties": False,
        }
        user = (f"Request: {query}\n"
                f"A current-practices document is attached: {bool(has_practices)}")
        resp = client.messages.create(
            model=MODEL_HAIKU,
            max_tokens=200,
            system=_CLASSIFY_SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_config={"format": {"type": "json_schema", "schema": schema}},
        )
        import json as _json
        data = _json.loads(_msg_text(resp))
        intent = data.get("intent", fb_intent)
        doc_type = "Procedure" if data.get("document_type") == "procedure" else "Policy"
        # An attached practices doc strongly implies gap analysis.
        if has_practices and intent == "qa":
            intent = "gap"
        return intent, doc_type
    except Exception as e:
        print(f"[classify] LLM router fell back to regex: {e}")
        return fb_intent, fb_type


def _convert_tab_blocks_to_md(text: str) -> str:
    lines = text.splitlines()
    out = []
    i = 0

    while i < len(lines):
        if "\t" not in lines[i]:
            out.append(lines[i])
            i += 1
            continue

        raw_block = []
        while i < len(lines) and "\t" in lines[i]:
            raw_block.append(lines[i].rstrip())
            i += 1

        rows = []
        for raw in raw_block:
            cols = [c.strip() for c in re.split(r"\t+", raw.strip())]
            if len(cols) >= 2:
                rows.append(cols)

        if len(rows) >= 2:
            max_cols = max(len(r) for r in rows)
            rows = [r + [""] * (max_cols - len(r)) for r in rows]

            out.append("| " + " | ".join(rows[0]) + " |")
            out.append("| " + " | ".join(["---"] * max_cols) + " |")
            for row in rows[1:]:
                out.append("| " + " | ".join(row) + " |")
            out.append("")
        else:
            out.extend(raw_block)

    return "\n".join(out)

def _clean_display_title(title: str) -> str:
    t = Path((title or "").strip()).stem
    t = re.sub(r"^\d+\s*[_\-. ]\s*", "", t)   # remove leading numbering like 5_
    t = re.sub(r"[_\-]+", " ", t)             # underscores/hyphens -> spaces
    t = re.sub(r"\s+", " ", t).strip(" ._-")
    return t

def _prepare_full_doc_for_display(text: str) -> str:
    t = text.strip()

    # remove frontmatter if any slips through
    t = re.sub(r"^---.*?---\s*", "", t, flags=re.S)

    # normalize Word / copied-text artifacts
    t = t.replace("\u00a0", " ")
    t = re.sub(r"[ \t]*[•▪◦●]\s*", "\n- ", t)

    # split inline lettered lists onto new lines
    t = re.sub(r"(?<!\n)\s+([a-z])\)\s+", r"\n\1) ", t)

    # drop useless standalone labels
    t = re.sub(r"(?im)^\s*(policy|procedure)\s*$\n?", "", t)

    # convert tab-separated pseudo tables into markdown tables
    t = _convert_tab_blocks_to_md(t)

    # collapse duplicate headings + promote plain section labels
    lines = t.splitlines()
    out = []
    prev_heading = None

    for line in lines:
        stripped = line.strip()

        if re.match(r"^#+\s+", stripped):
            heading_norm = re.sub(r"^#+\s*", "", stripped).strip().lower()
            if heading_norm == prev_heading:
                continue
            prev_heading = heading_norm

            hashes = re.match(r"^(#+)", stripped).group(1)
            new_hashes = "#" * min(len(hashes) + 1, 4)
            out.append(re.sub(r"^#+", new_hashes, stripped))
            continue

        # promote short standalone title-like lines into headings
        if (
            stripped
            and not stripped.startswith(("|", "-", "*", "```"))
            and len(stripped) <= 90
            and len(stripped.split()) <= 8
            and re.match(r"^[A-Z][A-Za-z0-9/&(),\-'\s\.]+$", stripped)
            and not stripped.endswith((".", ":", ";"))
            and stripped.lower() not in {"policy", "procedure"}
        ):
            out.append(f"## {stripped}")
            prev_heading = stripped.lower()
            continue

        out.append(line)

    t = "\n".join(out)

    # clean accidental outer markdown fence wrappers
    t = re.sub(r"```markdown\s*", "", t, flags=re.I)
    t = re.sub(r"\n```+\s*$", "", t)

    # normalize blank lines
    t = re.sub(r"\n{3,}", "\n\n", t)

    # strip lingering admin residue
    t = re.sub(
        r"(?im)^(?:"
        r"\[client\].*|client:.*|version\s*#.*|version\s+\S+.*|"
        r"issue\s*/\s*effective.*|date of next review.*|"
        r"document number.*|document type.*|status.*|effective date.*|"
        r"department/function.*|prepared by.*|reviewed by.*|approved by.*|"
        r"distribution.*|classification.*|policy custodian.*|content issuance.*"
        r")\n?",
        "",
        t,
    )

    return t.strip()

def _structure_retrieved_doc_for_display(text: str) -> str:
    """
    Keep the retrieved KB text faithful, but improve display structure only.
    No summarising, no content deletion, no policy rewriting.
    """
    prompt = f"""
You are formatting a retrieved policy/procedure document for clean display in chat.

STRICT RULES:
- Do NOT summarize.
- Do NOT omit content.
- Do NOT materially paraphrase.
- Do NOT change policy meaning.
- Do NOT invent text.
- Only improve structure and readability.

FORMATTING TASKS:
- Add clear markdown headings where obvious section labels exist.
- Put inline lettered lists like "a) ... b) ... c) ..." on separate lines.
- Put short policy points on separate lines where needed.
- Convert obvious column-like / pseudo-table text into valid markdown tables when possible.
- Remove duplicated standalone labels like:
  Purpose
  Policy
  Purpose
- Keep the document professional and clean.
- Preserve all substantive content.

DOCUMENT:
{text}
"""
    return _call_llm(
        "You are a strict document formatter. Preserve meaning exactly; improve structure only.",
        prompt,
        model=MODEL_SONNET,
        effort=SUPPORT_REASONING_EFFORT,
        max_tokens=10000,
    ).strip()

def ask_question(query: str) -> tuple:
    """
    KB-first Q&A with full-document retrieval and web fallback.
    Returns: (answer, sources, search_mode) — search_mode: 'kb'|'web'|'none'
    """
    q = query.lower().strip()

    # Smalltalk guard — do not waste web search on greetings
    if q in {"hi", "hello", "hey", "good morning", "good evening", "good afternoon"}:
        return (
            "Hello. How can I help you with a policy, procedure, generation request, or gap analysis?",
            [],
            "kb",
        )

    if not _vs_ready():
        return (
            "⚠️ Knowledge Base is not ready. Run:\n"
            "```\npython preprocess_documents.py --folder raw_data/\n"
            "python ingest_to_vectorstore.py\n```",
            [], "none",
        )
    
    #targetted subsection
    if _is_targeted_subsection_request(query):
        answer, sources = _extract_targeted_subsection(query)
        if answer:
            return answer, sources, "kb"
        
    #Explicit full document retrievel
    if _is_explicit_full_doc_request(query) or _is_full_doc_request(query):
        matched, docs = _get_full_document(query)
        if matched and docs:
            full_doc = _prepare_full_doc_for_display(docs[0].page_content)
            title = docs[0].metadata.get("document_title", "").strip()
            raw_title = docs[0].metadata.get("document_title", "") or matched
            title = _clean_display_title(raw_title)
            if title and not re.search(rf"(?im)^#\s+{re.escape(title)}\s*$", full_doc):
                full_doc = f"# {title}\n\n{full_doc}"

            #full_doc = _structure_retrieved_doc_for_display(full_doc)
            if len(full_doc.split()) <= 3500:
                full_doc = _structure_retrieved_doc_for_display(full_doc)
            return (full_doc,
            [matched],
            "kb",
        )

    # Hybrid chunk retrieval
    kb_query = query.lower()

    query_expansions = {
    "kpi": "kpi kpis metrics measurement monitoring performance indicators",
    "kpis": "kpi kpis metrics measurement monitoring performance indicators",

    "classification": "data classification confidential restricted internal public",
    "data classification": "data classification confidential restricted internal public",

    "onboarding": "customer onboarding kyc cdd edd customer acceptance",
    "customer": "customer onboarding kyc cdd verification screening",

    "approval": "approval authority approval matrix approver delegation",
    "approver": "approval authority approval matrix delegation",

    "risk": "risk assessment risk management controls mitigation",
    "audit": "audit internal audit compliance review findings",

    "policy": "policy governance standard procedure framework",
    "procedure": "workflow process steps escalation exception handling",

    "vendor": "third party outsourcing supplier vendor",
    "third party": "vendor outsourcing supplier third party",

    "security": "cybersecurity infosec controls protection monitoring",
    "pdpl": "personal data protection privacy sensitive data",
}
    for keyword, expansion in query_expansions.items():
        if keyword in kb_query:
            kb_query += " " + expansion

   
    ctx, sources = _search_kb(kb_query)
    if _has_ctx(ctx):
        user_msg = (
    f"Context:\n\n{ctx}\n\nQuestion: {query}\n\n"
    "Apply the relevant policy clauses to answer precisely. "
    "Preserve tables as proper markdown tables by default. "
    "Only convert table content into bullets or numbered points if the user explicitly asks for points, bullets, or a summary. "
    "For scenarios, walk through the procedure step-by-step. "
    "Do not append 'Applicable Policy Sections' or 'Sources' in the answer body."
)
        kb_answer = _strip_answer_metadata(_call_llm(KB_QA_PROMPT, user_msg,
                                                     model=MODEL_SONNET, effort=SUPPORT_REASONING_EFFORT))
        if not _is_not_found(kb_answer):
            return kb_answer, _combine_sources(kb_answer, sources), "kb"
        print(f"[rag] KB not-found for: {query[:60]} — trying web")

    web_ctx, web_sources = _search_web(query)
    if web_ctx:
        user_msg = f"Web results:\n\n{web_ctx}\n\nQuestion: {query}"
        web_answer = _strip_answer_metadata(_call_llm(WEB_QA_PROMPT, user_msg,
                                                      model=MODEL_SONNET, effort=SUPPORT_REASONING_EFFORT))
        return web_answer, web_sources, "web"

    return (
        f"{NOT_FOUND_PHRASE}\n\nPlease rephrase or consult your compliance team.",
        [], "none",
    )

def generate_policy(user_request: str, doc_type: str = None, progress=None) -> tuple:
    """
    5-stage multi-step policy/procedure generation.
    Produces 25-30 page enterprise-grade documents.

    doc_type: 'Policy' | 'Procedure'. If not supplied by the caller, the AI router
    (classify_request) decides it here, so the planner always gets a clean,
    non-hybrid type — which in turn drives the right section set and the flowchart.

    Stage 1: Evidence gathering
    Stage 2: Org intelligence extraction
    Stage 3: Document plan
    Stage 4: Section-by-section drafting
    Stage 5: Assembly + final review

    Returns: (complete_document_text, sources_list)
    """
    all_sources = []
    _t_start = time.time()

    def _report(msg):
        """Log to stdout AND push a live UI status update when a callback is given.
        Called only from the main thread, so calling Streamlit from inside is safe."""
        print(f"[generate] {msg}")
        if progress:
            try:
                progress(msg)
            except Exception:
                pass

    # Decide the document type up front (AI router) if the caller didn't pass one,
    # so the planner is told exactly what to build.
    if not doc_type:
        _, doc_type = classify_request(user_request)
    print(f"[generate] Document type: {_normalize_doc_type(doc_type)}")

    # Warm the vectorstore/BM25 singletons once, up front, so the concurrent
    # section workers below all share a fully-initialised index (no init race).
    _vs_ready()

    # ── Stage 1: Evidence Gathering ───────────────────────────────────────────
    _report("Gathering knowledge base + regulatory evidence…")

    kb_context, kb_sources = _search_kb(user_request, k=20)
    all_sources.extend(kb_sources)

    anchor_context, anchor_source = _pick_generation_anchor(user_request)
    if anchor_source and anchor_source not in all_sources:
        all_sources.append(anchor_source)

    web_query = f"{user_request} KSA policy SAMA NCA NDMO PDPL regulations current best practices"
    web_context, web_sources = _search_web(web_query)
    if web_sources:
        all_sources.extend(web_sources)

    # ── Stage 2: Org Intelligence Extraction ─────────────────────────────────
    _report("Extracting organisational details…")
    org_intel = _stage1_extract_org_intel(kb_context, anchor_context, user_request)


    # ── Stage 3: Document Plan ────────────────────────────────────────────────
    _report("Planning document structure…")
    plan = _stage2_generate_plan(user_request, org_intel, web_context, doc_type=doc_type)
    sections = plan["sections"]

    print(f"[generate] Stage 3: Plan complete — '{plan['title']}' ({len(sections)} sections)")

    # ── Stage 4: Section-by-Section Drafting (parallel) ──────────────────────
    # Each section is an independent LLM call, so we fan them out across a thread
    # pool instead of drafting one-at-a-time. Wall-clock for this stage drops from
    # "sum of all sections" to "slowest single section" (bounded by the worker
    # count / OpenAI rate limit). Order is preserved by writing into a pre-sized
    # list at each section's index.
    total = len(sections)
    drafted_sections = [None] * total
    _t_stage4 = time.time()

    def _draft_one(idx, section):
        title = section["title"]
        print(f"[generate] Stage 4: Drafting section {idx+1}/{total}: {title[:50]}...")
        section_query = f"{user_request} {title} {section['scope']}"
        section_kb, _ = _search_kb(section_query, k=10)
        return idx, _stage3_draft_section(
            section=section,
            plan=plan,
            org_intel=org_intel,
            web_context=web_context,
            section_kb=section_kb,
        )

    workers = max(1, min(SECTION_CONCURRENCY, total))
    print(f"[generate] Stage 4: Drafting {total} sections with {workers} concurrent workers...")
    _report(f"Writing {total} sections…")
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = [ex.submit(_draft_one, i, s) for i, s in enumerate(sections)]
        _done = 0
        for fut in as_completed(futures):   # this loop runs on the main thread
            idx, content = fut.result()
            drafted_sections[idx] = content
            _done += 1
            _report(f"Writing sections… {_done}/{total} done")

    print(f"[generate] Stage 4: All sections drafted in {time.time() - _t_stage4:.1f}s")

    # ── Stage 5: Assembly ─────────────────────────────────────────────────────
    _report("Assembling document…")
    complete_document = _stage4_assemble(drafted_sections, plan)

    # ── Flowchart shield (procedures): pull the section-11 DOT out BEFORE review ─
    # The final review rewrites the whole document and would strip a raw DOT block,
    # so we remove it first, guarantee we have one (generating from the section text
    # if drafting didn't emit a usable diagram), and reinsert it after the review.
    wf_num, wf_title = _find_workflow_section(plan)
    flowchart_dot = None
    if wf_num:
        flowchart_dot, complete_document = _extract_dot_block(complete_document)
        flowchart_dot = _clean_dot(flowchart_dot)
        if not flowchart_dot:
            wf_content = next(
                (c for c in drafted_sections
                 if c and re.search(rf"(?m)^##\s+{re.escape(wf_num)}\.\s", c)), "")
            if wf_content:
                print("[generate] Flowchart: drafting produced none — generating from section text...")
                flowchart_dot = _generate_flowchart_dot(wf_content)

    # ── Stage 6: Final review (does NOT see the flowchart) ────────────────────
    _report("Final quality review (the longest step)…")
    complete_document = _stage5_final_review_safe(complete_document, plan)

    # Reinsert / guarantee the Visio-style flowchart at the end of the workflow section.
    if wf_num and flowchart_dot:
        complete_document = _insert_flowchart(complete_document, wf_num, wf_title, flowchart_dot)
        print(f"[generate] Flowchart: embedded into section {wf_num} ({wf_title[:40]})")

    word_count = len(complete_document.split())
    page_est = word_count // 300
    _elapsed = time.time() - _t_start
    print(f"[generate] Complete: ~{word_count:,} words (~{page_est} pages) "
          f"in {_elapsed:.1f}s ({_elapsed/60:.1f} min)")

    # de-duplicate sources preserving order
    final_sources = []
    for s in all_sources:
        if s and s not in final_sources:
            final_sources.append(s)

    return complete_document, final_sources


def gap_analysis(current_practices: str, topic: str = "", progress=None) -> tuple:
    """Gap analysis: current practices vs KB policies. Returns (report, sources).
    `progress` is an optional UI callback (str) for live status updates."""
    def _report(msg):
        if progress:
            try:
                progress(msg)
            except Exception:
                pass

    # Blend the topic with an excerpt of the current practices so retrieval finds the
    # right policies even when the chat question is vague or the practices come from a file.
    parts = []
    if topic.strip():
        parts.append(topic.strip())
    if current_practices.strip():
        parts.append(current_practices[:600])
    query = " ".join(parts) if parts else current_practices[:400]
    _report("Finding relevant policies…")
    ctx, sources = _search_kb(query, k=15)
    if not _has_ctx(ctx):
        return (
            "Cannot perform gap analysis — no relevant policies found in KB. "
            "Run: python ingest_to_vectorstore.py",
            [],
        )
    # Cap very large practices docs so the call stays reliable (a whole policy doc can
    # be huge once diagrams are extracted). 30k chars ≈ ~7,500 words is plenty.
    practices = current_practices.strip()
    if len(practices) > 30000:
        practices = practices[:30000] + "\n\n[...current practices truncated for analysis...]"

    user_msg = (
        f"EXISTING POLICIES:\n\n{ctx}\n\n"
        f"CURRENT PRACTICES:\n\n{practices}\n\n"
        "Perform structured gap analysis. Follow the output format exactly. "
        "No inline citations. Cite specific KSA regulations + articles for HIGH/MEDIUM gaps."
    )
    _report("Analysing gaps against policy (this can take a minute)…")
    raw = _call_llm(GAP_ANALYSIS_PROMPT, user_msg, model=MODEL_SONNET,
                    effort=LLM_REASONING_EFFORT, max_tokens=8000)
    if not raw.strip():
        return (
            "⚠️ The gap analysis could not be generated (the model returned no content, "
            "likely due to a very large input). Try a shorter current-practices document.",
            sources,
        )
    return raw, _combine_sources(raw, sources)

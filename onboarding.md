# Policy & Procedure Agent — Onboarding

## What this app is

A **RAG-based (Retrieval-Augmented Generation) assistant** for enterprise **Policy & Procedure** work, built for a **Saudi Arabia (KSA) regulatory context**. It's a Streamlit web app that lets users:

1. **Q&A** — ask questions grounded in the company's own policy documents (with web fallback)
2. **Generate** — draft full enterprise **policies** or **procedures** from scratch, with an AI router deciding which, and (for procedures) an auto-generated **swimlane process flowchart**
3. **Gap Analysis** — compare "what we actually do" against the policies on file and flag compliance gaps
4. **Export** — download any generated output as a professionally formatted Word (`.docx`) document, flowchart included

The whole runtime lives in one folder: `client_build/`. There's no separate backend — it's a Python/Streamlit monolith that calls **Claude (Anthropic)** for generation/Q&A and a **local embedding model** for retrieval.

---

## The architecture at a glance

```
                    ┌─────────────────────────────────────────┐
   Raw docs         │  PREPROCESSING (offline / on upload)     │
  (.docx / .pdf) ──▶│  preprocess_documents.py                 │
                    │   • parse Word/PDF, tables, images        │
                    │   • Claude vision for diagrams/flowcharts │  ← build-time only
                    │     (LibreOffice converts EMF/Visio→PNG)  │
                    │   • failed extractions are quarantined    │
                    │   • chunk into knowledge_base/*.md        │
                    └──────────────────┬──────────────────────┘
                                       ▼
                    ┌─────────────────────────────────────────┐
                    │  INGEST                                  │
                    │  ingest_to_vectorstore.py                │
                    │   • full build / incremental / --sync    │
                    │   • FAISS index + BM25 corpus            │
                    │   • saves to vectorstore/                │
                    └──────────────────┬──────────────────────┘
                                       ▼
   User (browser) ─▶ app.py (Streamlit UI) ─▶ rag_pipeline.py (the brain)
                                       │            │
                                       │            ├─ AI router (Haiku): intent + doc-type
                                       │            ├─ clarifying-question intake
                                       │            ├─ FAISS + BM25 hybrid search
                                       │            ├─ Claude LLM calls (Sonnet / Haiku)
                                       │            ├─ parallel section drafting (6 workers)
                                       │            ├─ Graphviz swimlane flowchart (procedures)
                                       │            └─ Claude web search fallback
                                       ▼
                              word_export.py (.docx download, flowchart embedded)
```

---

## Runtime models (Claude) — the most important thing to know

The runtime LLM is **Claude (Anthropic)**, called through the **native Anthropic SDK** in one chokepoint: `_call_llm()` in `rag_pipeline.py` (it **always streams**, so large outputs never hit a timeout). Two tiers, configured in `config.py`:

| Tier | Model | `config.py` | Used for |
|------|-------|-------------|----------|
| **Quality** | Claude **Sonnet 4.6** (`claude-sonnet-4-6`) | `MODEL_SONNET` | Section drafting, gap analysis (HIGH effort); planning, org-intel, final review, flowchart, Q&A, formatter (MEDIUM effort) |
| **Light** | Claude **Haiku 4.5** (`claude-haiku-4-5`) | `MODEL_HAIKU` | AI router, clarification questions, query enrichment, targeted KB extraction |

- **Effort** (Claude `output_config.effort`) is the reasoning knob — `LLM_REASONING_EFFORT = "high"` (drafting + gap) and `SUPPORT_REASONING_EFFORT = "medium"` (everything else). Thinking is left **disabled** for speed; effort alone controls depth on Sonnet. **Haiku does not support effort**, so light-tier calls run plain.
- **No OpenAI/GPT anywhere — everything is Claude.** Runtime generation/Q&A/gap, the AI router, **web search**, AND **build-time vision** (`VISION_MODEL = claude-sonnet-4-6` in `config.py`) all use Claude. The only LLM dependency is `anthropic`.
- **API key**: set `ANTHROPIC_API_KEY` (or `CLAUDE_API_KEY` — both accepted) in `.env`. That's the **only LLM key required**. `OPENAI_API_KEY` and `TAVILY_API_KEY` are no longer used (left as harmless dead config).

---

## File-by-file tour

| File | Role |
|------|------|
| **`app.py`** | The Streamlit UI. Sidebar (mode selector, upload, Word export), chat, **Graphviz + Mermaid diagram rendering**, the embeddings **pre-warm** at startup, and the **conversational-clarification** state machine. Routes each message via the **AI router**. |
| **`rag_pipeline.py`** | The core engine. Native-Anthropic `_call_llm`; hybrid retrieval (FAISS + BM25); the 3 public modes (`ask_question`, `generate_policy`, `gap_analysis`); the **AI router** (`classify_request`) + regex fallback (`classify_intent`); the **6-stage, parallelized** generation pipeline; **procedure/policy template pruning**; **title-based section guidance**; and the **swimlane flowchart** generation + shield/guarantee logic. |
| **`prompts.py`** | All LLM prompts + a **baked-in KSA regulatory framework** (SAMA, CMA, NDMO, NCA, PDPL, etc.) so regulations aren't hallucinated. Per-section drafting guidance lives here (`SECTION_GUIDANCE`). |
| **`config.py`** | Central config: API key (`ANTHROPIC_API_KEY`/`CLAUDE_API_KEY` — the only LLM key; `SUPABASE_*`, `WHISPER_*` optional; `OPENAI_API_KEY`/`TAVILY_API_KEY` are legacy/unused), model IDs (`MODEL_SONNET`, `MODEL_HAIKU`, `VISION_MODEL`), effort levels, `SECTION_CONCURRENCY`, paths. Reads `.env` or Streamlit secrets. |
| **`preprocess_documents.py`** | Build-time document ingestion. Parses DOCX/PDF, extracts tables faithfully, handles embedded diagrams (raster, Word shapes, Visio OLE, SmartArt) via **Claude vision** (`VISION_MODEL`; requires **LibreOffice** to convert EMF/Visio→PNG), chunks into markdown with frontmatter. Failed extractions are **quarantined**. Optional **LLMWhisperer** path for PDFs. |
| **`ingest_to_vectorstore.py`** | Turns preprocessed `.md` chunks into a FAISS index + BM25 corpus. Full rebuild, **incremental** add/update, and `--sync` (auto-detect new chunks). Deliberately does **not** re-split chunks. |
| **`process_and_ingest.py`** | CLI one-shot: raw `.docx`/`.pdf` → preprocess → incremental index. The command-line equivalent of the app's upload button. |
| **`word_export.py`** | Converts generated markdown into a polished ISO-style `.docx` — headers/footers, document control block, revision history, approval sign-off, sources, and **the rendered flowchart** (DOT → PNG → embedded, wide swimlanes auto-rotated). |
| **`supabase_utils.py`** | Optional cloud document storage (upload/list/download/delete from a Supabase bucket). Only active if `SUPABASE_*` env vars are set. **Note:** this is file storage only — it is *not* the vector DB (that's the local FAISS index). |
| **`requirements.txt`** | Python deps. **`packages.txt`** (sibling) lists the `graphviz` **system** binary for Streamlit Cloud. |

---

## The 3 user modes (how requests flow)

`app.py` either uses the sidebar-selected mode or, in **Auto-detect**, calls the **AI router** `classify_request(query)` (a fast Haiku call with structured JSON output) which returns **both** the intent and the document type. A regex fallback (`classify_intent`) runs automatically if the model call ever fails, so routing never hard-depends on the LLM.

### 1. Q&A (`ask_question`) — the default
Tries, in order: targeted subsection extraction → full-document retrieval → hybrid chunk search (FAISS + BM25, with query expansion + reranking) → **web fallback** (**Claude's native web search tool**, ⚠️-flagged). The answer is written by **Sonnet** (medium effort).

### 2. Generate (`generate_policy`) — the showcase feature
First an optional **clarification intake** (below), then a **6-stage pipeline**:

- **Stage 1:** Gather evidence (KB chunks + closest anchor policy + web)
- **Stage 2:** Extract org-specific intelligence (role titles, governance bodies, …) — Sonnet, medium
- **Stage 3:** Build a document plan — Sonnet, medium. **The document type (POLICY vs PROCEDURE) is decided by the AI router and forced into the planner**, so it can never hedge to a hybrid "Policy and Procedure" label. The plan's section list is then **pruned per type** (see below).
- **Stage 4:** Draft each section with a **separate focused Sonnet call at HIGH effort** — **run in parallel** across `SECTION_CONCURRENCY` workers (default **6**, in `config.py`). For a **procedure**, the workflow section also emits a **swimlane flowchart**.
- **Stage 5:** Assemble the sections.
- **Stage 6:** A final quality-review pass — Sonnet, medium. This is the **slowest stage**: it's a single call that rewrites the *entire* document, and it can't be parallelized. (Pruning the template — fewer sections — directly shrinks it.)

The flowchart is **shielded** from Stage 6 (pulled out before the review, reinserted after) so the polish pass can't strip it, and **guaranteed** (if drafting didn't emit one, a dedicated call generates it from the workflow text).

### 3. Gap Analysis (`gap_analysis`)
The user provides current practices by **attaching a DOCX/PDF in the chat box** (the old "📊 Gap" paste panel was removed — chat upload covers it). The app retrieves relevant policies (blending the question + an excerpt of the practices into the query) and produces a structured report with severity ratings (🔴 HIGH / 🟡 MEDIUM / 🟢 LOW) and KSA regulation citations. Run by **Sonnet at HIGH effort** (single call).

---

## Document templates — Policy vs Procedure

The planner produces a section list, then `rag_pipeline.py` **prunes it by type**:

- **Policy** → keeps the full governance-focused set; the two operational-workflow sections are removed (`_remove_procedure_sections_for_policy`).
- **Procedure** → keeps only execution-focused sections (`_remove_policy_sections_for_procedure`). **Removed for procedures:** Executive Summary, Scope & Applicability, Regulatory & Compliance Framework, the three Policy Statements sections, Breach/Non-Compliance, Training, Internal Audit, Related Documents & Sign-Off. **A procedure is 9 lean sections:**

  1. Document Control · 2. Purpose & Objectives · 3. Definitions · 4. Roles & RACI · **5. Standard Workflow (← swimlane flowchart)** · 6. Exceptions & Escalation · 7. Controls, Approvals & Authority · 8. KPIs & Monitoring · 9. Records Management

> Sign-off isn't lost on procedures — `word_export.py` always appends a Revision History + Approval/Authorization block to every document.

Section **guidance is matched by title, not number** (`_guidance_key_for_title`), so pruning/renumbering can't misassign the per-section drafting instructions.

---

## The swimlane flowchart (procedures)

Procedures get a **Graphviz horizontal swimlane** in the Standard Workflow section — one lane per responsible role, steps flowing left→right:

- Generated as a ```dot fenced block (Claude is instructed to produce `rankdir=LR` + one `subgraph cluster` per role).
- **In the chat:** rendered live by `st.graphviz_chart` (browser-side; scrollable).
- **In Word:** `word_export.py` renders the DOT → PNG at 200 DPI and embeds it. Wide diagrams (swimlanes) are **rotated 90°** and placed on the normal portrait page (you turn the page sideways to read), so the document keeps a single consistent layout — no landscape page break.
- **Needs the Graphviz `dot` binary** for the Word render (the chat render does not). The code auto-finds `dot` in the standard install dirs even if it isn't on `PATH`.

> **This is independent of LibreOffice.** The generated procedure's swimlane is produced by Claude (the DOT text) and rendered by **Graphviz** — which is installed on Streamlit Cloud via `packages.txt`. **A generated procedure always contains its swimlane, with or without LibreOffice.** LibreOffice is a *different* tool used only to extract diagrams *from source documents* at build time (next section) — it plays no part in the diagram that appears in the output. Do not confuse the two.

---

## Conversational clarification (intake before Generate / Gap)

When a message routes to Generate or Gap, the app can ask **clarifying questions first** (one at a time, adaptive, Haiku-powered), then synthesize the answers into a detailed brief fed to the pipeline.

- `clarify_next_question(...)` asks the single most valuable next question, or stops when it has enough. A detailed request gets **0 questions**.
- Hard cap of **5** questions; a **"✅ Generate now (skip remaining)"** button is always shown.
- **Sidebar toggle "Ask clarifying questions first"** (default ON) — turn off for one-shot behaviour.
- The document type is decided by the AI router on the *enriched* brief, so the clarification path produces a correctly-typed (and correctly-labelled) document too.

---

## Key design decisions worth knowing

- **Local, free embeddings**: `sentence-transformers/all-MiniLM-L6-v2` on CPU — no API key for retrieval. They are **pre-warmed at app startup** (`warm_up()` via `@st.cache_resource`) so the first request has no cold-start hit.
- **One LLM chokepoint**: every runtime model call goes through `_call_llm()`, which selects the model + effort and always streams. Swapping models or tuning effort is a one-line change.
- **AI routing over keywords**: intent (qa/generate/gap) and doc-type (policy/procedure) come from a Haiku classifier with structured output — robust to phrasings like "generate a *process*" that keyword matching mishandled. Regex remains as a fallback.
- **Parallel drafting**: the ~9–17 section calls run concurrently (ThreadPoolExecutor, `SECTION_CONCURRENCY` workers). This is the big speed win — drafting drops from "sum of all sections" to "slowest few batches".
- **Anti-hallucination is a core theme**: the KSA regulatory framework is hard-coded in `prompts.py`; prompts forbid inventing approver names/dates/committees; web answers are visually flagged.
- **Hybrid search**: FAISS (meaning) + BM25 (exact keywords), merged and reranked.
- **Faithful table/diagram extraction**: much of `preprocess_documents.py` exists specifically to not lose RACI matrices, KPI tables, and flowcharts.
- **Incremental ingestion**: uploads don't re-embed the whole KB; old vectors for a re-uploaded source are deleted (matched by `source` = filename) and only new chunks added; the BM25 corpus is regenerated from the live index each time.

---

## ⚠️ Things to flag

- **API keys**: the **only required key is `ANTHROPIC_API_KEY`** (or `CLAUDE_API_KEY`) in `.env` — it powers generation, Q&A, gap, the AI router, web search, **and** build-time vision. Optional: `SUPABASE_*` (cloud storage), `WHISPER_*` (LLMWhisperer). `OPENAI_API_KEY`/`TAVILY_API_KEY` are **no longer used**. The `.env` file holds **live keys** — never commit it; rotate any key that's been shared.
- **Anthropic account must have credits/billing** — a valid-but-unfunded key returns `401 invalid x-api-key`.
- **Graphviz is required for the Word flowchart**: install the **system** Graphviz so `dot` exists (Windows: `winget install Graphviz.Graphviz`, then it lives at `C:\Program Files\Graphviz\bin`; Linux/Streamlit Cloud: `packages.txt` already lists `graphviz`). The chat diagram works without it; only the Word embed needs it. The Python `graphviz` package is in `requirements.txt`.
- **LibreOffice is OPTIONAL and NOT needed on Streamlit Cloud — and it has nothing to do with the diagram in the generated procedure.** Two separate "diagram" systems exist; don't conflate them:
  - **Generated swimlane (output):** rendered by **Graphviz** (`dot`, in `packages.txt`). **Always present in a generated procedure, with or without LibreOffice.** ✅
  - **Source-diagram extraction (input, build-time only):** LibreOffice converts embedded **Visio/EMF** diagrams in `.docx` source files to PNG so GPT vision can read them. This is the *only* thing LibreOffice does here.

  When LibreOffice is absent, the input path degrades gracefully — Visio/EMF diagrams in source docs are **skipped and logged once** (`[preprocess] LibreOffice not found …`), while **text, tables, raster images, generation, and the Word export with its swimlane all work normally**.

  **Is there a workaround for EMF extraction without LibreOffice?** Not a clean lightweight one. GPT vision only accepts PNG/JPEG/GIF/WEBP (not EMF), and there is no good pure-Python EMF→PNG renderer. The realistic options:
    1. **(Recommended) Build the index offline**, where LibreOffice is installed, and commit `vectorstore/`. The KB here is already built this way, so all existing diagrams are captured. The deployed app only reads the index — nothing to convert at runtime.
    2. **Inkscape** can convert EMF→PNG and is apt-installable (add `inkscape` to `packages.txt`), but it's heavy (~hundreds of MB) and may strain Streamlit Cloud's resource limits — only worth it if runtime extraction of Visio diagrams from user uploads is essential.
    3. **`libemf2svg` (`emf2svg-conv`) → SVG → `cairosvg`/`rsvg` → PNG** is lighter than LibreOffice but needs an apt build step and EMF fidelity varies.

  For this project's use case (KB pre-built, runtime is mostly Q&A + generation), option 1 is correct and nothing further is needed.

- **Output is a Word `.docx` (not PDF).** The swimlane is embedded in the `.docx` via Graphviz. If you ever need a **PDF** download instead, note that DOCX→PDF conversion typically *does* require LibreOffice (`soffice --convert-to pdf`) or a paid cloud converter — so adding PDF export would reintroduce a LibreOffice dependency. The current Word export needs only Graphviz.
- **Rate limits**: 6 concurrent drafting workers + the other stages can briefly exceed an entry-tier Anthropic rate limit. If you see `rate_limit`/`overloaded`, lower `SECTION_CONCURRENCY` (e.g. to 3) in `config.py`.
- **Stage 6 is the slow stage**: it rewrites the whole document in one call. Generation time is dominated by it, not by drafting (which is parallel). Pruning the template helps; you could also lower its effort or make it optional.
- **Streamlit only hot-reloads `app.py`**: when you edit an **imported module** (`rag_pipeline.py`, `word_export.py`, `config.py`), a browser refresh is **not** enough — you must **fully restart** the server (Ctrl+C → `streamlit run app.py`). Only `app.py` edits hot-reload.
- **Windows encoding**: generated text contains Unicode punctuation (non-breaking hyphen, em-dash). `rag_pipeline.py` reconfigures stdout/stderr to UTF-8, and you should launch with `PYTHONUTF8=1` so console logging never crashes on cp1252.
- **Python version**: the project's `.venv` targets **Python 3.12** (most reliable for faiss/sentence-transformers). 3.14 also works but is bleeding-edge (harmless Pydantic-V1 warning). Prefer **3.11/3.12** when deploying elsewhere.
- **Not a git repo at the top level** — only `client_build/` has a `.git`.
- **No tests** anywhere in the codebase.

---

## To run it locally

> **Prerequisites:** Python **3.12** (recommended) · **Graphviz** system binary (for the Word flowchart) · **LibreOffice** (only if you'll *preprocess* docs with embedded diagrams).

```powershell
# from a FRESH terminal so PATH picks up Graphviz
cd "client_build"

# 1. (first time) create the venv + install deps
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

# 2. install the Graphviz system binary (one time), so `dot` exists for Word export
winget install Graphviz.Graphviz          # adds C:\Program Files\Graphviz\bin

# 3. ensure .env has the key  (just one — everything is Claude)
#    ANTHROPIC_API_KEY=...   (or CLAUDE_API_KEY)   ← LLM, web search, AND vision

# 4. (only if the vector index isn't built yet)
python preprocess_documents.py --folder raw_data/   # vision = Claude; LibreOffice only for Visio/EMF diagrams
python ingest_to_vectorstore.py

# 5. launch (UTF-8 on for clean Windows logging)
$env:PYTHONUTF8 = "1"
python -m streamlit run app.py
```

The pre-built FAISS index ships in `vectorstore/`, so for a normal run you can skip step 4 entirely — just install deps, set `ANTHROPIC_API_KEY`, and launch. You can also add documents through the running app's sidebar (it preprocesses + reindexes on the fly).

> **Reminder:** after editing any `.py` module other than `app.py`, **fully restart** the server — Streamlit won't reload imported modules on its own.

---

## Adding documents without the GUI (CLI)

All three entry points update the index **incrementally** (no full re-embed) once an index exists.

**A. Raw doc (`.docx`/`.pdf`) — preprocess + index in one shot** (vision = Claude; LibreOffice only for Visio/EMF diagrams):
```powershell
python process_and_ingest.py --file "raw_data\New Policy.docx"
python process_and_ingest.py --folder raw_data            # everything in a folder
```

**B. You dropped preprocessed `.md` chunks into `knowledge_base/` — just sync:**
```powershell
python ingest_to_vectorstore.py --sync
```

**C. Force-refresh one known source:**
```powershell
python ingest_to_vectorstore.py --source "Information Security Procedure.docx"
```

Full rebuild from scratch: `python ingest_to_vectorstore.py` (add `--clear` to wipe first).

---

## Deploying to Streamlit Cloud

- Push `client_build/` to GitHub (the `vectorstore/` FAISS index is committed and ships with the repo — that's your read-only vector DB at runtime).
- `requirements.txt` (Python deps) and **`packages.txt`** (apt: `graphviz`) are both read by Streamlit Cloud.
- Set secrets in the Streamlit dashboard: **`ANTHROPIC_API_KEY`** (the only required one), plus `SUPABASE_*` / `WHISPER_*` if you use them.
- **Keep preprocessing offline; no LibreOffice on the server.** LibreOffice is only needed to extract Visio/EMF diagrams at build time — build/refresh the FAISS index on your machine (where LibreOffice is installed) and commit it. The deployed app only *reads* the index, so **LibreOffice is not a Streamlit Cloud dependency** and is not in `packages.txt`. Runtime uploads still work without it (Visio/EMF diagrams in those uploads are simply skipped; text/tables/generation/export are unaffected).
- Note: Streamlit Cloud's filesystem is ephemeral — documents users add at runtime won't persist across restarts. For persistent runtime ingestion you'd move the vector store to a hosted DB (e.g. Supabase **pgvector**).

---

## Quick glossary

| Term | Meaning |
|------|---------|
| **RAG** | Retrieval-Augmented Generation — fetch relevant docs, then let the LLM answer using them |
| **FAISS** | Facebook AI Similarity Search — the vector index for semantic search (the actual "vector DB") |
| **BM25** | A keyword-ranking algorithm — complements FAISS for exact-term matches |
| **KB** | Knowledge Base — the preprocessed `knowledge_base/` markdown chunks |
| **AI router** | `classify_request` — Haiku call that decides intent (qa/generate/gap) + doc-type (policy/procedure) |
| **Effort** | Claude's `output_config.effort` (low/medium/high) — the reasoning/quality knob (Sonnet only) |
| **Swimlane** | The horizontal Graphviz flowchart in a procedure's workflow section, grouped by responsible role |
| **Web search** | **Claude's native web search tool** — used as a fallback when the KB has no answer (replaced Tavily) |
| **KSA** | Kingdom of Saudi Arabia — the regulatory context (SAMA, CMA, NDMO, NCA, PDPL) |
| **Chunk** | A single retrievable piece of a document, stored as one `.md` file with metadata |

"""
config.py — Central configuration for Policy & Procedure Agent.
All modules import from here. Edit values here only.
"""
import os
from pathlib import Path
from dotenv import load_dotenv


import os
from pathlib import Path

_BASE = Path(__file__).parent.resolve()

# Load .env first for local runs
for _fname in [".env", ".env.example"]:
    _fp = _BASE / _fname
    if _fp.exists():
        with open(_fp, encoding="utf-8-sig") as _f:
            for _line in _f:
                _line = _line.strip()
                if not _line or _line.startswith("#"):
                    continue
                if "=" in _line:
                    _k, _, _v = _line.partition("=")
                    _k = _k.strip()
                    _v = _v.strip().strip('"').strip("'").strip()
                    if _k and _v:
                        os.environ.setdefault(_k, _v)
        break
# ── API Keys: prefer Streamlit secrets when deployed, else env/.env ──────────
OPENAI_API_KEY    = os.environ.get("OPENAI_API_KEY", "").strip()
# Accept either ANTHROPIC_API_KEY or CLAUDE_API_KEY (the SDK's own default is
# ANTHROPIC_API_KEY; we also honour CLAUDE_API_KEY for convenience).
ANTHROPIC_API_KEY = "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"
try:
    import streamlit as st
    OPENAI_API_KEY    = st.secrets.get("OPENAI_API_KEY", OPENAI_API_KEY).strip()
    ANTHROPIC_API_KEY = (st.secrets.get("ANTHROPIC_API_KEY",
                          st.secrets.get("CLAUDE_API_KEY", ANTHROPIC_API_KEY))).strip()
    TAVILY_API_KEY    = st.secrets.get("TAVILY_API_KEY", TAVILY_API_KEY).strip()
except Exception:
    pass
# ── Paths ─────────────────────────────────────────────────────────────────────
KNOWLEDGE_BASE_PATH = str(_BASE / "knowledge_base")   # output of preprocess_documents.py
VECTORSTORE_PATH    = str(_BASE / "vectorstore")       # FAISS index output of ingest_to_vectorstore.py
UPLOAD_FOLDER       = str(_BASE / "uploads")           # where app.py saves uploaded files

# ── Embedding model (local, free, no API key needed) ─────────────────────────
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ── LLM — Claude (Anthropic) ─────────────────────────────────────────────────
# Two tiers. Sonnet 4.6 for everything quality-sensitive (drafting, gap analysis,
# planning, intel, review, Q&A, flowchart); Haiku 4.5 for cheap/mechanical calls
# (intent extraction, clarification questions, query enrichment). Model IDs are the
# exact aliases — do NOT append a date suffix.
MODEL_SONNET = "claude-sonnet-4-6"   # quality tier
MODEL_HAIKU  = "claude-haiku-4-5"    # light/mechanical tier

# Back-compat aliases (older code referenced these names).
LLM_MODEL      = MODEL_SONNET
LLM_MODEL_HIGH = MODEL_SONNET

# ── Reasoning effort (Claude `output_config.effort`) ─────────────────────────
# Sonnet 4.6 supports the effort parameter (low | medium | high). Haiku 4.5 does
# NOT — light-tier calls run with no effort param. Section drafting and gap analysis
# run at HIGH (best writing quality); the support stages (intel, plan, review,
# flowchart, formatter, Q&A) run at MEDIUM to cut wall-clock.
LLM_REASONING_EFFORT     = os.environ.get("LLM_REASONING_EFFORT", "high").strip()
SUPPORT_REASONING_EFFORT = os.environ.get("SUPPORT_REASONING_EFFORT", "medium").strip()

# ── Vision model (diagrams / flowcharts / scanned-page extraction) ────────────
# Used by preprocess_documents.py (build-time only). Now Claude (multimodal) — no
# OpenAI/GPT dependency. Requires LibreOffice to convert Visio/EMF diagrams to PNG
# before vision (optional; see onboarding). VISION_REASONING_EFFORT is retained for
# back-compat but is not used by the Claude vision path.
VISION_MODEL            = os.environ.get("VISION_MODEL", MODEL_SONNET).strip()
VISION_REASONING_EFFORT = os.environ.get("VISION_REASONING_EFFORT", "high").strip()

# ── Optional layout-aware PDF parser (Unstract LLMWhisperer) ──────────────────
# OFF unless WHISPER_API_KEY is set. When enabled, PDFs are parsed by LLMWhisperer
# (exact layout-preserving extraction); otherwise the built-in pdfplumber/PyMuPDF
# path runs. NOTE: the default endpoint is US-cloud; for KSA data-residency-sensitive
# clients, LLMWhisperer can be self-hosted on-prem (set WHISPER_BASE_URL accordingly).
WHISPER_API_KEY  = os.environ.get("WHISPER_API_KEY", "").strip()
WHISPER_BASE_URL = os.environ.get(
    "WHISPER_BASE_URL", "https://llmwhisperer-api.us-central.unstract.com/api/v2"
).strip()
try:
    import streamlit as st
    WHISPER_API_KEY  = st.secrets.get("WHISPER_API_KEY", WHISPER_API_KEY).strip()
    WHISPER_BASE_URL = st.secrets.get("WHISPER_BASE_URL", WHISPER_BASE_URL).strip()
except Exception:
    pass
USE_LLMWHISPERER = bool(WHISPER_API_KEY)

# ── Retrieval ─────────────────────────────────────────────────────────────────
TOP_K_RESULTS        = 10     # chunks retrieved per query
SIMILARITY_THRESHOLD = 0.0    # accept all FAISS results (BM25 handles filtering)

# ── Generation parallelism ───────────────────────────────────────────────────
# Number of document sections drafted concurrently in generate_policy().
# Each section is one independent LLM call, so drafting them in parallel turns
# the ~20 sequential calls into a fan-out bounded by the slowest section.
# Keep modest to stay under the OpenAI account's requests-per-minute limit.
SECTION_CONCURRENCY = int(os.environ.get("SECTION_CONCURRENCY", "6"))

# ── Web search (Tavily) ───────────────────────────────────────────────────────
ENABLE_WEB_SEARCH = True      # set False to disable web fallback entirely

# ── Supabase Storage ──────────────────────────────────────────────
SUPABASE_URL    = os.environ.get("SUPABASE_URL",    "").strip()
SUPABASE_KEY    = os.environ.get("SUPABASE_KEY",    "").strip()
SUPABASE_BUCKET = os.environ.get("SUPABASE_BUCKET", "policy-docs").strip()

try:
    import streamlit as st
    SUPABASE_URL    = st.secrets.get("SUPABASE_URL",    SUPABASE_URL).strip()
    SUPABASE_KEY    = st.secrets.get("SUPABASE_KEY",    SUPABASE_KEY).strip()
    SUPABASE_BUCKET = st.secrets.get("SUPABASE_BUCKET", SUPABASE_BUCKET).strip()
except Exception:
    pass

SUPABASE_ENABLED = bool(SUPABASE_URL and SUPABASE_KEY)

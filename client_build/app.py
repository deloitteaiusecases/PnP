"""
app.py — Policy & Procedure Agent
All 7 requirements.
Updated UI: Upload button moved to sidebar, Gap Analysis moved to a small horizontal button near the chat input.
"""
 
from dotenv import load_dotenv
load_dotenv()
import streamlit.components.v1 as components
import re
 
from word_export import generate_word_doc
#from config import UPLOAD_FOLDER
from config import UPLOAD_FOLDER, SUPABASE_ENABLED, SUPABASE_BUCKET

if SUPABASE_ENABLED:
    from supabase_utils import (
        upload_file_to_supabase,
        list_supabase_files,
        download_supabase_file,
        delete_supabase_file,
    )
import streamlit as st
import os
from rag_pipeline import (
    ask_question, generate_policy, gap_analysis, classify_intent, classify_request, reset_runtime_caches,
    clarify_next_question, build_enriched_request,
)
from preprocess_documents import process_one_file
from ingest_to_vectorstore import build_vectorstore, add_sources_to_vectorstore
import re
import tempfile
from pathlib import Path
from uuid import uuid4

MAX_UPLOAD_MB = 50

def _safe_filename(name: str) -> str:
    name = Path(name).name
    name = re.sub(r"[^A-Za-z0-9._ -]", "_", name)
    return name[:180]

def _save_uploaded_file(uploaded_file, upload_dir: str) -> str:
    os.makedirs(upload_dir, exist_ok=True)

    raw = uploaded_file.getbuffer()
    size_mb = len(raw) / (1024 * 1024)
    if size_mb > MAX_UPLOAD_MB:
        raise ValueError(f"{uploaded_file.name} is too large ({size_mb:.1f} MB). Max allowed is {MAX_UPLOAD_MB} MB.")

    safe_name = _safe_filename(uploaded_file.name)
    stem = Path(safe_name).stem
    suffix = Path(safe_name).suffix.lower()

    if suffix not in {".docx", ".pdf"}:
        raise ValueError(f"Unsupported file type: {uploaded_file.name}")

    final_name = f"{stem}_{uuid4().hex[:8]}{suffix}"
    final_path = os.path.join(upload_dir, final_name)

    fd, tmp_path = tempfile.mkstemp(dir=upload_dir, suffix=suffix)
    try:
        with os.fdopen(fd, "wb") as tmp:
            tmp.write(raw)
        os.replace(tmp_path, final_path)   # atomic move
    except Exception:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        finally:
            raise

    return final_path

def _render_mermaid(diagram_code: str):
    html = f"""
    <div class="mermaid">
    {diagram_code}
    </div>
    <script type="module">
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
      mermaid.initialize({{ startOnLoad: true }});
    </script>
    """
    components.html(html, height=500, scrolling=True)

def render_answer_with_mermaid(answer: str):
    # Render both Graphviz (```dot / ```graphviz) and Mermaid (```mermaid) fenced
    # blocks as live diagrams; everything else is markdown. Graphviz is the format
    # used for procedure workflow flowcharts (also embedded into the Word export).
    pattern = re.compile(r"```(dot|graphviz|mermaid)\s*(.*?)```", re.S | re.I)
    pos = 0
    for m in pattern.finditer(answer):
        before = answer[pos:m.start()]
        if before.strip():
            st.markdown(before, unsafe_allow_html=True)
        lang = m.group(1).lower()
        diagram = m.group(2).strip()
        if lang == "mermaid":
            _render_mermaid(diagram)
        else:
            try:
                st.graphviz_chart(diagram)
            except Exception:
                # Fall back to showing the source rather than crashing the chat.
                st.code(diagram, language="dot")
        pos = m.end()
    tail = answer[pos:]
    if tail.strip():
        st.markdown(tail, unsafe_allow_html=True)
# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="P&P Agent", page_icon="📋", layout="wide")

# Preload the embedding model + FAISS/BM25 once per server so the first
# generation/Q&A doesn't pay the cold-start cost. Cached → runs a single time.
@st.cache_resource(show_spinner=False)
def _warm_models():
    # Defensive: a preload failure (e.g. a stale module after an in-place edit)
    # must never block the app from loading. Worst case, the first request just
    # pays the cold-start cost.
    try:
        from rag_pipeline import warm_up
        warm_up()
    except Exception as e:
        print(f"[warmup] skipped: {e}")
    return True
_warm_models()

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown(
    """
<style>
 
/* Keep header visible so sidebar can be reopened */
header[data-testid="stHeader"] { background: transparent !important; }
footer { display: none !important; }
.block-container {
    padding-top: 0.6rem !important;
    padding-bottom: 0 !important;
}
 
/* Header */
.pp-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 8px 4px 10px 4px;
}
.pp-title {
    font-size: 20px;
    font-weight: 700;
    color: #003366;
    margin: 0;
    line-height: 1.2;
}
.pp-subtitle {
    font-size: 11px;
    color: #777;
    margin: 0;
}
.pp-divider {
    height: 2px;
    background: #003366;
    margin: 6px 0 10px 0;
    border-radius: 999px;
}
 
/* Shared card */
.action-panel {
    background: #f4f7ff;
    border: 1px solid #c8d5f0;
    border-radius: 8px;
    padding: 12px 16px 14px 16px;
    margin-bottom: 6px;
}
 
/* Sidebar */
section[data-testid="stSidebar"] .block-container {
    padding-top: 0.8rem !important;
}
 
/* Small toolbar button row near chat input */
.pp-chat-toolbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    margin: 0 0 0.3rem 0;
}
 
/* Slightly tighter popover / expander labels */
div[data-testid="stPopover"] button,
div[data-testid="stExpander"] details summary {
    white-space: nowrap;
}
/* Smaller professional headings inside chat messages */
[data-testid="stChatMessage"] h1 {
    font-size: 1.20rem !important;
    margin-top: 0.5rem !important;
    margin-bottom: 0.25rem !important;
}
[data-testid="stChatMessage"] h2 {
    font-size: 1.05rem !important;
    margin-top: 0.45rem !important;
    margin-bottom: 0.2rem !important;
}
[data-testid="stChatMessage"] h3,
[data-testid="stChatMessage"] h4 {
    font-size: 0.95rem !important;
    margin-top: 0.35rem !important;
    margin-bottom: 0.15rem !important;
}
[data-testid="stChatMessage"] table {
    width: 100% !important;
    border-collapse: collapse !important;
    font-size: 0.88rem !important;
    display: table !important;
    table-layout: auto !important;
}

[data-testid="stChatMessage"] table th,
[data-testid="stChatMessage"] table td {
    border: 1px solid #d9dee7 !important;
    padding: 6px 8px !important;
    vertical-align: top !important;
    white-space: normal !important;
    word-break: break-word !important;
}

[data-testid="stChatMessage"] table th {
    background: #f5f7fb !important;
    font-weight: 600 !important;
}


[data-testid="stChatMessage"] table td strong {
    display: inline-block !important;
    margin-bottom: 2px !important;
}

[data-testid="stChatMessage"] ul,
[data-testid="stChatMessage"] ol {
    padding-left: 1.2rem !important;
    margin-top: 0.2rem !important;
    margin-bottom: 0.45rem !important;
}

[data-testid="stChatMessage"] p {
    margin-bottom: 0.45rem !important;
    line-height: 1.55 !important;
}
</style>
""",
    unsafe_allow_html=True,
)
 
# ── Session state ─────────────────────────────────────────────────────────────
_defaults = {
    "messages": [],
    "last_generated_text": "",
    "last_generated_srcs": [],
    "last_export_enabled": False,
    "last_generated_kind": "",
    "upload_processing": False,
    "current_practices": "",
    "gap_uploaded": "",          # practices text extracted from a chat-attached file
    "sb_file_list": None,
    # ── Conversational clarification state ──
    "clarify_active": False,
    "clarify_mode": "",
    "clarify_original": "",
    "clarify_qa": [],
    "clarify_pending_question": "",
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ── Generate / Gap / clarification runners ─────────────────────────────────────
def _detect_doc_type(text: str) -> str:
    ql = (text or "").lower()
    if "procedure" in ql and "policy" not in ql:
        return "Procedure"
    return "Policy"


def _do_generate(request_text: str, doc_type: str):
    with st.status(f"Generating {doc_type}…", expanded=True) as _status:
        def _progress(msg):
            _status.update(label=f"Generating {doc_type} — {msg}")
        try:
            policy_text, sources = generate_policy(request_text, doc_type=doc_type, progress=_progress)
            _status.update(label=f"✅ {doc_type} generated", state="complete")
        except Exception as e:
            policy_text, sources = f"Error: {e}", []
            _status.update(label="⚠️ Generation failed", state="error")
    st.session_state.last_generated_text = policy_text
    st.session_state.last_generated_srcs = sources
    st.session_state.last_export_enabled = True
    st.session_state.last_generated_kind = doc_type.lower()
    st.session_state.messages.append({
        "role": "assistant",
        "content": policy_text,
        "sources": sources,
        "export_available": True,
    })


def _do_gap(practices: str, topic_text: str):
    with st.status("Running gap analysis…", expanded=True) as _status:
        def _progress(msg):
            _status.update(label=f"Gap analysis — {msg}")
        try:
            report, sources = gap_analysis(current_practices=practices, topic=topic_text, progress=_progress)
            _status.update(label="✅ Gap analysis complete", state="complete")
        except Exception as e:
            report, sources = f"Error: {e}", []
            _status.update(label="⚠️ Gap analysis failed", state="error")
    st.session_state.last_generated_text = report
    st.session_state.last_generated_srcs = sources
    st.session_state.last_export_enabled = True
    st.session_state.last_generated_kind = "gap analysis"
    st.session_state.messages.append({
        "role": "assistant",
        "content": report,
        "sources": sources,
        "export_available": True,
    })


def _finalize_clarification():
    """Synthesize the enriched brief, then run the actual generation / gap analysis."""
    mode     = st.session_state.clarify_mode
    original = st.session_state.clarify_original
    qa       = list(st.session_state.clarify_qa)

    # Clear clarification state first so a rerun cannot re-enter the loop.
    st.session_state.clarify_active = False
    st.session_state.clarify_pending_question = ""

    if qa:
        with st.spinner("Preparing your tailored brief…"):
            try:
                enriched = build_enriched_request(mode, original, qa)
            except Exception:
                enriched = original
    else:
        enriched = original

    if mode == "generate":
        # AI router decides the type from the enriched brief (was brittle regex).
        _, _dt = classify_request(enriched)
        _do_generate(enriched, _dt)
    elif mode == "gap":
        _do_gap(st.session_state.current_practices, enriched)

    st.session_state.clarify_qa = []
    st.session_state.clarify_original = ""
    st.session_state.clarify_mode = ""


def _ask_clarifying_question():
    """Ask the next clarifying question, or finalize when enough info / cap reached."""
    qa = st.session_state.clarify_qa
    if len(qa) >= 5:
        _finalize_clarification()
        return
    with st.spinner("Thinking of the most useful question…"):
        try:
            q = clarify_next_question(
                st.session_state.clarify_mode,
                st.session_state.clarify_original,
                qa,
            )
        except Exception:
            q = ""   # on error, proceed to generation rather than blocking the user
    if not q:
        _finalize_clarification()
    else:
        st.session_state.clarify_pending_question = q
        st.session_state.messages.append({"role": "assistant", "content": q})


def _start_clarification(mode: str, original: str):
    st.session_state.clarify_active           = True
    st.session_state.clarify_mode             = mode
    st.session_state.clarify_original         = original
    st.session_state.clarify_qa               = []
    st.session_state.clarify_pending_question = ""
    _ask_clarifying_question()
 
 
# ── Helpers ───────────────────────────────────────────────────────────────────
def _action_container(label: str):
    """Use popover when available, else fall back to expander."""
    if hasattr(st, "popover"):
        return st.popover(label)
    return st.expander(label, expanded=False)
 


def _extract_text_from_upload(uploaded_file) -> str:
    """
    Extract text from an uploaded DOCX/PDF for gap-analysis 'current practices'.
    Uses the SAME full pipeline as KB ingestion (tables + diagrams/flowcharts captured
    via gpt-5.1 vision / LLMWhisperer), but fully in-memory — nothing is written to the
    knowledge base. Returns "" if no extractable text.
    """
    import os as _os
    import tempfile
    suffix = Path(uploaded_file.name).suffix.lower()
    if suffix not in (".docx", ".pdf"):
        raise ValueError(f"Unsupported file type: {uploaded_file.name}")

    fd, tmp = tempfile.mkstemp(suffix=suffix)
    _os.close(fd)
    try:
        with open(tmp, "wb") as f:
            f.write(uploaded_file.getvalue())

        from preprocess_documents import process_docx, process_pdf, run_vision
        sections = (process_docx(tmp) if suffix == ".docx" else process_pdf(tmp))[0]

        # Capture diagrams / flowcharts / images via the same vision pass as KB ingestion
        # (no-op when the document has no images, e.g. LLMWhisperer-parsed PDFs).
        try:
            run_vision(sections)
        except Exception:
            pass

        parts = [str(line) for s in sections for line in s.lines if line and str(line).strip()]
        return "\n".join(parts).strip()
    finally:
        try:
            _os.unlink(tmp)
        except Exception:
            pass


def _ingest_files_to_kb(files) -> tuple:
    """
    Add attached file(s) to the knowledge base: preprocess + incremental index.
    Used when a document is attached in the chat in a non-Gap mode.
    Returns (added_labels, errors).
    """
    added, errs = [], []
    saved = []
    for f in files:
        try:
            path = _save_uploaded_file(f, UPLOAD_FOLDER)
            saved.append((path, _safe_filename(f.name)))
        except Exception as e:
            errs.append(f"{f.name}: {e}")

    log_box = st.empty()
    logs = []

    def _log(m):
        logs.append(str(m))
        log_box.code("\n".join(logs[-30:]), language="")

    with st.spinner("Adding to the knowledge base (preprocess + index)…"):
        for path, label in saved:
            try:
                process_one_file(
                    path, dry_run=False, log_fn=_log,
                    continue_on_warning=True, source_label_override=label,
                )
                added.append(label)
            except Exception as e:
                errs.append(f"{label}: {e}")
        if added:
            try:
                add_sources_to_vectorstore(added, log_fn=_log)
                reset_runtime_caches()
            except Exception as e:
                errs.append(f"index update: {e}")
    return added, errs


def _render_gap_panel():
    st.markdown('<div class="action-panel">', unsafe_allow_html=True)
    st.markdown("**📊 Gap Analysis — Current Practices**")
    st.caption(
        "Paste your current practices here, **or attach a document (📎) in the chat box "
        "below**. Then type your gap analysis question in the chat."
    )

    _typed = st.text_area(
        "current_practices_input",
        height=150,
        placeholder=(
            "Example: We currently approve invoices verbally for amounts under SAR 10,000. "
            "No formal vendor onboarding checklist. Payments within 30 days, "
            "no dispute escalation path..."
        ),
        label_visibility="collapsed",
        key="gap_textarea",
    )
    # Effective practices: pasted text wins; otherwise fall back to a doc attached in chat.
    st.session_state.current_practices = _typed.strip() or st.session_state.get("gap_uploaded", "")
    if st.session_state.current_practices.strip():
        st.success("✅ Current practices saved — ask your gap analysis question in the chat.")
    st.markdown("</div>", unsafe_allow_html=True)


def _render_upload_panel():
    st.markdown('<div class="action-panel">', unsafe_allow_html=True)
    st.markdown("**🔄 Reindex VectorDB** — add documents to the knowledge base")
 
    # ── Show tabs if Supabase is configured, else just local upload ───────────
    if SUPABASE_ENABLED:
        tab_local, tab_sb = st.tabs(["💻 Local Upload", "☁️ Supabase Storage"])
    else:
        tab_local = st.container()
        tab_sb    = None
 
    # ══════════════════════════════════════════════════════════════════════════
    # LOCAL UPLOAD — your original behaviour, unchanged
    # ══════════════════════════════════════════════════════════════════════════
    with tab_local:
        st.caption("Upload files directly from your computer.")
 
        up_files = st.file_uploader(
            "upload_docs",
            type=["docx", "pdf"],
            accept_multiple_files=True,
            label_visibility="collapsed",
            key="panel_uploader",
        )
 
        process_now = st.button(
            "⚙️ Preprocess + Add to Index",
            use_container_width=True,
            type="primary",
            disabled=st.session_state.upload_processing,
            key="local_process_btn",
        )
 
        if up_files:
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            saved_items = []
            for f in up_files:
                saved_path = _save_uploaded_file(f, UPLOAD_FOLDER)
                logical_source = _safe_filename(f.name)
                saved_items.append((saved_path, logical_source))
 
            st.success(f"✅ {len(up_files)} file(s) saved to `{UPLOAD_FOLDER}/`")
 
            if process_now:
                st.session_state.upload_processing = True
                log_box = st.empty()
                logs = []
 
                def log_fn(msg: str):
                    logs.append(str(msg))
                    log_box.code("\n".join(logs[-40:]), language="")
 
                try:
                    for path, logical_source in saved_items:
                        log_fn(f"Processing: {logical_source}")
                        process_one_file(
                            path,
                            dry_run=False,
                            log_fn=log_fn,
                            continue_on_warning=True,
                            source_label_override=logical_source,
                        )
 
                    log_fn("Updating vectorstore (incremental)...")
                    add_sources_to_vectorstore(
                        [logical_source for _, logical_source in saved_items],
                        log_fn=log_fn,
                    )
                    reset_runtime_caches()
                    log_fn("Done.")
                    st.success("✅ Upload complete, preprocessing complete, and vectorstore updated.")
                except Exception as e:
                    st.error(
                        "Preprocessing finished, but vectorstore rebuild failed. "
                        f"Most likely cause: embedding model/network issue. Details: {e}"
                    )
                finally:
                    st.session_state.upload_processing = False
 
    # ══════════════════════════════════════════════════════════════════════════
    # SUPABASE STORAGE TAB
    # ══════════════════════════════════════════════════════════════════════════
    if SUPABASE_ENABLED and tab_sb is not None:
        with tab_sb:
            st.caption(f"Files stored in Supabase bucket: **{SUPABASE_BUCKET}**")
 
            # ── Upload new files to Supabase ──────────────────────────────────
            st.markdown("**Upload new files:**")
            sb_up_files = st.file_uploader(
                "supabase_upload",
                type=["docx", "pdf"],
                accept_multiple_files=True,
                label_visibility="collapsed",
                key="supabase_uploader",
            )
 
            col1, col2 = st.columns(2)
            upload_only_btn    = col1.button(
                "☁️ Upload Only",
                use_container_width=True,
                key="sb_upload_only",
            )
            upload_process_btn = col2.button(
                "⚙️ Upload + Process",
                use_container_width=True,
                type="primary",
                key="sb_upload_process",
                disabled=st.session_state.upload_processing,
            )
 
            if sb_up_files and (upload_only_btn or upload_process_btn):
                uploaded_names = []
                with st.spinner("Uploading to Supabase..."):
                    for f in sb_up_files:
                        try:
                            safe_name = _safe_filename(f.name)
                            upload_file_to_supabase(
                                file_bytes=f.getvalue(),
                                filename=safe_name,
                                bucket=SUPABASE_BUCKET,
                            )
                            uploaded_names.append(safe_name)
                            st.success(f"✅ Uploaded: {f.name}")
                        except Exception as e:
                            st.error(f"❌ Failed: {f.name} — {e}")
 
                if upload_process_btn and uploaded_names:
                    st.session_state.upload_processing = True
                    log_box2 = st.empty()
                    logs2    = []
 
                    def sb_log(msg: str):
                        logs2.append(str(msg))
                        log_box2.code("\n".join(logs2[-40:]), language="")
 
                    try:
                        for filename in uploaded_names:
                            sb_log(f"Downloading from Supabase: {filename}")
                            tmp_path = download_supabase_file(filename, SUPABASE_BUCKET)
                            try:
                                sb_log(f"Processing: {filename}")
                                process_one_file(
                                    tmp_path,
                                    dry_run=False,
                                    log_fn=sb_log,
                                    continue_on_warning=True,
                                    source_label_override=filename,
                                )
                            finally:
                                os.unlink(tmp_path)
 
                        sb_log("Updating vectorstore (incremental)...")
                        add_sources_to_vectorstore(uploaded_names, log_fn=sb_log)
                        reset_runtime_caches()
                        sb_log("Done.")
                        st.success("✅ Files uploaded, preprocessed, and KB updated.")
                        st.session_state.sb_file_list = None  # force refresh
                    except Exception as e:
                        st.error(f"Processing error: {e}")
                    finally:
                        st.session_state.upload_processing = False
 
            st.divider()
 
            # ── Files already in Supabase ─────────────────────────────────────
            st.markdown("**Files in Supabase bucket:**")
 
            if st.button("🔄 Refresh list", key="sb_refresh", use_container_width=True):
                st.session_state.sb_file_list = None
 
            if st.session_state.sb_file_list is None:
                with st.spinner("Loading..."):
                    st.session_state.sb_file_list = list_supabase_files(SUPABASE_BUCKET)
 
            sb_files = st.session_state.sb_file_list or []
 
            if not sb_files:
                st.info("No files in Supabase yet. Upload some above.")
            else:
                st.caption(f"{len(sb_files)} file(s) in bucket")
                selected = []
                for f in sb_files:
                    col_chk, col_info = st.columns([0.08, 0.92])
                    checked = col_chk.checkbox(
                        "", key=f"sb_chk_{f['name']}",
                        label_visibility="collapsed",
                    )
                    size_str = f"{f['size_mb']} MB" if f["size_mb"] else ""
                    col_info.markdown(f"📄 **{f['name']}** {size_str} {f['last_modified']}")
                    if checked:
                        selected.append(f["name"])
 
                if selected:
                    col_p, col_d = st.columns(2)
                    proc_btn = col_p.button(
                        f"⚙️ Process {len(selected)} file(s)",
                        use_container_width=True,
                        type="primary",
                        key="sb_proc_sel",
                        disabled=st.session_state.upload_processing,
                    )
                    del_btn = col_d.button(
                        f"🗑️ Delete {len(selected)} file(s)",
                        use_container_width=True,
                        key="sb_del_sel",
                    )
 
                    if proc_btn:
                        st.session_state.upload_processing = True
                        log_box3 = st.empty()
                        logs3    = []
 
                        def proc_log(msg: str):
                            logs3.append(str(msg))
                            log_box3.code("\n".join(logs3[-40:]), language="")
 
                        try:
                            for filename in selected:
                                proc_log(f"Downloading: {filename}")
                                tmp_path = download_supabase_file(filename, SUPABASE_BUCKET)
                                try:
                                    proc_log(f"Processing: {filename}")
                                    process_one_file(
                                        tmp_path,
                                        dry_run=False,
                                        log_fn=proc_log,
                                        continue_on_warning=True,
                                        source_label_override=filename,
                                    )
                                finally:
                                    os.unlink(tmp_path)
 
                            proc_log("Updating vectorstore (incremental)...")
                            add_sources_to_vectorstore(selected, log_fn=proc_log)
                            reset_runtime_caches()
                            proc_log("Done.")
                            st.success("✅ Selected files processed and KB updated.")
                        except Exception as e:
                            st.error(f"Processing error: {e}")
                        finally:
                            st.session_state.upload_processing = False
 
                    if del_btn:
                        deleted = 0
                        for filename in selected:
                            if delete_supabase_file(filename, SUPABASE_BUCKET):
                                deleted += 1
                        st.success(f"✅ Deleted {deleted} file(s) from Supabase.")
                        st.session_state.sb_file_list = None
                        st.rerun()
 
    st.markdown("</div>", unsafe_allow_html=True)
# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR — mode + upload + word export
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    #try:
        #st.image("logo.png", width=110)
    #except Exception:
    #st.markdown("### 📋")
    st.markdown("#### Policy & Procedure Agent")
    st.markdown("---")
 
    st.markdown("**Mode**")
    mode = st.radio(
        "mode_sel",
        ["Auto-detect", "Q&A", "Generate Policy / Procedure", "Gap Analysis"],
        index=0,
        label_visibility="collapsed",
        help="Auto-detect picks the right mode from your message automatically.",
    )

    clarify_enabled = st.checkbox(
        "Ask clarifying questions first",
        value=True,
        help=(
            "When generating a policy/procedure or running a gap analysis, the assistant "
            "asks a few targeted questions first to tailor the output. Detailed requests "
            "may skip straight to generation."
        ),
    )
 
    st.markdown("---")
    st.markdown("**Reindex VectorDB**")
    with _action_container("🔄 Reindex VectorDB"):
        _render_upload_panel()
 
    st.markdown("---")
    st.markdown("**Export to Word**")
    if st.session_state.last_export_enabled and st.session_state.last_generated_text:
        dept = st.text_input("Department", value="", key="exp_dept")
        doc_number = st.text_input("Doc number", value="POL-001", key="exp_doc")
        version = st.text_input("Version", value="1.0", key="exp_ver")
        owner = st.text_input("Owner", value="Policy Owner", key="exp_own")
        approver = st.text_input("Approved by", value="Compliance Head", key="exp_app")
        try:
            docx_bytes = generate_word_doc(
                policy_text=st.session_state.last_generated_text,
                sources=st.session_state.last_generated_srcs,
                department=dept,
                doc_number=doc_number,
                version=version,
                owner=owner,
                approver=approver,
                document_type=st.session_state.last_generated_kind.upper() if st.session_state.last_generated_kind else "",
            )
            st.download_button(
                "⬇ Download Word Document",
                docx_bytes,
                file_name=f"{doc_number}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
                type="primary",
            )
        except Exception as e:
            st.error(f"Export error: {e}")
    else:
        st.caption("Generate a policy or gap analysis first.")
 
# ═══════════════════════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════════════════════
try:
    import base64
 
    logo_b64 = base64.b64encode(open("logo.png", "rb").read()).decode()
    logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:28px;width:auto;">'
except Exception:
    logo_html = '<span style="font-size:26px">📋</span>'
 
st.markdown(
    f"""
<div class="pp-header">
    {logo_html}
    <div>
        <p class="pp-title">Policy &amp; Procedure Agent</p>
        <p class="pp-subtitle">Knowledge base · Web search fallback · Word export</p>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
 
st.markdown('<div class="pp-divider"></div>', unsafe_allow_html=True)
 
# ═══════════════════════════════════════════════════════════════════════════════
# CHAT HISTORY
# ═══════════════════════════════════════════════════════════════════════════════
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        render_answer_with_mermaid(msg["content"])
        if msg.get("sources"):
            with st.expander("📄 Sources", expanded=False):
                for s in msg["sources"]:
                    st.write(f"- {s}")
        if msg.get("web_used"):
            st.warning(
                "⚠️ Answer from **web search** — not from company policy documents. "
                "Verify with your compliance team.",
                icon="🌐",
            )
        if msg.get("export_available") and st.session_state.last_export_enabled:
            st.info("💡 Use **Export to Word** in the sidebar to download this document.")
 
# (Removed: the floating "📊 Gap" panel near the chat. Gap analysis now takes its
#  current-practices document straight from a chat 📎 upload — no separate panel.)

# ── Clarification progress + skip control ─────────────────────────────────────
if st.session_state.clarify_active:
    _answered = len(st.session_state.clarify_qa)
    _kind_lbl = "gap analysis" if st.session_state.clarify_mode == "gap" else "document"
    st.caption(f"🧭 Scoping your {_kind_lbl} — {_answered}/5 questions answered.")
    if st.button("✅ Generate now (skip remaining questions)", use_container_width=True):
        _finalize_clarification()
        st.rerun()

# ── Chat input (inline 📎 attach = gap-analysis current practices) ────────────
if st.session_state.clarify_active:
    _chat_placeholder = "Type your answer…"
elif mode == "Gap Analysis":
    _chat_placeholder = "Ask your gap question — or attach your current-practices doc (📎)…"
else:
    _chat_placeholder = "Ask a question — or attach a document (📎) to add it to the knowledge base…"

chat_val = st.chat_input(
    _chat_placeholder,
    accept_file=True,
    file_type=["docx", "pdf"],
)

if chat_val:
    # With accept_file, st.chat_input returns an object with .text and .files
    if isinstance(chat_val, str):
        query, _uploaded = chat_val, []
    else:
        query, _uploaded = (chat_val.text or ""), (chat_val.files or [])

    # ── Mid-clarification: capture the message as an answer, then continue ──
    if st.session_state.clarify_active:
        st.session_state.messages.append({"role": "user", "content": query or "(continue)"})
        st.session_state.clarify_qa.append({
            "question": st.session_state.clarify_pending_question,
            "answer": query,
        })
        _ask_clarifying_question()
        st.rerun()

    # ── Attached file — route by mode ──
    _attached_practice = False
    if _uploaded:
        if mode == "Gap Analysis":
            # Light: use the document as gap-analysis current practices.
            try:
                with st.spinner("Extracting text from attached document…"):
                    _extracted = _extract_text_from_upload(_uploaded[0])
                if _extracted:
                    st.session_state.gap_uploaded = _extracted
                    st.session_state.current_practices = _extracted
                    _attached_practice = True
                else:
                    st.session_state.messages.append({"role": "assistant", "content": (
                        "⚠️ Couldn't extract text from that file (it may be scanned/image-only). "
                        "Try a text-based DOCX/PDF, or paste the practices into your message."
                    )})
            except Exception as e:
                st.session_state.messages.append(
                    {"role": "assistant", "content": f"Could not read attachment: {e}"}
                )
        else:
            # Heavy: add the document(s) to the knowledge base, then end this turn.
            _names = ", ".join(f.name for f in _uploaded)
            st.session_state.messages.append({"role": "user", "content": (
                (f"{query}\n\n📎 *{_names}*").strip() if query.strip()
                else f"📎 Uploaded **{_names}**"
            )})
            _added, _errs = _ingest_files_to_kb(_uploaded)
            if _added:
                st.session_state.messages.append({"role": "assistant", "content": (
                    f"✅ Added to the knowledge base: **{', '.join(_added)}**. "
                    "You can now ask questions about it."
                )})
            for _e in _errs:
                st.session_state.messages.append({"role": "assistant", "content": f"❌ {_e}"})
            st.rerun()

    current_practices = st.session_state.current_practices

    # Record the user's message (note the attachment if it was gap practices)
    if _attached_practice:
        _fname = _uploaded[0].name
        _user_msg = (f"{query}\n\n📎 *{_fname}*").strip() if query.strip() \
            else f"📎 Uploaded **{_fname}** as current practices"
    else:
        _user_msg = query
    st.session_state.messages.append({"role": "user", "content": _user_msg})

    # Intent — AI router decides intent + document type (regex fallback inside).
    auto_doc_type = None
    if mode == "Auto-detect":
        intent, auto_doc_type = classify_request(query, has_practices=bool(current_practices.strip()))
    elif mode == "Q&A":
        intent = "qa"
    elif mode == "Generate Policy / Procedure":
        intent = "generate"
    elif mode == "Gap Analysis":
        intent = "gap"
    else:
        intent = "qa"

    # A document attached in Gap mode signals a gap analysis.
    if _attached_practice:
        intent = "gap"
        if not query.strip():
            query = "Perform a gap analysis of the attached current practices against our policies."

    # ── Route generate / gap through conversational clarification first ──
    if intent in ("generate", "gap") and clarify_enabled and not st.session_state.clarify_active:
        if intent == "gap" and not current_practices.strip():
            st.session_state.messages.append({"role": "assistant", "content": (
                "To run a gap analysis, attach your current-practices document (📎) in the "
                "chat box, then ask your question."
            )})
            st.rerun()
        _start_clarification(intent, query)
        st.rerun()
 
    #with st.chat_message("assistant"):
 
        # ── Q&A + scenario + web fallback (Req 1,2,4,5) ──────────────────────
    if intent == "qa":
        with st.spinner("Searching knowledge base…"):
            try:
                answer, sources, search_mode = ask_question(query)
            except Exception as e:
                answer, sources, search_mode = f"Error: {e}", [], "none"
 
        render_answer_with_mermaid(answer)
 
        st.session_state.last_generated_text = ""
        st.session_state.last_generated_srcs = []
        st.session_state.last_export_enabled = False
        st.session_state.last_generated_kind = ""
        st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": sources,
                    "web_used": (search_mode == "web"),
                }
            )
        st.rerun()
        # ── Generate procedure (Req 3) ────────────────────────────────────────
    elif intent == "generate":
        # Document type comes from the AI router (auto-detect). In the explicit
        # "Generate" mode the router didn't run, so ask it now (cheap Haiku call).
        if auto_doc_type:
            doc_type = auto_doc_type
        else:
            _, doc_type = classify_request(query)

        import time as _time
        _gen_t0 = _time.time()
        with st.status(f"Generating {doc_type}…", expanded=True) as _status:
            def _progress(msg):
                _status.update(label=f"Generating {doc_type} — {msg}")
            try:
                policy_text, sources = generate_policy(query, doc_type=doc_type, progress=_progress)
                _status.update(label=f"✅ {doc_type} generated", state="complete")
            except Exception as e:
                policy_text, sources = f"Error: {e}", []
                _status.update(label="⚠️ Generation failed", state="error")
        _gen_secs = _time.time() - _gen_t0

        st.session_state.last_generated_text = policy_text
        st.session_state.last_generated_srcs = sources
        st.session_state.last_export_enabled = True
        st.session_state.last_generated_kind = doc_type.lower()
        st.info(f"✅ {doc_type} generated in {_gen_secs:.0f}s ({_gen_secs/60:.1f} min). "
                f"Use **Export to Word** in the sidebar to download it.")
        st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": policy_text,
                    "sources": sources,
                    "export_available": True,
                }
            )
        st.rerun()
 
        # ── Gap analysis (Req 6) ──────────────────────────────────────────────
    elif intent == "gap":
        if not current_practices.strip():
            msg = (
                    "To run a gap analysis, attach your current-practices document (📎) "
                    "in the chat box, then ask your question."
                )
            #st.warning(msg)
            st.session_state.messages.append({"role": "assistant", "content": msg})
            st.rerun()
        else:
            with st.status("Running gap analysis…", expanded=True) as _status:
                def _progress(msg):
                    _status.update(label=f"Gap analysis — {msg}")
                try:
                    report, sources = gap_analysis(
                        current_practices=current_practices,
                        topic=query,
                        progress=_progress,
                        )
                    _status.update(label="✅ Gap analysis complete", state="complete")
                except Exception as e:
                    report, sources = f"Error: {e}", []
                    _status.update(label="⚠️ Gap analysis failed", state="error")
 
            st.markdown(report)
 
            if sources:
                with st.expander("📄 Policy documents referenced", expanded=False):
                    for s in sources:
                        st.write(f"- {s}")
 
            st.session_state.last_generated_text = report
            st.session_state.last_generated_srcs = sources
            st.session_state.last_export_enabled = True
            st.session_state.last_generated_kind = "gap analysis"   
            st.info("✅ Gap analysis complete. Use **Export to Word** in the sidebar.")
            st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": report,
                        "sources": sources,
                        "export_available": True,
                    }
                )
            st.rerun() 
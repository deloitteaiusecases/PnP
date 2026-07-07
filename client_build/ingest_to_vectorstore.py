"""
ingest_to_vectorstore.py — Build FAISS vectorstore from knowledge_base/

CRITICAL DESIGN DECISIONS (do not change without understanding these):

1. NO RE-SPLITTING: preprocess_documents.py already produced correctly-sized
   semantic chunks with structural boundaries respected and table integrity
   preserved. Re-splitting with RecursiveCharacterTextSplitter would destroy
   that work (cuts RACI tables mid-row, splits policy statements from headings).
   Each .md file → exactly ONE LangChain Document. No further splitting.

2. RECURSIVE WALK: preprocess_documents.py saves to nested subfolders:
   knowledge_base/<dept>/<NNN>_<section>.md
   Must walk recursively, not glob flat.

3. FRONTMATTER PARSING: preprocess_documents.py writes CAPITAL-key frontmatter:
   Department: ..., Section: ..., Source: ..., Chunk: ..., Chunk_Name: ...
   These are stored as LOWERCASE metadata keys in the vectorstore for
   consistent access in rag_pipeline.py.

4. CHUNK ORDERING: files are named with NNN_ prefix (001_, 002_...).
   The chunk_order metadata preserves this for full-document assembly in
   rag_pipeline.py.

Run:
    python ingest_to_vectorstore.py             # full build (first-time / rebuild)
    python ingest_to_vectorstore.py --clear     # wipe and rebuild from scratch
    python ingest_to_vectorstore.py --sync      # add ONLY new files dropped into knowledge_base/
                                                #   (incremental — no full re-embed)
    python ingest_to_vectorstore.py --source "My Doc.docx" "Other.pdf"
                                                # (re)ingest specific source(s) incrementally

Typical no-GUI workflow:
    1. Drop the preprocessed .md chunk(s) into knowledge_base/<dept>/...
    2. python ingest_to_vectorstore.py --sync

Prerequisites:
    python preprocess_documents.py --folder raw_data/   (or your DOCX folder)
"""

import os, re, pickle, argparse, shutil
from pathlib import Path

from config import (
    KNOWLEDGE_BASE_PATH,
    VECTORSTORE_PATH,
    EMBEDDING_MODEL,
)

os.makedirs(VECTORSTORE_PATH, exist_ok=True)


def _parse_frontmatter(raw: str) -> tuple:
    """
    Parse YAML-style frontmatter from preprocess_documents.py output.
    Returns (metadata_dict, body_text).
    Handles capital keys: Department, Section, Source, Chunk, Chunk_Name, Images.
    """
    meta = {}
    body = raw

    if raw.startswith("---"):
        parts = raw.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                line = line.strip()
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip().lower()] = v.strip()
            body = parts[2].strip()

    return meta, body


def _extract_chunk_order(filepath: Path) -> int:
    """Extract the NNN prefix number from filename for ordering."""
    m = re.match(r"(\d+)", filepath.name)
    return int(m.group(1)) if m else 9999


def _build_embeddings():
    """Local, free sentence-transformers embeddings (no API key needed)."""
    from langchain_huggingface import HuggingFaceEmbeddings
    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def _doc_from_md(fp: Path):
    """Parse one KB .md file into a LangChain Document, or None if unreadable/too small."""
    from langchain_core.documents import Document
    try:
        raw = fp.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  SKIP (read error): {fp.name}: {e}")
        return None

    meta, body = _parse_frontmatter(raw)

    # Defense-in-depth: strip any leftover extraction-error placeholders so they
    # never pollute the index. Older chunks (built before quarantine) may contain
    # lines like "[VISION_ERROR: ...]"; drop those lines here.
    if any(m in body for m in ("[VISION_ERROR", "[VISION_FAILED", "[FLOWCHART_PARSE_ERROR")):
        body = "\n".join(
            ln for ln in body.split("\n")
            if not ln.lstrip().startswith(("[VISION_ERROR", "[VISION_FAILED", "[FLOWCHART_PARSE_ERROR"))
        ).strip()

    # Skip empty or near-empty chunks (headers without content)
    if len(body.strip()) < 40:
        return None

    # Build normalised metadata for rag_pipeline.py — all keys lowercase.
    chunk_order = _extract_chunk_order(fp)

    # Some older chunks come from a different extraction script and use alternate
    # frontmatter keys: `Source_Document` / `Page_Number` instead of `Source` / `Section`.
    # Normalise those so source attribution and incremental updates work for them too.
    source = meta.get("source") or meta.get("source_document") or fp.name
    section = meta.get("section") or (
        f"Page {meta.get('page_number')}" if meta.get("page_number") else ""
    )

    doc_meta = {k: v for k, v in meta.items()}
    doc_meta.update({
        "source": source,
        "section": section,
        "department": meta.get("department", ""),
        "chunk_name": meta.get("chunk_name", ""),
        "chunk_num": meta.get("chunk", meta.get("page_number", "")),
        "chunk_order": chunk_order,
        "file": fp.name,
        "document_title": meta.get("document_title", ""),
        "document_view": meta.get("document_view", "full"),
        "document_class": meta.get("document_class", "section_chunk"),
        "is_full_document": str(meta.get("is_full_document", "false")).lower(),
        "section_priority": meta.get("section_priority", "normal").lower(),
        "section_kind": meta.get("section_kind", "core").lower(),})

    # CRITICAL: do NOT further split the body — each chunk is already complete.
    return Document(page_content=body, metadata=doc_meta)


def _load_docs_from_kb(only_sources=None):
    """
    Load KB .md files into Documents.
    only_sources: optional iterable of source labels — when given, only chunks whose
    `source` metadata is in it are returned (used by incremental ingestion).
    """
    kb_path = Path(KNOWLEDGE_BASE_PATH)
    if not kb_path.exists():
        return []

    # Walk recursively — preprocess saves to knowledge_base/<dept>/*.md
    md_files = sorted(kb_path.rglob("*.md"))
    src_filter = set(only_sources) if only_sources is not None else None

    docs = []
    for fp in md_files:
        doc = _doc_from_md(fp)
        if doc is None:
            continue
        if src_filter is not None and doc.metadata.get("source") not in src_filter:
            continue
        docs.append(doc)
    return docs


def _save_bm25_corpus(vs) -> int:
    """
    Regenerate all_docs.pkl from the LIVE FAISS docstore so the BM25 corpus in
    rag_pipeline.py always matches the vector index exactly (after add/delete).
    """
    all_docs = list(vs.docstore._dict.values())
    pkl_path = Path(VECTORSTORE_PATH) / "all_docs.pkl"
    with open(pkl_path, "wb") as f:
        pickle.dump(all_docs, f)
    return len(all_docs)


def build_vectorstore(log_fn=None):
    """Full rebuild from the entire knowledge_base/ folder."""
    _log = log_fn or print
    from langchain_community.vectorstores import FAISS

    kb_path = Path(KNOWLEDGE_BASE_PATH)
    if not kb_path.exists():
        _log(f"ERROR: knowledge_base/ not found at {kb_path}")
        _log("Run: python preprocess_documents.py --folder raw_data/")
        return

    docs = _load_docs_from_kb()
    if not docs:
        _log("ERROR: No usable .md chunks found. Check preprocessing output.")
        _log("Run: python preprocess_documents.py --folder raw_data/")
        return

    _log(f"\nLoaded {len(docs)} chunks from {kb_path}")

    # Per-source summary
    sources: dict = {}
    for d in docs:
        src = d.metadata["source"]
        sources[src] = sources.get(src, 0) + 1
    _log(f"  TOTAL: {len(docs)} chunks from {len(sources)} source documents")

    _log(f"Building embeddings with {EMBEDDING_MODEL} (first run downloads ~90MB model)...")
    embeddings = _build_embeddings()

    _log("Building FAISS index...")
    vs = FAISS.from_documents(docs, embeddings)
    vs.save_local(VECTORSTORE_PATH)
    n = _save_bm25_corpus(vs)
    _log(f"  ✅ Vectorstore built — {n} chunks → {VECTORSTORE_PATH}/")


def add_sources_to_vectorstore(source_labels, log_fn=None):
    """
    Incrementally add (or update) ONLY the given source documents — without
    re-embedding the entire knowledge base.

    - If no index exists yet, falls back to a full build (the first build anyway).
    - Otherwise loads the existing FAISS index, removes any existing vectors for
      these sources first (so re-uploading/updating a file leaves no stale duplicate
      chunks), then embeds and adds only the new chunks for these sources.
    - Regenerates all_docs.pkl from the live index so BM25 stays in sync.

    source_labels: list of source labels exactly as written into chunk frontmatter
                   (the `source_label_override` passed to process_one_file).
    """
    _log = log_fn or print
    from langchain_community.vectorstores import FAISS

    source_set = set(source_labels)
    vs_path = Path(VECTORSTORE_PATH)
    index_exists = (vs_path / "index.faiss").exists()

    # First-ever build: do a full build so nothing already in the KB is missed.
    if not index_exists:
        _log("  [incremental] no existing index — building from full knowledge base")
        return build_vectorstore(log_fn=_log)

    new_docs = _load_docs_from_kb(only_sources=source_set)
    embeddings = _build_embeddings()
    vs = FAISS.load_local(str(vs_path), embeddings, allow_dangerous_deserialization=True)

    # 1) Remove old vectors for these sources (re-upload / update safety).
    ids_to_delete = [
        doc_id for doc_id, doc in vs.docstore._dict.items()
        if doc.metadata.get("source") in source_set
    ]
    if ids_to_delete:
        vs.delete(ids_to_delete)
        _log(f"  [incremental] removed {len(ids_to_delete)} old vector(s) for updated source(s)")

    # 2) Add the new chunks for these sources.
    if new_docs:
        vs.add_documents(new_docs)
        _log(f"  [incremental] added {len(new_docs)} new chunk(s)")
    else:
        _log("  [incremental] no new chunks for these source(s) — treated as removal")

    vs.save_local(str(vs_path))
    total = _save_bm25_corpus(vs)
    _log(f"  ✅ Vectorstore updated — {total} chunks total (no full rebuild)")


def _kb_sources() -> set:
    """Set of every `source` label currently present in knowledge_base/ .md chunks."""
    return {d.metadata["source"] for d in _load_docs_from_kb()}


def _indexed_sources() -> set:
    """Set of every `source` label currently present in the live FAISS index."""
    from langchain_community.vectorstores import FAISS

    vs_path = Path(VECTORSTORE_PATH)
    if not (vs_path / "index.faiss").exists():
        return set()
    embeddings = _build_embeddings()
    vs = FAISS.load_local(str(vs_path), embeddings, allow_dangerous_deserialization=True)
    return {
        doc.metadata.get("source")
        for doc in vs.docstore._dict.values()
        if doc.metadata.get("source")
    }


def sync_new_sources(log_fn=None):
    """
    Incrementally index any source document that is present in knowledge_base/ but
    not yet in the FAISS index — i.e. files you dropped into the folder manually.
    No full re-embed of the existing knowledge base.
    """
    _log = log_fn or print

    # If there's no index yet, the first build has to embed everything anyway.
    if not (Path(VECTORSTORE_PATH) / "index.faiss").exists():
        _log("No existing index — doing a full build first.")
        return build_vectorstore(log_fn=_log)

    kb = _kb_sources()
    if not kb:
        _log("ERROR: No usable .md chunks found in knowledge_base/. Nothing to sync.")
        _log("If you dropped a raw DOCX/PDF, run preprocess_documents.py first.")
        return

    new_sources = sorted(kb - _indexed_sources())
    if not new_sources:
        _log("Index already up to date — no new sources found in knowledge_base/.")
        return

    _log(f"Found {len(new_sources)} new source(s) to add:")
    for s in new_sources:
        _log(f"   • {s}")
    add_sources_to_vectorstore(new_sources, log_fn=_log)


def main():
    parser = argparse.ArgumentParser(
        description="Build FAISS+BM25 vectorstore from preprocessed knowledge base"
    )
    parser.add_argument("--clear", action="store_true",
                        help="Wipe existing vectorstore and rebuild from scratch")
    parser.add_argument("--sync", action="store_true",
                        help="Incrementally index only NEW files found in knowledge_base/ "
                             "(no full re-embed). Use after manually dropping in a file.")
    parser.add_argument("--source", nargs="+", metavar="LABEL",
                        help="Incrementally (re)ingest specific source label(s) — exactly as "
                             "written in the chunk frontmatter `Source:` field.")
    args = parser.parse_args()

    if args.clear and Path(VECTORSTORE_PATH).exists():
        shutil.rmtree(VECTORSTORE_PATH)
        print(f"Cleared: {VECTORSTORE_PATH}")
        os.makedirs(VECTORSTORE_PATH, exist_ok=True)

    if args.source:
        add_sources_to_vectorstore(args.source)
    elif args.sync:
        sync_new_sources()
    else:
        build_vectorstore()


if __name__ == "__main__":
    main()

"""
process_and_ingest.py — One-shot CLI: preprocess raw doc(s) → incrementally index.

This is the command-line equivalent of what the app's "Preprocess + Add to Index"
button does: it takes a RAW document (.docx / .pdf), runs the full preprocessing
pipeline (tables, gpt-5.1 vision for diagrams, chunking into knowledge_base/), and
then adds ONLY that document to the FAISS + BM25 index — no full re-embed.

Use this when you want to add a document without opening the GUI.

Run:
    # one raw file
    python process_and_ingest.py --file "raw_data\\New Policy.docx"

    # several raw files
    python process_and_ingest.py --file "raw_data\\A.docx" "raw_data\\B.pdf"

    # every .docx/.pdf in a folder (default: raw_data/)
    python process_and_ingest.py --folder raw_data

Notes:
    - The `source` label written into the chunks (and used to de-dupe on re-runs) is
      the file's name, e.g. "New Policy.docx" — re-running with the same file cleanly
      replaces its old chunks/vectors instead of duplicating them.
    - If you ALREADY have preprocessed .md chunks in knowledge_base/ and just want to
      index them, use `python ingest_to_vectorstore.py --sync` instead (no preprocessing).
    - LibreOffice must be installed for embedded Visio/EMF diagram extraction.
"""

import os
import sys
import argparse
import traceback
from pathlib import Path

from preprocess_documents import process_one_file, RAW_DOCS_FOLDER
from ingest_to_vectorstore import add_sources_to_vectorstore


def _collect_targets(files, folder) -> list:
    """Resolve the --file / --folder arguments into a concrete list of raw doc paths."""
    if files:
        return [str(Path(f)) for f in files]

    folder_path = Path(folder)
    if not folder_path.exists():
        print(f"ERROR: folder not found: {folder_path}")
        sys.exit(1)

    targets = sorted(
        str(f) for f in folder_path.rglob("*")
        if f.suffix.lower() in (".docx", ".pdf")
    )
    if not targets:
        print(f"No DOCX or PDF files found in {folder_path}/")
        sys.exit(0)
    return targets


def process_and_ingest(files=None, folder=RAW_DOCS_FOLDER, log_fn=None):
    """
    Preprocess each raw document then incrementally index the ones that succeeded.
    Returns (added_source_labels, errors).
    """
    _log = log_fn or print
    targets = _collect_targets(files, folder)

    _log(f"Files to process: {len(targets)}")
    for t in targets:
        _log(f"  {t}")

    added, errs = [], []
    for target in targets:
        if not os.path.exists(target):
            errs.append(f"{target}: file not found")
            _log(f"\nERROR: file not found: {target}")
            continue

        label = Path(target).name
        _log(f"\n{'=' * 65}")
        _log(f"Processing: {target}")
        _log(f"{'=' * 65}")
        try:
            process_one_file(
                target, dry_run=False, log_fn=_log,
                continue_on_warning=True, source_label_override=label,
            )
            added.append(label)
        except Exception as e:
            errs.append(f"{label}: {e}")
            _log(f"\nERROR on {target}: {e}")
            traceback.print_exc()

    if added:
        _log(f"\n{'=' * 65}")
        _log(f"Indexing {len(added)} document(s) incrementally (no full rebuild)...")
        _log(f"{'=' * 65}")
        try:
            add_sources_to_vectorstore(added, log_fn=_log)
        except Exception as e:
            errs.append(f"index update: {e}")
            _log(f"\nERROR during indexing: {e}")
            traceback.print_exc()
    else:
        _log("\nNothing was preprocessed successfully — index left unchanged.")

    if errs:
        _log("\nFinished with errors:")
        for e in errs:
            _log(f"  • {e}")
    else:
        _log("\n✅ Done — document(s) preprocessed and added to the index.")

    return added, errs


def main():
    parser = argparse.ArgumentParser(
        description="Preprocess raw DOCX/PDF and incrementally add to the vector index "
                    "(CLI equivalent of the app's 'Preprocess + Add to Index' button)."
    )
    parser.add_argument("--file", nargs="+", metavar="PATH",
                        help="One or more raw .docx/.pdf files to process and index.")
    parser.add_argument("--folder", metavar="PATH", default=RAW_DOCS_FOLDER,
                        help=f"Process every .docx/.pdf in this folder "
                             f"(default: {RAW_DOCS_FOLDER}/). Ignored if --file is given.")
    args = parser.parse_args()

    process_and_ingest(files=args.file, folder=args.folder)


if __name__ == "__main__":
    main()

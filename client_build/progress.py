"""
progress.py — live status for the diagram re-processing job (reprocess.log).
Run from anywhere:  python progress.py
Refreshes every 3s; press Ctrl+C to exit. Exits automatically when the job finishes.
"""
import os, re, time, sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "reprocess.log")
TOTAL_DOCS = 6


def bar(frac, width=34):
    frac = max(0.0, min(1.0, frac))
    n = int(frac * width)
    return "[" + "#" * n + "-" * (width - n) + f"] {frac * 100:5.1f}%"


def parse():
    if not os.path.exists(LOG):
        return None
    with open(LOG, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    text = "".join(lines)

    docs_done = text.count("DONE:")                 # one per completed doc
    recovered = len(re.findall(r"\]\s*✓", text))  # "] ✓"
    failures  = text.count("quarantined")

    cur_doc = "(starting...)"
    for ln in lines:
        m = re.search(r"Re-processing:\s*(.+?)\s*$", ln)
        if m:
            cur_doc = m.group(1)

    total = cur = 0
    for ln in lines:
        m = re.search(r"vision on (\d+) images", ln)
        if m:
            total = int(m.group(1)); cur = 0; continue
        m = re.search(r"\[\s*(\d+)/(\d+)\]", ln)
        if m and total and int(m.group(2)) == total:
            cur = max(cur, int(m.group(1)))

    return {
        "docs_done": docs_done, "recovered": recovered, "failures": failures,
        "cur_doc": cur_doc, "cur": cur, "total": total,
        "done": "ALL DONE" in text,
    }


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("=== Diagram re-processing — live status ===\n")
        st = parse()
        if not st:
            print("Waiting for reprocess.log to appear...")
        else:
            print(f"Documents : {st['docs_done']}/{TOTAL_DOCS}  {bar(st['docs_done'] / TOTAL_DOCS)}")
            if st["total"]:
                print(f"This doc  : {st['cur']}/{st['total']} images  {bar(st['cur'] / st['total'])}")
            print(f"Current   : {st['cur_doc']}")
            print(f"Diagrams recovered: {st['recovered']}   |   Failures quarantined: {st['failures']}")
            if st["done"]:
                print("\n*** ALL DONE ***")
                break
        print("\n(refreshing every 3s — Ctrl+C to exit)")
        try:
            time.sleep(3)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()

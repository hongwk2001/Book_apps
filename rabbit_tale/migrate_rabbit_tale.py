"""
Build rabbit_tale/src/main/assets/books/ch_NN.json from the drafted chapter cards.

Reads  TKprof_book/books/rabbit_tale/json/ch_NN.json (hand-drafted bilingual cards)
and writes the row format :shared expects:

    [{"id": 1, "tag": "C01_h", "en": "...", "ko": "...", "is_header": true}, ...]

Before writing, the script refuses when a card has an empty side, or when a
body card is longer than CARD_CAP characters on either side. An asset edited
outside this script is refused too; --force overwrites it.

Usage:  python migrate_rabbit_tale.py
        python migrate_rabbit_tale.py --force
"""
import hashlib
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\git_repo\TKprof_book\books\rabbit_tale\json"
DEST = os.path.join(BASE, "src", "main", "assets", "books")
MANIFEST = os.path.join(DEST, "_source.json")
CHAPTERS = 12
CARD_CAP = 300


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(rows):
    return (json.dumps(rows, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def build(ch):
    path = os.path.join(SRC, f"ch_{ch:02d}.json")
    cards = json.load(open(path, encoding="utf-8"))
    rows, errors = [], []
    for n, c in enumerate(cards, start=1):
        for side in ("en", "ko"):
            text = (c.get(side) or "").strip()
            if not text:
                errors.append(f"{c['tag']} empty {side}")
            elif not c["is_header"] and len(text) > CARD_CAP:
                errors.append(f"{c['tag']} {side} over {CARD_CAP} chars")
        rows.append({"id": n, "tag": c["tag"], "en": c["en"], "ko": c["ko"], "is_header": c["is_header"]})
    return rows, errors


def hand_edits():
    """Asset files whose bytes differ from what the last run wrote."""
    existing = sorted(f for f in os.listdir(DEST) if f.startswith("ch_")) if os.path.isdir(DEST) else []
    if not os.path.exists(MANIFEST):
        return [f"{f} (no _source.json)" for f in existing]
    recorded = json.load(open(MANIFEST, encoding="utf-8"))["files"]
    return [f for f in existing if recorded.get(f) != sha(open(os.path.join(DEST, f), "rb").read())]


def main():
    force = "--force" in sys.argv[1:]

    built, failures = {}, []
    for ch in range(1, CHAPTERS + 1):
        rows, errors = build(ch)
        built[f"ch_{ch:02d}.json"] = rows
        failures += [f"ch_{ch:02d}: {e}" for e in errors]
    if failures:
        sys.exit(f"{len(failures)} card problem(s), nothing written:\n  " + "\n  ".join(failures))

    edited = hand_edits()
    if edited and not force:
        sys.exit("These assets were changed outside this script; nothing written.\n"
                 "Put the fix in the source JSON, or rerun with --force to overwrite:\n  " + "\n  ".join(edited))

    os.makedirs(DEST, exist_ok=True)
    hashes, total = {}, 0
    for name, rows in built.items():
        data = encode(rows)
        with open(os.path.join(DEST, name), "wb") as fh:
            fh.write(data)
        hashes[name] = sha(data)
        total += len(rows)
        body = sum(not r["is_header"] for r in rows)
        print(f"  {name}  {len(rows):>3} cards ({body} body)")

    manifest = {"source": "TKprof_book/books/rabbit_tale/json",
                "generated_by": "rabbit_tale/migrate_rabbit_tale.py",
                "files": hashes}
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=1)
        fh.write("\n")
    print(f"\n{total} cards written to {DEST}")


if __name__ == "__main__":
    main()

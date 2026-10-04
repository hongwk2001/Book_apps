"""
Build romeo_juliet/src/main/assets/books/ch_NN.json from the play's source JSON.

Reads  TKprof_book/books/romeo_juliet/json/ch_NN.json  (the single source)
through that folder's narrate.py, so the app gets exactly the cards
`python narrate.py N --json` prints, flattened to the row format :shared expects:

    [{"id": 1, "tag": "P0001", "en": "...", "ko": "...", "is_header": true}, ...]

Assets are generated, never hand-edited. assets/books/_source.json records the
source commit and a sha256 per asset file. Before writing, the script refuses to
run when:
  - the source json/, glossary.json or narrate.py has uncommitted changes
    (the recorded commit would not describe what was shipped);
  - any card is still pending (⚙), has an empty side, or is over the card cap;
  - an existing asset no longer matches its recorded hash, or assets exist
    without _source.json (someone edited the app copy; fix the source instead).
--force skips only the last check.

Usage:  python migrate_romeo_juliet.py            # all 24 chapters, all or nothing
        python migrate_romeo_juliet.py --force
"""
import hashlib
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\git_repo\TKprof_book\books\romeo_juliet"
DEST = os.path.join(BASE, "src", "main", "assets", "books")
MANIFEST = os.path.join(DEST, "_source.json")
CHAPTERS = 24

sys.path.insert(0, SRC)
import narrate  # noqa: E402  (lives in the source folder)


def git(*args):
    return subprocess.run(["git", *args], cwd=SRC, capture_output=True, text=True, check=True).stdout.strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(rows):
    return (json.dumps(rows, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def build(ch):
    cards = narrate.build_cards(narrate.load(ch))
    rows, errors = [], []
    for n, c in enumerate(cards, start=1):
        for side in ("en", "ko"):
            text = c.get(side) or ""
            if not text.strip():
                errors.append(f"{c['tag']} empty {side}")
            elif narrate.PENDING in text:
                errors.append(f"{c['tag']} pending {side}")
            elif len(text) > narrate.CARD_CAP and not c["is_header"]:
                errors.append(f"{c['tag']} {side} over {narrate.CARD_CAP} chars")
        rows.append({"id": n, "tag": c["tag"], "en": c["en"], "ko": c["ko"], "is_header": c["is_header"]})
    return rows, errors


def hand_edits():
    """Asset files whose bytes differ from what the last run wrote."""
    existing = sorted(f for f in os.listdir(DEST) if f.startswith("ch_")) if os.path.isdir(DEST) else []
    if not os.path.exists(MANIFEST):
        return [f"{f} (no _source.json)" for f in existing]
    recorded = json.load(open(MANIFEST, encoding="utf-8"))["files"]
    bad = []
    for f in existing:
        if recorded.get(f) != sha(open(os.path.join(DEST, f), "rb").read()):
            bad.append(f)
    return bad


def main():
    force = "--force" in sys.argv[1:]

    dirty = git("status", "--porcelain", "--", "json", "glossary.json", "narrate.py")
    if dirty:
        sys.exit(f"Source has uncommitted changes; commit them first:\n{dirty}")
    commit = git("rev-parse", "HEAD")

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

    manifest = {"source": "TKprof_book/books/romeo_juliet/json", "commit": commit,
                "generated_by": "romeo_juliet/migrate_romeo_juliet.py", "files": hashes}
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=1)
        fh.write("\n")
    print(f"\n{total} cards written to {DEST}\nsource commit {commit[:10]}")


if __name__ == "__main__":
    main()

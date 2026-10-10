"""
Build chunhyang/src/main/assets/books/ch_NN.json from the book's source JSON.

Reads  TKprof_book/books/chunhyang/json/ch_NN.json  (the single source: one
header row per chapter, then passages whose `sentences` hold paired ko/en) and
flattens it to the row format :shared expects:

    [{"id": 1, "tag": "P0001", "en": "...", "ko": "...", "is_header": true}, ...]

Each sentence pair becomes one card, tagged <passage>_<n> (e.g. P0003_4), the
same id the review page shows. Chapter 1 also gets a source card after its
title: the scans are 공공누리 제1유형, which requires crediting the National
Museum of Korea where the work is used.

Assets are generated, never hand-edited. assets/books/_source.json records the
source commit and a sha256 per asset file. Before writing, the script refuses to
run when:
  - the source json/ has uncommitted changes;
  - any card has an empty side, or is over the card cap (en 300 / ko 170);
  - an existing asset no longer matches its recorded hash (someone edited the
    app copy; fix the source instead). --force skips only this check.

Usage:  python migrate_chunhyang.py            # all 21 chapters, all or nothing
        python migrate_chunhyang.py --force
"""
import hashlib
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\git_repo\TKprof_book\books\chunhyang"
DEST = os.path.join(BASE, "src", "main", "assets", "books")
MANIFEST = os.path.join(DEST, "_source.json")
CHAPTERS = 21
EN_CAP, KO_CAP = 300, 170  # Korean runs ~2x denser than English; 170 matches a 300-char English card

CREDIT = {
    "tag": "P0001_src",
    "en": "Source: the 1911 Wanpan woodblock edition of this story, from images held by "
          "the National Museum of Korea (KOGL Type 1). Modern Korean and English by TKProf.",
    "ko": "원문: 완판 84장본 「열녀춘향수절가」(1911), 국립중앙박물관 소장 이미지(공공누리 제1유형). "
          "현대어·영어: TKProf.",
}


def git(*args):
    return subprocess.run(["git", *args], cwd=SRC, capture_output=True, text=True, check=True).stdout.strip()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def encode(rows):
    return (json.dumps(rows, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def build(ch):
    src = json.load(open(os.path.join(SRC, "json", f"ch_{ch:02d}.json"), encoding="utf-8"))
    head = src[0]
    # The drawer and top bar already number chapters, so titles carry no "Chapter N".
    cards = [{"tag": "P0001", "en": head["en_title"], "ko": head["ko_title"], "is_header": True}]
    if ch == 1:
        cards.append({**CREDIT, "is_header": False})
    errors = []
    for p in src[1:]:
        if not p["sentences"]:
            errors.append(f"{p['tag']} has no sentences")
        for s in p["sentences"]:
            tag = f"{p['tag']}_{s['n']}"
            for side, cap in (("en", EN_CAP), ("ko", KO_CAP)):
                text = (s.get(side) or "").strip()
                if not text:
                    errors.append(f"{tag} empty {side}")
                elif len(text) > cap:
                    errors.append(f"{tag} {side} over {cap} chars")
            cards.append({"tag": tag, "en": s["en"].strip(), "ko": s["ko"].strip(), "is_header": False})
    rows = [{"id": n, **c} for n, c in enumerate(cards, start=1)]
    rows = [{"id": r["id"], "tag": r["tag"], "en": r["en"], "ko": r["ko"], "is_header": r["is_header"]} for r in rows]
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

    dirty = git("status", "--porcelain", "--", "json")
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
        print(f"  {name}  {len(rows):>3} cards")

    manifest = {"source": "TKprof_book/books/chunhyang/json", "commit": commit,
                "generated_by": "chunhyang/migrate_chunhyang.py", "files": hashes}
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(manifest, fh, indent=1)
        fh.write("\n")
    print(f"\n{total} cards written to {DEST}\nsource commit {commit[:10]}")


if __name__ == "__main__":
    main()

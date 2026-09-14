"""
Build samguk_yusa/src/main/assets/books/ch_NN.json from the translation output.

Reads  TKprof_book/books/samguk_yusa/batches/batch_ch_NN.json  (structure, headers, tags)
   and TKprof_book/books/samguk_yusa/batches/result_ch_NN.json  (ko + en paragraphs)

and emits the flat row format :shared expects, matching the other six books:

    [{"id": 1, "tag": "H01", "en": "...", "ko": "...", "is_header": true}, ...]

One translation item yields several rows, because a ~135-hanja item is translated into
3-4 paragraphs and each paragraph becomes its own card. Tags get a _1/_2 suffix in that
case, the way migrate_the_heroes does for split paragraphs.

Refuses to write a chapter whose ko and en paragraph counts disagree: a misaligned
chapter would silently pair the wrong Korean with the wrong English, which is far worse
than a missing file.

Usage:  python migrate_samguk_yusa.py          # all chapters
        python migrate_samguk_yusa.py ch_01
"""
import json
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = r"C:\git_repo\TKprof_book\books\samguk_yusa\batches"
DEST = os.path.join(BASE, "src", "main", "assets", "books")

# The English side drives the reader's TTS and card height; the shipped books cap it at
# 300 characters. Anything longer is reported rather than split, since splitting here
# would break the ko/en pairing the translation stage guarantees.
EN_SOFT_CAP = 300


def build(cid):
    batch = json.load(open(os.path.join(SRC, f"batch_{cid}.json"), encoding="utf-8"))
    rpath = os.path.join(SRC, f"result_{cid}.json")
    if not os.path.exists(rpath):
        return None, f"{cid}: no result file"
    result = json.load(open(rpath, encoding="utf-8"))["items"]

    rows, rid, long_en = [], 0, 0
    for item in batch["items"]:
        if item["is_header"]:
            rid += 1
            rows.append({"id": rid, "tag": item["tag"], "en": item["en"], "ko": item["ko"],
                         "is_header": True})
            continue

        got = result.get(str(item["id"]))
        if not got:
            return None, f"{cid}: item {item['id']} ({item['tag']}) missing from result"
        ko, en = got["ko"], got["en"]
        if len(ko) != len(en):
            return None, f"{cid}: {item['tag']} misaligned ko={len(ko)} en={len(en)}"

        multi = len(ko) > 1
        for n, (k, e) in enumerate(zip(ko, en), start=1):
            rid += 1
            tag = f"{item['tag']}_{n}" if multi else item["tag"]
            if len(e) > EN_SOFT_CAP:
                long_en += 1
            rows.append({"id": rid, "tag": tag, "en": e, "ko": k, "is_header": False})

    return {"rows": rows, "long_en": long_en}, None


def main():
    os.makedirs(DEST, exist_ok=True)
    cids = [sys.argv[1]] if len(sys.argv) > 1 else [f"ch_{n:02d}" for n in range(1, 25)]

    total_rows = total_long = 0
    failures = []
    for cid in cids:
        built, err = build(cid)
        if err:
            failures.append(err)
            print(f"  {cid}  SKIPPED — {err}")
            continue
        rows = built["rows"]
        with open(os.path.join(DEST, f"{cid}.json"), "w", encoding="utf-8") as fh:
            json.dump(rows, fh, ensure_ascii=False, indent=1)
        body = [r for r in rows if not r["is_header"]]
        total_rows += len(rows)
        total_long += built["long_en"]
        flag = f"  ({built['long_en']} en over {EN_SOFT_CAP})" if built["long_en"] else ""
        print(f"  {cid}  {len(rows):>3} rows ({len(body)} body, {len(rows) - len(body)} headers){flag}")

    print(f"\n{total_rows} rows written to {DEST}")
    if total_long:
        print(f"{total_long} English paragraphs exceed {EN_SOFT_CAP} chars — check card height")
    if failures:
        print(f"\n{len(failures)} chapter(s) NOT written:")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)


if __name__ == "__main__":
    main()

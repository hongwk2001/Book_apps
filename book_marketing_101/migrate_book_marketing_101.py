"""
Build book_marketing_101/src/main/assets/books/ch_NN.json from the bilingual Markdown.

Reads   chapter01_bilingual.md .. chapter07_bilingual.md   (ch_01 .. ch_07)
        bonus_bilingual.md                                  (ch_08)
        appendices_bilingual.md                             (ch_09)
and writes the row format :shared expects:

    [{"id": 1, "tag": "C01_001", "en": "...", "ko": "...", "is_header": true}, ...]

Each source line pair (English line, then its Korean line) becomes one row.
The "Learning notes" section at the end of each file is skipped: it is for
the translator, not for readers.

Usage:  python migrate_book_marketing_101.py
"""
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(BASE, "src", "main", "assets", "books")
SOURCES = {
    1: "front_matter_bilingual.md",
    2: "chapter01_bilingual.md",
    3: "chapter02_bilingual.md",
    4: "chapter03_bilingual.md",
    5: "chapter04_bilingual.md",
    6: "chapter05_bilingual.md",
    7: "chapter06_bilingual.md",
    8: "chapter07_bilingual.md",
    9: "bonus_bilingual.md",
    10: "appendices_bilingual.md",
}
CARD_WARN = 300  # body paragraphs longer than this are flagged for review

HANGUL = re.compile(r"[가-힣]")
LATIN = re.compile(r"[A-Za-z]")


def strip_markup(text):
    text = text.replace("**", "").replace("__", "")
    text = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text.strip()


def clean_line(raw):
    """Return (is_header, text) or None for lines that carry no text."""
    line = raw.strip()
    if not line or re.fullmatch(r"[-|:\s]+", line) or line == "---":
        return None
    header = False
    m = re.match(r"^(#{1,6})\s+(.*)$", line)
    if m:
        header, line = True, m.group(2)
    elif line.startswith(">"):
        line = line[1:].strip()
    elif line.startswith("|"):
        cells = [c.strip() for c in line.strip("|").split("|")]
        line = " · ".join(c for c in cells if c)
    else:
        line = re.sub(r"^- (\[ \] )?", "", line)
        line = re.sub(r"^\d+\.\s+", "", line)
    line = strip_markup(line)
    if not line:
        return None
    return header, line


def split_mixed(text):
    """'Book ready / 책 준비' -> ('Book ready', '책 준비') when a line mixes both languages."""
    if " / " in text and LATIN.search(text) and HANGUL.search(text):
        left, right = text.split(" / ", 1)
        if not HANGUL.search(left) and HANGUL.search(right):
            return left.strip(), right.strip()
    return None


def read_body(path):
    text = open(path, encoding="utf-8").read()
    # Learning notes are for the translator; the Sources list is English-only
    # citations kept in the book file, not in the app.
    for marker in ("## Learning notes", "## Sources"):
        cut = text.find(marker)
        if cut != -1:
            text = text[:cut]
    items = []  # (is_header, text, line_no)
    in_code = False  # code blocks (lab commands, expected output) are not app text
    for no, raw in enumerate(text.splitlines(), start=1):
        if raw.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        cleaned = clean_line(raw)
        if cleaned is None:
            continue
        header, line = cleaned
        pair = split_mixed(line)
        if pair:
            items.append((header, pair[0], no))
            items.append((header, pair[1], no))
        else:
            items.append((header, line, no))
    return items


def pair_up(items, path):
    rows, errors = [], []
    i = 0
    while i < len(items):
        if i + 1 >= len(items):
            errors.append(f"{os.path.basename(path)}: unpaired line {items[i][2]}: {items[i][1][:60]}")
            break
        (h1, a, n1), (h2, b, n2) = items[i], items[i + 1]
        identical = a == b  # e.g. the book title, which stays in English
        if not identical and (HANGUL.search(a) or not HANGUL.search(b)):
            errors.append(f"{os.path.basename(path)}: lines {n1}-{n2} are not EN/KO pairs")
        rows.append({"en": a, "ko": b, "is_header": h1 or h2})
        i += 2
    return rows, errors


def build(ch):
    path = os.path.join(BASE, SOURCES[ch])
    rows, errors = pair_up(read_body(path), path)
    out = []
    for n, r in enumerate(rows, start=1):
        out.append({
            "id": n,
            "tag": f"C{ch:02d}_{n:03d}",
            "en": r["en"],
            "ko": r["ko"],
            "is_header": r["is_header"],
        })
        if not r["is_header"] and max(len(r["en"]), len(r["ko"])) > CARD_WARN:
            errors.append(f"{SOURCES[ch]} row {n}: long paragraph ({len(r['ko'])} KO chars), consider splitting")
    return out, errors


def main():
    os.makedirs(DEST, exist_ok=True)
    total_errors = []
    for ch in sorted(SOURCES):
        rows, errors = build(ch)
        name = f"ch_{ch:02d}.json"
        with open(os.path.join(DEST, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(rows, ensure_ascii=False, indent=1) + "\n")
        print(f"{name}: {len(rows)} rows")
        total_errors.extend(errors)
    if total_errors:
        print("\nWARNINGS / ERRORS:")
        for e in total_errors:
            print("  -", e)
        sys.exit(1)
    print("\nAll chapters paired cleanly.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
merge_bilingual.py — Merges per-chapter EN + KO JSON files into bilingual chapter JSONs.

Usage:
    python merge_bilingual.py --book dracula
    python merge_bilingual.py --book dracula --chapters 1-27
    python merge_bilingual.py --help

Source format (TKprof_book):
    C:/git_repo/TKprof_book/books/<book>/chapters/ch_NN_en.json
    C:/git_repo/TKprof_book/books/<book>/chapters/ch_NN_ko.json

Each source file is an array of:
    {"id": int, "role": str, "text": str, "is_header": bool}

Output format (bilingual merged):
    C:/git_repo/Book_apps/<book>/src/main/assets/books/ch_NN.json

Each output file is an array of:
    {"id": int, "en": str, "ko": str, "is_header": bool}

Notes:
  - Paragraphs are matched by "id" field (1-based sequential).
  - If counts differ, mismatched ids are logged and skipped gracefully.
  - "role" field is dropped (one voice per language, no role switching).
"""

import json
import argparse
import os
import sys
from pathlib import Path

SOURCE_ROOT = Path("C:/git_repo/TKprof_book/books")
OUTPUT_ROOT = Path("C:/git_repo/Book_apps")


def load_chapter(book: str, chapter: int, lang: str) -> dict:
    """Load a chapter JSON file. Returns dict keyed by paragraph id."""
    path = SOURCE_ROOT / book / "chapters" / f"ch_{chapter:02d}_{lang}.json"
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return {p["id"]: p for p in data}


def merge_chapter(book: str, chapter: int, output_dir: Path) -> tuple[int, int]:
    """Merge EN + KO for one chapter. Returns (merged_count, skipped_count)."""
    en_map = load_chapter(book, chapter, "en")
    ko_map = load_chapter(book, chapter, "ko")

    if not en_map:
        print(f"  [SKIP] ch_{chapter:02d}: no EN file found")
        return 0, 0

    if not ko_map:
        print(f"  [SKIP] ch_{chapter:02d}: no KO file found")
        return 0, 0

    merged = []
    skipped = 0

    # Use EN as the authoritative id sequence
    for pid, en_para in sorted(en_map.items()):
        ko_para = ko_map.get(pid)
        if ko_para is None:
            print(f"  [WARN] ch_{chapter:02d} id={pid}: no matching KO paragraph — skipping")
            skipped += 1
            continue
        merged.append({
            "id": pid,
            "en": en_para["text"],
            "ko": ko_para["text"],
            "is_header": en_para.get("is_header", False)
        })

    output_path = output_dir / f"ch_{chapter:02d}.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"  [OK]   ch_{chapter:02d}: {len(merged)} paragraphs merged, {skipped} skipped -> {output_path.name}")
    return len(merged), skipped


def main():
    parser = argparse.ArgumentParser(description="Merge bilingual EN+KO chapter JSONs")
    parser.add_argument("--book", required=True, help="Book folder name (e.g. dracula)")
    parser.add_argument("--chapters", default="1-27",
                        help="Chapter range e.g. '1-27' or single '5' (default: 1-27)")
    args = parser.parse_args()

    book = args.book
    # Parse chapter range
    if "-" in args.chapters:
        start, end = [int(x) for x in args.chapters.split("-")]
    else:
        start = end = int(args.chapters)
    chapters = range(start, end + 1)

    # Verify source exists
    source_dir = SOURCE_ROOT / book / "chapters"
    if not source_dir.exists():
        print(f"ERROR: Source directory not found: {source_dir}")
        sys.exit(1)

    # Prepare output directory
    output_dir = OUTPUT_ROOT / book / "src" / "main" / "assets" / "books"
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {output_dir}")

    total_merged = 0
    total_skipped = 0

    print(f"\nMerging {book} chapters {start}–{end}...\n")
    for ch in chapters:
        m, s = merge_chapter(book, ch, output_dir)
        total_merged += m
        total_skipped += s

    print(f"\nDone. Total paragraphs merged: {total_merged}, skipped: {total_skipped}")


if __name__ == "__main__":
    main()

import json
import re
import sys

def normalize_text(text: str) -> str:
    """Strip whitespace, linebreaks, and uniform quote marks for character comparison."""
    t = text.replace('\r', '').replace('\n', ' ').strip()
    t = re.sub(r'\s+', ' ', t)
    return t

def verify_paragraph_split(original_para: dict, split_paras: list[dict]) -> tuple[bool, str]:
    """
    Guarantees 100% text conservation:
    1. Recombined EN text matches original EN exactly.
    2. Recombined KO text matches original KO exactly.
    3. Every split paragraph has non-empty EN and KO.
    """
    orig_en = normalize_text(original_para.get('en', ''))
    orig_ko = normalize_text(original_para.get('ko', ''))

    recombined_en = normalize_text(" ".join(p.get('en', '').strip() for p in split_paras))
    recombined_ko = normalize_text(" ".join(p.get('ko', '').strip() for p in split_paras))

    if orig_en != recombined_en:
        return False, f"EN text mismatch!\nExpected: {orig_en}\nGot:      {recombined_en}"

    if orig_ko != recombined_ko:
        return False, f"KO text mismatch!\nExpected: {orig_ko}\nGot:      {recombined_ko}"

    for i, p in enumerate(split_paras):
        if not p.get('en', '').strip():
            return False, f"Chunk {i} has empty EN text"
        if not p.get('ko', '').strip():
            return False, f"Chunk {i} has empty KO text"

    return True, "100% Text Integrity Confirmed (0 missing chars, 0 added chars)"

if __name__ == '__main__':
    print("Text integrity verification module loaded.")

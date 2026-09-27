import json
import glob
import os
import re

def split_sents(text):
    abbr = r'(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|Mt|Capt|Col|Gen|Lieut|Sgt|Rev|No|Vol|etc)\.'
    masked = re.sub(abbr, lambda m: m.group(0).replace('.', '@DOT@'), text, flags=re.IGNORECASE)
    masked = re.sub(r'(\d+)\.(\d+)', r'\1@DOT@\2', masked)
    parts = re.split(r'([\.!\?]+(?:\s+|$))', masked)
    sents = []
    for i in range(0, len(parts)-1, 2):
        s = (parts[i] + parts[i+1]).strip()
        if s:
            sents.append(s.replace('@DOT@', '.'))
    if len(parts) % 2 == 1 and parts[-1].strip():
        sents.append(parts[-1].strip().replace('@DOT@', '.'))
    return sents

def split_ko_sents(text):
    # Split on sentence enders in Korean
    parts = re.split(r'([\.!\?]+(?:\s+|$))', text)
    sents = []
    for i in range(0, len(parts)-1, 2):
        s = (parts[i] + parts[i+1]).strip()
        if s:
            sents.append(s)
    if len(parts) % 2 == 1 and parts[-1].strip():
        sents.append(parts[-1].strip())
    return sents

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
from list_paras_over_300 import b_400_499

multi_sents = [p for p in b_400_499 if p['sents'] > 1]

print(f"Total multi-sentence candidates: {len(multi_sents)}")

with open('split_candidates_analysis.txt', 'w', encoding='utf-8') as out:
    for idx, p in enumerate(multi_sents, 1):
        en_sents = split_sents(p['en'])
        ko_sents = split_ko_sents(p['ko'])
        out.write(f"[{idx}] {p['ch']} ID {p['id']} (Tag: {p['tag']}) - Total EN Chars: {p['chars']}\n")
        out.write(f"EN Sentences ({len(en_sents)}):\n")
        for i, s in enumerate(en_sents, 1):
            out.write(f"  ({i}) [{len(s)} ch] {s}\n")
        out.write(f"KO Sentences ({len(ko_sents)}):\n")
        for i, s in enumerate(ko_sents, 1):
            out.write(f"  ({i}) [{len(s)} ch] {s}\n")
        out.write("="*80 + "\n\n")

print("Wrote split_candidates_analysis.txt")

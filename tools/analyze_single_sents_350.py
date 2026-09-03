import json
import glob
import os
import re

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))

from list_paras_over_300 import split_sents

singles_350 = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for p in data:
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()
        if 350 <= len(en) < 400:
            sents = split_sents(en)
            if len(sents) == 1:
                singles_350.append({
                    'ch': ch,
                    'id': p.get('id'),
                    'tag': p.get('tag', ''),
                    'chars': len(en),
                    'ko_chars': len(ko),
                    'en': en,
                    'ko': ko
                })

singles_350.sort(key=lambda x: x['chars'], reverse=True)
print(f"Total single-sentence paragraphs in 350-399 tier: {len(singles_350)}")

with open('single_sents_350_analysis.txt', 'w', encoding='utf-8') as out:
    for idx, p in enumerate(singles_350, 1):
        out.write(f"[{idx}] {p['ch']} ID {p['id']} (Tag: {p['tag']}) - {p['chars']} EN chars / {p['ko_chars']} KO chars\n")
        out.write(f"  EN: {p['en']}\n")
        out.write(f"  KO: {p['ko']}\n\n")

print("Wrote single_sents_350_analysis.txt")

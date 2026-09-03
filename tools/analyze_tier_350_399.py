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
files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))

tier_350_399 = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for p in data:
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()
        if 350 <= len(en) < 400:
            en_sents = split_sents(en)
            ko_sents = split_ko_sents(ko)
            tier_350_399.append({
                'ch': ch,
                'id': p.get('id'),
                'tag': p.get('tag', ''),
                'chars': len(en),
                'ko_chars': len(ko),
                'en_sents': en_sents,
                'ko_sents': ko_sents,
                'en': en,
                'ko': ko
            })

tier_350_399.sort(key=lambda x: x['chars'], reverse=True)

single_sents = [p for p in tier_350_399 if len(p['en_sents']) == 1]
multi_sents = [p for p in tier_350_399 if len(p['en_sents']) > 1]

print(f"Total paragraphs in 350-399 tier: {len(tier_350_399)}")
print(f"  Single sentence: {len(single_sents)}")
print(f"  Multi sentence : {len(multi_sents)}")

with open('tier_350_399_analysis.txt', 'w', encoding='utf-8') as out:
    out.write(f"TIER 350-399 CHARACTERS ANALYSIS (Total: {len(tier_350_399)})\n")
    out.write(f"  Multi-sentence (Can split easily) : {len(multi_sents)}\n")
    out.write(f"  Single-sentence (Unbroken thought): {len(single_sents)}\n")
    out.write("="*80 + "\n\n")

    out.write("=== MULTI-SENTENCE CANDIDATES ===\n\n")
    for i, p in enumerate(multi_sents, 1):
        out.write(f"[{i}] {p['ch']} ID {p['id']} (Tag: {p['tag']}) - {p['chars']} EN chars, {len(p['en_sents'])} EN sents / {len(p['ko_sents'])} KO sents\n")
        out.write("EN Sentences:\n")
        for s_idx, s in enumerate(p['en_sents'], 1):
            out.write(f"  ({s_idx}) [{len(s)} ch] {s}\n")
        out.write("KO Sentences:\n")
        for s_idx, s in enumerate(p['ko_sents'], 1):
            out.write(f"  ({s_idx}) [{len(s)} ch] {s}\n")
        out.write("-" * 80 + "\n\n")

    out.write("\n=== SINGLE-SENTENCE PARAGRAPHS ===\n\n")
    for i, p in enumerate(single_sents, 1):
        out.write(f"[{i}] {p['ch']} ID {p['id']} (Tag: {p['tag']}) - {p['chars']} EN chars\n")
        out.write(f"  EN: {p['en']}\n")
        out.write(f"  KO: {p['ko']}\n\n")

print("Wrote tier_350_399_analysis.txt")

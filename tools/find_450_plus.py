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

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))

top_long = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for p in data:
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()
        if len(en) >= 450:
            en_s = split_sents(en)
            ko_s = split_sents(ko)
            top_long.append({
                'ch': ch,
                'id': p.get('id'),
                'tag': p.get('tag', ''),
                'chars': len(en),
                'en_sents': len(en_s),
                'ko_sents': len(ko_s),
                'en': en,
                'ko': ko
            })

top_long.sort(key=lambda x: x['chars'], reverse=True)

print(f"Total paragraphs >= 450 chars in Two Cities: {len(top_long)}")
with open('two_cities_450_plus.txt', 'w', encoding='utf-8') as out:
    for i, p in enumerate(top_long, 1):
        out.write(f"[{i}] {p['ch']} ID {p['id']} (Tag: {p['tag']}) - {p['chars']} chars, EN={p['en_sents']} sent, KO={p['ko_sents']} sent\n")
        out.write(f"EN: {p['en']}\n")
        out.write(f"KO: {p['ko']}\n\n")

print("Wrote two_cities_450_plus.txt")

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

over_300 = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for p in data:
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()
        if len(en) > 300:
            sents = split_sents(en)
            over_300.append({
                'ch': ch,
                'id': p.get('id'),
                'tag': p.get('tag', ''),
                'chars': len(en),
                'ko_chars': len(ko),
                'words': len(en.split()),
                'sents': len(sents),
                'en': en,
                'ko': ko
            })

over_300.sort(key=lambda x: x['chars'], reverse=True)

# Sub-brackets:
b_400_499 = [p for p in over_300 if p['chars'] >= 400]
b_350_399 = [p for p in over_300 if 350 <= p['chars'] < 400]
b_301_349 = [p for p in over_300 if 300 < p['chars'] < 350]

print(f"Total paragraphs > 300 chars in Two Cities: {len(over_300)}")
print(f"  400 - 499 chars : {len(b_400_499)}")
print(f"  350 - 399 chars : {len(b_350_399)}")
print(f"  301 - 349 chars : {len(b_301_349)}")

with open('paras_over_300.txt', 'w', encoding='utf-8') as out:
    out.write(f"TOTAL PARAGRAPHS OVER 300 CHARACTERS IN TWO CITIES: {len(over_300)}\n")
    out.write(f"  400 - 499 chars (Long)          : {len(b_400_499)}\n")
    out.write(f"  350 - 399 chars (Moderate-Long) : {len(b_350_399)}\n")
    out.write(f"  301 - 349 chars (Moderate)      : {len(b_301_349)}\n")
    out.write("="*80 + "\n\n")

    for i, p in enumerate(over_300, 1):
        out.write(f"[{i}] {p['ch']} ID {p['id']} (Tag: {p['tag']})\n")
        out.write(f"    Length: {p['chars']} EN chars ({p['words']} words), {p['ko_chars']} KO chars, {p['sents']} sentences\n")
        out.write(f"    EN: {p['en']}\n")
        out.write(f"    KO: {p['ko']}\n")
        out.write("-" * 80 + "\n\n")

print("Wrote paras_over_300.txt")

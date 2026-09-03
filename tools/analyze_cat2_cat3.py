import json
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

cat2_targets = [
    ('ch_02.json', 18),
    ('ch_03.json', 61),
    ('ch_13.json', 38),
    ('ch_40.json', 114),
]

cat3_targets = [
    ('ch_04.json', 209),
    ('ch_09.json', 210),
    ('ch_27.json', 30),
    ('ch_27.json', 31),
    ('ch_28.json', 39),
    ('ch_31.json', 173),
    ('ch_34.json', 16),
    ('ch_34.json', 40),
    ('ch_40.json', 7),
]

with open('cat2_cat3_details.txt', 'w', encoding='utf-8') as out:
    out.write("=== CATEGORY 2: ASYMMETRIC SENTENCES ===\n\n")
    for ch_file, pid in cat2_targets:
        fpath = os.path.join(assets_dir, ch_file)
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        p = [x for x in data if x.get('id') == pid][0]
        en_s = split_sents(p['en'])
        ko_s = split_sents(p['ko'])
        out.write(f"--- {ch_file} ID {pid} ({p.get('tag')}): EN={len(en_s)} sent, KO={len(ko_s)} sent, {len(p['en'])} chars ---\n")
        out.write("EN Sentences:\n")
        for i, s in enumerate(en_s, 1):
            out.write(f"  [{i}] {s}\n")
        out.write("KO Sentences:\n")
        for i, s in enumerate(ko_s, 1):
            out.write(f"  [{i}] {s}\n")
        out.write("\n")

    out.write("\n=== CATEGORY 3: DICKENS MEGA-SENTENCES ===\n\n")
    for ch_file, pid in cat3_targets:
        fpath = os.path.join(assets_dir, ch_file)
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        p = [x for x in data if x.get('id') == pid][0]
        en_s = split_sents(p['en'])
        ko_s = split_sents(p['ko'])
        out.write(f"--- {ch_file} ID {pid} ({p.get('tag')}): EN={len(en_s)} sent, KO={len(ko_s)} sent, {len(p['en'])} chars ---\n")
        out.write("EN Full Text:\n" + p['en'] + "\n")
        out.write("KO Full Text:\n" + p['ko'] + "\n")
        # Check semicolons or em-dashes
        en_semis = p['en'].count(';')
        en_dashes = p['en'].count('—') + p['en'].count('--')
        out.write(f"EN Punctuation: semicolons={en_semis}, dashes={en_dashes}\n\n")

print("Analysis written to cat2_cat3_details.txt")

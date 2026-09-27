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

targets = [
    ('ch_04.json', 149),
    ('ch_05.json', 19),
    ('ch_07.json', 13),
    ('ch_09.json', 12),
    ('ch_13.json', 44),
    ('ch_21.json', 178),
    ('ch_27.json', 117),
    ('ch_27.json', 144),
    ('ch_31.json', 200),
    ('ch_34.json', 32),
    ('ch_38.json', 11),
]

assets_dir = r'C:\git_repo\Book_apps\two_cities\src\main\assets\books'

with open('candidates_report.txt', 'w', encoding='utf-8') as out:
    for ch_file, pid in targets:
        fpath = os.path.join(assets_dir, ch_file)
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        p = [x for x in data if x.get('id') == pid][0]
        en_s = split_sents(p['en'])
        ko_s = split_sents(p['ko'])
        header = f"\n=== {ch_file} ID {pid} (tag={p.get('tag')}): EN={len(en_s)} sent, KO={len(ko_s)} sent, {len(p['en'])} chars ==="
        print(header)
        out.write(header + "\n")
        for i, (e, k) in enumerate(zip(en_s, ko_s), 1):
            line_en = f"  {i}. EN: {e}"
            line_ko = f"     KO: {k}"
            out.write(line_en + "\n" + line_ko + "\n")
            print(f"  {i}. EN: {e[:70]}... (KO len: {len(k)} chars)")

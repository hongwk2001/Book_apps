import json
import os
import re

def normalize_text(text: str) -> str:
    t = text.replace('\r', '').replace('\n', ' ').strip()
    return re.sub(r'\s+', ' ', t)

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

# Define mapping: (ch_file, pid) -> list of (en_range, ko_range)
# ranges are (start, end) 1-based inclusive
TARGET_MAPPINGS = {
    # Category 2
    ('ch_02.json', 18): [((1, 5), (1, 5)), ((6, 7), (6, 8))],
    ('ch_03.json', 61): [((1, 4), (1, 2)), ((5, 10), (3, 8))],
    ('ch_13.json', 38): [((1, 1), (1, 2)), ((2, 3), (3, 4))],
    ('ch_40.json', 114): [((1, 1), (1, 3)), ((2, 4), (4, 6))],
    
    # Category 3A (2-sentence paragraphs)
    ('ch_27.json', 30): [((1, 1), (1, 2)), ((2, 2), (3, 3))],
    ('ch_27.json', 31): [((1, 1), (1, 1)), ((2, 2), (2, 2))],
    ('ch_28.json', 39): [((1, 1), (1, 1)), ((2, 2), (2, 2))],
    ('ch_40.json', 7): [((1, 1), (1, 2)), ((2, 2), (3, 3))],
}

print("=== VERIFYING CATEGORY 2 & 3A SPLITS ===")
for (ch_file, pid), chunk_rules in TARGET_MAPPINGS.items():
    fpath = os.path.join(assets_dir, ch_file)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    p = [x for x in data if x.get('id') == pid][0]
    en_s = split_sents(p['en'])
    ko_s = split_sents(p['ko'])
    
    chunks_en = []
    chunks_ko = []
    for en_rng, ko_rng in chunk_rules:
        c_en = " ".join(en_s[en_rng[0]-1:en_rng[1]])
        c_ko = " ".join(ko_s[ko_rng[0]-1:ko_rng[1]])
        chunks_en.append(c_en)
        chunks_ko.append(c_ko)
        
    recon_en = normalize_text(" ".join(chunks_en))
    orig_en = normalize_text(p['en'])
    assert recon_en == orig_en, f"EN mismatch for {ch_file} ID {pid}"
    
    recon_ko = normalize_text(" ".join(chunks_ko))
    orig_ko = normalize_text(p['ko'])
    assert recon_ko == orig_ko, f"KO mismatch for {ch_file} ID {pid}"
    
    print(f"PASS: {ch_file} ID {pid:3d} ({p.get('tag')}) -> {len(chunk_rules)} chunks. Invariant 100% OK.")

print("\nAll 8 target paragraphs pass the 100% character invariant test!")

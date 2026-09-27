import json
import os

def normalize_text(text: str) -> str:
    return " ".join(text.replace('\r', '').replace('\n', ' ').split())

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

TEST_SPLITS = {
    ('ch_31.json', 173): {
        'en_split': "heightened to the extreme. ",
        'ko_split': "극에 달해 있었다. "
    },
    ('ch_34.json', 16): {
        'en_split': "seated on the bodies of their victims. ",
        'ko_split': "그를 발견했다. "
    },
    ('ch_34.json', 40): {
        'en_split': "while it flamed by so fast. ",
        'ko_split': "길게 느껴졌다. "
    }
}

print("=== TESTING 3B CANDIDATE SPLITS ===")
for (ch_file, pid), anchors in TEST_SPLITS.items():
    fpath = os.path.join(assets_dir, ch_file)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    p = [x for x in data if x.get('id') == pid][0]
    
    en_split_at = anchors['en_split']
    ko_split_at = anchors['ko_split']
    
    assert en_split_at in p['en'], f"EN anchor not found in {ch_file} ID {pid}!"
    assert ko_split_at in p['ko'], f"KO anchor not found in {ch_file} ID {pid}!"
    
    en_p1, en_p2 = p['en'].split(en_split_at, 1)
    chunk1_en = (en_p1 + en_split_at).strip()
    chunk2_en = en_p2.strip()
    
    ko_p1, ko_p2 = p['ko'].split(ko_split_at, 1)
    chunk1_ko = (ko_p1 + ko_split_at).strip()
    chunk2_ko = ko_p2.strip()
    
    # Assert character conservation invariant
    assert normalize_text(chunk1_en + " " + chunk2_en) == normalize_text(p['en'])
    assert normalize_text(chunk1_ko + " " + chunk2_ko) == normalize_text(p['ko'])
    
    print(f"PASS: {ch_file} ID {pid:3d} ({p.get('tag')})")
    print(f"   Chunk 1: EN={len(chunk1_en)} ch, KO={len(chunk1_ko)} ch")
    print(f"   Chunk 2: EN={len(chunk2_en)} ch, KO={len(chunk2_ko)} ch")

print("\nALL 3 CANDIDATE SPLITS 100% INVARIANT PASS!")

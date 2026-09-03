import json
import os
import shutil
import re
from datetime import datetime

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

# Define split rules for symmetric paragraphs:
# list of chunk sentence-ranges (1-based, inclusive)
SPLIT_RULES = {
    # ('ch_04.json', 149): 9 sentences -> 3 chunks (3, 3, 3)
    ('ch_04.json', 149): [(1, 3), (4, 6), (7, 9)],
    
    # ('ch_05.json', 19): 3 sentences -> 2 chunks (1, 2-3)
    ('ch_05.json', 19): [(1, 1), (2, 3)],
    
    # ('ch_07.json', 13): 4 sentences -> 2 chunks (2, 2)
    ('ch_07.json', 13): [(1, 2), (3, 4)],
    
    # ('ch_09.json', 12): 3 sentences -> 2 chunks (1, 2-3)
    ('ch_09.json', 12): [(1, 1), (2, 3)],
    
    # ('ch_13.json', 44): 3 sentences -> 2 chunks (1, 2-3)
    ('ch_13.json', 44): [(1, 1), (2, 3)],
    
    # ('ch_21.json', 178): 4 sentences -> 2 chunks (2, 2)
    ('ch_21.json', 178): [(1, 2), (3, 4)],
    
    # ('ch_27.json', 117): 6 sentences -> 2 chunks (3, 3)
    ('ch_27.json', 117): [(1, 3), (4, 6)],
    
    # ('ch_27.json', 144): 6 sentences -> 2 chunks (3, 3)
    ('ch_27.json', 144): [(1, 3), (4, 6)],
    
    # ('ch_31.json', 200): 5 sentences -> 2 chunks (2, 3)
    ('ch_31.json', 200): [(1, 2), (3, 5)],
    
    # ('ch_34.json', 32): 7 sentences -> 3 chunks (3, 2, 2)
    ('ch_34.json', 32): [(1, 3), (4, 5), (6, 7)],
    
    # ('ch_38.json', 11): 6 sentences -> 2 chunks (3, 3)
    ('ch_38.json', 11): [(1, 3), (4, 6)],
}

def dry_run_check():
    assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
    print("=== DRY RUN VERIFICATION OF ALL 11 TARGET PARAGRAPHS ===")
    
    for (ch_file, pid), ranges in SPLIT_RULES.items():
        fpath = os.path.join(assets_dir, ch_file)
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
            
        p = [x for x in data if x.get('id') == pid][0]
        en_s = split_sents(p['en'])
        ko_s = split_sents(p['ko'])
        
        assert len(en_s) == len(ko_s), f"Sentence count mismatch in {ch_file} ID {pid}: EN={len(en_s)}, KO={len(ko_s)}"
        
        chunks_en = []
        chunks_ko = []
        for start_idx, end_idx in ranges:
            c_en = " ".join(en_s[start_idx-1:end_idx])
            c_ko = " ".join(ko_s[start_idx-1:end_idx])
            chunks_en.append(c_en)
            chunks_ko.append(c_ko)
            
        reconstructed_en = " ".join(chunks_en)
        reconstructed_ko = " ".join(chunks_ko)
        
        # Test invariant
        orig_en_clean = normalize_text(p['en'])
        recon_en_clean = normalize_text(reconstructed_en)
        assert orig_en_clean == recon_en_clean, f"EN invariant failed for {ch_file} ID {pid}!\nOrig:  {orig_en_clean}\nRecon: {recon_en_clean}"
        
        orig_ko_clean = normalize_text(p['ko'])
        recon_ko_clean = normalize_text(reconstructed_ko)
        assert orig_ko_clean == recon_ko_clean, f"KO invariant failed for {ch_file} ID {pid}!\nOrig:  {orig_ko_clean}\nRecon: {recon_ko_clean}"
        
        print(f"PASS: {ch_file} ID {pid:3d} ({p.get('tag')}): {len(en_s)} sent -> {len(ranges)} chunks ({[end-start+1 for start, end in ranges]} sent/chunk). Invariant 100% OK.")

if __name__ == '__main__':
    dry_run_check()

import os
import re

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

def analyze_chapter(ch_num, out_f):
    en_file = rf'c:\git_repo\Book_apps\secret_garden\ch_{ch_num}_en.txt'
    ko_file = rf'c:\git_repo\Book_apps\secret_garden\ch_{ch_num}_ko.txt'
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_lines = [line.strip() for line in f if line.strip()]
    with open(ko_file, 'r', encoding='utf-8') as f:
        ko_lines = [line.strip() for line in f if line.strip()]
        
    out_f.write(f"\n--- Analyzing Chapter {ch_num} ---\n")
    out_f.write(f"EN lines: {len(en_lines)}, KO lines: {len(ko_lines)}\n")
    
    e = 0
    k = 0
    while e < min(len(en_lines), len(ko_lines)):
        e_text = strip_prefix(en_lines[e])
        k_text = strip_prefix(ko_lines[k])
        
        ratio = len(e_text) / len(k_text) if len(k_text) > 0 else 0
        if ratio < 0.3 or ratio > 3.0:
            out_f.write(f"\nPossible drift around line {e+1}:\n")
            out_f.write(f"EN[{e+1}]: {en_lines[e][:80]}...\n")
            out_f.write(f"KO[{k+1}]: {ko_lines[k][:80]}...\n")
            
            out_f.write("Context EN:\n")
            for i in range(max(0, e-1), min(len(en_lines), e+4)):
                out_f.write(f"  {en_lines[i][:100]}\n")
            out_f.write("Context KO:\n")
            for i in range(max(0, k-1), min(len(ko_lines), k+4)):
                out_f.write(f"  {ko_lines[i][:100]}\n")
            break
        e += 1
        k += 1

with open(r'c:\git_repo\Book_apps\secret_garden\drift_analysis.txt', 'w', encoding='utf-8') as f:
    analyze_chapter('24', f)
    analyze_chapter('27', f)

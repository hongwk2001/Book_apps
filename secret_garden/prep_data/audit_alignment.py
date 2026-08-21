import os
import glob
import re

def get_paragraphs(filepath):
    paras = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^P(\d+)([a-z]?)\|(.*)', line)
            if match:
                num = int(match.group(1))
                suffix = match.group(2)
                text = match.group(3).strip()
                if num not in paras:
                    paras[num] = []
                paras[num].append((suffix, text))
    return paras

def audit_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    raw_files = glob.glob(os.path.join(directory, 'raw_ch_*.txt'))
    
    suspicious = []
    
    for raw_file in sorted(raw_files):
        basename = os.path.basename(raw_file)
        match = re.search(r'raw_ch_(\d+)\.txt', basename)
        if not match: continue
        ch_num = match.group(1)
        en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
        if not os.path.exists(en_file): continue
        
        raw_paras = get_paragraphs(raw_file)
        en_paras = get_paragraphs(en_file)
        
        for num in sorted(raw_paras.keys()):
            r_text = raw_paras[num][0][1]
            r_len = len(r_text)
            
            if num not in en_paras:
                suspicious.append(f"Chapter {ch_num} - P{num}: Missing in English (Raw length {r_len})")
                continue
                
            e_items = en_paras[num]
            e_len = sum(len(t) for _, t in e_items)
            
            # Check for splits
            if len(e_items) > 1:
                suffixes = [s for s, _ in e_items]
                suspicious.append(f"Chapter {ch_num} - P{num}: Split into {len(e_items)} parts in EN ({', '.join(suffixes)})")
            
            # Check for length mismatch (too short or too long)
            if r_len > 50:
                ratio = e_len / r_len
                if ratio < 0.5:
                    suspicious.append(f"Chapter {ch_num} - P{num}: EN is suspiciously short (Ratio {ratio:.2f})")
                elif ratio > 2.0:
                    suspicious.append(f"Chapter {ch_num} - P{num}: EN is suspiciously long (Ratio {ratio:.2f})")

    with open(os.path.join(directory, 'audit_report.txt'), 'w', encoding='utf-8') as f:
        for s in suspicious:
            f.write(s + "\n")
    print(f"Found {len(suspicious)} suspicious items.")

if __name__ == '__main__':
    audit_files()

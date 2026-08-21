import os
import glob
import re

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

def align_chapter(raw_file, en_file):
    with open(raw_file, 'r', encoding='utf-8') as f:
        raw_lines = [strip_prefix(line) for line in f if strip_prefix(line)]
    with open(en_file, 'r', encoding='utf-8') as f:
        en_lines = [strip_prefix(line) for line in f if strip_prefix(line)]
        
    if len(raw_lines) == len(en_lines):
        mapped_en = [f"P{i}| {line}\n" for i, line in enumerate(en_lines, 1)]
        mapped_raw = [f"P{i}| {line}\n" for i, line in enumerate(raw_lines, 1)]
        return mapped_raw, mapped_en

    total_raw_len = sum(len(r) for r in raw_lines)
    total_en_len = sum(len(e) for e in en_lines)
    ratio = total_en_len / total_raw_len if total_raw_len > 0 else 1.0

    mapped_raw = []
    mapped_en = []
    
    e_idx = 0
    for r_idx, r_line in enumerate(raw_lines, 1):
        mapped_raw.append(f"P{r_idx}| {r_line}\n")
        expected_len = len(r_line) * ratio
        
        if e_idx >= len(en_lines):
            continue
            
        current_len = len(en_lines[e_idx])
        assigned_en = [en_lines[e_idx]]
        e_idx += 1
        
        while e_idx < len(en_lines):
            if r_idx == len(raw_lines):
                assigned_en.append(en_lines[e_idx])
                e_idx += 1
                continue
                
            next_len = len(en_lines[e_idx])
            dist_without = abs(expected_len - current_len)
            dist_with = abs(expected_len - (current_len + next_len))
            
            if dist_with < dist_without:
                current_len += next_len
                assigned_en.append(en_lines[e_idx])
                e_idx += 1
            else:
                break
                
        if len(assigned_en) == 1:
            mapped_en.append(f"P{r_idx}| {assigned_en[0]}\n")
        else:
            letters = 'abcdefghijklmnopqrstuvwxyz'
            for i, en_line in enumerate(assigned_en):
                suffix = letters[i] if i < len(letters) else str(i)
                mapped_en.append(f"P{r_idx}{suffix}| {en_line}\n")

    return mapped_raw, mapped_en

def process_files():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    # get chapter numbers
    raw_files = glob.glob(os.path.join(directory, 'raw_ch_*.txt'))
    for raw_file in raw_files:
        basename = os.path.basename(raw_file)
        match = re.search(r'raw_ch_(\d+)\.txt', basename)
        if match:
            ch_num = match.group(1)
            en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
            if os.path.exists(en_file):
                mapped_raw, mapped_en = align_chapter(raw_file, en_file)
                with open(raw_file, 'w', encoding='utf-8') as f:
                    f.writelines(mapped_raw)
                with open(en_file, 'w', encoding='utf-8') as f:
                    f.writelines(mapped_en)
                print(f"Aligned Chapter {ch_num} (RAW: {len(mapped_raw)} EN: {len(mapped_en)})")

if __name__ == '__main__':
    process_files()

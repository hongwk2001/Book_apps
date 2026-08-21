import os
import re
import glob

directory = r'c:\git_repo\Book_apps\secret_garden'
for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
    ko_file = os.path.join(directory, f'ch_{ch_num}_ko.txt')
    
    with open(en_file, 'r', encoding='utf-8') as f:
        en_lines = [line.strip() for line in f if line.strip()]
        
    with open(ko_file, 'r', encoding='utf-8') as f:
        ko_lines = [re.sub(r'^P\d+[a-z]?\|\s*', '', line).strip() for line in f if line.strip()]
        
    if len(en_lines) != len(ko_lines):
        print(f"Error: length mismatch in ch {ch_num}")
        continue
        
    mapped_ko = []
    for en, ko in zip(en_lines, ko_lines):
        match = re.match(r'^(P\d+[a-z]?\|)\s*', en)
        if match:
            prefix = match.group(1)
            mapped_ko.append(f"{prefix} {ko}\n")
        else:
            mapped_ko.append(f"{ko}\n")
            
    with open(ko_file, 'w', encoding='utf-8') as f:
        f.writelines(mapped_ko)

print("Applied EN prefixes to KO files.")

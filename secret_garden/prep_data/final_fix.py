import os
import re
import glob

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

def fix_ch24():
    # KO needs 2 splits
    ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_ko.txt'
    with open(ko_file, 'r', encoding='utf-8') as f:
        lines = [strip_prefix(line) for line in f if strip_prefix(line)]
    
    # Split 1
    idx1 = lines[12].find('"')
    if idx1 != -1:
        p1 = lines[12][:idx1].strip()
        p2 = lines[12][idx1:].strip()
        lines[12:13] = [p1, p2]
    
    # Split 2
    idx2 = lines[16].find('"')
    if idx2 != -1:
        p1 = lines[16][:idx2].strip()
        p2 = lines[16][idx2:].strip()
        lines[16:17] = [p1, p2]
        
    with open(ko_file, 'w', encoding='utf-8') as f:
        for l in lines:
            f.write(f"{l}\n")

def fix_ch27():
    # EN needs 1 split
    en_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_en.txt'
    with open(en_file, 'r', encoding='utf-8') as f:
        lines = [strip_prefix(line) for line in f if strip_prefix(line)]
        
    # EN[9] starts with "As he sat gazing..."
    target = "but he wasn't."
    idx = lines[9].find(target)
    if idx != -1:
        p1 = lines[9][:idx + len(target)].strip()
        p2 = lines[9][idx + len(target):].strip()
        lines[9:10] = [p1, p2]
        
    with open(en_file, 'w', encoding='utf-8') as f:
        for l in lines:
            f.write(f"{l}\n")

fix_ch24()
fix_ch27()

import os
import re

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

def fix_ch24():
    ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_ko.txt'
    with open(ko_file, 'r', encoding='utf-8') as f:
        lines = [strip_prefix(line) for line in f if strip_prefix(line)]
    
    # Split P13 (index 12)
    # Text starts with "'S" ??' ?-',S" ? ,zO" ?' ^^1~, ?  ~O  ~ S" . ?~, ,?<~?' o ?,"<~?' S S o ,  ^~ z^< S" ,  OO ?~c' ?^?',? ?,<~~ Z, ? 3','  O' O " ~"
    # Actually, let's just split by the first quotation mark.
    idx1 = lines[12].find('"')
    if idx1 != -1:
        p1 = lines[12][:idx1].strip()
        p2 = lines[12][idx1:].strip()
        lines[12:13] = [p1, p2]
    
    # Now the next split is at index 15 (was 14, but shifted by +1 = 15)
    # Text: Dickon stopped weeding... "Master Colin..."
    idx2 = lines[16].find('"') # shifted by 1, so old index 15 is now 16
    if idx2 != -1:
        p1 = lines[16][:idx2].strip()
        p2 = lines[16][idx2:].strip()
        lines[16:17] = [p1, p2]
        
    # Write back
    with open(ko_file, 'w', encoding='utf-8') as f:
        for i, l in enumerate(lines, 1):
            f.write(f"P{i}| {l}\n")
            
def fix_ch27():
    ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_ko.txt'
    with open(ko_file, 'r', encoding='utf-8') as f:
        lines = [strip_prefix(line) for line in f if strip_prefix(line)]
        
    # Merge P11 and P12 (index 10 and 11)
    p_merged = lines[10] + " " + lines[11]
    lines[10:12] = [p_merged]
    
    with open(ko_file, 'w', encoding='utf-8') as f:
        for i, l in enumerate(lines, 1):
            f.write(f"P{i}| {l}\n")

fix_ch24()
fix_ch27()

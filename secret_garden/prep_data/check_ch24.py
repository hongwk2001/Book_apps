import os
import re

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

en_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_en.txt'
ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_ko.txt'

with open(en_file, 'r', encoding='utf-8') as f:
    en_lines = [strip_prefix(line) for line in f if line.strip()]
with open(ko_file, 'r', encoding='utf-8') as f:
    ko_lines = [strip_prefix(line) for line in f if line.strip()]

# Let's align them by assuming EN has splits. We will just use an interactive approach or dump them side by side
with open(r'c:\git_repo\Book_apps\secret_garden\ch24_dump.txt', 'w', encoding='utf-8') as out:
    # First shift: after KO line 13, KO is missing 1 line compared to EN
    # So we align EN[14] with KO[13]
    # Let's just print EN 12-80 and KO 12-80
    for i in range(12, 80):
        out.write(f"EN[{i}]: {en_lines[i][:50]}...\n")
        if i-1 < len(ko_lines):
            out.write(f"KO[{i-1}]: {ko_lines[i-1][:50]}...\n")
        out.write("\n")

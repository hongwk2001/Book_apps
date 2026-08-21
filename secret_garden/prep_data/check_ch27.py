import os
import re

def strip_prefix(text):
    return re.sub(r'^P\d+[a-z]?\|\s*', '', text).strip()

en_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_en.txt'
ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_ko.txt'

with open(en_file, 'r', encoding='utf-8') as f:
    en_lines = [strip_prefix(line) for line in f if line.strip()]
with open(ko_file, 'r', encoding='utf-8') as f:
    ko_lines = [strip_prefix(line) for line in f if line.strip()]

with open(r'c:\git_repo\Book_apps\secret_garden\ch27_out.txt', 'w', encoding='utf-8') as out:
    for i in range(15):
        out.write(f"EN[{i+1}]: {en_lines[i][:60]}... (Len: {len(en_lines[i])})\n")
        out.write(f"KO[{i+1}]: {ko_lines[i][:60]}... (Len: {len(ko_lines[i])})\n")
        out.write("-\n")

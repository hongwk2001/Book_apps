import json
import re

def split_sents(text):
    text = re.sub(r'(Mr|Mrs|Dr|St|Prof|Rev|No)\.', r'\1<DOT>', text)
    sents = []
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z\"\'\uAC00-\uD7A3])', text)
    for p in parts:
        if p.strip():
            sents.append(p.strip().replace('<DOT>', '.'))
    return sents

data = json.load(open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_23.json', encoding='utf-8'))
mismatches = [38, 51, 60, 86, 107, 108]

with open('mismatched_sents.txt', 'w', encoding='utf-8') as f:
    for d in data:
        if d['id'] in mismatches:
            en_sents = split_sents(d['en'])
            ko_sents = split_sents(d['ko'])
            f.write(f"--- ID {d['id']} ---\n")
            f.write("EN:\n")
            for i, s in enumerate(en_sents): f.write(f"{i}: {s}\n")
            f.write("KO:\n")
            for i, s in enumerate(ko_sents): f.write(f"{i}: {s}\n")
            f.write("\n")

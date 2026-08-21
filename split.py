import json
import re

def split_sents(text):
    text = re.sub(r'(Mr|Mrs|Dr|St|Prof|Rev|No)\.', r'\1<DOT>', text)
    sents = []
    # Split by sentence endings, but keep the punctuation attached
    # A sentence ending is . ! ? followed by space and a capital letter or quote
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z\"\'\uAC00-\uD7A3])', text)
    for p in parts:
        if p.strip():
            sents.append(p.strip().replace('<DOT>', '.'))
    return sents

data = json.load(open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_23.json', encoding='utf-8'))
mismatches = []
for d in data:
    en_text = d.get('en', '')
    ko_text = d.get('ko', '')
    if not en_text: continue
    en_sents = split_sents(en_text)
    if len(en_sents) > 3:
        ko_sents = split_sents(ko_text)
        if len(en_sents) != len(ko_sents):
            print(f"ID: {d['id']} EN={len(en_sents)} KO={len(ko_sents)}")
            mismatches.append(d['id'])
print('Mismatches:', mismatches)

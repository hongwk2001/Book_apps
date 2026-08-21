import json
import re

with open('C:\\git_repo\\Book_apps\\dracula\\long_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_sentences(text):
    sentences = re.split(r'([.!?]+(?:\s+|$))', text)
    result = []
    current = ""
    for piece in sentences:
        current += piece
        if re.search(r'[.!?]', piece):
            result.append(current.strip())
            current = ""
    if current.strip():
        result.append(current.strip())
    return result

mismatches = []
for i in data:
    en_sents = split_sentences(i.get('en', ''))
    ko_sents = split_sentences(i.get('ko', ''))
    
    if len(en_sents) != len(ko_sents):
        mismatches.append({'id': i['id'], 'en': en_sents, 'ko': ko_sents})

with open('C:\\git_repo\\Book_apps\\dracula\\mismatches.json', 'w', encoding='utf-8') as f:
    json.dump(mismatches, f, ensure_ascii=False, indent=2)

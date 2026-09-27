import json
import re

with open('C:\\git_repo\\Book_apps\\dracula\\long_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_sentences(text):
    text = text.replace('Mr.', 'Mr<DOT>').replace('Mrs.', 'Mrs<DOT>').replace('Dr.', 'Dr<DOT>')
    sentences = re.split(r'([.!?]+[\"”]*(?:\s+|$))', text)
    result = []
    current = ""
    for piece in sentences:
        current += piece
        if re.search(r'[.!?]', piece):
            result.append(current.strip().replace('<DOT>', '.'))
            current = ""
    if current.strip():
        result.append(current.strip().replace('<DOT>', '.'))
    return result

mismatches = []
for i in data:
    en_sents = split_sentences(i.get('en', ''))
    ko_sents = split_sentences(i.get('ko', ''))
    
    if len(en_sents) != len(ko_sents):
        mismatches.append(i['id'])

print("Mismatches:", mismatches)

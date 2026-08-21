import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_25.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def get_sentences(text):
    sentences = re.split(r'([.?!](?:\s+|$))', text)
    result = []
    for i in range(0, len(sentences)-1, 2):
        result.append((sentences[i] + sentences[i+1]).strip())
    if len(sentences) % 2 != 0 and sentences[-1].strip():
        result.append(sentences[-1].strip())
    return result

mismatch = 0
total = 0
for item in data:
    en = item.get('en', '')
    ko = item.get('ko', '')
    en_sents = get_sentences(en)
    ko_sents = get_sentences(ko)
    if len(en_sents) > 3:
        total += 1
        if len(en_sents) != len(ko_sents):
            mismatch += 1
            print(f"ID: {item['id']}, EN: {len(en_sents)}, KO: {len(ko_sents)}")

print(f'Total >3: {total}, Mismatch: {mismatch}')

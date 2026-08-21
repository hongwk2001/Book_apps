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

mismatches = []
for item in data:
    en = item.get('en', '')
    ko = item.get('ko', '')
    en_sents = get_sentences(en)
    ko_sents = get_sentences(ko)
    if len(en_sents) > 3 and len(en_sents) != len(ko_sents):
        mismatches.append({
            'id': item['id'],
            'en_sents': en_sents,
            'ko_sents': ko_sents
        })

with open(r'C:\git_repo\Book_apps\mismatches_sents.json', 'w', encoding='utf-8') as f:
    json.dump(mismatches, f, ensure_ascii=False, indent=2)

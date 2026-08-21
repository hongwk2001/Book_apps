import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_en(text):
    text = re.sub(r'\b(Dr|Mr|Mrs|Ms|Prof)\.', r'\1<DOT>', text)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9\"\'\u201c\u2018])', text.strip())
    sentences = [s.replace('<DOT>', '.') for s in sentences if s]
    return sentences

def split_ko(text):
    sentences = re.split(r'(?<=[.!?])\s+(?=[가-힣\"\'\u201c\u2018a-zA-Z0-9])', text.strip())
    sentences = [s for s in sentences if s]
    return sentences

mismatches = []
for item in data:
    if 'en' in item:
        en_sents = split_en(item['en'])
        ko_sents = split_ko(item['ko'])
        # if len(en_sents) > 3 or len(ko_sents) > 3:
        if len(en_sents) != len(ko_sents):
            mismatches.append({
                'tag': item['tag'],
                'en_count': len(en_sents),
                'ko_count': len(ko_sents),
                'en': en_sents,
                'ko': ko_sents
            })

with open('mismatches.json', 'w', encoding='utf-8') as f:
    json.dump(mismatches, f, ensure_ascii=False, indent=2)

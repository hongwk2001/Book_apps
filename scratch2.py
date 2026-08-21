import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_14.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    en = item.get('en', '')
    ko = item.get('ko', '')
    en_sents = [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'’‘“])', en.strip()) if s]
    ko_sents = [s for s in re.split(r'(?<=[.!?])\s+(?=[가-힣"\'’‘“])', ko.strip()) if s]
    if len(en_sents) > 3:
        if len(en_sents) != len(ko_sents):
            print(f"ID {item['id']} tag {item.get('tag')} Mismatch: en={len(en_sents)}, ko={len(ko_sents)}")

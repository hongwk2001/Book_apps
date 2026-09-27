import json
import re

with open('C:\\git_repo\\Book_apps\\dracula\\long_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mismatch = 0
for i in data:
    en_text = i.get('en', '').strip()
    ko_text = i.get('ko', '').strip()
    
    en_sents = [s for s in re.split(r'[.!?]+(?:\s+|$)', en_text) if s.strip()]
    ko_sents = [s for s in re.split(r'[.!?]+(?:\s+|$)', ko_text) if s.strip()]
    
    if len(en_sents) != len(ko_sents):
        print(f"Mismatch: id {i.get('id')}, en: {len(en_sents)}, ko: {len(ko_sents)}")
        mismatch += 1

print(f"Total mismatches: {mismatch}")

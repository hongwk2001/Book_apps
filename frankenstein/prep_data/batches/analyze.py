import json
import re

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_9.ch5.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    en = item['en'].replace('\n', ' ')
    ko = item['ko'].replace('\n', ' ')
    
    en_sents = [s for s in re.split(r'(?<=[.!?])\s+', en) if s]
    ko_sents = [s for s in re.split(r'(?<=[.!?])\s+', ko) if s]
    
    print(f"P{item['id']:03d}: EN={len(en_sents)}, KO={len(ko_sents)}")

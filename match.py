import json
import re

with open('long_items.json', 'r', encoding='utf-8') as f:
    long_items = json.load(f)

for item in long_items:
    en_sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', item['en']) if s.strip()]
    ko_sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', item['ko']) if s.strip()]
    if len(en_sents) == len(ko_sents):
        print(f"MATCH: Tag {item['tag']} - {len(en_sents)} sentences")

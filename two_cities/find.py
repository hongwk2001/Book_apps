import json
import re

with open('C:\\git_repo\\Book_apps\\dracula\\src\\main\\assets\\books\\ch_13.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

long_items = []
for item in data:
    en = item.get('en', '')
    sentences = [s for s in re.split(r'[.!?]+(?:\s+|$)', en.strip()) if s.strip()]
    if len(sentences) > 3:
        long_items.append(item)

with open('C:\\git_repo\\Book_apps\\dracula\\long_items.json', 'w', encoding='utf-8') as f:
    json.dump(long_items, f, ensure_ascii=False, indent=2)

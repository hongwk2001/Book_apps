import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

long_items = []
for item in data:
    if 'en' in item:
        sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9])', item['en'].strip())
        sentences = [s for s in sentences if s]
        if len(sentences) > 3:
            long_items.append(item)

with open('long_items.json', 'w', encoding='utf-8') as f:
    json.dump(long_items, f, ensure_ascii=False, indent=2)

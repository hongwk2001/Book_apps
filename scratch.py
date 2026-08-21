import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_14.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    en = item.get('en', '')
    sentences = [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'’‘“])', en.strip()) if s]
    if len(sentences) > 3:
        print(f"ID {item['id']} tag {item.get('tag')} has {len(sentences)} sentences")

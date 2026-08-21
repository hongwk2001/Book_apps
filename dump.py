import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_14.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

res = []
for item in data:
    en_sents = [s for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'’‘“])', item.get('en', '').strip()) if s]
    if len(en_sents) > 3:
        res.append(item)

with open(r'C:\git_repo\Book_apps\split_me.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2, ensure_ascii=False)

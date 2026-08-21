import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_26.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mismatch = 0
for item in data:
    if 'en' in item:
        en_s = [s.strip() for s in re.split(r'(?<=[.!?])\s+', item['en'].strip()) if s.strip()]
        ko_s = [s.strip() for s in re.split(r'(?<=[.!?])\s+', item['ko'].strip()) if s.strip()]
        if len(en_s) > 3:
            if len(en_s) != len(ko_s):
                print(f"Mismatch {item.get('tag')}: EN {len(en_s)}, KO {len(ko_s)}")
                mismatch += 1

print(f"Total mismatches: {mismatch}")

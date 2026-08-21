import json
import os

for i in range(1, 4):
    src_file = rf'C:\git_repo\TKprof_book\books\dracula\scripts\bilingual_ch_{i:02d}.json'
    with open(src_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"File: bilingual_ch_{i:02d}.json")
    print(data[0])

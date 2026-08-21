import json
import re

with open('src/main/assets/books/ch_11.json', encoding='utf-8') as f:
    data = json.load(f)

for x in data:
    if x['tag'].startswith('P006-'):
        print(f"[{x['tag']}]")
        print(f"EN: {x['en']}")
        print(f"KO: {x['ko']}")
        print()

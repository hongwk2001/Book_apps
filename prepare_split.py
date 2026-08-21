import json
import re

def count_sentences(text):
    return len([s for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()])

def split_sentences(text):
    sents = []
    # this split is a bit simple, let's use a better regex
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'\uAC00-\uD7A3])', text.strip())
    # but the above might fail on some. Let's just use a basic one.
    return [p.strip() for p in re.split(r'(?<=[.!?])\s+', text.strip()) if p.strip()]

with open('C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_10.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

long_items = []
for item in data:
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    if count_sentences(item['en']) > 3:
        long_items.append((item, en_sents, ko_sents))

mismatched = []
for item, en, ko in long_items:
    if len(en) != len(ko):
        mismatched.append({'id': item['id'], 'tag': item['tag'], 'en': item['en'], 'ko': item['ko']})

with open('mismatched.json', 'w', encoding='utf-8') as f:
    json.dump(mismatched, f, ensure_ascii=False, indent=2)

print(f"Total mismatched items: {len(mismatched)}")

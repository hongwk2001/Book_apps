import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_25.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def count_sentences(text):
    return len([s for s in re.split(r'[.?!](?:\s+|$)', text) if s.strip()])

for item in data:
    en_text = item.get('en', '')
    if count_sentences(en_text) > 3:
        print(f"ID: {item['id']}, tag: {item.get('tag')}, Sentences: {count_sentences(en_text)}")

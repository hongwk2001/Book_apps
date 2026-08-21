import json
import re

def split_sentences(text):
    text = re.sub(r'(Dr|Mr|Mrs|Ms)\.', r'\1<DOT>', text)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z\"\'\uAC00-\uD7A3])', text)
    return [s.replace('<DOT>', '.') for s in sentences]

def process_file():
    with open('C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_22.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    long_items = []
    for d in data:
        en_sents = split_sentences(d['en'])
        ko_sents = split_sentences(d['ko'])
        if len(en_sents) > 3 or len(ko_sents) > 3:
            long_items.append((d, en_sents, ko_sents))
            
    print(f"Total long items: {len(long_items)}")
    
process_file()

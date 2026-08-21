import json
import re

def split_sentences(text):
    text = re.sub(r'(Dr|Mr|Mrs|Ms|St|Prof|etc)\.', r'\1<DOT>', text)
    text = re.sub(r'([A-Z])\.', r'\1<DOT>', text)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z\"\'\uAC00-\uD7A3\u201C\u2018])', text)
    return [s.replace('<DOT>', '.') for s in sentences]

def process_file():
    with open('C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_22.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mismatched = []
    matched = []
    
    for d in data:
        en_sents = split_sentences(d['en'])
        ko_sents = split_sentences(d['ko'])
        if len(en_sents) > 3 or len(ko_sents) > 3:
            if len(en_sents) == len(ko_sents):
                matched.append(d)
            else:
                mismatched.append({'id': d['id'], 'en_len': len(en_sents), 'ko_len': len(ko_sents), 'en': en_sents, 'ko': ko_sents})
                
    print(f"Matched: {len(matched)}")
    print(f"Mismatched: {len(mismatched)}")
    
    with open('mismatched.json', 'w', encoding='utf-8') as f:
        json.dump(mismatched, f, ensure_ascii=False, indent=2)

process_file()

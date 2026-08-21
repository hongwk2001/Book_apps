import json
import re

with open('src/main/assets/books/ch_11.json', encoding='utf-8') as f:
    data = json.load(f)

def extract_and_combine(data, prefix):
    en_full = ""
    ko_full = ""
    for x in data:
        if x['tag'].startswith(prefix):
            en_full += x['en'] + " "
            ko_full += x['ko'] + " "
    return en_full.strip(), ko_full.strip()

def split_sentences_en(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"“‘])', text) if s.strip()]

def split_sentences_ko(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

paragraphs = ['P006', 'P024', 'P027', 'P028', 'P029', 'P034', 'P036', 'P040', 'P049', 'P050']
output = {}

for p in paragraphs:
    en, ko = extract_and_combine(data, f"{p}-")
    output[p] = {
        'en': split_sentences_en(en),
        'ko': split_sentences_ko(ko)
    }

with open('debug.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

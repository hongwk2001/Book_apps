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

en, ko = extract_and_combine(data, 'P006-')
print("EN:", repr(en))
print("KO length:", len(ko))

def split_sentences_en(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z"“‘])', text) if s.strip()]

def split_sentences_ko(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

print("EN sentences:", split_sentences_en(en))
print("KO sentences count:", len(split_sentences_ko(ko)))

import json
import re

def split_en_sentences(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?;:])\s+(?=[A-Za-z”\"])', text.strip())
    return [s.strip() for s in sents if s.strip()]

def split_ko_sentences(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?])\s+(?=[가-힣”\"])', text.strip())
    return [s.strip() for s in sents if s.strip()]

data = json.load(open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_28.ch24.json', encoding='utf-8'))
mismatch = 0
for item in data:
    en_sents = split_en_sentences(item['en'])
    ko_sents = split_ko_sentences(item['ko'])
    if len(en_sents) != len(ko_sents):
        mismatch += 1
        print(f"ID {item['id']} mismatch: {len(en_sents)} vs {len(ko_sents)}")
        # print("EN:", en_sents)
        # print("KO:", ko_sents)
print(mismatch)

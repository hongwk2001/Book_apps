import json
import re

def split_en(text):
    sentences = re.split(r'(?<=[.!?\"])\s+(?=[A-Z\"\'I])', text)
    return [s.strip() for s in sentences if s.strip()]

def split_ko(text):
    # Korean sentences typically end with . ? ! or " followed by space and a new word.
    sentences = re.split(r'(?<=[.!?\"])\s+(?=[가-힣\"\'(])', text)
    return [s.strip() for s in sentences if s.strip()]

with open('C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_21.json', encoding='utf-8') as f:
    data = json.load(f)

mismatch_count = 0
for item in data:
    en = item['en']
    en_s = split_en(en)
    if len(en_s) > 3:
        ko_s = split_ko(item['ko'])
        if len(en_s) != len(ko_s):
            print(f"ID {item['id']} mismatch: EN {len(en_s)} vs KO {len(ko_s)}")
            mismatch_count += 1
            
print(f"Total mismatches: {mismatch_count}")

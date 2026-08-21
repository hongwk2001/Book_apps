import json
import re

def split_sentences(text):
    # simple split by punctuation
    sentences = re.split(r'(?<=[.!?\"])\s+(?=[A-Z\"\'I])', text)
    return [s for s in sentences if s.strip()]

with open('C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_21.json', encoding='utf-8') as f:
    data = json.load(f)

with open('C:/git_repo/Book_apps/analysis.txt', 'w', encoding='utf-8') as out:
    for item in data:
        en = item['en']
        sentences_en = split_sentences(en)
        if len(sentences_en) > 3:
            out.write(f"ID: {item['id']}, Tag: {item['tag']}, Sentences: {len(sentences_en)}\n")
            out.write(f"EN: {en}\n")
            out.write(f"KO: {item['ko']}\n")
            out.write('-'*40 + '\n')

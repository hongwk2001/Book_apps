import json
import re

def split_sentences_en(text):
    text = re.sub(r'(Mr\.|Mrs\.|Dr\.|St\.|Prof\.|Rev\.|Mt\.)', lambda m: m.group(1).replace('.', '<DOT>'), text)
    text = re.sub(r'([.!?])\s+(?=[A-Z0-9\"\'\u201C\u2018])', r'\1|', text)
    text = text.replace('<DOT>', '.')
    return [s.strip() for s in text.split('|') if s.strip()]

def split_sentences_ko(text):
    text = re.sub(r'([.!?])\s+(?=[가-힣0-9\"\'\u201C\u2018A-Z])', r'\1|', text)
    return [s.strip() for s in text.split('|') if s.strip()]

data = json.load(open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_18.json', encoding='utf-8'))
errors = 0
for d in data:
    for c in d['chunks']:
        if len(split_sentences_en(c['en'])) > 3:
            print('EN > 3:', c['en'])
            errors += 1
        if len(split_sentences_ko(c['ko'])) > 3:
            print('KO > 3:', c['ko'])
            errors += 1
print('Errors:', errors)

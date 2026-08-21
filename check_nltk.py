import json
import re
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_26.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

mismatches = 0
for item in data:
    if 'en' in item:
        en_s = nltk.sent_tokenize(item['en'].replace('.—', '. '))
        
        # basic regex for ko but ignoring dots in middle of words/sentences?
        # A simple approach for KO: split on . ! ? followed by space and a Korean letter or quote
        ko_text = item['ko'].replace('.—', '. ')
        ko_s = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[가-힣"\'(])', ko_text.strip()) if s.strip()]
        
        if len(en_s) > 3 or len(ko_s) > 3:
            if len(en_s) != len(ko_s):
                print(f"Mismatch {item.get('tag')}: EN {len(en_s)}, KO {len(ko_s)}")
                mismatches += 1

print(f"Total mismatches: {mismatches}")

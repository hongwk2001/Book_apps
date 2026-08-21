import os
import json
import re

directory = r'c:\git_repo\Book_apps\secret_garden\json_output'
exact_match = 0
mismatch = 0
total_long = 0

def count_sentences(text):
    # split by . ! ? optionally followed by quotes
    sentences = re.split(r'[.!?]+["\']?(?=\s|$)', text)
    return len([s for s in sentences if s.strip()])

for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    with open(os.path.join(directory, f'ch_{ch_num}.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        en_sents = count_sentences(item['en'])
        ko_sents = count_sentences(item['ko'])
        
        if en_sents > 3:
            total_long += 1
            if en_sents == ko_sents:
                exact_match += 1
            else:
                mismatch += 1

print(f"Total >3 sentences: {total_long}")
print(f"Exact sentence count match: {exact_match}")
print(f"Sentence count mismatch: {mismatch}")

import os
import json
import re

directory = r'c:\git_repo\Book_apps\secret_garden\json_output'
batch_dir = r'c:\git_repo\Book_apps\secret_garden\batches'
os.makedirs(batch_dir, exist_ok=True)

def count_sentences(text):
    sentences = re.split(r'[.!?]+["\']?(?=\s|$)', text)
    return len([s for s in sentences if s.strip()])

long_paragraphs = []

for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    with open(os.path.join(directory, f'ch_{ch_num}.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        en_sents = count_sentences(item['en'])
        ko_sents = count_sentences(item['ko'])
        # If either has > 3 sentences
        if en_sents > 3 or ko_sents > 3:
            long_paragraphs.append({
                "file": f'ch_{ch_num}.json',
                "id": item['id'],
                "tag": item['tag'],
                "en": item['en'],
                "ko": item['ko']
            })

# Split into batches of 15
batch_size = 15
batches = [long_paragraphs[i:i + batch_size] for i in range(0, len(long_paragraphs), batch_size)]

for i, batch in enumerate(batches, 1):
    with open(os.path.join(batch_dir, f'batch_{i}.json'), 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Created {len(batches)} batches.")

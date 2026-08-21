import os
import json
import re

directory = r'c:\git_repo\Book_apps\secret_garden\json_output'
long_count = 0
total_count = 0

for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    with open(os.path.join(directory, f'ch_{ch_num}.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        total_count += 1
        # count sentences roughly by punctuation
        sentences = re.split(r'[.!?]+', item['en'])
        sentences = [s for s in sentences if s.strip()]
        if len(sentences) > 3:
            long_count += 1

print(f"Total paragraphs: {total_count}")
print(f"Paragraphs > 3 sentences: {long_count}")

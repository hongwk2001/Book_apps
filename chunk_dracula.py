import json
import os
import re

books_dir = r"C:\git_repo\Book_apps\dracula\src\main\assets\books"

def split_sentences(text):
    # Match sentences ending in . ! or ? possibly followed by quotes, then space
    sents = re.split(r'(?<=[.!?])(?:\s+|$)|(?<=[.!?]["' + r"'" + r'])(?:\s+|$)', text)
    sents = [s.strip() for s in sents if s.strip()]
    # Sometimes regex split by lookbehind still leaves empty strings or we need to handle better
    # Let's use a simpler approach: find all boundaries
    # Actually, a simple regex split:
    # return re.findall(r'[^.!?]+[.!?]+', text)
    
    # Better:
    raw_sents = re.split(r'([.!?]+["' + r"'" + r']?(?:\s+|$))', text)
    result = []
    current = ""
    for part in raw_sents:
        current += part
        if re.search(r'[.!?]', part):
            result.append(current.strip())
            current = ""
    if current.strip():
        result.append(current.strip())
    
    return result if result else [text]

def chunk_list(items, max_size=3):
    return [items[i:i + max_size] for i in range(0, len(items), max_size)]

for i in range(1, 28):
    filename = f"ch_{i:02d}.json"
    filepath = os.path.join(books_dir, filename)
    
    if not os.path.exists(filepath): continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    new_data = []
    
    for item in data:
        en_sents = split_sentences(item['en'])
        
        if len(en_sents) > 3:
            ko_sents = split_sentences(item['ko'])
            
            en_chunks = chunk_list(en_sents, 3)
            
            # Proportional distribution for ko_sents
            ko_chunks = []
            ko_idx = 0
            for chunk in en_chunks:
                # How many ko sentences to take?
                # ratio = len(chunk) / len(en_sents)
                # ko_count = round(ratio * len(ko_sents))
                ko_count = max(1, round(len(chunk) / len(en_sents) * len(ko_sents)))
                
                # Adjust if it's the last chunk
                if chunk == en_chunks[-1]:
                    ko_chunk = ko_sents[ko_idx:]
                else:
                    ko_chunk = ko_sents[ko_idx:ko_idx + ko_count]
                    ko_idx += ko_count
                
                ko_chunks.append(" ".join(ko_chunk))
                
            for j, (en_c, ko_c) in enumerate(zip(en_chunks, ko_chunks)):
                new_item = {
                    "id": 0, # Will renumber later
                    "tag": f"{item['tag']}-{j+1}",
                    "en": " ".join(en_c),
                    "ko": ko_c,
                    "is_header": item['is_header']
                }
                new_data.append(new_item)
        else:
            new_data.append(item)
            
    # Renumber IDs
    for idx, item in enumerate(new_data):
        item['id'] = idx + 1
        
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=2)

print("Chunking complete.")
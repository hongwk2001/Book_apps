import json
import re
import math

def split_sentences(text, lang='en'):
    if lang == 'en':
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"\'’‘“])', text) if s.strip()]
    else:
        sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+(?=[가-힣"\'’‘“])', text) if s.strip()]
    if not sents:
        return [text]
    
    # Re-attach spaces or just use the split as is? 
    # Wait, re.split with lookbehind keeps the punctuation, but consumes the space!
    # So we can just join them with space later.
    return sents

def chunk_list(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def process_item(item, new_id):
    en_text = item.get('en', '')
    ko_text = item.get('ko', '')
    tag = item.get('tag', '')
    
    en_sents = split_sentences(en_text, 'en')
    ko_sents = split_sentences(ko_text, 'ko')
    
    if len(en_sents) <= 3:
        # No need to split
        chunks = [{
            "tag": tag,
            "en": en_text,
            "ko": ko_text
        }]
    else:
        # Determine number of chunks based on en_sents (max 3 per chunk)
        num_chunks = math.ceil(len(en_sents) / 3.0)
        
        # We try to distribute en_sents and ko_sents into `num_chunks` chunks evenly
        en_chunk_size = math.ceil(len(en_sents) / num_chunks)
        ko_chunk_size = math.ceil(len(ko_sents) / num_chunks)
        
        chunks = []
        for i in range(num_chunks):
            en_part = en_sents[i * en_chunk_size : (i + 1) * en_chunk_size]
            
            # For the last chunk, take all remaining ko_sents
            if i == num_chunks - 1:
                ko_part = ko_sents[i * ko_chunk_size : ]
            else:
                ko_part = ko_sents[i * ko_chunk_size : (i + 1) * ko_chunk_size]
                
            chunks.append({
                "tag": f"{tag}-{i+1}",
                "en": " ".join(en_part),
                "ko": " ".join(ko_part)
            })
            
    return {
        "id": new_id,
        "original_id": item['id'],
        "chunks": chunks
    }

def main():
    file_path = r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_14.json'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    out_data = []
    new_id = 1
    for item in data:
        processed = process_item(item, new_id)
        out_data.append(processed)
        new_id += 1
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()

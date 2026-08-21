import json
import re

def split_sentences_en(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?])\s+(?=[\"\'“‘A-Z])', text)
    return [s.strip() for s in sents if s.strip()]

def split_sentences_ko(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?])\s+(?=[\"\'“‘가-힣])', text)
    return [s.strip() for s in sents if s.strip()]

def align_and_chunk(en_sents, ko_sents):
    chunks = []
    en_len = len(en_sents)
    ko_len = len(ko_sents)
    en_idx = 0
    ko_idx = 0
    
    while en_idx < en_len or ko_idx < ko_len:
        en_step = min(3, en_len - en_idx)
        if en_idx + en_step == en_len:
            ko_step = ko_len - ko_idx
        else:
            ko_step = int(round((en_idx + en_step) / max(1, en_len) * ko_len)) - ko_idx
            
        if ko_step <= 0 and ko_idx < ko_len:
            ko_step = 1
            
        while ko_step > 3 and en_step > 1:
            en_step -= 1
            ko_step = int(round((en_idx + en_step) / max(1, en_len) * ko_len)) - ko_idx
            if ko_step <= 0 and ko_idx < ko_len:
                ko_step = 1

        if ko_step > 3:
            ko_step = min(3, ko_len - ko_idx)
            
        en_chunk = en_sents[en_idx:en_idx+en_step]
        ko_chunk = ko_sents[ko_idx:ko_idx+ko_step]
        
        chunks.append({
            'en': ' '.join(en_chunk),
            'ko': ' '.join(ko_chunk)
        })
        
        en_idx += en_step
        ko_idx += ko_step
        
    return chunks

def process():
    data = json.load(open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_11.ch7.json', encoding='utf-8'))
    out_data = []
    
    for item in data:
        en_sents = split_sentences_en(item['en'])
        ko_sents = split_sentences_ko(item['ko'])
        
        chunks = align_and_chunk(en_sents, ko_sents)
        
        chunk_objs = []
        for i, c in enumerate(chunks):
            chunk_objs.append({
                'tag': f"{item['tag']}-{i+1}",
                'en': c['en'],
                'ko': c['ko']
            })
            
        out_data.append({
            'original_id': item['id'],
            'chunks': chunk_objs
        })
        
    with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_11.ch7_done.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

process()
print("Done")

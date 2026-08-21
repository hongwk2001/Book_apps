import json
import re

def parse_sentences(text):
    # Split by sentence-ending punctuation followed by space and a capital letter, quote, or Korean character
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z가-힣"“\'_])', text)
    return [s.strip() for s in sents if s.strip()]

def align(en_sents, ko_sents):
    res = []
    e_idx, k_idx = 0, 0
    while e_idx < len(en_sents) or k_idx < len(ko_sents):
        e_remain = len(en_sents) - e_idx
        k_remain = len(ko_sents) - k_idx
        
        e_step = min(2, e_remain)
        if len(en_sents) > 0:
            k_step = max(1, round(e_step * len(ko_sents) / len(en_sents)))
        else:
            k_step = k_remain
            
        e_step = min(e_step, 3)
        k_step = min(k_step, 3)
        
        if e_idx + e_step >= len(en_sents): e_step = e_remain
        if k_idx + k_step >= len(ko_sents): k_step = k_remain
        
        if e_step == 0 and e_idx < len(en_sents): e_step = 1
        if k_step == 0 and k_idx < len(ko_sents): k_step = 1
            
        # Make sure no chunk exceeds 3 sentences
        e_step = min(e_step, 3)
        k_step = min(k_step, 3)

        res.append((
            " ".join(en_sents[e_idx:e_idx+e_step]),
            " ".join(ko_sents[k_idx:k_idx+k_step])
        ))
        e_idx += e_step
        k_idx += k_step
    return res

input_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_24.ch20.json'
output_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_24.ch20_done.json'

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

output = []
for item in data:
    orig_id = item['id']
    tag = item['tag']
    en = item['en'].replace('\n', ' ')
    ko = item['ko'].replace('\n', ' ')
    
    en_sents = parse_sentences(en)
    ko_sents = parse_sentences(ko)
    
    aligned = align(en_sents, ko_sents)
    
    chunks = []
    for i, (e, k) in enumerate(aligned):
        chunks.append({
            "tag": f"{tag}-{i+1}",
            "en": e,
            "ko": k
        })
    output.append({
        "original_id": orig_id,
        "chunks": chunks
    })

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Processing complete.")

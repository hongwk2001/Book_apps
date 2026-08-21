import json
import nltk
import re

def split_sentences_en(text):
    sents = nltk.sent_tokenize(text.replace('.—', '. '))
    # clean trailing spaces if any
    return [s.strip() for s in sents if s.strip()]

def split_sentences_ko(text):
    text = text.replace('.—', '. ')
    sentences = []
    curr = ""
    for char in text:
        curr += char
        if curr.endswith('. ') or curr.endswith('! ') or curr.endswith('? ') or curr.endswith('." ') or curr.endswith('!" ') or curr.endswith('?" '):
            sentences.append(curr.strip())
            curr = ""
    if curr.strip():
        sentences.append(curr.strip())
    if not sentences:
        sentences = [text]
    return sentences

def align_chunks(en_text, ko_text):
    en_sents = split_sentences_en(en_text)
    ko_sents = split_sentences_ko(ko_text)
    
    en_chunks = []
    for i in range(0, len(en_sents), 3):
        en_chunks.append(" ".join(en_sents[i:i+3]))
        
    if len(en_chunks) == 1:
        return [{"en": en_text, "ko": ko_text}]
        
    en_lens = [len(c) for c in en_chunks]
    total_en = sum(en_lens)
    if total_en == 0: total_en = 1
    target_ko_lens = [int(l / total_en * len(ko_text)) for l in en_lens]
    
    ko_chunks = []
    curr_chunk = []
    curr_len = 0
    chunk_idx = 0
    
    for s in ko_sents:
        if chunk_idx < len(target_ko_lens) - 1:
            if curr_len + len(s)/2 > target_ko_lens[chunk_idx] and curr_chunk:
                ko_chunks.append(" ".join(curr_chunk))
                curr_chunk = [s]
                curr_len = len(s)
                chunk_idx += 1
            else:
                curr_chunk.append(s)
                curr_len += len(s)
        else:
            curr_chunk.append(s)
            
    if curr_chunk:
        ko_chunks.append(" ".join(curr_chunk))
    
    while len(ko_chunks) < len(en_chunks):
        ko_chunks.append("")
        
    res = []
    for e, k in zip(en_chunks, ko_chunks):
        res.append({"en": e, "ko": k})
    return res

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_26.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

new_data = []
new_id = 1

for item in data:
    en_text = item.get('en', "")
    ko_text = item.get('ko', "")
    tag = item.get('tag', "")
    
    if en_text:
        en_sents = split_sentences_en(en_text)
        if len(en_sents) > 3:
            aligned = align_chunks(en_text, ko_text)
            chunks = []
            for i, chunk in enumerate(aligned, start=1):
                chunks.append({
                    "tag": f"{tag}-{i}",
                    "en": chunk['en'],
                    "ko": chunk['ko']
                })
            new_data.append({
                "id": new_id,
                "original_id": item["id"],
                "chunks": chunks
            })
            new_id += 1
        else:
            new_data.append({
                "id": new_id,
                "original_id": item["id"],
                "chunks": [{
                    "tag": tag + "-1",
                    "en": en_text,
                    "ko": ko_text
                }]
            })
            new_id += 1
    else:
        # For items that don't have en (if any)
        new_data.append({
            "id": new_id,
            "original_id": item["id"],
            "chunks": [{
                "tag": tag + "-1",
                "en": "",
                "ko": ""
            }]
        })
        new_id += 1

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_26.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print("Saved to ch_26.json")

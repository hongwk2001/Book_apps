import json
import re

def split_en(text):
    return re.split(r'(?<=[.!?])\s+(?=[A-Z“"”])', text)

def split_ko(text):
    return re.split(r'(?<=[.!?])\s+(?=[가-힣"“”])', text)

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_18.ch14.json', encoding='utf-8') as f:
    data = json.load(f)

result = []
for item in data:
    en_text = item['en'].replace('\n', ' ')
    ko_text = item['ko'].replace('\n', ' ')
    
    e = split_en(en_text)
    k = split_ko(ko_text)
    
    # Fixes for mismatches
    if item['id'] == 3:
        # e has 5, k has 6
        k[4] = k[4] + ' ' + k[5]
        k.pop(5)
    elif item['id'] == 8:
        # e has 5, k has 6
        k[0] = k[0] + ' ' + k[1]
        k.pop(1)
    elif item['id'] == 12:
        # e has 3, k has 3
        pass
    elif item['id'] == 13:
        # e has 4, k has 4
        pass
    elif item['id'] == 19:
        # e has 5, k has 6
        k[1] = k[1] + ' ' + k[2]
        k.pop(2)

    if len(e) != len(k):
        print(f"Warning: id {item['id']} len mismatch {len(e)} vs {len(k)}")
    
    # Now group 1-3 sentences
    chunks = []
    i = 0
    while i < len(e):
        if len(e) - i == 4:
            # split into 2 and 2
            chunks.append((e[i:i+2], k[i:i+2]))
            chunks.append((e[i+2:i+4], k[i+2:i+4]))
            i += 4
        elif len(e) - i == 5:
            # split into 3 and 2
            chunks.append((e[i:i+3], k[i:i+3]))
            chunks.append((e[i+3:i+5], k[i+3:i+5]))
            i += 5
        else:
            n = min(3, len(e) - i)
            chunks.append((e[i:i+n], k[i:i+n]))
            i += n
            
    out_chunks = []
    for idx, (e_c, k_c) in enumerate(chunks):
        out_chunks.append({
            "tag": f"{item['tag']}-{idx+1}",
            "en": " ".join(e_c),
            "ko": " ".join(k_c)
        })
        
    result.append({
        "original_id": item['id'],
        "chunks": out_chunks
    })

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_18.ch14_done.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print("Done")

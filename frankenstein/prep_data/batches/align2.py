import json
import re

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_25.ch21.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_sentences(text):
    text = text.replace('\n', ' ')
    sentences = re.split(r'(?<=[.!?;])\s+(?=[A-Z가-힣\"“\'])', text.strip())
    return [s for s in sentences if s]

out_data = []

def align_sentences(en_sents, ko_sents):
    target_ratio = sum(len(s) for s in ko_sents) / max(1, sum(len(s) for s in en_sents))
    n = len(en_sents)
    m = len(ko_sents)
    dp = {}
    dp[(0, 0)] = (0, [])
    
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) not in dp: continue
            for di in range(1, 4):
                if i + di > n: break
                for dj in range(1, 4):
                    if j + dj > m: break
                    en_group = " ".join(en_sents[i:i+di])
                    ko_group = " ".join(ko_sents[j:j+dj])
                    ratio = len(ko_group) / max(1, len(en_group))
                    cost = dp[(i, j)][0] + (ratio - target_ratio)**2
                    if (i+di, j+dj) not in dp or cost < dp[(i+di, j+dj)][0]:
                        dp[(i+di, j+dj)] = (cost, dp[(i, j)][1] + [(di, dj)])
                        
    if (n, m) in dp:
        best_path = dp[(n, m)][1]
        chunks = []
        i, j = 0, 0
        for di, dj in best_path:
            en_chunk = " ".join(en_sents[i:i+di])
            ko_chunk = " ".join(ko_sents[j:j+dj])
            chunks.append((en_chunk, ko_chunk))
            i += di
            j += dj
        return chunks
    else:
        return None

for item in data:
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    
    if len(en_sents) <= 3 and len(ko_sents) <= 3:
        chunks = [(" ".join(en_sents), " ".join(ko_sents))]
    else:
        chunks = align_sentences(en_sents, ko_sents)
        if not chunks:
            # Fallback
            chunks = []
            max_len = max(len(en_sents), len(ko_sents))
            num_chunks = (max_len + 2) // 3
            for k in range(num_chunks):
                en_c = " ".join(en_sents[k*3:(k+1)*3])
                ko_c = " ".join(ko_sents[k*3:(k+1)*3])
                chunks.append((en_c, ko_c))

    obj_chunks = []
    for idx, (en_c, ko_c) in enumerate(chunks):
        obj_chunks.append({
            "tag": f"{item['tag']}-{idx+1}",
            "en": en_c,
            "ko": ko_c
        })
        
    out_data.append({
        "original_id": item['id'],
        "chunks": obj_chunks
    })

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_25.ch21_done.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

print("Done alignment!")

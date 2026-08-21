import json
import nltk

def split_ko(text):
    text = text.replace('\n', ' ')
    import re
    matches = re.finditer(r'([^.!?]+[.!?]+[\"\']?)(\s+|$)', text)
    sents = [m.group(1).strip() for m in matches]
    if not sents:
        return [text.strip()]
    return sents

mappings = {
    0: [(1, 1)],
    1: [(1, 1), (1, 1), (1, 1), (1, 2), (1, 1)],
    2: [(1, 1), (1, 1), (2, 2), (1, 2), (1, 2)],
    3: [(1, 2), (1, 2), (1, 2)],
    4: [(2, 2)],
    5: [(2, 2), (2, 2), (1, 1)],
    6: [(1, 2), (1, 2), (1, 1)],
    7: [(3, 3), (2, 2), (1, 2)],
    8: [(1, 2), (1, 2)],
    9: [(2, 3)],
    10: [(2, 3), (3, 3)],
    11: [(3, 3)],
    12: [(3, 3), (3, 3)],
    13: [(1, 2), (1, 1), (1, 2), (1, 1)],
    14: [(1, 1)],
    15: [(3, 3), (1, 2), (2, 3)],
    16: [(3, 3), (3, 3), (1, 1)],
    17: [(3, 3), (1, 3), (3, 3), (3, 3), (1, 3)],
    18: [(2, 3), (3, 3)],
    19: [(1, 1), (2, 2), (2, 2), (2, 2), (2, 3)],
    20: [(3, 3), (2, 2)],
    21: [(2, 3), (2, 3)],
    22: [(2, 3)],
    23: [(1, 1)],
    24: [(2, 2)],
    25: [(3, 3)],
    26: [(1, 1), (1, 3), (1, 2)],
    27: [(2, 3), (3, 3), (1, 1)],
    28: [(1, 2)],
    29: [(2, 2), (1, 3), (1, 1)],
    30: [(2, 3)],
    31: [(1, 2)],
    32: [(1, 3), (1, 2)], # Needs manual split of EN
    33: [(2, 3), (1, 1), (1, 3)],
    34: [(2, 2)],
    35: [(1, 1), (1, 2), (1, 1), (1, 3), (1, 2)], # Needs manual split of EN
    36: [(1, 2), (2, 2), (1, 3), (2, 2), (2, 2)],
    37: [(1, 2), (1, 1), (1, 1), (1, 3), (2, 2)],
}

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_20.ch16.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

out_data = []

for item in data:
    en_text = item['en'].replace('\n', ' ')
    
    if item['id'] == 32:
        en_sents = [
            "“I gazed on my victim, and my heart swelled with exultation and hellish triumph; clapping my hands, I exclaimed, ‘I too can create desolation;",
            "my enemy is not invulnerable; this death will carry despair to him, and a thousand other miseries shall torment and destroy him.’"
        ]
    elif item['id'] == 35:
        en_sents = nltk.sent_tokenize(en_text)
        # Split the last sentence into 2
        last_sent = en_sents[-1]
        s1 = "And then I bent over her and whispered, ‘Awake, fairest, thy lover is near—"
        s2 = "he who would give his life but to obtain one look of affection from thine eyes; my beloved, awake!’"
        en_sents[-1] = s1
        en_sents.append(s2)
    else:
        en_sents = nltk.sent_tokenize(en_text)
        
    ko_sents = split_ko(item['ko'])
    
    mapping = mappings[item['id']]
    
    chunks = []
    en_idx = 0
    ko_idx = 0
    
    for i, (e_count, k_count) in enumerate(mapping):
        en_chunk_sents = en_sents[en_idx:en_idx+e_count]
        ko_chunk_sents = ko_sents[ko_idx:ko_idx+k_count]
        
        chunk = {
            "tag": f"{item['tag']}-{i+1}",
            "en": " ".join(en_chunk_sents),
            "ko": " ".join(ko_chunk_sents)
        }
        chunks.append(chunk)
        
        en_idx += e_count
        ko_idx += k_count
        
    out_data.append({
        "original_id": item['id'],
        "chunks": chunks
    })

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_20.ch16_done.json', 'w', encoding='utf-8') as f:
    json.dump(out_data, f, ensure_ascii=False, indent=2)

import json
import re

def split_sentences(text):
    parts = re.split(r'([.?!]+[\"”\']?)(?:\s+|$)', text)
    sentences = []
    current_sent = ""
    for i in range(0, len(parts)-1, 2):
        if parts[i]:
            current_sent += parts[i]
        if i+1 < len(parts) and parts[i+1]:
            current_sent += parts[i+1]
            sentences.append(current_sent.strip())
            current_sent = ""
    if parts[-1].strip():
        current_sent += parts[-1]
    if current_sent.strip():
        sentences.append(current_sent.strip())
    return sentences

with open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_4.Lt4.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Hardcoded alignments for mismatched IDs (list of EN sentence count per chunk, KO sentence count per chunk)
# Format: ID: [(en_count, ko_count), ...]
alignments = {
    1: [(1, 1)],  # Just combine everything
    3: [(1, 2)],
    5: [(2, 2), (2, 3)],
    8: [(3, 3), (2, 4)],
    12: [(2, 2), (2, 3)],
    13: [(2, 3)],
    14: [(1, 2)],
    17: [(1, 2)],
    18: [(2, 4)],
    19: [(1, 2)],
    24: [(1, 2)],
    28: [(3, 3), (3, 3), (2, 3), (3, 4), (1, 2)],
    29: [(1, 2)],
    31: [(1, 4), (3, 4)],
    33: [(3, 4)],
    34: [(3, 3), (2, 3)],
    36: [(2, 3), (2, 5), (2, 4)],
    38: [(3, 10)],
    39: [(3, 3), (2, 3), (2, 3)]
}

output_data = []

for item in data:
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    
    chunks = []
    if item['id'] in alignments:
        align = alignments[item['id']]
        en_idx = 0
        ko_idx = 0
        for i, (ec, kc) in enumerate(align):
            en_chunk = " ".join(en_sents[en_idx:en_idx+ec])
            ko_chunk = " ".join(ko_sents[ko_idx:ko_idx+kc])
            chunks.append({
                "tag": f"{item['tag']}-{i+1}",
                "en": en_chunk,
                "ko": ko_chunk
            })
            en_idx += ec
            ko_idx += kc
    else:
        # Match lengths exactly
        # We group by 2 or 3 sentences. Let's do 3.
        # If lengths match exactly, just take 3 at a time.
        for i in range(0, len(en_sents), 3):
            ec = min(3, len(en_sents) - i)
            kc = ec
            en_chunk = " ".join(en_sents[i:i+ec])
            ko_chunk = " ".join(ko_sents[i:i+kc])
            chunks.append({
                "tag": f"{item['tag']}-{i//3+1}",
                "en": en_chunk,
                "ko": ko_chunk
            })
            
    output_data.append({
        "original_id": item['id'],
        "chunks": chunks
    })

with open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_4.Lt4_done.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("Done processing")

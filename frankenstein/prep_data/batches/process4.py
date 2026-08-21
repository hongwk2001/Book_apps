import json
import re

def split_sentences(text):
    parts = re.split(r'([.?!;]+[\"”\']?)(?:\s+|$)', text)
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

alignments = {
    1: [(2, 1)],
    3: [(1, 2)],
    6: [(2, 1), (1, 1), (1, 1)],
    8: [(2, 2), (2, 1), (1, 1), (1, 3)],
    12: [(2, 2), (2, 3)],
    14: [(1, 2)],
    17: [(1, 2)],
    18: [(1, 1), (2, 3)],
    20: [(2, 1)],
    21: [(1, 1), (2, 1)],
    22: [(1, 1), (2, 1), (1, 1)],
    27: [(1, 1), (1, 1), (1, 1), (2, 1)],
    28: [(2, 2), (2, 2), (2, 2), (1, 1), (1, 1), (2, 1), (2, 2), (2, 2), (2, 2)],
    30: [(2, 1), (1, 1), (1, 1), (1, 1)],
    31: [(1, 2), (1, 2), (1, 2), (1, 1), (1, 1)],
    33: [(1, 1), (1, 1), (1, 2)],
    34: [(2, 2), (2, 1), (1, 1), (2, 2)],
    36: [(1, 2), (1, 1), (2, 2), (1, 1), (1, 2), (1, 1), (3, 3)],
    38: [(2, 3), (1, 1), (2, 3), (1, 1), (1, 2)],
    39: [(2, 2), (2, 2), (2, 2), (2, 1), (1, 1), (1, 1)]
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
            # If the original text didn't have a space after semicolon, it might look slightly different,
            # but joining with space is fine for plain text paragraphs. 
            # To be strictly perfectly re-assembling, we should just use them.
            chunks.append({
                "tag": f"{item['tag']}-{i+1}",
                "en": en_chunk,
                "ko": ko_chunk
            })
            en_idx += ec
            ko_idx += kc
    else:
        # Match lengths exactly
        # If lengths match exactly, group by up to 3
        # First ensure length match
        if len(en_sents) != len(ko_sents):
            print(f"ERROR: length mismatch not in alignments for ID {item['id']}")
            break
        for i in range(0, len(en_sents), 3):
            ec = min(3, len(en_sents) - i)
            en_chunk = " ".join(en_sents[i:i+ec])
            ko_chunk = " ".join(ko_sents[i:i+ec])
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

print("Finished process4")

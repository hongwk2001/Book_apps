import json

mappings = {
    'P006': [
        ([0, 1], [0, 1]),
        ([2, 3], [2, 3]),
        ([4], [4, 5])
    ],
    'P024': [
        ([0, 1, 2], [0, 1, 2]),
        ([3, 4, 5], [3, 4, 5, 6, 7])
    ],
    'P027': [
        ([0, 1], [0, 1, 2]),
        ([2, 3, 4], [3, 4, 5]),
        ([5], [6])
    ],
    'P028': [
        ([0, 1], [0, 1, 2, 3, 4]),
        ([2, 3, 4], [5, 6, 7])
    ],
    'P029': [
        ([0, 1], [0, 1, 2, 3, 4, 5, 6]),
        ([2, 3, 4], [7, 8, 9, 10, 11]),
        ([5, 6, 7], [12, 13, 14, 15, 16]),
        ([8, 9, 10], [17, 18, 19, 20]),
        ([11], [21])
    ],
    'P034': [
        ([0, 1, 2], [0, 1, 2, 3]),
        ([3, 4, 5], [4, 5, 6]),
        ([6, 7, 8], [7, 8, 9, 10, 11]),
        ([9, 10], [12, 13, 14, 15, 16, 17])
    ],
    'P036': [
        ([0, 1], [0, 1, 2, 3])
    ],
    'P040': [
        ([0, 1], [0, 1, 2, 3, 4])
    ],
    'P049': [
        ([0], [0, 1, 2, 3])
    ],
    'P050': [
        ([0], [0, 1, 2, 3])
    ]
}

with open('debug.json', encoding='utf-8') as f:
    debug_data = json.load(f)

new_chunks = {}
for p, mapping in mappings.items():
    p_chunks = []
    en_sentences = debug_data[p]['en']
    ko_sentences = debug_data[p]['ko']
    for idx, (e_idx, k_idx) in enumerate(mapping):
        en_text = " ".join([en_sentences[i] for i in e_idx])
        ko_text = " ".join([ko_sentences[i] for i in k_idx])
        tag = f"{p}-{idx+1}"
        p_chunks.append({
            "id": None, # will fix later
            "tag": tag,
            "en": en_text,
            "ko": ko_text,
            "is_header": False
        })
    new_chunks[p] = p_chunks

with open('src/main/assets/books/ch_11.json', encoding='utf-8') as f:
    orig_data = json.load(f)

final_data = []
skip_prefix = None

for item in orig_data:
    tag = item['tag']
    base_tag = tag.split('-')[0]
    
    if base_tag in new_chunks:
        if skip_prefix != base_tag:
            # First time seeing this base_tag
            final_data.extend(new_chunks[base_tag])
            skip_prefix = base_tag
        # skip this item as it's being replaced
    else:
        final_data.append(item)
        skip_prefix = None

# fix IDs
for i, item in enumerate(final_data):
    item['id'] = i + 1

with open('src/main/assets/books/ch_11.json', 'w', encoding='utf-8') as f:
    json.dump(final_data, f, ensure_ascii=False, indent=2)

print("Done applying fixes")

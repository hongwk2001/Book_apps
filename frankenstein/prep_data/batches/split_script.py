import json
import re

def split_sentences_en(text):
    # Match sentence endings followed by space and a capital letter or quote
    # For simplicity, we just use a basic sentence splitter or regex
    # But since quotes can be tricky, a simple regex:
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z“"”])', text)
    return sents

def split_sentences_ko(text):
    # Match Korean sentence endings
    sents = re.split(r'(?<=[.!?])\s+(?=[가-힣"“”])', text)
    return sents

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_18.ch14.json', encoding='utf-8') as f:
    data = json.load(f)

result = []
for item in data:
    en_text = item['en'].replace('\n', ' ')
    ko_text = item['ko'].replace('\n', ' ')
    
    en_sents = split_sentences_en(en_text)
    ko_sents = split_sentences_ko(ko_text)
    
    # Custom alignment fixes based on our analysis
    if item['id'] == 3:
        # ko has 6 sentences due to semicolon split. Join the last two.
        if len(ko_sents) == 6:
            ko_sents[4] = ko_sents[4] + ' ' + ko_sents[5]
            ko_sents = ko_sents[:5]
    if item['id'] == 4:
        # en has 3 sentences, ko has 3 sentences
        pass
    if item['id'] == 13:
        # en has 4 sentences.
        # ko has 4 sentences, but sent 3 doesn't end in .!? - wait, let's just make sure lengths match.
        pass
    
    # Ensure lengths match or group them all together if they don't match
    chunks = []
    
    if len(en_sents) != len(ko_sents):
        # Fallback to single chunk if counts don't match
        chunks.append((en_sents, ko_sents))
    else:
        # General grouping logic: 1-3 sentences per chunk
        if item['id'] == 2:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:], ko_sents[2:]))
        elif item['id'] == 3:
            chunks.append((en_sents[:3], ko_sents[:3]))
            chunks.append((en_sents[3:], ko_sents[3:]))
        elif item['id'] == 4:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:4], ko_sents[2:4]))
            if len(en_sents) > 4:
                chunks[-1] = (en_sents[2:], ko_sents[2:])
        elif item['id'] == 8:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:4], ko_sents[2:4]))
            if len(en_sents) > 4:
                chunks[-1] = (en_sents[2:], ko_sents[2:])
        elif item['id'] == 12:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:], ko_sents[2:]))
        elif item['id'] == 13:
            chunks.append((en_sents[:3], ko_sents[:3]))
            chunks.append((en_sents[3:], ko_sents[3:]))
        elif item['id'] == 16:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:], ko_sents[2:]))
        elif item['id'] == 19:
            chunks.append((en_sents[:3], ko_sents[:3]))
            chunks.append((en_sents[3:], ko_sents[3:]))
        elif item['id'] == 20:
            chunks.append((en_sents[:2], ko_sents[:2]))
            chunks.append((en_sents[2:], ko_sents[2:]))
        else:
            if len(en_sents) <= 3:
                chunks.append((en_sents, ko_sents))
            else:
                chunks.append((en_sents[:3], ko_sents[:3]))
                chunks.append((en_sents[3:], ko_sents[3:]))
        
    out_chunks = []
    for i, (e_c, k_c) in enumerate(chunks):
        out_chunks.append({
            "tag": f"{item['tag']}-{i+1}",
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

import json
import re

input_path = 'C:\\git_repo\\Book_apps\\dracula\\src\\main\\assets\\books\\ch_13.json'

with open(input_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix ID 125 and 126 in the data
for d in data:
    if d['id'] == 125:
        # Split out the 5th sentence
        sents = re.split(r'([.!?]+[\"”]*(?:\s+|$))', d['ko'])
        res = []
        cur = ""
        for p in sents:
            cur += p
            if re.search(r'[.!?]', p):
                res.append(cur.strip())
                cur = ""
        if cur.strip(): res.append(cur.strip())
        
        d['ko'] = " ".join(res[:4])
        extra_125 = res[4]
        
for d in data:
    if d['id'] == 126:
        d['ko'] = extra_125 + " " + d['ko']

def split_sentences_custom(text, item_id, lang):
    text = text.replace('Mr.', 'Mr<DOT>').replace('Mrs.', 'Mrs<DOT>').replace('Dr.', 'Dr<DOT>')
    
    if item_id == 18 and lang == 'ko':
        text = text.replace('기다리시오." 하고', '기다리시오<QUOTE> 하고')
        
    if item_id == 126 and lang == 'en':
        text = text.replace('come!', 'come<EXCL>')
        text = text.replace('arrived!\'.', 'arrived<EXCL>\'.')
        
    if item_id == 126 and lang == 'ko':
        text = text.replace('왔도다!', '왔도다<EXCL>')
        text = text.replace('왔노라!\'', '왔노라<EXCL>\'')
        text = text.replace('아닙니다, 존.', '아닙니다, 존<DOT>')

    sentences = re.split(r'([.!?]+[\"”]*(?:\s+|$))', text)
    result = []
    current = ""
    for piece in sentences:
        current += piece
        if re.search(r'[.!?]', piece):
            result.append(current.strip().replace('<DOT>', '.').replace('<QUOTE>', '."').replace('<EXCL>', '!'))
            current = ""
    if current.strip():
        result.append(current.strip().replace('<DOT>', '.').replace('<QUOTE>', '."').replace('<EXCL>', '!'))
    return result

output = []

for item in data:
    en_sents = split_sentences_custom(item.get('en', ''), item['id'], 'en')
    ko_sents = split_sentences_custom(item.get('ko', ''), item['id'], 'ko')
    
    if len(en_sents) > 3:
        if len(en_sents) != len(ko_sents):
            raise Exception(f"Mismatch at ID {item['id']}: EN {len(en_sents)}, KO {len(ko_sents)}\nEN: {en_sents}\nKO: {ko_sents}")
        
        chunks_en = []
        chunks_ko = []
        
        n = len(en_sents)
        i = 0
        while n > 0:
            if n % 3 == 0 or (n >= 3 and (n - 3) != 1):
                take = 3
            elif n % 2 == 0 or n >= 2:
                take = 2
            else:
                take = 1
                
            chunks_en.append(" ".join(en_sents[i:i+take]))
            chunks_ko.append(" ".join(ko_sents[i:i+take]))
            i += take
            n -= take
            
        new_chunks = []
        base_tag = item.get('tag', f"P{item['id']:03d}")
        import string
        if base_tag[-1] in string.ascii_lowercase:
            base_tag = base_tag[:-1]
            
        for idx, (ce, ck) in enumerate(zip(chunks_en, chunks_ko)):
            new_chunks.append({
                "tag": f"{base_tag}-{idx+1}",
                "en": ce,
                "ko": ck
            })
            
        output.append({
            "original_id": item['id'],
            "chunks": new_chunks
        })

for idx, obj in enumerate(output):
    obj['id'] = idx + 1
    
with open(input_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("Done. Wrote", len(output), "items.")

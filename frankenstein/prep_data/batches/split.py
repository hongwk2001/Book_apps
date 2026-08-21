import json
import re

def split_sentences(text, lang='en'):
    if lang == 'en':
        text = text.replace("M. Krempe", "M_Krempe_DOT")
        text = text.replace("M. Waldman", "M_Waldman_DOT")
        text = text.replace("St. ", "St_DOT_ ")
        text = text.replace("Mr. ", "Mr_DOT_ ")
        text = text.replace("Mrs. ", "Mrs_DOT_ ")
        text = text.replace("Dr. ", "Dr_DOT_ ")

    if lang == 'en':
        sents = []
        raw_sents = re.split(r'(?<=[.?!])\s+(?=["“\'A-Z])', text)
        for s in raw_sents:
            s = s.strip()
            if s:
                s = s.replace("M_Krempe_DOT", "M. Krempe")
                s = s.replace("M_Waldman_DOT", "M. Waldman")
                s = s.replace("St_DOT_", "St.")
                s = s.replace("Mr_DOT_", "Mr.")
                s = s.replace("Mrs_DOT_", "Mrs.")
                s = s.replace("Dr_DOT_", "Dr.")
                s = s.replace("\n", " ")
                sents.append(s)
        return sents
    else:
        sents = []
        raw_sents = re.split(r'(?<=[.?!])\s+(?=["“\'가-힣])', text)
        for s in raw_sents:
            s = s.strip()
            if s:
                s = s.replace("\n", " ")
                sents.append(s)
        return sents

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    out_data = []
    for item in data:
        en_text = item['en']
        ko_text = item['ko']
        
        if not re.search(r'[.?!]', en_text):
            en_sents = [en_text]
        else:
            en_sents = split_sentences(en_text, 'en')
            
        if not re.search(r'[.?!]', ko_text):
            ko_sents = [ko_text]
        else:
            ko_sents = split_sentences(ko_text, 'ko')
            
        en_sents = [re.sub(r'\s+', ' ', s).strip() for s in en_sents if s.strip()]
        ko_sents = [re.sub(r'\s+', ' ', s).strip() for s in ko_sents if s.strip()]
        
        chunks = []
        if len(en_sents) != len(ko_sents):
            print(f"Warning: ID {item['id']} mismatch! en:{len(en_sents)} ko:{len(ko_sents)}")
            with open('mismatch.txt', 'a', encoding='utf-8') as mf:
                mf.write(f"ID {item['id']} mismatch! en:{len(en_sents)} ko:{len(ko_sents)}\n")
                mf.write("EN:\n" + "\n".join(en_sents) + "\n")
                mf.write("KO:\n" + "\n".join(ko_sents) + "\n\n")
            # Default chunking to 3 for EN, just shove KO into them to be fixed later
            chunk_idx = 1
            for i in range(0, max(len(en_sents), len(ko_sents)), 3):
                en_chunk = " ".join(en_sents[i:i+3])
                ko_chunk = " ".join(ko_sents[i:i+3])
                chunks.append({
                    "tag": f"{item['tag']}-{chunk_idx}",
                    "en": en_chunk,
                    "ko": ko_chunk
                })
                chunk_idx += 1
        else:
            chunk_idx = 1
            for i in range(0, len(en_sents), 3):
                en_chunk = " ".join(en_sents[i:i+3])
                ko_chunk = " ".join(ko_sents[i:i+3])
                chunks.append({
                    "tag": f"{item['tag']}-{chunk_idx}",
                    "en": en_chunk,
                    "ko": ko_chunk
                })
                chunk_idx += 1
            
        out_data.append({
            "original_id": item['id'],
            "chunks": chunks
        })
        
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print("Done")

process_file('batch_8.ch4.json', 'test.json')

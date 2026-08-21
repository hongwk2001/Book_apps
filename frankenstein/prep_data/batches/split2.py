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
    
    mappings = {
        2: [ (0,2, 0,2), (2,4, 2,4), (4,6, 4,6), (6,7, 6,8), (7,8, 8,9) ],
        3: [ (0,1, 0,1), (1,2, 1,3), (2,3, 3,5), (3,5, 5,7), (5,6, 7,8), (6,7, 8,10), (7,9, 10,12), (9,10, 12,13), (10,12, 13,15), (12,13, 15,17), (13,14, 17,20) ],
        4: [ (0,2, 0,2), (2,3, 2,3), (3,4, 3,5) ],
        5: [ (0,2, 0,2), (2,4, 2,4), (4,5, 4,6), (5,6, 6,7) ],
        6: [ (0,1, 0,2), (1,2, 2,4), (2,3, 4,5), (3,4, 5,6) ], # With manual fix for en_sents
        7: [ (0,2, 0,2), (2,3, 2,4), (3,4, 4,5), (4,5, 5,8), (5,7, 8,10), (7,9, 10,12) ],
        9: [ (0,2, 0,2), (2,4, 2,4), (4,5, 4,5), (5,6, 5,8), (6,7, 8,9), (7,8, 9,10), (8,9, 10,12), (9,10, 12,14) ],
        10: [ (0,2, 0,3), (2,3, 3,4), (3,4, 4,6), (4,5, 6,7) ],
        14: [ (0,1, 0,1), (1,2, 1,3), (2,4, 3,5), (4,5, 5,7), (5,6, 7,10) ]
    }
    
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
        
        if item['id'] == 6:
            part1 = "I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect to be informed of the secret with which I am acquainted; that cannot be;"
            part2 = "listen patiently until the end of my story, and you will easily perceive why I am reserved upon that subject."
            en_sents = [part1, part2, en_sents[1], en_sents[2]]
            
        chunks = []
        if item['id'] in mappings:
            chunk_idx = 1
            for e_s, e_e, k_s, k_e in mappings[item['id']]:
                en_chunk = " ".join(en_sents[e_s:e_e])
                ko_chunk = " ".join(ko_sents[k_s:k_e])
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
    print("Done writing to", out_path)

process_file('batch_8.ch4.json', 'batch_8.ch4_done.json')

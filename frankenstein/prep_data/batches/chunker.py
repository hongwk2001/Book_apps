import json
import re

def split_en(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?])\s+(?=[A-Z\u201c\u201d\"\[])', text)
    return [s.strip() for s in sents if s.strip()]

def split_ko(text):
    text = text.replace('\n', ' ')
    sents = re.split(r'(?<=[.!?])\s+(?=[가-힣\u201c\u201d\"\[a-zA-Z])', text)
    return [s.strip() for s in sents if s.strip()]

def align_sentences(en_sents, ko_sents):
    # dynamic programming based on length
    # Cost function: we want to minimize the variance of length ratios
    # Allowed merges: 1-1, 1-2, 2-1, 2-2, 3-1, 1-3
    
    mean_ratio = sum(len(k) for k in ko_sents) / max(1, sum(len(e) for e in en_sents))
    
    dp = {}
    
    def get_cost(en_len, ko_len):
        if en_len == 0 and ko_len == 0: return 0
        if en_len == 0 or ko_len == 0: return 999999
        expected_ko = en_len * mean_ratio
        return abs(ko_len - expected_ko)
        
    def solve(i, j):
        if i == len(en_sents) and j == len(ko_sents):
            return 0, []
        if i == len(en_sents) or j == len(ko_sents):
            return 999999, []
        
        if (i, j) in dp:
            return dp[(i, j)]
            
        best_cost = 99999999
        best_path = None
        
        # Try different matches
        for di in range(1, 4):
            for dj in range(1, 4):
                if i + di <= len(en_sents) and j + dj <= len(ko_sents):
                    en_len = sum(len(x) for x in en_sents[i:i+di])
                    ko_len = sum(len(x) for x in ko_sents[j:j+dj])
                    
                    cost = get_cost(en_len, ko_len)
                    
                    # penalty for 2-2, 3-1, 1-3 etc to prefer 1-1
                    if di == 1 and dj == 1: cost *= 1.0
                    else: cost += 20.0 * (di + dj - 2)
                    
                    next_cost, next_path = solve(i + di, j + dj)
                    total_cost = cost + next_cost
                    
                    if total_cost < best_cost:
                        best_cost = total_cost
                        best_path = [(di, dj)] + next_path
                        
        dp[(i, j)] = (best_cost, best_path)
        return best_cost, best_path

    _, path = solve(0, 0)
    
    if not path:
        # Fallback if impossible, just chunk them by 1 as much as possible
        return [(en_sents, ko_sents)]
        
    aligned = []
    i, j = 0, 0
    for di, dj in path:
        en_chunk = " ".join(en_sents[i:i+di])
        ko_chunk = " ".join(ko_sents[j:j+dj])
        aligned.append((en_chunk, ko_chunk))
        i += di
        j += dj
        
    return aligned

data = json.load(open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_15.ch11.json', encoding='utf-8'))
final_out = []

for item in data:
    en_sents = split_en(item['en'])
    ko_sents = split_ko(item['ko'])
    
    aligned = align_sentences(en_sents, ko_sents)
    
    # Now group aligned into chunks of max 3 sentences
    # An aligned block might already have >3 sentences if di or dj is 3, but that's rare and counts as 1 logical sentence chunk.
    # Wait, the instruction says "no chunk has more than 3 sentences".
    # So we group 1-3 aligned items per chunk.
    chunks = []
    current_en = []
    current_ko = []
    current_en_sents = 0
    current_ko_sents = 0
    
    chunk_idx = 1
    
    for en_c, ko_c in aligned:
        # how many sentences in this aligned pair? (approx based on .!?)
        e_s = len(split_en(en_c))
        k_s = len(split_ko(ko_c))
        
        if current_en_sents + e_s > 3 or current_ko_sents + k_s > 3:
            if current_en:
                chunks.append({
                    "tag": f"{item['tag']}-{chunk_idx}",
                    "en": " ".join(current_en),
                    "ko": " ".join(current_ko)
                })
                chunk_idx += 1
                current_en = []
                current_ko = []
                current_en_sents = 0
                current_ko_sents = 0
                
        current_en.append(en_c)
        current_ko.append(ko_c)
        current_en_sents += e_s
        current_ko_sents += k_s
        
    if current_en:
        chunks.append({
            "tag": f"{item['tag']}-{chunk_idx}",
            "en": " ".join(current_en),
            "ko": " ".join(current_ko)
        })
        
    final_out.append({
        "original_id": item["id"],
        "chunks": chunks
    })

json.dump(final_out, open('c:/git_repo/Book_apps/frankenstein/prep_data/batches/batch_15.ch11_done.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("Done!")

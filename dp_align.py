import json
import re

def split_en(text):
    sentences = re.split(r'(?<=[.!?\"])\s+(?=[A-Z\"\'I])', text)
    return [s.strip() for s in sentences if s.strip()]

def split_ko(text):
    sentences = re.split(r'(?<=[.!?\"])\s+(?=[가-힣\"\'(])', text)
    return [s.strip() for s in sentences if s.strip()]

def align(en_s, ko_s):
    n, m = len(en_s), len(ko_s)
    dp = {}
    
    def solve(i, j):
        if i == n and j == m:
            return 0, []
        if i == n or j == m:
            return float('inf'), []
        if (i, j) in dp:
            return dp[(i, j)]
        
        best_cost = float('inf')
        best_path = []
        
        for di in range(1, 4):
            for dj in range(1, 4):
                if i + di <= n and j + dj <= m:
                    en_len = sum(len(en_s[k]) for k in range(i, i + di))
                    ko_len = sum(len(ko_s[k]) for k in range(j, j + dj))
                    
                    ratio = en_len / max(1, ko_len)
                    cost = abs(ratio - 2.2) + 0.1 * (di + dj)
                    
                    sub_cost, sub_path = solve(i + di, j + dj)
                    
                    if cost + sub_cost < best_cost:
                        best_cost = cost + sub_cost
                        best_path = [(di, dj)] + sub_path
                        
        dp[(i, j)] = (best_cost, best_path)
        return dp[(i, j)]
        
    cost, path = solve(0, 0)
    
    if cost == float('inf'):
        # Fallback if DP fails (e.g., >3 sentences left but can't match)
        return [(" ".join(en_s), " ".join(ko_s))]
        
    res = []
    i, j = 0, 0
    for di, dj in path:
        res.append((
            " ".join(en_s[i:i+di]),
            " ".join(ko_s[j:j+dj])
        ))
        i += di
        j += dj
    return res

def process():
    file_path = 'C:/git_repo/Book_apps/dracula/src/main/assets/books/ch_21.json'
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        
    out_data = []
    current_id = 1
    
    for item in data:
        en = item['en']
        en_s = split_en(en)
        
        if len(en_s) > 3:
            ko_s = split_ko(item['ko'])
            chunks = align(en_s, ko_s)
        else:
            chunks = [(en, item['ko'])]
            
        chunk_list = []
        for idx, (chunk_en, chunk_ko) in enumerate(chunks):
            tag = item['tag']
            if len(chunks) > 1:
                tag = f"{item['tag']}-{idx+1}"
                
            chunk_obj = {
                "id": current_id,
                "tag": tag,
                "en": chunk_en,
                "ko": chunk_ko
            }
            if "is_header" in item:
                chunk_obj["is_header"] = item["is_header"]
                
            chunk_list.append(chunk_obj)
            current_id += 1
            
        out_data.append({
            "original_id": item['id'],
            "chunks": chunk_list
        })
        
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

process()

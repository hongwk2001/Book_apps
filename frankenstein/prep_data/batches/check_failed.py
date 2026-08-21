import json
import re

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_25.ch21.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_sentences(text):
    text = text.replace('\n', ' ')
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z가-힣\"“\'])', text.strip())
    return [s for s in sentences if s]

for item in data:
    en_sents = split_sentences(item['en'])
    ko_sents = split_sentences(item['ko'])
    
    if len(en_sents) <= 3 and len(ko_sents) <= 3:
        continue
    
    target_ratio = sum(len(s) for s in ko_sents) / max(1, sum(len(s) for s in en_sents))
    n = len(en_sents)
    m = len(ko_sents)
    dp = {}
    dp[(0, 0)] = (0, [])
    for i in range(n + 1):
        for j in range(m + 1):
            if (i, j) not in dp: continue
            for di in range(1, 4):
                if i + di > n: break
                for dj in range(1, 4):
                    if j + dj > m: break
                    en_group = ' '.join(en_sents[i:i+di])
                    ko_group = ' '.join(ko_sents[j:j+dj])
                    ratio = len(ko_group) / max(1, len(en_group))
                    cost = dp[(i, j)][0] + (ratio - target_ratio)**2
                    if (i+di, j+dj) not in dp or cost < dp[(i+di, j+dj)][0]:
                        dp[(i+di, j+dj)] = (cost, dp[(i, j)][1] + [(di, dj)])
    if (n, m) not in dp:
        print(f"Failed ID: {item['id']} ({n} EN, {m} KO)")

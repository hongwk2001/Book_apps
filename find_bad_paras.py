import os
import json

assets = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"
suspicious_paragraphs = set()
count = 0

for i in range(1, 29):
    path = os.path.join(assets, f"ch_{i:02d}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for item in data:
        en = item.get("en", "").strip()
        ko = item.get("ko", "").strip()
        
        if len(en) < 3 or len(ko) < 3:
            if en == "." or ko == "." or not en or not ko:
                if item["tag"] == "P004-3": # fixed already manually by user
                    continue
                tag_base = item["tag"].split("-")[0]
                suspicious_paragraphs.add((i, tag_base))
                count += 1
            continue
            
        en_len = len(en)
        ko_len = len(ko)
        ratio = ko_len / en_len
        
        if ratio > 3.0 or ratio < 0.3:
            if en_len > 20 and ko_len > 20:
                tag_base = item["tag"].split("-")[0]
                suspicious_paragraphs.add((i, tag_base))
                count += 1

print(f"Total skewed chunks: {count}")
print("Paragraphs to fix:")
for i, tag in sorted(suspicious_paragraphs):
    print(f"Chapter {i}: {tag}")

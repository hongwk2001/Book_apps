import os
import json

assets = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"

for i in range(1, 29):
    path = os.path.join(assets, f"ch_{i:02d}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for item in data:
        en = item.get("en", "")
        ko = item.get("ko", "")
        
        # Replace newlines and collapse multiple spaces
        if en:
            en = " ".join(en.replace('\n', ' ').split())
            item["en"] = en
            
        if ko:
            ko = " ".join(ko.replace('\n', ' ').split())
            item["ko"] = ko
            
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Successfully removed all hard-wrapped newlines and collapsed extra spaces across all 28 chapters!")

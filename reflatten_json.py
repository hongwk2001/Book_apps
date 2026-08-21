import os
import json
import glob

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data\batches"
assets_dir = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"

for i in range(1, 29):
    pattern = os.path.join(base_dir, f"batch_{i}.*_done.json")
    matches = glob.glob(pattern)
    if not matches:
        continue
        
    with open(matches[0], "r", encoding="utf-8") as f:
        data = json.load(f)
        
    flattened = []
    counter = 1
    for item in data:
        chunks = item.get("chunks", [])
        for chunk in chunks:
            tag = chunk.get("tag", "")
            if not tag:
                tag = chunk.get("id", "")
                
            is_header = False
            # Check if it's the title paragraph (usually the first one, or starts with Chapter/Letter)
            if counter == 1 or tag.endswith("P000-1") or chunk.get("en", "").startswith("Chapter") or chunk.get("en", "").startswith("Letter"):
                is_header = True
                
            flattened.append({
                "id": counter,
                "tag": tag,
                "en": chunk.get("en", ""),
                "ko": chunk.get("ko", ""),
                "is_header": is_header
            })
            counter += 1
            
    out_filename = f"ch_{i:02d}.json"
    out_path = os.path.join(assets_dir, out_filename)
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(flattened, f, ensure_ascii=False, indent=2)

print("Re-flattened 28 JSON files with correct format!")

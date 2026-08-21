import os
import json
import glob

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data\batches"
assets_dir = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\frankenstein"
os.makedirs(assets_dir, exist_ok=True)

# Files are named batch_1.Lt1_done.json, batch_2.Lt2_done.json, etc.
# We want to extract the leading number.
for i in range(1, 29):
    # Find the matching file
    pattern = os.path.join(base_dir, f"batch_{i}.*_done.json")
    matches = glob.glob(pattern)
    if not matches:
        print(f"ERROR: Missing batch {i}")
        continue
        
    filepath = matches[0]
    
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    flattened = []
    for item in data:
        # Some chunks might not have "tag", or maybe named differently
        # Let's ensure standard format
        for chunk in item.get("chunks", []):
            tag = chunk.get("tag", "")
            if not tag:
                tag = chunk.get("id", "")
            
            flattened.append({
                "id": tag,
                "en": chunk.get("en", ""),
                "ko": chunk.get("ko", "")
            })
            
    out_filename = f"ch_{i:02d}.json"
    out_path = os.path.join(assets_dir, out_filename)
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(flattened, f, ensure_ascii=False, indent=2)
        
print("All 28 JSON files have been compiled and flattened into assets!")

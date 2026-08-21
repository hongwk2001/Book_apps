import os
import json
import random

assets_dir = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"
audit_dir = r"c:\git_repo\Book_apps\frankenstein\audit_batches"
os.makedirs(audit_dir, exist_ok=True)

all_samples = []

# Loop through ch_01.json to ch_28.json
for i in range(1, 29):
    filepath = os.path.join(assets_dir, f"ch_{i:02d}.json")
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    # Sample 3 chunks randomly
    if len(data) >= 3:
        samples = random.sample(data, 3)
    else:
        samples = data
        
    for s in samples:
        s["chapter"] = f"{i:02d}"
        all_samples.append(s)

# Shuffle and split into 4 batches (21 items each)
random.shuffle(all_samples)
batches = [all_samples[i::4] for i in range(4)]

for idx, batch in enumerate(batches):
    batch_file = os.path.join(audit_dir, f"audit_batch_{idx+1}.json")
    with open(batch_file, "w", encoding="utf-8") as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Generated 4 audit batches with a total of {len(all_samples)} samples.")

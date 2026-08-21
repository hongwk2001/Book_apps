import os
import json

base_dir = r'c:\git_repo\Book_apps\secret_garden\json_output'
audit_dir = r'c:\git_repo\Book_apps\secret_garden\audit_batches'
os.makedirs(audit_dir, exist_ok=True)

samples = []

for ch_num in [f"{i:02d}" for i in range(1, 28)]:
    file_path = os.path.join(base_dir, f'ch_{ch_num}.json')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Get every 7th item (e.g. index 6, 13, 20...)
        # or we can literally do every 7th item starting from index 0
        for i, item in enumerate(data):
            if (i + 1) % 7 == 0:
                samples.append({
                    "chapter": ch_num,
                    "id": item['id'],
                    "tag": item['tag'],
                    "en": item['en'],
                    "ko": item['ko']
                })

print(f"Total samples collected: {len(samples)}")

# Batch them into groups of 25
batch_size = 25
batches = [samples[i:i + batch_size] for i in range(0, len(samples), batch_size)]

for i, batch in enumerate(batches, 1):
    batch_file = os.path.join(audit_dir, f'audit_batch_{i}.json')
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(batch, f, ensure_ascii=False, indent=2)

print(f"Created {len(batches)} batches.")

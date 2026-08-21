import os
import json
import time

def merge():
    base_dir = r'c:\git_repo\Book_apps\secret_garden\json_output'
    batch_dir = r'c:\git_repo\Book_apps\secret_garden\batches'
    
    # Wait until all 56 batch_done files exist
    for i in range(1, 57):
        done_file = os.path.join(batch_dir, f'batch_{i}_done.json')
        while not os.path.exists(done_file):
            print(f"Waiting for {done_file}...")
            time.sleep(2)
            
    # Load all completed batches
    chunk_map = {} # (ch_num, original_id) -> list of chunks
    for i in range(1, 57):
        batch_file = os.path.join(batch_dir, f'batch_{i}.json')
        done_file = os.path.join(batch_dir, f'batch_{i}_done.json')
        
        # We need the original ch_num. Let's read the batch input to map id -> ch_num
        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_data = json.load(f)
            id_to_file = {item['id']: item['file'] for item in batch_data}
            
        with open(done_file, 'r', encoding='utf-8') as f:
            done_data = json.load(f)
            
        for item in done_data:
            orig_id = item['original_id']
            ch_file = id_to_file[orig_id]
            ch_num = ch_file.replace('ch_', '').replace('.json', '')
            
            key = (ch_num, orig_id)
            chunk_map[key] = item['chunks']
            
    # Process each chapter
    for ch_num in [f"{i:02d}" for i in range(1, 28)]:
        orig_file = os.path.join(base_dir, f'ch_{ch_num}.json')
        with open(orig_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        new_data = []
        new_id = 1
        
        for item in data:
            key = (ch_num, item['id'])
            if key in chunk_map:
                chunks = chunk_map[key]
                for idx, chunk in enumerate(chunks):
                    new_item = {
                        "id": new_id,
                        "tag": chunk['tag'],
                        "en": chunk['en'],
                        "ko": chunk['ko'],
                        "is_header": item['is_header'] if idx == 0 else False
                    }
                    new_data.append(new_item)
                    new_id += 1
            else:
                item['id'] = new_id
                new_data.append(item)
                new_id += 1
                
        # Write back
        with open(orig_file, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=2)

    print("All chapters successfully merged and chunked!")

if __name__ == '__main__':
    merge()

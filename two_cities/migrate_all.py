import json
import glob
import os

source_dir = 'C:/git_repo/TKprof_book/books/two_cities/json'
dest_dir = 'C:/git_repo/Book_apps/two_cities/src/main/assets/books'
raw_dest_dir = 'C:/git_repo/Book_apps/two_cities/raw_reference_data'

# Get all files sorted by book and chapter
files = sorted(glob.glob(f'{source_dir}/book*.json'))

chapter_counter = 1
for file in files:
    # Use the backup file for chapter 1!
    if 'book1_ch_01.json' in file:
        file = 'C:/git_repo/TKprof_book/books/two_cities/book1_ch_01_backup.json'
        
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    app_data = []
    raw_data = []
    
    for item in data:
        raw_data.append({'raw_ref_id': item['id'], 'raw': item.get('raw', '')})
        app_item = {
            'id': item['id'],
            'tag': item.get('tag', ''),
            'en': item.get('en', ''),
            'ko': item.get('ko', ''),
            'is_header': item.get('is_header', False),
            'raw_ref_id': item['id']
        }
        app_data.append(app_item)
        
    # Write to destination
    ch_str = f'ch_{chapter_counter:02d}.json'
    raw_str = f'raw_ch_{chapter_counter:02d}.json'
    
    with open(os.path.join(dest_dir, ch_str), 'w', encoding='utf-8') as f:
        json.dump(app_data, f, ensure_ascii=False, indent=2)
        
    with open(os.path.join(raw_dest_dir, raw_str), 'w', encoding='utf-8') as f:
        json.dump(raw_data, f, ensure_ascii=False, indent=2)
        
    chapter_counter += 1

print(f'Successfully migrated and chunked {chapter_counter - 1} chapters!')


import json

backup_file = 'C:/git_repo/TKprof_book/books/two_cities/book1_ch_01_backup.json'
dest_file = 'C:/git_repo/Book_apps/two_cities/src/main/assets/books/ch_01.json'
raw_dest_file = 'C:/git_repo/Book_apps/two_cities/raw_reference_data/raw_ch_01.json'

with open(backup_file, 'r', encoding='utf-8') as f:
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

with open(dest_file, 'w', encoding='utf-8') as f:
    json.dump(app_data, f, ensure_ascii=False, indent=2)

with open(raw_dest_file, 'w', encoding='utf-8') as f:
    json.dump(raw_data, f, ensure_ascii=False, indent=2)

print('Chapter 1 restored successfully!')


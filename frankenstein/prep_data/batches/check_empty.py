import json
with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_25.ch21_done.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
empty_found = False
for item in data:
    for chunk in item['chunks']:
        if not chunk['en'] or not chunk['ko']:
            print(f"Empty found in ID {item['original_id']}")
            empty_found = True
if not empty_found:
    print('No empty strings found!')

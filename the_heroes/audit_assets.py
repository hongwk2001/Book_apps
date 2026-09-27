import os
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

dir_path = r'c:\git_repo\Book_apps\the_heroes\src\main\assets\books'
files = sorted(os.listdir(dir_path))
print('Asset files found:', len(files))
assert len(files) == 16, f'Expected 16 files, got {len(files)}'

total_cards = 0
for idx, f in enumerate(files, 1):
    expected_name = f'ch_{idx:02d}.json'
    assert f == expected_name, f'Expected {expected_name}, got {f}'
    
    with open(os.path.join(dir_path, f), 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    
    assert len(data) > 0, f'{f} is empty'
    assert data[0]['is_header'] is True, f'{f} first item is not header'
    print(f"{f}: {len(data)} cards | Title: {data[0]['en']} / {data[0]['ko']}")
    
    for i, item in enumerate(data, 1):
        assert item['id'] == i, f'Non-sequential ID in {f}: {item["id"]} != {i}'
        assert item['en'].strip(), f'Empty en at {f} id {i}'
        assert item['ko'].strip(), f'Empty ko at {f} id {i}'
        assert isinstance(item['is_header'], bool), f'is_header not bool at {f} id {i}'
    
    total_cards += len(data)

print(f'\nAUDIT PASSED! All 16 chapters valid. Total cards: {total_cards}')

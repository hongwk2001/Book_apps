import json
import glob
import os

app_dir = 'C:/git_repo/Book_apps/two_cities/src/main/assets/books'
raw_dir = 'C:/git_repo/Book_apps/two_cities/raw_reference_data'

extreme_long = []
extreme_short = []

for i in range(1, 46):
    ch_str = f'{i:02d}'
    app_file = os.path.join(app_dir, f'ch_{ch_str}.json')
    raw_file = os.path.join(raw_dir, f'raw_ch_{ch_str}.json')
    
    if not os.path.exists(app_file): continue
        
    with open(app_file, 'r', encoding='utf-8') as f: app_data = json.load(f)
    with open(raw_file, 'r', encoding='utf-8') as f: raw_data = json.load(f)
        
    en_by_ref = {}
    is_header_by_ref = {}
    for item in app_data:
        ref_id = item.get('raw_ref_id')
        if ref_id is None: continue
        en_text = item.get('en', '').strip()
        is_header_by_ref[ref_id] = item.get('is_header', False)
        if ref_id in en_by_ref:
            en_by_ref[ref_id] += ' ' + en_text
        else:
            en_by_ref[ref_id] = en_text
            
    for raw_item in raw_data:
        ref_id = raw_item.get('raw_ref_id')
        if is_header_by_ref.get(ref_id, False): continue
            
        raw_text = raw_item.get('raw', '').strip()
        en_text = en_by_ref.get(ref_id, '').strip()
        
        raw_words = len(raw_text.split())
        en_words = len(en_text.split())
        
        if raw_words > 10:
            ratio = en_words / raw_words
            if ratio > 2.0:
                extreme_long.append((ch_str, ref_id, ratio, raw_text, en_text))
            elif ratio < 0.4:
                extreme_short.append((ch_str, ref_id, ratio, raw_text, en_text))

extreme_long.sort(key=lambda x: x[2], reverse=True)
extreme_short.sort(key=lambda x: x[2])

print('--- EXTREMELY LONG (POTENTIAL DUPLICATIONS) ---')
for x in extreme_long[:3]:
    print(f'Ch {x[0]} ID {x[1]} (Ratio: {x[2]:.2f})')
    print(f'  RAW: {x[3][:100]}...')
    print(f'  EN:  {x[4][:100]}...\n')

print('--- EXTREMELY SHORT (POTENTIAL MISSING TEXT) ---')
for x in extreme_short[:3]:
    print(f'Ch {x[0]} ID {x[1]} (Ratio: {x[2]:.2f})')
    print(f'  RAW: {x[3][:100]}...')
    print(f'  EN:  {x[4][:100]}...\n')


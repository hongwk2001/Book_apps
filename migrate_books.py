import json
import os
import sys

src_dir = r'C:\git_repo\TKprof_book\books\dracula\scripts'
dst_dir = r'C:\git_repo\Book_apps\dracula\src\main\assets\books'

all_valid = True
error_messages = []

for i in range(1, 28):
    src_file = os.path.join(src_dir, f'bilingual_ch_{i:02d}.json')
    dst_file = os.path.join(dst_dir, f'ch_{i:02d}.json')
    
    if not os.path.exists(src_file):
        print(f"Warning: Source file {src_file} does not exist.")
        continue
        
    with open(src_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    grouped = {}
    for item in data:
        tag = item.get('tag')
        lang = item.get('lang')
        text = item.get('text')
        
        if not tag:
            error_messages.append(f"Chapter {i}: Found item missing a tag: {item}")
            all_valid = False
            continue
            
        if tag not in grouped:
            grouped[tag] = {}
            
        if lang in grouped[tag]:
            error_messages.append(f"Chapter {i}: Tag {tag} has duplicate '{lang}' entries!")
            all_valid = False
            
        grouped[tag][lang] = text

    # Validation pass
    for tag, langs in grouped.items():
        if 'en' not in langs:
            error_messages.append(f"Chapter {i}: Tag {tag} is missing English ('en') text.")
            all_valid = False
        if 'ko' not in langs:
            error_messages.append(f"Chapter {i}: Tag {tag} is missing Korean ('ko') text.")
            all_valid = False

    if not all_valid:
        continue # Skip writing if there are errors in this or any previous

    # Write output
    out_data = []
    pid = 1
    for tag, langs in grouped.items():
        out_data.append({
            'id': pid,
            'tag': tag,
            'en': langs.get('en', ''),
            'ko': langs.get('ko', ''),
            'is_header': False
        })
        pid += 1
        
    with open(dst_file, 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)

if not all_valid:
    print("VALIDATION FAILED:")
    for err in error_messages:
        print(err)
    sys.exit(1)
else:
    print("All 27 chapters validated and migrated successfully!")

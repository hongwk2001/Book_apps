import json
import os

# Fix Ch 09 ID 56
ch9_path = r'c:\git_repo\Book_apps\secret_garden\json_output\ch_09.json'
with open(ch9_path, 'r', encoding='utf-8') as f:
    data9 = json.load(f)
    
for item in data9:
    if item['id'] == 56:
        item['ko'] = item['ko'].replace('?????.', '????.')
        print("Fixed Ch 9")
        
with open(ch9_path, 'w', encoding='utf-8') as f:
    json.dump(data9, f, ensure_ascii=False, indent=2)

# Fix Ch 21 ID 105
ch21_path = r'c:\git_repo\Book_apps\secret_garden\json_output\ch_21.json'
with open(ch21_path, 'r', encoding='utf-8') as f:
    data21 = json.load(f)
    
for item in data21:
    if item['id'] == 105:
        item['ko'] = '"???!" ??? ????.'
        print("Fixed Ch 21")
        
with open(ch21_path, 'w', encoding='utf-8') as f:
    json.dump(data21, f, ensure_ascii=False, indent=2)


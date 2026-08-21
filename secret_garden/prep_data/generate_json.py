import os
import re
import json

def pad_prefix(prefix):
    # prefix is like P1, P31a
    match = re.match(r'^P(\d+)([a-z]?)$', prefix)
    if match:
        num = int(match.group(1))
        suffix = match.group(2)
        return f"P{num:03d}{suffix}"
    return prefix

def generate_json():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    out_dir = os.path.join(directory, 'json_output')
    os.makedirs(out_dir, exist_ok=True)
    
    for ch_num in [f"{i:02d}" for i in range(1, 28)]:
        en_file = os.path.join(directory, f'ch_{ch_num}_en.txt')
        ko_file = os.path.join(directory, f'ch_{ch_num}_ko.txt')
        
        with open(en_file, 'r', encoding='utf-8') as f:
            en_lines = [line.strip() for line in f if line.strip()]
        with open(ko_file, 'r', encoding='utf-8') as f:
            ko_lines = [line.strip() for line in f if line.strip()]
            
        json_data = []
        id_counter = 1
        
        for en_line, ko_line in zip(en_lines, ko_lines):
            en_match = re.match(r'^(P\d+[a-z]?)\|', en_line)
            ko_match = re.match(r'^(P\d+[a-z]?)\|', ko_line)
            
            if en_match and ko_match:
                prefix = en_match.group(1)
                padded_tag = pad_prefix(prefix)
                
                en_text = en_line[len(prefix)+1:].strip()
                ko_text = ko_line[len(prefix)+1:].strip()
                
                json_data.append({
                    "id": id_counter,
                    "tag": padded_tag,
                    "lang": "en",
                    "text": en_text
                })
                id_counter += 1
                
                json_data.append({
                    "id": id_counter,
                    "tag": padded_tag,
                    "lang": "ko",
                    "text": ko_text
                })
                id_counter += 1
                
        out_file = os.path.join(out_dir, f'bilingual_ch_{ch_num}.json')
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    generate_json()

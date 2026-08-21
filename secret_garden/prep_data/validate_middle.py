import os
import re

def extract_lines(file_path):
    # Returns a list of (prefix, text) keeping original order
    lines = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^(P\d+[a-z]?)\|', line)
            if match:
                prefix = match.group(1)
                text = line[len(prefix)+1:].strip()
                lines.append((prefix, text))
    return lines

def run_validation():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    all_chapters = [f"{i:02d}" for i in range(1, 28)]
    
    samples = []
    
    for ch in all_chapters:
        raw_file = os.path.join(directory, f'raw_ch_{ch}.txt')
        en_file = os.path.join(directory, f'ch_{ch}_en.txt')
        ko_file = os.path.join(directory, f'ch_{ch}_ko.txt')
        
        raw_lines_list = extract_lines(raw_file)
        en_lines_list = extract_lines(en_file)
        ko_lines_list = extract_lines(ko_file)
        
        # We need to pick one in the middle of the chapter.
        # Since EN and KO have the exact same lines now, we can pick the middle of EN.
        if not en_lines_list:
            continue
            
        mid_idx = len(en_lines_list) // 2
        chosen_prefix, en_text = en_lines_list[mid_idx]
        
        # Find the matching KO text
        ko_dict = {p: t for p, t in ko_lines_list}
        ko_text = ko_dict.get(chosen_prefix, "MISSING")
        
        # Find the matching RAW text (strip suffix)
        raw_prefix = re.sub(r'[a-z]$', '', chosen_prefix)
        raw_dict = {p: t for p, t in raw_lines_list}
        raw_text = raw_dict.get(raw_prefix, "MISSING")
        
        samples.append({
            'chapter': ch,
            'prefix': chosen_prefix,
            'raw_p': raw_prefix,
            'raw': raw_text,
            'en': en_text,
            'ko': ko_text
        })
        
    with open(r'c:\git_repo\Book_apps\secret_garden\alignment_validation.txt', 'w', encoding='utf-8') as f:
        f.write("# Chapter-by-Chapter Alignment Validation\n\n")
        f.write("Here is one paragraph extracted from the exact middle of every chapter to verify that the translations remain perfectly aligned.\n\n")
        for s in samples:
            f.write(f"## Chapter {s['chapter']} (Sample `{s['prefix']}`)\n")
            f.write(f"- **RAW (Source `{s['raw_p']}`)**: {s['raw']}\n")
            f.write(f"- **EN (Modern `{s['prefix']}`)**: {s['en']}\n")
            f.write(f"- **KO (Translation `{s['prefix']}`)**: {s['ko']}\n\n")

if __name__ == '__main__':
    run_validation()

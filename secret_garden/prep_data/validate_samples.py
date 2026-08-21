import os
import glob
import re
import random

def extract_lines(file_path):
    lines = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.match(r'^(P\d+[a-z]?)\|', line)
            if match:
                prefix = match.group(1)
                text = line[len(prefix)+1:].strip()
                lines[prefix] = text
    return lines

def run_validation():
    directory = r'c:\git_repo\Book_apps\secret_garden'
    all_chapters = [f"{i:02d}" for i in range(1, 28)]
    
    samples = []
    
    # We want 5 samples. Let's randomly pick 5 chapters.
    random.seed() # Use system time
    sample_chapters = random.sample(all_chapters, 5)
    
    for ch in sample_chapters:
        raw_file = os.path.join(directory, f'raw_ch_{ch}.txt')
        en_file = os.path.join(directory, f'ch_{ch}_en.txt')
        ko_file = os.path.join(directory, f'ch_{ch}_ko.txt')
        
        raw_lines = extract_lines(raw_file)
        en_lines = extract_lines(en_file)
        ko_lines = extract_lines(ko_file)
        
        # Pick a random prefix that exists in EN
        en_prefixes = list(en_lines.keys())
        if not en_prefixes:
            continue
            
        # Try to pick one with a suffix if available, otherwise any
        suffixed = [p for p in en_prefixes if re.search(r'[a-z]$', p)]
        if suffixed and random.random() < 0.5:
            chosen_p = random.choice(suffixed)
        else:
            chosen_p = random.choice(en_prefixes)
            
        # The raw file might not have the suffix (e.g. if chosen_p is P9a, raw only has P9)
        raw_p = re.sub(r'[a-z]$', '', chosen_p)
        
        raw_text = raw_lines.get(raw_p, "MISSING")
        en_text = en_lines.get(chosen_p, "MISSING")
        ko_text = ko_lines.get(chosen_p, "MISSING")
        
        samples.append({
            'chapter': ch,
            'prefix': chosen_p,
            'raw_p': raw_p,
            'raw': raw_text,
            'en': en_text,
            'ko': ko_text
        })
        
    with open(r'c:\git_repo\Book_apps\secret_garden\alignment_validation.txt', 'w', encoding='utf-8') as f:
        f.write("# Alignment Validation Samples\n\n")
        f.write("Here are 5 randomly selected paragraphs from across the book to verify that the translations and formatting align perfectly.\n\n")
        for i, s in enumerate(samples, 1):
            f.write(f"## Sample {i} - Chapter {s['chapter']} ({s['prefix']})\n")
            f.write(f"- **RAW (Source `{s['raw_p']}`)**: {s['raw']}\n")
            f.write(f"- **EN (Modern `{s['prefix']}`)**: {s['en']}\n")
            f.write(f"- **KO (Translation `{s['prefix']}`)**: {s['ko']}\n\n")

if __name__ == '__main__':
    run_validation()

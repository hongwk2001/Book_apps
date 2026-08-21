import os
import re

def fix_title_newline(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # If it starts with "?X?" followed by a single newline
    text = re.sub(r'^(?\d+?)\s*\n([^\n])', r'\1\n\n\2', text)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Processed {os.path.basename(filepath)}")

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"
fix_title_newline(os.path.join(base_dir, "5.ch1_ko.txt"))
fix_title_newline(os.path.join(base_dir, "6.ch2_ko.txt"))

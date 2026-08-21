import os
import re

def force_fix(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Replace single newline after ?X? with double newline
    text = re.sub(r'^(?\d+?)\s*\n([^\n])', r'\1\n\n\2', text, count=1)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Forced fix {os.path.basename(filepath)}")

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"
force_fix(os.path.join(base_dir, "5.ch1_ko.txt"))
force_fix(os.path.join(base_dir, "6.ch2_ko.txt"))

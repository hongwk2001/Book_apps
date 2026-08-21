import os

def fix_title_newline(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    
    if text.startswith("?") and text[text.find('\n')+1] != '\n':
        text = text.replace('\n', '\n\n', 1)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Fixed {os.path.basename(filepath)}")

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"
fix_title_newline(os.path.join(base_dir, "5.ch1_ko.txt"))
fix_title_newline(os.path.join(base_dir, "6.ch2_ko.txt"))

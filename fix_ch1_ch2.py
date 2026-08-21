import os

def fix_title(filepath):
    with open(filepath, "r", encoding="utf-8-sig") as f:
        text = f.read()
    
    text = text.replace("\r\n", "\n")
    if text.startswith("?") and text.find("\n") != -1:
        idx = text.find("\n")
        if text[idx+1] != "\n":
            text = text[:idx] + "\n\n" + text[idx+1:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Fixed {filepath}")

base_dir = r"c:\git_repo\Book_apps\frankenstein\prep_data"
fix_title(os.path.join(base_dir, "5.ch1_ko.txt"))
fix_title(os.path.join(base_dir, "6.ch2_ko.txt"))

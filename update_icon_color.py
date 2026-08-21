import os
import re

def update_color(filepath):
    if not os.path.exists(filepath):
        print(f"Not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'<color name="tkprof_purple">#130319</color>', '<color name="tkprof_purple">#302864</color>', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_color(r"c:\git_repo\Book_apps\secret_garden\src\main\res\values\colors.xml")
update_color(r"c:\git_repo\Book_apps\dracula\src\main\res\values\colors.xml")

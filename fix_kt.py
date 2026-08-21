import os
import re

kt_file = r'c:\git_repo\Book_apps\secret_garden\src\main\java\com\tkprof\secretgarden\MainActivity.kt'
with open(kt_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the double comma and the question marks
content = re.sub(r'titleKo\s*=\s*".*?",*,,?', 'titleKo = "비밀의 화원",', content)

with open(kt_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Saved via Python")
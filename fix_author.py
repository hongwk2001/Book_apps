import os

kt_file = r'c:\git_repo\Book_apps\secret_garden\src\main\java\com\tkprof\secretgarden\MainActivity.kt'
with open(kt_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('author = "Bram Stoker"', 'author = "Frances Hodgson Burnett"')
# Let's ensure the titleKo is correct in case it got corrupted
import re
content = re.sub(r'titleKo = ".*"', 'titleKo = "??? ??"', content)

with open(kt_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed author and titleKo")

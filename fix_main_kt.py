import os

kt_file = r'c:\git_repo\Book_apps\secret_garden\src\main\java\com\tkprof\secretgarden\MainActivity.kt'
with open(kt_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('bookId = "dracula"', 'bookId = "secretgarden"')
content = content.replace('titleEn = "Dracula"', 'titleEn = "Secret Garden"')
content = content.replace('titleKo = "????"', 'titleKo = "??? ??"')
content = content.replace('iapProductId = "com.tkprof.dracula.full"', 'iapProductId = "com.tkprof.secretgarden.full"')

with open(kt_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed MainActivity.kt")

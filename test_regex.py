import re

with open(r'C:\git_repo\Book_apps\shared\src\main\java\com\tkprof\shared\ui\reader\ReaderScreen.kt', 'r', encoding='utf-8') as f:
    text = f.read()

# I will find 'fun ParagraphCard' and see its arguments.
match = re.search(r'fun ParagraphCard.*?\{', text, re.DOTALL)
if match:
    print(match.group(0))

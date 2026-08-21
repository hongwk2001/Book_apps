import os

filepath = r'c:\git_repo\TKprof_book\books\frankenstein\chapters\raw_ch_20.txt'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

chars = len(text)
words = len(text.split())

print(f"RAW File ({os.path.basename(filepath)}):")
print(f"Characters: {chars}")
print(f"Words: {words}")

import re
with open(r"c:\git_repo\TKprof_book\books\frankenstein\raw_source.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Find all "Letter X" or "Chapter X"
matches = re.finditer(r'^(Letter \d+|Chapter \d+)$', text, re.MULTILINE)
for m in matches:
    print(m.group(1))

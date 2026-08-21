import re
with open(r"c:\git_repo\TKprof_book\books\frankenstein\raw_source.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Let's find "Letter 1" where it's followed by "To Mrs. Saville"
idx = text.find("To Mrs. Saville, England.")
# Find "Letter 1" right before this.
start_idx = text.rfind("Letter 1", 0, idx)

content = text[start_idx:]
end_idx = content.find("*** END OF THE PROJECT GUTENBERG EBOOK")
if end_idx == -1: end_idx = content.find("End of the Project Gutenberg eBook")
content = content[:end_idx]

# To avoid TOC, we are already past it.
pattern = r'^(Letter \d+|Chapter \d+)$'
parts = re.split(pattern, content, flags=re.MULTILINE)
if not parts[0].strip():
    parts = parts[1:]

print(f"Number of parts: {len(parts)} (should be 56)")
for i in range(0, min(10, len(parts)), 2):
    print(parts[i])

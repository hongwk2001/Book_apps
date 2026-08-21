ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_ko.txt'
with open(ko_file, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

def split_line(line):
    # Find first " that is not at index 0
    idx = line.find('"', 1)
    if idx != -1:
        # Also check if it's "He does it to keep..." which might be double quotes inside. 
        # But actually in Korean they might use other quotes.
        # Let's just find the last period or punctuation before the quote.
        return line[:idx].strip(), line[idx:].strip()
    return line, ""

p1a, p1b = split_line(lines[12])
p2a, p2b = split_line(lines[15])

lines[12:13] = [p1a, p1b]
# After inserting 1 element, index 15 becomes index 16
lines[16:17] = [p2a, p2b]

with open(ko_file, 'w', encoding='utf-8') as f:
    for l in lines:
        f.write(f"{l}\n")

ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_24_ko.txt'
with open(ko_file, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]
    
print("KO[12]:", repr(lines[12]))
print("KO[15]:", repr(lines[15]))

with open(ko_file, 'w', encoding='utf-8') as f:
    for l in lines:
        f.write(f"{l}\n")

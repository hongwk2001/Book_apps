en_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_en.txt'
ko_file = r'c:\git_repo\Book_apps\secret_garden\ch_27_ko.txt'
with open(en_file, 'r', encoding='utf-8') as f:
    en_lines = [line.strip() for line in f if line.strip()]
with open(ko_file, 'r', encoding='utf-8') as f:
    ko_lines = [line.strip() for line in f if line.strip()]

with open(r'c:\git_repo\Book_apps\secret_garden\ch27_full.txt', 'w', encoding='utf-8') as out:
    for i in range(9, 14):
        out.write(f"EN[{i+1}]: {en_lines[i]}\n")
        out.write(f"KO[{i+1}]: {ko_lines[i]}\n\n")

with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\19.ch15_en.txt", "r", encoding="utf-8") as f:
    paras = [p for p in f.read().split("\n\n") if p.strip()]
print("EN P4:")
print(paras[4][-150:])

with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\19.ch15_ko.txt", "r", encoding="utf-8") as f:
    paras_ko = [p for p in f.read().split("\n\n") if p.strip()]
print("\nKO P4:")
print(paras_ko[4][-150:])

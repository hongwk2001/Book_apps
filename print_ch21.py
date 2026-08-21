with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\25.ch21_en.txt", "r", encoding="utf-8") as f:
    en_paras = "".join(f.readlines()).split("\n\n")
with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\25.ch21_ko.txt", "r", encoding="utf-8") as f:
    ko_paras = "".join(f.readlines()).split("\n\n")

print("EN 9:")
print(en_paras[9])
print("EN 10:")
print(en_paras[10])

print("\nKO 9:")
print(ko_paras[9])

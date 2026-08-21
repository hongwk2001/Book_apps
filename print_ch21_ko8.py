with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\25.ch21_ko.txt", "r", encoding="utf-8") as f:
    ko_paras = "".join(f.readlines()).split("\n\n")

print("KO 8:")
print(ko_paras[8])

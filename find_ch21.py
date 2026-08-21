with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\25.ch21_en.txt", "r", encoding="utf-8") as f:
    en_lines = f.readlines()
with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\25.ch21_ko.txt", "r", encoding="utf-8") as f:
    ko_lines = f.readlines()

en_paras = "".join(en_lines).split("\n\n")
ko_paras = "".join(ko_lines).split("\n\n")

for i in range(1, 40):
    if abs(len(en_paras[i]) - len(ko_paras[i])*2) > 300: # rough proxy
        print(f"Possible mismatch at {i}")
        break

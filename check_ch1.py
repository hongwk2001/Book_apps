with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\5.ch1_en.txt", "r", encoding="utf-8") as f:
    en_lines = f.readlines()
with open(r"c:\git_repo\Book_apps\frankenstein\prep_data\numbered\5.ch1_ko.txt", "r", encoding="utf-8") as f:
    ko_lines = f.readlines()
print("EN:")
print("".join(en_lines[:15]))
print("KO:")
print("".join(ko_lines[:15]))

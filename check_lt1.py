with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\1.Lt1_en.txt", "r", encoding="utf-8") as f:
    en_lines = f.readlines()
with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\1.Lt1_ko.txt", "r", encoding="utf-8") as f:
    ko_lines = f.readlines()
print("EN:")
print("".join(en_lines[:5]))
print("KO:")
print("".join(ko_lines[:5]))

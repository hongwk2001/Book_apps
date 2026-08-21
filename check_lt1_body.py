with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\1.Lt1_en.txt", "r", encoding="utf-8") as f:
    en_lines = f.readlines()
print("EN:")
print("".join(en_lines[7:12]))

with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\20.ch16_en.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("".join(lines[-5:]))

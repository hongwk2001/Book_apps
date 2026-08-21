with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\raw_ch_20.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("".join(lines[:10]))

with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\raw_ch_00.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()
print("RAW:")
print("".join(raw_lines[13:20]))

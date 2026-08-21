with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\raw_ch_00.txt", "r", encoding="utf-8") as f:
    text = f.read()
idx = text.find("I am already far north of London")
print(text[idx-200:idx+400])

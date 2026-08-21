with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\5.ch1_ko.txt", "r", encoding="utf-8") as f:
    text = f.read()

paras = [p for p in text.split("\n\n") if p.strip()]
print(f"Original KO paras: {len(paras)}")
for i, p in enumerate(paras[:2]):
    print(f"P{i}: {repr(p)}")

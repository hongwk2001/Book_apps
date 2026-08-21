with open(r"c:\git_repo\TKprof_book\books\frankenstein\raw_source.txt", "r", encoding="utf-8") as f:
    text = f.read()
print(f"Total size: {len(text)}")
print(text[:200])

with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\5.ch1_ko.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("\r\n", "\n")
idx = text.find("\n")
if text[idx+1] != "\n":
    text = text[:idx] + "\n\n" + text[idx+1:]

new_paras = [p for p in text.split("\n\n") if p.strip()]
print(f"Fixed KO paras: {len(new_paras)}")
for i, p in enumerate(new_paras[:3]):
    print(f"P{i}: {repr(p)}")

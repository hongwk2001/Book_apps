with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\5.ch1_ko.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Check how many paragraphs we get if we split by \n\n
paras = [p for p in text.split("\n\n") if p.strip()]
print(f"Original KO paras: {len(paras)}")

# Manually insert \n\n after ?X? if it's missing
if text.startswith("?") and "\n\n" not in text[:20]:
    text = text.replace("\n", "\n\n", 1)

new_paras = [p for p in text.split("\n\n") if p.strip()]
print(f"Fixed KO paras: {len(new_paras)}")

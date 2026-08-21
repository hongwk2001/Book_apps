with open(r"c:\git_repo\TKprof_book\books\frankenstein\chapters\5.ch1_ko.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Replace all \r\n with \n to normalize
text = text.replace("\r\n", "\n")

if text.startswith("?") and text.find("\n") != -1:
    idx = text.find("\n")
    if text[idx+1] != "\n":
        text = text[:idx] + "\n\n" + text[idx+1:]

new_paras = [p for p in text.split("\n\n") if p.strip()]
print(f"Fixed KO paras: {len(new_paras)}")

import os
filepath = r"c:\git_repo\Book_apps\frankenstein\prep_data\9.ch5_ko.txt"
with open(filepath, "r", encoding="utf-8") as f:
    paras = [p for p in f.read().split("\n\n") if p.strip()]
for i, p in enumerate(paras[:10]):
    print(f"[{i}]: {p[:30]}...")

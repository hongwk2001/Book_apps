import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_30.json", encoding='utf-8'))
for idx in range(23, 31):
    p = data[idx]
    print(f"idx={idx}, id={p['id']}, tag={p.get('tag')}")
    print("  EN:", p['en'])
    print("  KO:", p['ko'])
    print()

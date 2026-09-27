import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_30.json", encoding='utf-8'))

for idx in range(45, 60):
    p = data[idx]
    print(f"[{idx} / ID {p['id']}]")
    print(f"  EN: {p['en'][:90]}")
    print(f"  KO: {p['ko'][:90]}")
    print()

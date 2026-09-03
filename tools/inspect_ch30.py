import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

data30 = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_30.json", encoding='utf-8'))
for p in data30:
    if 30 <= p['id'] <= 50:
        print(f"[{p['id']} - {p.get('tag')}]")
        print(f"  EN: {p['en']}")
        print(f"  KO: {p['ko']}")
        print()

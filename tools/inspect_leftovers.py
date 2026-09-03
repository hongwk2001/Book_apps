import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Inspect ch_18 around ID 22
print("=== CH_18 AROUND ID 22 ===")
data18 = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_18.json", encoding='utf-8'))
for p in data18:
    if 20 <= p['id'] <= 25:
        print(f"[{p['id']} - {p.get('tag')}]")
        print(f"EN: {p['en']}")
        print(f"KO: {p['ko']}")
        print()

# Inspect ch_07 around ID 33
print("=== CH_07 AROUND ID 33 ===")
data07 = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_07.json", encoding='utf-8'))
for p in data07:
    if 31 <= p['id'] <= 36:
        print(f"[{p['id']} - {p.get('tag')}]")
        print(f"EN: {p['en']}")
        print(f"KO: {p['ko']}")
        print()

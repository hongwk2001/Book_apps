import json
import os

assets = r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books"

def print_tags(chapter, prefix):
    path = os.path.join(assets, f"ch_{chapter}.json")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n--- Chapter {chapter} {prefix} ---")
    for item in data:
        if item["tag"].startswith(prefix):
            print(f"[{item['tag']}]")
            print(f"EN: {item['en']}")
            print(f"KO: {item['ko']}")

print_tags("10", "P008")
print_tags("16", "P013")
print_tags("15", "P014")
print_tags("11", "P022")
print_tags("24", "P025")
print_tags("10", "P019")
print_tags("28", "P076")

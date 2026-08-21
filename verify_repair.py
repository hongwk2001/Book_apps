import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_24.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    if item["tag"] == "P025-6":
        print(f"EN: {item['en']}\nKO: {item['ko']}")

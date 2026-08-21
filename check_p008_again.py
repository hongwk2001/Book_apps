import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_10.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    if item["tag"].startswith("P008"):
        print(f"[{item['tag']}] EN: {item['en']}\nKO: {item['ko']}\n")

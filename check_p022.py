import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_11.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    if item["tag"] in ["P022-3", "P022-4"]:
        print(f"[{item['tag']}] EN: {item['en']}\nKO: {item['ko']}\n")

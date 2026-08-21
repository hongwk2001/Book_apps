import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_15.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for item in data:
    if item["tag"] in ["P014-5", "P014-6", "P014-7"]:
        print(f"[{item['tag']}] EN: {item['en']}\nKO: {item['ko']}\n")

import json
with open(r"c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_19.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    
for item in data:
    if "P004" in item["tag"]:
        print(f"[{item['tag']}]")
        print(f"EN: {item['en']}")
        print(f"KO: {item['ko']}")
        print("-" * 20)

import json
with open(r"c:\git_repo\Book_apps\secret_garden\src\main\assets\books\ch_01.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(json.dumps(data[:3], ensure_ascii=False, indent=2))

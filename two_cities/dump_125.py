import json

with open('C:\\git_repo\\Book_apps\\dracula\\long_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i in data:
    if i['id'] == 125:
        with open('C:\\git_repo\\Book_apps\\dracula\\id_125.json', 'w', encoding='utf-8') as out:
            json.dump(i, out, ensure_ascii=False, indent=2)

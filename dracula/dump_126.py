import json
with open('C:\\git_repo\\Book_apps\\dracula\\src\\main\\assets\\books\\ch_13.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('C:\\git_repo\\Book_apps\\dracula\\id_126.json', 'w', encoding='utf-8') as out:
    json.dump(next(i for i in data if i['id'] == 126), out, ensure_ascii=False, indent=2)

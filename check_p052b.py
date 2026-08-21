import json

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

res = []
for tag in ['P052a', 'P052b', 'P052c']:
    item = next((x for x in data if x.get('tag') == tag), None)
    res.append(item)

with open('p052b_output.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

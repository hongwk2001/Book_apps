import json

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

res = []
for item in data:
    if 'chunks' in item:
        tag = item['chunks'][0]['tag'].split('-')[0]
        if tag in ['P020b', 'P052b', 'P052c']:
            res.append(item)
    else:
        tag = item.get('tag')
        if tag in ['P020b', 'P052b', 'P052c']:
            res.append(item)
with open('debug_out.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, ensure_ascii=False, indent=2)

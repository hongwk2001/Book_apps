import json

paragraphs = ['P006', 'P024', 'P027', 'P028', 'P029', 'P034', 'P036', 'P040', 'P049', 'P050']
with open('debug.json', encoding='utf-8') as f:
    d = json.load(f)

with open('sentences.txt', 'w', encoding='utf-8') as f:
    for p in paragraphs:
        f.write(f'=== {p} ===\n')
        for i, e in enumerate(d[p]['en']):
            f.write(f'E{i+1}: {e}\n')
        for i, k in enumerate(d[p]['ko']):
            f.write(f'K{i+1}: {k}\n')
        f.write('\n')

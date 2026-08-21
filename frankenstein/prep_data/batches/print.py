import json

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_25.ch21.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ids = [2, 8, 9, 11, 12, 14, 20, 21, 27, 28, 35, 39, 42, 43, 44, 45, 46, 47, 48, 49]
with open('out.txt', 'w', encoding='utf-8') as out:
    for item in data:
        if item['id'] in ids:
            out.write(f"ID {item['id']}\n")
            out.write(f"EN: {item['en']}\n")
            out.write(f"KO: {item['ko']}\n")
            out.write('-'*40 + '\n')

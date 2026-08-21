import json
with open('batch_26.ch22.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
with open('debug.txt', 'w', encoding='utf-8') as f:
    for d in data:
        f.write(f"ID: {d['id']}\nEN: {d['en']}\nKO: {d['ko']}\n\n")

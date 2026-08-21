import json
with open('src/main/assets/books/ch_11.json', encoding='utf-8') as f:
    d = json.load(f)
with open('chunks.txt', 'w', encoding='utf-8') as f:
    for x in d:
        if x['tag'].startswith('P006-'):
            f.write(x['tag'] + '\n')
            f.write(f"EN: {x['en']}\n")
            f.write(f"KO: {x['ko']}\n")

import sys, json
sys.stdout.reconfigure(encoding='utf-8')
d = json.load(open(r'c:\git_repo\Book_apps\frankenstein\src\main\assets\books\ch_24.json', encoding='utf-8'))
for p in ['P001', 'P002']:
    for c in d:
        if c['tag'].startswith(p + '-'):
            print(f"{c['tag']}:\n EN: {c['en']}\n KO: {c['ko']}\n")

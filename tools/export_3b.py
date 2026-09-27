import json
import os

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

targets = [
    ('ch_04.json', 'P090_1'),
    ('ch_09.json', 'P095_3'),
    ('ch_31.json', 'P097_2'),
    ('ch_34.json', 'P005_4'),
    ('ch_34.json', 'P012_1'),
]

with open('cat3b_show.txt', 'w', encoding='utf-8') as out:
    for ch_file, tag in targets:
        fpath = os.path.join(assets_dir, ch_file)
        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)
        p = [x for x in data if x.get('tag') == tag][0]
        out.write(f"=== {ch_file} Current ID {p['id']} (tag: {tag}) ===\n")
        out.write(f"Length: {len(p['en'])} EN chars, {len(p['ko'])} KO chars\n")
        out.write("EN:\n" + p['en'] + "\n\n")
        out.write("KO:\n" + p['ko'] + "\n\n")
        out.write("---------------------------------------------------\n\n")

print("Wrote cat3b_show.txt")

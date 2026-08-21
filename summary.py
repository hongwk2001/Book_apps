import json
data = json.load(open('C:\\git_repo\\Book_apps\\mismatches.json', encoding='utf-8'))
with open('C:\\git_repo\\Book_apps\\mismatches_summary.txt', 'w', encoding='utf-8') as f:
    for idx, (k, v) in enumerate(data.items()):
        f.write(f'ID: {k}\n')
        f.write(f'EN ({len(v["en_sents"])}): {v["en"]}\n')
        f.write(f'KO ({len(v["ko_sents"])}): {v["ko"]}\n\n')

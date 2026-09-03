import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
data = json.load(open(r"C:\git_repo\Book_apps\two_cities\src\main\assets\books\ch_30.json", encoding='utf-8'))

with open('ch30_alignment_table.txt', 'w', encoding='utf-8') as out:
    out.write("INDEX | ID | EN TEXT | CURRENT KO TEXT\n")
    out.write("="*80 + "\n")
    for idx in range(18, 52):
        p = data[idx]
        out.write(f"[{idx}] ID {p['id']} ({p.get('tag')}):\n")
        out.write(f"  EN: {p['en']}\n")
        out.write(f"  KO: {p['ko']}\n\n")

print("Wrote ch30_alignment_table.txt")

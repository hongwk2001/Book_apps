import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('two_cities_mr_audit.txt', encoding='utf-8') as f:
    text = f.read()

entries = text.split('='*70)

print(f"Total entries: {len(entries)-1}")
for i, e in enumerate(entries[:-1], 1):
    lines = [l for l in e.strip().splitlines() if l.strip()]
    if lines:
        header = lines[0]
        en_lines = [l for l in lines if l.strip().startswith('EN:')]
        ko_lines = [l for l in lines if l.strip().startswith('KO:')]
        next_en = [l for l in lines if l.strip().startswith('NEXT EN:')]
        if en_lines and ko_lines:
            print(f"[{i}] {header}")
            print(f"    EN: ...{en_lines[0][-60:]}")
            print(f"    KO: ...{ko_lines[0][-60:]}")
            if next_en:
                print(f"    NEXT: {next_en[0][13:80]}...")
            print()

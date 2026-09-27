import sys

with open('split_candidates_analysis.txt', encoding='utf-8') as f:
    text = f.read()

entries = text.split('='*80)
print(f"Total entries: {len(entries)-1}")
for e in entries[:-1]:
    lines = [l for l in e.strip().splitlines() if l.strip()]
    if lines:
        print(lines[0])
        # count EN sentences and KO sentences
        en_lines = [l for l in lines if l.strip().startswith('(') and 'ch]' in l]
        # check
        header = lines[0]
        print(f"  Header: {header}")

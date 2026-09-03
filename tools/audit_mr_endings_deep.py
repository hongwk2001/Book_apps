import json
import glob
import os
import re

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))

results = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for idx, p in enumerate(data):
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()

        # Check for ending with Mr, Mrs, Dr, Ms, St followed by quote or dot
        m = re.search(r'\b(Mr|Mrs|Ms|Dr|Prof|St)\.?["\'”’]?$', en, re.IGNORECASE)
        m_ko = re.search(r'(미스터|씨\s*)$', ko)
        if m or m_ko or en.endswith(('Mr.', 'Mr."', 'Mr.' + "''", 'Mrs.', 'Mrs."')):
            next_p = data[idx+1] if idx+1 < len(data) else None
            prev_p = data[idx-1] if idx > 0 else None
            results.append({
                'ch': ch,
                'idx': idx,
                'id': p.get('id'),
                'tag': p.get('tag'),
                'en': en,
                'ko': ko,
                'next_id': next_p.get('id') if next_p else None,
                'next_en': next_p.get('en') if next_p else None,
                'next_ko': next_p.get('ko') if next_p else None,
            })

print(f"Total 'Mr.' style bad endings found in Two Cities: {len(results)}")

with open('two_cities_mr_audit.txt', 'w', encoding='utf-8') as out:
    for i, r in enumerate(results, 1):
        out.write(f"[{i}] {r['ch']} ID {r['id']} ({r['tag']})\n")
        out.write(f"    EN: {r['en']}\n")
        out.write(f"    KO: {r['ko']}\n")
        if r['next_en']:
            out.write(f"    --> NEXT ID {r['next_id']}:\n")
            out.write(f"    NEXT EN: {r['next_en'][:120]}...\n")
            out.write(f"    NEXT KO: {r['next_ko'][:120]}...\n")
        out.write("="*70 + "\n\n")

print("Wrote two_cities_mr_audit.txt")

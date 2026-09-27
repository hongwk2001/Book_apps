import json
import glob
import os
import re

ABBREVIATIONS = [
    'mr.', 'mrs.', 'ms.', 'dr.', 'prof.', 'sr.', 'jr.', 'st.', 'mt.', 
    'capt.', 'col.', 'gen.', 'lieut.', 'sgt.', 'rev.', 'no.', 'vol.', 'etc.'
]

def audit_book_bad_endings(book_name, assets_dir):
    files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))
    if not files:
        return []

    issues = []

    for fpath in files:
        ch = os.path.basename(fpath)
        with open(fpath, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                continue

        paras = [p for p in data if not p.get('is_header')]

        for idx, p in enumerate(paras):
            en = p.get('en', '').strip()
            ko = p.get('ko', '').strip()
            pid = p.get('id')
            tag = p.get('tag', '')

            # Check 1: Ends with abbreviation (e.g. Mr., Mrs., Mr.")
            clean_end = re.sub(r'["\'”’\s]+$', '', en).lower()
            for abbr in ABBREVIATIONS:
                if clean_end.endswith(abbr):
                    # Check if it's really an abbreviation and not a word like 'etc.'
                    issues.append({
                        'book': book_name,
                        'ch': ch,
                        'id': pid,
                        'tag': tag,
                        'type': f"Ends with abbreviation '{abbr}'",
                        'en_tail': en[-60:],
                        'ko_tail': ko[-60:],
                        'en_full': en,
                        'ko_full': ko,
                        'next_en': paras[idx+1].get('en', '')[:60] if idx+1 < len(paras) else None
                    })

            # Check 2: Ends with dangling comma, colon, semicolon, or dash
            clean_punct_end = re.sub(r'["\'”’\s]+$', '', en)
            if clean_punct_end.endswith((',', ':', ';', '—', '--', '-')):
                issues.append({
                    'book': book_name,
                    'ch': ch,
                    'id': pid,
                    'tag': tag,
                    'type': f"Dangling punctuation end: '{clean_punct_end[-2:]}'",
                    'en_tail': en[-60:],
                    'ko_tail': ko[-60:],
                    'en_full': en,
                    'ko_full': ko,
                    'next_en': paras[idx+1].get('en', '')[:60] if idx+1 < len(paras) else None
                })

            # Check 3: Next paragraph starts with lowercase letter (mid-sentence break)
            if idx + 1 < len(paras):
                next_en = paras[idx+1].get('en', '').strip()
                # strip leading quotes or dashes
                clean_start = re.sub(r'^["\'“‘—\-\s]+', '', next_en)
                if clean_start and clean_start[0].islower():
                    issues.append({
                        'book': book_name,
                        'ch': ch,
                        'id': pid,
                        'tag': tag,
                        'type': f"Next paragraph starts with lowercase: '{clean_start[:20]}...'",
                        'en_tail': en[-60:],
                        'ko_tail': ko[-60:],
                        'en_full': en,
                        'ko_full': ko,
                        'next_en': next_en[:60]
                    })

            # Check 4: Ends without terminal punctuation in English
            # Valid ends: . ! ? " ” ’ ' …
            if en and not re.search(r'[\.!\?"”’\'…]$', en):
                issues.append({
                    'book': book_name,
                    'ch': ch,
                    'id': pid,
                    'tag': tag,
                    'type': "Missing terminal punctuation",
                    'en_tail': en[-60:],
                    'ko_tail': ko[-60:],
                    'en_full': en,
                    'ko_full': ko,
                    'next_en': paras[idx+1].get('en', '')[:60] if idx+1 < len(paras) else None
                })

    return issues

if __name__ == '__main__':
    books = [
        ("Two Cities", r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"),
        ("Dracula", r"C:\git_repo\Book_apps\dracula\src\main\assets\books"),
        ("Frankenstein", r"C:\git_repo\Book_apps\frankenstein\src\main\assets\books"),
        ("Secret Garden", r"C:\git_repo\Book_apps\secret_garden\src\main\assets\books"),
    ]

    all_issues = {}
    with open('bad_endings_report.txt', 'w', encoding='utf-8') as out:
        for b_name, b_path in books:
            if not os.path.exists(b_path): continue
            issues = audit_book_bad_endings(b_name, b_path)
            all_issues[b_name] = issues
            out.write(f"\n{'='*70}\nBOOK: {b_name} - Found {len(issues)} potential boundary issues\n{'='*70}\n")
            for i, iss in enumerate(issues, 1):
                out.write(f"\n[{i}] {iss['ch']} ID {iss['id']} ({iss['tag']}) - Type: {iss['type']}\n")
                out.write(f"    Current EN end: ...{iss['en_tail']}\n")
                out.write(f"    Current KO end: ...{iss['ko_tail']}\n")
                if iss['next_en']:
                    out.write(f"    Next EN start : {iss['next_en']}...\n")

    print("Bad endings audit finished. Report written to bad_endings_report.txt")
    for b_name, issues in all_issues.items():
        print(f"{b_name:15}: {len(issues)} issues found")

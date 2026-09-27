import json
import glob
import os
import re

def split_sents(text):
    abbr = r'(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|Mt|Capt|Col|Gen|Lieut|Sgt|Rev|No|Vol|etc)\.'
    masked = re.sub(abbr, lambda m: m.group(0).replace('.', '@DOT@'), text, flags=re.IGNORECASE)
    masked = re.sub(r'(\d+)\.(\d+)', r'\1@DOT@\2', masked)
    parts = re.split(r'([\.!\?]+(?:\s+|$))', masked)
    sents = []
    for i in range(0, len(parts)-1, 2):
        s = (parts[i] + parts[i+1]).strip()
        if s:
            sents.append(s.replace('@DOT@', '.'))
    if len(parts) % 2 == 1 and parts[-1].strip():
        sents.append(parts[-1].strip().replace('@DOT@', '.'))
    return sents

def audit_book(name, assets_dir):
    files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))
    if not files:
        return None

    total_paras = 0
    brackets = {
        "500+ chars (Very Long)": [],
        "400-499 chars (Long)": [],
        "350-399 chars (Moderate-Long)": [],
        "300-349 chars (Moderate)": [],
        "200-299 chars (Bite-sized)": [],
        "< 200 chars (Short)": [],
    }
    multi_sentence = [] # 4+ sentences

    all_paras = []

    for fpath in files:
        ch = os.path.basename(fpath)
        with open(fpath, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                continue

        for p in data:
            if p.get('is_header'):
                continue
            total_paras += 1
            en = p.get('en', '').strip()
            ko = p.get('ko', '').strip()
            en_s = split_sents(en)
            chars = len(en)
            words = len(en.split())

            item = {
                'ch': ch,
                'id': p.get('id'),
                'tag': p.get('tag', ''),
                'sents': len(en_s),
                'words': words,
                'chars': chars,
                'ko_chars': len(ko),
                'en': en,
                'ko': ko
            }
            all_paras.append(item)

            if chars >= 500:
                brackets["500+ chars (Very Long)"].append(item)
            elif chars >= 400:
                brackets["400-499 chars (Long)"].append(item)
            elif chars >= 350:
                brackets["350-399 chars (Moderate-Long)"].append(item)
            elif chars >= 300:
                brackets["300-349 chars (Moderate)"].append(item)
            elif chars >= 200:
                brackets["200-299 chars (Bite-sized)"].append(item)
            else:
                brackets["< 200 chars (Short)"].append(item)

            if len(en_s) >= 4:
                multi_sentence.append(item)

    all_paras.sort(key=lambda x: x['chars'], reverse=True)

    return {
        'name': name,
        'total': total_paras,
        'chapters': len(files),
        'brackets': brackets,
        'multi_sentence': multi_sentence,
        'top_10': all_paras[:10]
    }

if __name__ == '__main__':
    books = [
        ("Two Cities", r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"),
        ("Dracula", r"C:\git_repo\Book_apps\dracula\src\main\assets\books"),
        ("Frankenstein", r"C:\git_repo\Book_apps\frankenstein\src\main\assets\books"),
        ("Secret Garden", r"C:\git_repo\Book_apps\secret_garden\src\main\assets\books"),
    ]

    with open('full_audit_report.txt', 'w', encoding='utf-8') as out:
        for name, path in books:
            if not os.path.exists(path):
                continue
            res = audit_book(name, path)
            if not res:
                continue

            header = f"\n{'='*70}\nBOOK AUDIT: {res['name']} ({res['chapters']} chapters, {res['total']} paragraphs)\n{'='*70}\n"
            out.write(header)
            out.write("--- Character Length Distribution ---\n")
            for b_name, items in res['brackets'].items():
                pct = len(items) / res['total'] * 100 if res['total'] else 0
                out.write(f"  {b_name:32}: {len(items):4d} ({pct:5.1f}%)\n")

            pct_multi = len(res['multi_sentence']) / res['total'] * 100 if res['total'] else 0
            out.write(f"\n--- Sentence Count Distribution ---\n")
            out.write(f"  Paragraphs with 4+ sentences    : {len(res['multi_sentence']):4d} ({pct_multi:5.1f}%)\n")

            out.write(f"\n--- TOP 10 LONGEST PARAGRAPHS ---\n")
            for i, p in enumerate(res['top_10'], 1):
                out.write(f"\n[{i}] {p['ch']} ID {p['id']} (Tag: {p['tag']})\n")
                out.write(f"    Length: {p['chars']} EN chars ({p['words']} words), {p['ko_chars']} KO chars, {p['sents']} sentences\n")
                out.write(f"    EN: \"{p['en']}\"\n")
                out.write(f"    KO: \"{p['ko']}\"\n")

    print("Full audit report written to full_audit_report.txt")

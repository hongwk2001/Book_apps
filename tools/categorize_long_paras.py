import json
import glob
import re
import os

def split_sentences_en(text):
    abbr = r'(?:Mr|Mrs|Ms|Dr|Prof|Sr|Jr|St|Mt|Capt|Col|Gen|Lieut|Sgt|Rev|No|Vol|etc)\.'
    text_masked = re.sub(abbr, lambda m: m.group(0).replace('.', '@DOT@'), text, flags=re.IGNORECASE)
    text_masked = re.sub(r'(\d+)\.(\d+)', r'\1@DOT@\2', text_masked)
    raw = [s.strip() for s in re.split(r'[\.!\?]+(?:\s+|$)', text_masked) if s.strip()]
    return [s.replace('@DOT@', '.') for s in raw]

def split_sentences_ko(text):
    raw = [s.strip() for s in re.split(r'[\.!\?]+(?:\s+|$)', text) if s.strip()]
    return raw

assets_dir = r'C:\git_repo\Book_apps\two_cities\src\main\assets\books'
files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))

same_count = []
diff_count = []
single_huge = []

for fpath in files:
    ch = os.path.basename(fpath)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    for p in data:
        if p.get('is_header'): continue
        en = p.get('en', '').strip()
        ko = p.get('ko', '').strip()
        en_s = split_sentences_en(en)
        ko_s = split_sentences_ko(ko)
        
        if len(en) < 500 and len(en_s) < 6:
            continue
        
        info = {
            'ch': ch, 'id': p['id'], 'tag': p.get('tag', ''),
            'en_count': len(en_s), 'ko_count': len(ko_s),
            'chars': len(en),
            'max_en': max(len(s) for s in en_s) if en_s else 0
        }
        
        if len(en_s) <= 2 and len(en) >= 500:
            single_huge.append(info)
        elif len(en_s) == len(ko_s):
            same_count.append(info)
        else:
            diff_count.append(info)

total = len(same_count) + len(diff_count) + len(single_huge)
print(f"Total extreme paragraphs analyzed in Two Cities: {total}")

print(f"\n--- Category 1: Symmetric Sentences (EN == KO count) [{len(same_count)} paragraphs] ---")
print("  These can be safely split on verified 1-to-1 sentence boundaries!")
for x in same_count:
    print(f"  * {x['ch']} ID {x['id']:3d} ({x['tag']}): {x['en_count']} EN sent == {x['ko_count']} KO sent ({x['chars']} chars)")

print(f"\n--- Category 2: Asymmetric Sentences (EN count != KO count) [{len(diff_count)} paragraphs] ---")
print("  Korean was translated into more/fewer sentences than English.")
for x in diff_count:
    print(f"  * {x['ch']} ID {x['id']:3d} ({x['tag']}): {x['en_count']} EN sent vs {x['ko_count']} KO sent ({x['chars']} chars)")

print(f"\n--- Category 3: Author Long Run-on Sentences (Dickens style) [{len(single_huge)} paragraphs] ---")
print("  Only 1-2 grammatical sentences, but 500-650+ characters long!")
for x in single_huge:
    print(f"  * {x['ch']} ID {x['id']:3d} ({x['tag']}): {x['en_count']} EN sent (max single sent = {x['max_en']} chars, total {x['chars']} chars)")

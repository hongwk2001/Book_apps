import json
import glob
import re
import os

def analyze_book(name, assets_dir):
    files = sorted(glob.glob(os.path.join(assets_dir, 'ch_*.json')))
    if not files:
        print(f"No files found in {assets_dir}")
        return

    print(f"\n==========================================")
    print(f"Book: {name} ({len(files)} chapters)")
    print(f"==========================================")

    total_paras = 0
    bracket_counts = {
        "1-2 sentences (Bite-sized)": 0,
        "3 sentences (Moderate)": 0,
        "4-5 sentences (Long)": 0,
        "6+ sentences (Very Long)": 0,
    }
    
    char_brackets = {
        "< 150 chars": 0,
        "150 - 300 chars": 0,
        "300 - 500 chars (Long)": 0,
        "500+ chars (Very Long)": 0,
    }

    very_long = []

    for fpath in files:
        ch_name = os.path.basename(fpath)
        with open(fpath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"Error loading {fpath}: {e}")
                continue

        for p in data:
            if p.get('is_header'):
                continue
            total_paras += 1
            en = p.get('en', '').strip()
            ko = p.get('ko', '').strip()
            
            # Sentence counting: split by sentence end punctuation
            sentences = [s.strip() for s in re.split(r'[\.!\?]+(?:\s+|$)', en) if s.strip()]
            num_sent = len(sentences)
            num_chars = len(en)
            num_words = len(en.split())

            if num_sent <= 2:
                bracket_counts["1-2 sentences (Bite-sized)"] += 1
            elif num_sent == 3:
                bracket_counts["3 sentences (Moderate)"] += 1
            elif 4 <= num_sent <= 5:
                bracket_counts["4-5 sentences (Long)"] += 1
            else:
                bracket_counts["6+ sentences (Very Long)"] += 1

            if num_chars < 150:
                char_brackets["< 150 chars"] += 1
            elif num_chars <= 300:
                char_brackets["150 - 300 chars"] += 1
            elif num_chars <= 500:
                char_brackets["300 - 500 chars (Long)"] += 1
            else:
                char_brackets["500+ chars (Very Long)"] += 1

            if num_chars >= 400 or num_sent >= 5:
                very_long.append({
                    'chapter': ch_name,
                    'id': p.get('id'),
                    'tag': p.get('tag', ''),
                    'sentences': num_sent,
                    'words': num_words,
                    'chars': num_chars,
                    'preview': en[:90] + '...' if len(en) > 90 else en
                })

    print(f"Total Content Paragraphs: {total_paras}\n")
    print("--- By Sentence Count ---")
    for k, v in bracket_counts.items():
        pct = (v / total_paras * 100) if total_paras else 0
        print(f"  {k:28}: {v:4d} ({pct:5.1f}%)")

    print("\n--- By Character Count (EN) ---")
    for k, v in char_brackets.items():
        pct = (v / total_paras * 100) if total_paras else 0
        print(f"  {k:28}: {v:4d} ({pct:5.1f}%)")

    print(f"\nTotal Flagged Paragraphs (>=400 chars or >=5 sentences): {len(very_long)} ({len(very_long)/total_paras*100:.1f}%)")

    extreme = [x for x in very_long if x['sentences'] >= 6 or x['chars'] >= 500]
    print(f"\nExtreme Paragraphs (>=6 sentences or >=500 chars): {len(extreme)}")
    extreme.sort(key=lambda x: x['chars'], reverse=True)
    for idx, item in enumerate(extreme, 1):
        print(f"  {idx:2d}. [{item['chapter']} id={item['id']} tag={item['tag']}] {item['sentences']} sent, {item['words']} words, {item['chars']} chars")
        print(f"      Preview: \"{item['preview']}\"")

if __name__ == '__main__':
    books = [
        ("Two Cities", r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"),
        ("Dracula", r"C:\git_repo\Book_apps\dracula\src\main\assets\books"),
        ("Frankenstein", r"C:\git_repo\Book_apps\frankenstein\src\main\assets\books"),
        ("Secret Garden", r"C:\git_repo\Book_apps\secret_garden\src\main\assets\books"),
    ]
    for name, path in books:
        if os.path.exists(path):
            analyze_book(name, path)

import json

src_file = r'C:\git_repo\TKprof_book\books\dracula\scripts\bilingual_ch_01.json'
with open(src_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

grouped = {}
for item in data:
    tag = item.get('tag')
    lang = item.get('lang')
    text = item.get('text')
    if tag not in grouped:
        grouped[tag] = {}
    grouped[tag][lang] = text

out_data = []
pid = 1
for tag, langs in grouped.items():
    is_header = False
    en_text = langs.get('en', '')
    if tag == 'P001' and en_text.lower().startswith('chapter'):
        is_header = True
        
    out_data.append({
        'id': pid,
        'en': en_text,
        'ko': langs.get('ko', ''),
        'is_header': is_header
    })
    pid += 1

with open('test_out.json', 'w', encoding='utf-8') as f:
    json.dump(out_data[:3], f, ensure_ascii=False, indent=2)

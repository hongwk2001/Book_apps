import json
import os

def normalize_text(text: str) -> str:
    return " ".join(text.replace('\r', '').replace('\n', ' ').split())

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

SPLIT_SPECS = [
    # ch_file, tag, en_split, ko_split
    ('ch_39.json', 'P090', 'corrupt priests. ', '어두운 교회 탑들을 보았다. '),
    ('ch_28.json', 'P028_1', 'watch him struggle. ', '뒤로 물러섰다. '),
    ('ch_27.json', 'P075_2', 'while cutting it. ', '신발 위로 말이다. '),
    ('ch_28.json', 'P021_12', 'can grow from him! ', '그에게서 풀이 자라게 하라! '),
    ('ch_05.json', 'P003_4', "into babies' mouths. ", '짜 넣어주기도 했다. '),
    ('ch_09.json', 'P072_2', 'defense counsel. ', '영향을 살폈다. '),
    ('ch_05.json', 'P004_5', 'walked back down to their rooms. ', '걸어 내려갔다. '),
    ('ch_05.json', 'P007_2', 'most especially poverty. ', '빈곤이 그러했다. '),
    ('ch_27.json', 'P043_3', 'rattling like a furious sea. ', '덜컥거렸습니다. '),
    ('ch_04.json', 'P008_2', 'walked past on his way to breakfast. ', '아침 식사를 하러 지나갔다. '),
    ('ch_31.json', 'P003_3', 'names on custom lists. ', '세관 명단에서 이름을 찾았다. '),
    ('ch_31.json', 'P111_1', 'mixed with shouting voices. ', '둔탁한 북소리처럼 들렸다. ')
]

print("=== DRY RUN VERIFICATION OF 12 CANDIDATES ===")
for ch_file, tag, en_s, ko_s in SPLIT_SPECS:
    fpath = os.path.join(assets_dir, ch_file)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    p = [x for x in data if x.get('tag') == tag][0]

    assert en_s in p['en'], f"EN anchor '{en_s}' not in {ch_file} ({tag})!"
    assert ko_s in p['ko'], f"KO anchor '{ko_s}' not in {ch_file} ({tag})!"

    en_p1, en_p2 = p['en'].split(en_s, 1)
    c1_en = (en_p1 + en_s).strip()
    c2_en = en_p2.strip()

    ko_p1, ko_p2 = p['ko'].split(ko_s, 1)
    c1_ko = (ko_p1 + ko_s).strip()
    c2_ko = ko_p2.strip()

    assert normalize_text(c1_en + " " + c2_en) == normalize_text(p['en'])
    assert normalize_text(c1_ko + " " + c2_ko) == normalize_text(p['ko'])

    print(f"PASS: {ch_file} ({tag}) -> Chunk 1: {len(c1_en)} ch, Chunk 2: {len(c2_en)} ch. 100% Invariant OK.")

print("\nALL 12 SPLITS 100% INVARIANT VERIFIED!")

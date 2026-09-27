import json
import os

def normalize_text(text: str) -> str:
    return " ".join(text.replace('\r', '').replace('\n', ' ').split())

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

# Define exact split anchors for Category 2 & Category 3A:
ANCHOR_SPLITS = {
    # ── Category 2: Asymmetric Sentences ──────────────────────────────────
    ('ch_02.json', 18): {
        'en_split': "The only person who wasn't suspicious was the coachman. ",
        'ko_split': "유일하게 의심하지 않은 사람은 마부였습니다. "
    },
    ('ch_03.json', 61): {
        'en_split': "snapping him back to reality. ",
        'ko_split': "현실로 끌어올릴 때까지. "
    },
    ('ch_13.json', 38): {
        'en_split': "pushed back into the Center through fasting and spiritual visions. ",
        'ko_split': "중심부로 다시 밀어 넣어야 한다고 주장했다. "
    },
    ('ch_40.json', 114): {
        'en_split': "keep a single tame bird of our own. ",
        'ko_split': "단 한 마리의 새도 기를 수 없었습니다. "
    },

    # ── Category 3A: 2-Sentence Mega Paragraphs ───────────────────────────
    ('ch_27.json', 30): {
        'en_split': 'marriage picnic, Darnay!" ',
        'ko_split': '다네이!"라고 했다. '
    },
    ('ch_27.json', 31): {
        'en_split': 'kept him from being caught. ',
        'ko_split': "맞받아친 빼어난 술수들에 대해 열변을 토하곤 했다. "
    },
    ('ch_28.json', 39): {
        'en_split': "came pouring down into the streets; but the women were a sight to chill the bravest heart. ",
        'ko_split': "가장 용감한 사람의 간담도 서늘하게 할 정도였다. "
    },
    ('ch_40.json', 7): {
        'en_split': "when a carriage approached rapidly behind me. ",
        'ko_split': "그때 뒤쪽에서 마차 한 대가 아주 빠른 속도로 달려왔다. "
    }
}

print("=== TESTING SUBSTRING ANCHOR SPLITS ===")
for (ch_file, pid), anchors in ANCHOR_SPLITS.items():
    fpath = os.path.join(assets_dir, ch_file)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    p = [x for x in data if x.get('id') == pid][0]
    
    en_split_at = anchors['en_split']
    ko_split_at = anchors['ko_split']
    
    assert en_split_at in p['en'], f"EN anchor not found in {ch_file} ID {pid}!"
    assert ko_split_at in p['ko'], f"KO anchor not found in {ch_file} ID {pid}!"
    
    en_p1, en_p2 = p['en'].split(en_split_at, 1)
    chunk1_en = (en_p1 + en_split_at).strip()
    chunk2_en = en_p2.strip()
    
    ko_p1, ko_p2 = p['ko'].split(ko_split_at, 1)
    chunk1_ko = (ko_p1 + ko_split_at).strip()
    chunk2_ko = ko_p2.strip()
    
    # Assert character conservation invariant
    assert normalize_text(chunk1_en + " " + chunk2_en) == normalize_text(p['en'])
    assert normalize_text(chunk1_ko + " " + chunk2_ko) == normalize_text(p['ko'])
    
    print(f"PASS: {ch_file} ID {pid:3d} ({p.get('tag')}) -> Chunk 1 ({len(chunk1_en)} ch), Chunk 2 ({len(chunk2_en)} ch). Invariant 100% OK.")

print("\nALL 8 TARGET PARAGRAPHS PASSED THE SUBSTRING ANCHOR INVARIANT TEST!")

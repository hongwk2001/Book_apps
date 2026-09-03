import json
import os
import shutil
from datetime import datetime

def normalize_text(text: str) -> str:
    return " ".join(text.replace('\r', '').replace('\n', ' ').split())

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"

# Group splits by chapter file:
# ch_file -> list of (pid, en_split_anchor, ko_split_anchor, category)
CHAPTER_SPLITS = {
    'ch_02.json': [
        (18, "The only person who wasn't suspicious was the coachman. ", "유일하게 의심하지 않은 사람은 마부였습니다. ", "Category 2 (Asymmetric)")
    ],
    'ch_03.json': [
        (61, "snapping him back to reality. ", "현실로 끌어올릴 때까지. ", "Category 2 (Asymmetric)")
    ],
    'ch_13.json': [
        (38, "pushed back into the Center through fasting and spiritual visions. ", "중심부로 다시 밀어 넣어야 한다고 주장했다. ", "Category 2 (Asymmetric)")
    ],
    'ch_27.json': [
        (30, 'marriage picnic, Darnay!" ', '다네이!"라고 했다. ', "Category 3A (2-Sentence Mega)"),
        (31, 'kept him from being caught. ', "맞받아친 빼어난 술수들에 대해 열변을 토하곤 했다. ", "Category 3A (2-Sentence Mega)")
    ],
    'ch_28.json': [
        (39, "came pouring down into the streets; but the women were a sight to chill the bravest heart. ", "가장 용감한 사람의 간담도 서늘하게 할 정도였다. ", "Category 3A (2-Sentence Mega)")
    ],
    'ch_40.json': [
        (7, "when a carriage approached rapidly behind me. ", "그때 뒤쪽에서 마차 한 대가 아주 빠른 속도로 달려왔다. ", "Category 3A (2-Sentence Mega)"),
        (114, "keep a single tame bird of our own. ", "단 한 마리의 새도 기를 수 없었습니다. ", "Category 2 (Asymmetric)")
    ]
}

def execute():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_processed = 0

    for ch_file, targets in CHAPTER_SPLITS.items():
        fpath = os.path.join(assets_dir, ch_file)
        bak_path = fpath + ".bak"

        if not os.path.exists(bak_path):
            shutil.copyfile(fpath, bak_path)
            print(f"Created backup: {bak_path}")

        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)

        orig_clean_en = ''.join(p['en'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_clean_ko = ''.join(p['ko'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_count = len(data)

        # Find target items and their current indices
        target_dict = {pid: (en_a, ko_a, cat) for pid, en_a, ko_a, cat in targets}
        target_indices = []
        for idx, p in enumerate(data):
            if p.get('id') in target_dict:
                en_a, ko_a, cat = target_dict[p.get('id')]
                target_indices.append((idx, p.get('id'), en_a, ko_a, cat))

        assert len(target_indices) == len(targets), f"Could not find all targets in {ch_file}!"

        # Process in reverse order of index to prevent shifting
        target_indices.sort(key=lambda x: x[0], reverse=True)

        audit_entries = []

        for idx, pid, en_anchor, ko_anchor, category in target_indices:
            orig_p = data[idx]
            base_tag = orig_p.get('tag', f"P{pid:03d}").split('_')[0]
            raw_ref_id = orig_p.get('raw_ref_id', pid)

            assert en_anchor in orig_p['en'], f"EN anchor missing in {ch_file} ID {pid}"
            assert ko_anchor in orig_p['ko'], f"KO anchor missing in {ch_file} ID {pid}"

            en_p1, en_p2 = orig_p['en'].split(en_anchor, 1)
            chunk1_en = (en_p1 + en_anchor).strip()
            chunk2_en = en_p2.strip()

            ko_p1, ko_p2 = orig_p['ko'].split(ko_anchor, 1)
            chunk1_ko = (ko_p1 + ko_anchor).strip()
            chunk2_ko = ko_p2.strip()

            chunk1 = {
                "id": 0,
                "tag": f"{base_tag}_1",
                "en": chunk1_en,
                "ko": chunk1_ko,
                "is_header": False,
                "raw_ref_id": raw_ref_id
            }
            chunk2 = {
                "id": 0,
                "tag": f"{base_tag}_2",
                "en": chunk2_en,
                "ko": chunk2_ko,
                "is_header": False,
                "raw_ref_id": raw_ref_id
            }

            data = data[:idx] + [chunk1, chunk2] + data[idx+1:]
            total_processed += 1

            audit_entries.append({
                'pid': pid,
                'tag': orig_p.get('tag'),
                'category': category,
                'chars': len(orig_p['en']),
                'chunk1': chunk1,
                'chunk2': chunk2
            })

        # Renumber IDs sequentially
        for new_id, p in enumerate(data, 1):
            p['id'] = new_id

        # Check whole-chapter character invariant
        new_clean_en = ''.join(p['en'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        new_clean_ko = ''.join(p['ko'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)

        assert orig_clean_en == new_clean_en, f"EN character invariant failed in {ch_file}!"
        assert orig_clean_ko == new_clean_ko, f"KO character invariant failed in {ch_file}!"

        # Save JSON
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"SUCCESS {ch_file}: {orig_count} paragraphs -> {len(data)} paragraphs (IDs 1 to {len(data)}). 100% Invariant PASSED.")

        # Log audit entries
        with open(log_path, 'a', encoding='utf-8') as log_file:
            for ae in reversed(audit_entries):
                log_file.write(f"\n## Audit Entry: {timestamp}\n")
                log_file.write(f"- **Book**: Two Cities (`two_cities`)\n")
                log_file.write(f"- **File**: `{ch_file}`\n")
                log_file.write(f"- **Original Target**: ID {ae['pid']} (`{ae['tag']}`)\n")
                log_file.write(f"- **Category**: {ae['category']}\n")
                log_file.write(f"- **Reason for Split**: Paragraph was {ae['chars']} chars EN.\n")
                log_file.write(f"- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.\n")
                log_file.write(f"- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).\n")
                log_file.write(f"### Split Chunks:\n")
                log_file.write(f"#### Chunk 1 (`{ae['chunk1']['tag']}`)\n")
                log_file.write(f"- **EN**: `{ae['chunk1']['en']}`\n")
                log_file.write(f"- **KO**: `{ae['chunk1']['ko']}`\n")
                log_file.write(f"#### Chunk 2 (`{ae['chunk2']['tag']}`)\n")
                log_file.write(f"- **EN**: `{ae['chunk2']['en']}`\n")
                log_file.write(f"- **KO**: `{ae['chunk2']['ko']}`\n")
                log_file.write("\n---\n")

    print(f"\nAll {total_processed} target paragraphs in Category 2 & 3A successfully split and verified!")
    print(f"Audit log updated at: {log_path}")

if __name__ == '__main__':
    execute()

import json
import os
import shutil
from datetime import datetime

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"

CHAPTER_SPLITS = {
    'ch_04.json': [
        ('P008_2', 'walked past on his way to breakfast. ', '아침 식사를 하러 지나갔다. ', "Hotel staff watching Mr. Lorry go to breakfast")
    ],
    'ch_05.json': [
        ('P003_4', "into babies' mouths. ", '짜 넣어주기도 했다. ', "People scooping up spilled wine in Saint Antoine"),
        ('P004_5', 'walked back down to their rooms. ', '걸어 내려갔다. ', "Street returning to dark gloom after wine is gone"),
        ('P007_2', 'most especially poverty. ', '빈곤이 그러했다. ', "Cold, sickness, and poverty attendants")
    ],
    'ch_09.json': [
        ('P072_2', 'defense counsel. ', '영향을 살폈다. ', "Lucie's anxious testimony & spectator reactions")
    ],
    'ch_27.json': [
        ('P043_3', 'rattling like a furious sea. ', '덜컥거렸습니다. ', "Bastille storming & Defarge at his cannon"),
        ('P075_2', 'while cutting it. ', '신발 위로 말이다. ', "Spilled blood at City Hall & hanging the guard")
    ],
    'ch_28.json': [
        ('P021_12', 'can grow from him! ', '그에게서 풀이 자라게 하라! ', "Women screaming for the blood of Foulon"),
        ('P028_1', 'watch him struggle. ', '뒤로 물러섰다. ', "The mob dragging Foulon to the lamppost")
    ],
    'ch_31.json': [
        ('P003_3', 'names on custom lists. ', '세관 명단에서 이름을 찾았다. ', "Citizen-patriots checking travelers at town gates"),
        ('P111_1', 'mixed with shouting voices. ', '둔탁한 북소리처럼 들렸다. ', "Darnay pacing cell repeating 'Five paces by four and a half'")
    ],
    'ch_39.json': [
        ('P090', 'corrupt priests. ', '어두운 교회 탑들을 보았다. ', "Sydney Carton walking through city of death at night")
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

        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)

        orig_clean_en = ''.join(p['en'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_clean_ko = ''.join(p['ko'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_count = len(data)

        # Locate target indices by tag
        target_dict = {t[0]: (t[1], t[2], t[3]) for t in targets}
        target_indices = []
        for idx, p in enumerate(data):
            tag = p.get('tag')
            if tag in target_dict:
                en_a, ko_a, desc = target_dict[tag]
                target_indices.append((idx, tag, en_a, ko_a, desc))

        assert len(target_indices) == len(targets), f"Could not find all targets in {ch_file}!"

        # Process in reverse order of index to prevent shifting
        target_indices.sort(key=lambda x: x[0], reverse=True)

        audit_entries = []

        for idx, tag, en_anchor, ko_anchor, desc in target_indices:
            orig_p = data[idx]
            base_tag = tag.split('_')[0]
            raw_ref_id = orig_p.get('raw_ref_id', orig_p.get('id', 0))

            assert en_anchor in orig_p['en'], f"EN anchor missing in {ch_file} ({tag})"
            assert ko_anchor in orig_p['ko'], f"KO anchor missing in {ch_file} ({tag})"

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
                'orig_id': orig_p.get('id'),
                'tag': tag,
                'desc': desc,
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
                log_file.write(f"- **Original Target**: ID {ae['orig_id']} (`{ae['tag']}`)\n")
                log_file.write(f"- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)\n")
                log_file.write(f"- **Description**: {ae['desc']}\n")
                log_file.write(f"- **Reason for Split**: Paragraph was {ae['chars']} chars EN.\n")
                log_file.write(f"- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.\n")
                log_file.write(f"- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).\n")
                log_file.write(f"### Split Chunks:\n")
                log_file.write(f"#### Chunk 1 (`{ae['chunk1']['tag']}`)\n")
                log_file.write(f"- **EN**: `{ae['chunk1']['en']}`\n")
                log_file.write(f"- **KO**: `{ae['chunk1']['ko']}`\n")
                log_file.write(f"#### Chunk 2 (`{ae['chunk2']['tag']}`)\n")
                log_file.write(f"- **EN**: `{ae['chunk2']['en']}`\n")
                log_file.write(f"- **KO**: `{ae['chunk2']['ko']}`\n")
                log_file.write("\n---\n")

    print(f"\nAll {total_processed} target paragraphs in Phase 4 successfully split and verified!")
    print(f"Audit log updated at: {log_path}")

if __name__ == '__main__':
    execute()

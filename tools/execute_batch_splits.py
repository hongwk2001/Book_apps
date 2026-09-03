import json
import os
import shutil
import re
from datetime import datetime

def normalize_text(text: str) -> str:
    t = text.replace('\r', '').replace('\n', ' ').strip()
    return re.sub(r'\s+', ' ', t)

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

# Target splits grouped by chapter
CHAPTER_SPLITS = {
    'ch_04.json': [
        (149, [(1, 3), (4, 6), (7, 9)])
    ],
    'ch_05.json': [
        (19, [(1, 1), (2, 3)])
    ],
    'ch_07.json': [
        (13, [(1, 2), (3, 4)])
    ],
    'ch_09.json': [
        (12, [(1, 1), (2, 3)])
    ],
    'ch_13.json': [
        (44, [(1, 1), (2, 3)])
    ],
    'ch_21.json': [
        (178, [(1, 2), (3, 4)])
    ],
    'ch_27.json': [
        (117, [(1, 3), (4, 6)]),
        (144, [(1, 3), (4, 6)])
    ],
    'ch_31.json': [
        (200, [(1, 2), (3, 5)])
    ],
    'ch_34.json': [
        (32, [(1, 3), (4, 5), (6, 7)])
    ],
    'ch_38.json': [
        (11, [(1, 3), (4, 6)])
    ]
}

def execute_batch():
    assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
    log_path = r"C:\git_repo\Book_apps\PARAGRAPH_SPLITTING_AUDIT_LOG.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total_split_count = 0

    for ch_file, targets in CHAPTER_SPLITS.items():
        fpath = os.path.join(assets_dir, ch_file)
        bak_path = fpath + ".bak"

        # 1. Create backup if not present
        if not os.path.exists(bak_path):
            shutil.copyfile(fpath, bak_path)
            print(f"Created backup: {bak_path}")

        with open(fpath, encoding='utf-8') as f:
            data = json.load(f)

        orig_clean_en = ''.join(p['en'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_clean_ko = ''.join(p['ko'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        orig_count = len(data)

        # 2. Process targets in reverse order of appearance so indices don't shift
        # Find indices of each target id
        id_to_target = {pid: ranges for pid, ranges in targets}
        target_indices = []
        for idx, p in enumerate(data):
            if p.get('id') in id_to_target:
                target_indices.append((idx, p.get('id'), id_to_target[p.get('id')]))

        assert len(target_indices) == len(targets), f"Could not find all targets in {ch_file}!"

        # Sort reverse by index
        target_indices.sort(key=lambda x: x[0], reverse=True)

        audit_entries = []

        for idx, pid, ranges in target_indices:
            orig_p = data[idx]
            en_s = split_sents(orig_p['en'])
            ko_s = split_sents(orig_p['ko'])
            base_tag = orig_p.get('tag', f"P{pid:03d}").split('_')[0]
            raw_ref_id = orig_p.get('raw_ref_id', pid)

            new_chunks = []
            for chunk_idx, (start, end) in enumerate(ranges, 1):
                chunk_en = " ".join(en_s[start-1:end])
                chunk_ko = " ".join(ko_s[start-1:end])
                new_chunks.append({
                    "id": 0,
                    "tag": f"{base_tag}_{chunk_idx}",
                    "en": chunk_en,
                    "ko": chunk_ko,
                    "is_header": False,
                    "raw_ref_id": raw_ref_id
                })

            data = data[:idx] + new_chunks + data[idx+1:]
            total_split_count += 1

            audit_entries.append({
                'pid': pid,
                'tag': orig_p.get('tag'),
                'num_sent': len(en_s),
                'chars': len(orig_p['en']),
                'num_chunks': len(new_chunks),
                'chunks': new_chunks
            })

        # 3. Renumber all IDs sequentially from 1 to len(data)
        for new_id, p in enumerate(data, 1):
            p['id'] = new_id

        # 4. Check chapter-wide character invariant
        new_clean_en = ''.join(p['en'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)
        new_clean_ko = ''.join(p['ko'].replace(' ', '').replace('\n', '').replace('\r', '') for p in data)

        assert orig_clean_en == new_clean_en, f"EN character mismatch in {ch_file}!"
        assert orig_clean_ko == new_clean_ko, f"KO character mismatch in {ch_file}!"

        # 5. Save updated JSON
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"SUCCESS {ch_file}: {orig_count} paragraphs -> {len(data)} paragraphs (IDs 1 to {len(data)}). 100% Invariant PASSED.")

        # 6. Append to audit log
        with open(log_path, 'a', encoding='utf-8') as log_file:
            for ae in reversed(audit_entries):
                log_file.write(f"\n## Audit Entry: {timestamp}\n")
                log_file.write(f"- **Book**: Two Cities (`two_cities`)\n")
                log_file.write(f"- **File**: `{ch_file}`\n")
                log_file.write(f"- **Original Target**: ID {ae['pid']} (`{ae['tag']}`)\n")
                log_file.write(f"- **Reason for Split**: Paragraph was {ae['num_sent']} sentences ({ae['chars']} chars EN).\n")
                log_file.write(f"- **Split Strategy**: Split into {ae['num_chunks']} bite-sized chunks.\n")
                log_file.write(f"- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).\n")
                log_file.write(f"### Split Chunks:\n")
                for c_i, c in enumerate(ae['chunks'], 1):
                    log_file.write(f"#### Chunk {c_i} (`{c['tag']}`)\n")
                    log_file.write(f"- **EN**: `{c['en']}`\n")
                    log_file.write(f"- **KO**: `{c['ko']}`\n")
                log_file.write("\n---\n")

    print(f"\nAll {total_split_count} target paragraphs successfully split and verified!")
    print(f"Audit log updated at: {log_path}")

if __name__ == '__main__':
    execute_batch()

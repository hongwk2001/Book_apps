import os
import json
import math
import re

SOURCE_DIR = r"C:\git_repo\TKprof_book\books\the_heroes\json"
DEST_DIR = r"c:\git_repo\Book_apps\the_heroes\src\main\assets\books"
os.makedirs(DEST_DIR, exist_ok=True)

CHAPTER_TITLES = {
    "ch_00": {
        "en": "Preface: To My Children",
        "ko": "머리말: 아이들에게"
    },
    "ch_01": {
        "en": "Perseus - Part I: How Perseus and His Mother Came to Seriphos",
        "ko": "페르세우스 - 1부: 페르세우스와 그의 어머니가 세리포스 섬에 오다"
    },
    "ch_02": {
        "en": "Perseus - Part II: How Perseus Vowed a Rash Vow",
        "ko": "페르세우스 - 2부: 페르세우스가 경솔한 맹세를 하다"
    },
    "ch_03": {
        "en": "Perseus - Part III: How Perseus Slew the Gorgon",
        "ko": "페르세우스 - 3부: 페르세우스가 고르고를 물리치다"
    },
    "ch_04": {
        "en": "Perseus - Part IV: How Perseus Came to the Æthiops",
        "ko": "페르세우스 - 4부: 페르세우스가 에티오피아에 이르다"
    },
    "ch_05": {
        "en": "Perseus - Part V: How Perseus Came Home Again",
        "ko": "페르세우스 - 5부: 페르세우스가 고향으로 돌아오다"
    },
    "ch_06": {
        "en": "The Argonauts - Part I: How the Centaur Trained the Heroes on Pelion",
        "ko": "아르고 호 원정대 - 1부: 켄타우로스가 펠리온 산에서 영웅들을 가르치다"
    },
    "ch_07": {
        "en": "The Argonauts - Part II: How Jason Lost His Sandal in Anauros",
        "ko": "아르고 호 원정대 - 2부: 이아손이 아나우로스 강에서 샌들을 잃어버리다"
    },
    "ch_08": {
        "en": "The Argonauts - Part III: How They Built the Ship Argo in Iolcos",
        "ko": "아르고 호 원정대 - 3부: 이올코스에서 아르고 호를 건조하다"
    },
    "ch_09": {
        "en": "The Argonauts - Part IV: How the Argonauts Sailed to Colchis",
        "ko": "아르고 호 원정대 - 4부: 아르고 호 원정대가 콜키스로 향하다"
    },
    "ch_10": {
        "en": "The Argonauts - Part V: How the Argonauts Were Driven into the Unknown Sea",
        "ko": "아르고 호 원정대 - 5부: 아르고 호 원정대가 미지의 바다로 휩쓸려 가다"
    },
    "ch_11": {
        "en": "The Argonauts - Part VI: What Was the End of the Heroes",
        "ko": "아르고 호 원정대 - 6부: 영웅들의 최후는 어떠했는가"
    },
    "ch_12": {
        "en": "Theseus - Part I: How Theseus Lifted the Stone",
        "ko": "테세우스 - 1부: 테세우스가 바위를 들어 올리다"
    },
    "ch_13": {
        "en": "Theseus - Part II: How Theseus Slew the Devourers of Men",
        "ko": "테세우스 - 2부: 테세우스가 식인종들을 물리치다"
    },
    "ch_14": {
        "en": "Theseus - Part III: How Theseus Slew the Minotaur",
        "ko": "테세우스 - 3부: 테세우스가 미노타우로스를 물리치다"
    },
    "ch_15": {
        "en": "Theseus - Part IV: How Theseus Fell by His Pride",
        "ko": "테세우스 - 4부: 오만함으로 몰락한 테세우스"
    },
}

def strip_brackets(text: str) -> str:
    t = text.strip()
    if t.startswith('[') and t.endswith(']'):
        return t[1:-1].strip()
    return t

def chunk_list(items, max_chunk=3):
    n = len(items)
    if n <= max_chunk:
        return [items]
    k = math.ceil(n / max_chunk)
    base = n // k
    rem = n % k
    chunks = []
    idx = 0
    for i in range(k):
        size = base + (1 if i < rem else 0)
        chunks.append(items[idx:idx + size])
        idx += size
    return chunks

def migrate():
    files = sorted([f for f in os.listdir(SOURCE_DIR) if f.startswith("ch_") and f.endswith(".json")])
    print(f"Migrating {len(files)} chapters from {SOURCE_DIR} to {DEST_DIR}...")
    
    total_app_items = 0
    total_sentences_processed = 0

    for idx, f in enumerate(files):
        ch_num = idx + 1
        ch_key = f.replace(".json", "")
        src_path = os.path.join(SOURCE_DIR, f)
        
        with open(src_path, "r", encoding="utf-8") as in_f:
            data = json.load(in_f)
            
        app_paragraphs = []
        
        # 1. Add canonical chapter header
        title_info = CHAPTER_TITLES.get(ch_key, {
            "en": f"Chapter {ch_num}",
            "ko": f"제{ch_num}장"
        })
        app_paragraphs.append({
            "id": 1,
            "tag": f"H{ch_num:02d}",
            "en": title_info["en"],
            "ko": title_info["ko"],
            "is_header": True
        })
        
        # 2. Process items
        for item in data:
            raw_text = item.get("raw", "").strip()
            is_header = item.get("is_header", False)
            translations = item.get("translation", [])
            
            # Special case: Trailing "THE END" marker
            if raw_text.upper() == "THE END":
                app_paragraphs.append({
                    "id": len(app_paragraphs) + 1,
                    "tag": "THE_END",
                    "en": "THE END",
                    "ko": "끝",
                    "is_header": False
                })
                continue
                
            # If it's a chapter header in the source, we already added canonical header at the top
            # But if it's a greeting header like "MY DEAR CHILDREN,", we can preserve as subtitle or opening
            if is_header:
                # Check if it is a greeting like "MY DEAR CHILDREN,"
                if "DEAR CHILDREN" in raw_text.upper():
                    t_en = strip_brackets(translations[0]["en"]) if translations else "My dear children,"
                    t_ko = strip_brackets(translations[0]["kr"]) if translations else "사랑하는 나의 아이들에게,"
                    app_paragraphs.append({
                        "id": len(app_paragraphs) + 1,
                        "tag": item.get("tag", "P_GREETING"),
                        "en": t_en,
                        "ko": t_ko,
                        "is_header": True
                    })
                continue

            # Standard paragraph
            if not translations:
                continue

            total_sentences_processed += len(translations)

            if len(translations) <= 3:
                en_text = " ".join(t["en"].strip() for t in translations)
                ko_text = " ".join(t["kr"].strip() for t in translations)
                app_paragraphs.append({
                    "id": len(app_paragraphs) + 1,
                    "tag": item.get("tag", f"P{len(app_paragraphs)+1:04d}"),
                    "en": en_text,
                    "ko": ko_text,
                    "is_header": False
                })
            else:
                chunks = chunk_list(translations, max_chunk=3)
                p_tag = item.get("tag", f"P{len(app_paragraphs)+1:04d}")
                for c_idx, chunk in enumerate(chunks, 1):
                    en_text = " ".join(t["en"].strip() for t in chunk)
                    ko_text = " ".join(t["kr"].strip() for t in chunk)
                    app_paragraphs.append({
                        "id": len(app_paragraphs) + 1,
                        "tag": f"{p_tag}_{c_idx}",
                        "en": en_text,
                        "ko": ko_text,
                        "is_header": False
                    })
                    
        # Sequential renumbering
        for i, p in enumerate(app_paragraphs, 1):
            p["id"] = i
            
        out_filename = f"ch_{ch_num:02d}.json"
        out_path = os.path.join(DEST_DIR, out_filename)
        with open(out_path, "w", encoding="utf-8") as out_f:
            json.dump(app_paragraphs, out_f, ensure_ascii=False, indent=2)
            
        print(f"  [OK] Generated {out_filename} with {len(app_paragraphs)} items ({title_info['en']})")
        total_app_items += len(app_paragraphs)
        
    print(f"\nMigration complete! Generated 16 chapter files with {total_app_items} total cards.")
    print(f"Total sentence pairs processed: {total_sentences_processed}")

if __name__ == "__main__":
    migrate()

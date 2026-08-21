import json
import re

def process_file():
    input_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_7.ch3.json'
    output_file = r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_7.ch3_done.json'

    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    splits = {
        0: [],
        1: [],
        2: [
            ("she could no longer control her anxiety.", "더 이상 불안을 억누를 수 없었다."),
            ("prognosticated the worst event.", "최악의 사태를 예고했다."),
            ("prospect of your union.", "전망에 놓여 있었단다."),
            ("is it not hard to quit you all?", "어찌 가혹하지 않겠니?"),
        ],
        3: [
            ("never more to be heard.", "참으로 긴 시간이 걸린다."),
            ("and must feel?", "어찌 묘사해야 한단 말인가?"),
        ],
        4: [
            ("rush into the thick of life.", "신성모독처럼 여겨졌다."),
        ],
        5: [
            ("call her uncle and cousins.", "자신을 헌신했다."),
        ],
        6: [
            ("my fellow student, but in vain.", "설득하려 애썼지만 헛수고였다."),
        ],
        7: [],
        8: [
            ("form my own friends and be my own protector.", "스스로의 보호자가 되어야 했다."),
            ("my spirits and hopes rose.", "활력과 희망은 솟아올랐다."),
        ],
        9: [],
        10: [
            ("deeply imbued in the secrets of his science.", "자신의 학문의 비밀에 깊이 스며들어 있었다."),
        ],
        11: [
            ("exploded systems and useless names.", "기억력을 짐 지웠소."),
        ],
        12: [],
        13: [
            ("concerning them in my early years.", "설명을 한 셈이다."),
            ("contempt for the uses of modern natural philosophy.", "경멸감을 가지고 있었다."),
        ],
        14: [],
        15: [
            ("back of his head were nearly black.", "거의 검은색이었다."),
            ("many of its elementary terms.", "여러 기초 용어들을 설명했다."),
        ],
        16: [
            ("works in her hiding-places.", "어떻게 작용하는지 보여줍니다."),
        ],
        17: [],
        18: [
            ("sleep came.", "수면이 찾아왔다."),
            ("paid M. Waldman a visit.", "발트만 씨를 방문했다."),
            ("contempt that M. Krempe had exhibited.", "크렘페 씨가 보였던 경멸은 없었다."),
            ("solid advantage of mankind.”", "실패하는 법이 거의 없습니다.\""),
        ],
        19: [
            ("neglected the other branches of science.", "소홀히 하지 않았습니다."),
        ],
        20: [],
        21: []
    }

    output_data = []

    for item in data:
        item_id = item['id']
        tag = item['tag']
        en_text = item['en']
        ko_text = item['ko']

        chunks = []
        chunk_idx = 1
        
        for en_end, ko_end in splits.get(item_id, []):
            # Create regex patterns replacing spaces with \s+
            en_pattern = re.escape(en_end).replace(r'\ ', r'\s+')
            match_en = re.search(en_pattern, en_text)
            if not match_en:
                print(f"Warning: could not find '{en_end}' in item {item_id} (en)")
                break
            en_split_pos = match_en.end()
            en_chunk = en_text[:en_split_pos].strip()
            en_text = en_text[en_split_pos:].strip()

            ko_pattern = re.escape(ko_end).replace(r'\ ', r'\s+')
            match_ko = re.search(ko_pattern, ko_text)
            if not match_ko:
                print(f"Warning: could not find '{ko_end}' in item {item_id} (ko)")
                break
            ko_split_pos = match_ko.end()
            ko_chunk = ko_text[:ko_split_pos].strip()
            ko_text = ko_text[ko_split_pos:].strip()

            chunks.append({
                "tag": f"{tag}-{chunk_idx}",
                "en": en_chunk,
                "ko": ko_chunk
            })
            chunk_idx += 1

        if en_text or ko_text:
            chunks.append({
                "tag": f"{tag}-{chunk_idx}",
                "en": en_text,
                "ko": ko_text
            })

        output_data.append({
            "original_id": item_id,
            "chunks": chunks
        })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully processed {len(data)} items and wrote to {output_file}")

if __name__ == '__main__':
    process_file()

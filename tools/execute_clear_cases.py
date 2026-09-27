import json
import os

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

# 1. ch_09.json: Replace ID 20 & 21 with 2 clean chunks
fpath_09 = os.path.join(assets_dir, 'ch_09.json')
with open(fpath_09, encoding='utf-8') as f:
    data_09 = json.load(f)

for idx, p in enumerate(data_09):
    if p['id'] == 20:
        chunk1 = {
            "id": 20,
            "tag": "P003_1",
            "en": "The Solicitor General then questioned the witness, John Barsad. His testimony perfectly matched the Attorney General's description, perhaps a little too perfectly.",
            "ko": "그런 다음 법무차관이 증인 존 바사드를 심문했습니다. 그의 증언은 법무장관의 묘사와 완벽하게, 어쩌면 너무 완벽하게 일치했습니다.",
            "is_header": False,
            "raw_ref_id": 20
        }
        chunk2 = {
            "id": 21,
            "tag": "P003_2",
            "en": "After sharing his story, he prepared to leave. But the defense lawyer sitting near Mr. Lorry stopped him for cross-examination. The other lawyer opposite just kept staring at the ceiling.",
            "ko": "자신의 이야기를 나눈 후, 그는 떠날 준비를 했습니다. 그러나 로리 씨 근처에 앉아 있던 변호인이 반대 심문을 위해 그를 멈춰 세웠습니다. 맞은편에 있는 다른 변호사는 계속 천장만 쳐다보고 있었습니다.",
            "is_header": False,
            "raw_ref_id": 20
        }
        data_09[idx] = chunk1
        data_09[idx+1] = chunk2
        print("ch_09: Replaced ID 20 & 21 with clean chunks.")
        break

for new_id, p in enumerate(data_09, 1):
    p['id'] = new_id

with open(fpath_09, 'w', encoding='utf-8') as f:
    json.dump(data_09, f, ensure_ascii=False, indent=2)

# 2. ch_18.json: Fix ID 22
fpath_18 = os.path.join(assets_dir, 'ch_18.json')
with open(fpath_18, encoding='utf-8') as f:
    data_18 = json.load(f)

for p in data_18:
    if p['id'] == 22 and p['en'].endswith('asked Mr.'):
        p['en'] = '"Can I do anything for you, Mr. Stryver?" asked Mr. Lorry.'
        p['ko'] = '"무엇을 도와드릴까요, 스트라이버 씨?" 로리 씨가 물었다.'
        print("ch_18: Fixed ID 22.")
        break

with open(fpath_18, 'w', encoding='utf-8') as f:
    json.dump(data_18, f, ensure_ascii=False, indent=2)

# 3. ch_07.json: Fix ID 33 and insert new paragraph for the joke
fpath_07 = os.path.join(assets_dir, 'ch_07.json')
with open(fpath_07, encoding='utf-8') as f:
    data_07 = json.load(f)

for idx, p in enumerate(data_07):
    if p['id'] == 33 and '(Mr.' in p['en']:
        p['en'] = 'The scene was Mr. Cruncher’s private lodging in Hanging-sword Alley, Whitefriars; the time, half-past seven on a windy March morning, in the year of our Lord 1780.'
        p['ko'] = '배경은 화이트프라이어스의 행잉소드 골목에 위치한 크런처 씨의 사적인 거처였다. 때는 서기 1780년, 바람 부는 3월 어느 날 아침 7시 반이었다.'
        
        joke_para = {
            "id": 0,
            "tag": "P009_2",
            "en": "(Mr. Cruncher himself always spoke of the year of our Lord as Anna Dominoes: apparently under the impression that the Christian era dated from the invention of a popular game, by a lady who had bestowed her name upon it.)",
            "ko": "(크런처 씨 자신은 ‘서기’라는 말을 늘 ‘안나 도미노’라고 불렀는데, 이는 분명 서기 연호가 그 이름을 가진 어떤 귀부인이 발명한 인기 보드게임에서 비롯된 것이라 생각했기 때문인 듯했다.)",
            "is_header": False,
            "raw_ref_id": p.get('raw_ref_id', 33)
        }
        data_07.insert(idx + 1, joke_para)
        print("ch_07: Fixed ID 33 and added Anna Dominoes joke as new paragraph.")
        break

for new_id, p in enumerate(data_07, 1):
    p['id'] = new_id

with open(fpath_07, 'w', encoding='utf-8') as f:
    json.dump(data_07, f, ensure_ascii=False, indent=2)

print("\nClear cases executed successfully!")

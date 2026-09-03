import json
import os
import shutil

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

# 1. ch_25.json: Merge ID 116 into 117
fpath_25 = os.path.join(assets_dir, 'ch_25.json')
with open(fpath_25, encoding='utf-8') as f:
    data_25 = json.load(f)

for idx, p in enumerate(data_25):
    if p['id'] == 116 and p['en'] == '"But," Mr.':
        next_p = data_25[idx+1]
        next_p['en'] = '"But," Mr. Lorry said, "as a practical man who deals only with money and concrete things, wouldn\'t keeping the tools keep the memory alive?"'
        next_p['ko'] = '하지만, 로리 씨가 말했습니다. 오직 돈과 구체적인 것들만 다루는 실용적인 사람의 입장에서, 그 도구들을 간직하는 것이 기억을 살아있게 하지 않을까요?'
        data_25.pop(idx)
        print("ch_25: Merged ID 116 into 117")
        break

for new_id, p in enumerate(data_25, 1):
    p['id'] = new_id

with open(fpath_25, 'w', encoding='utf-8') as f:
    json.dump(data_25, f, ensure_ascii=False, indent=2)

# 2. ch_38.json: Merge ID 51 into 52
fpath_38 = os.path.join(assets_dir, 'ch_38.json')
with open(fpath_38, encoding='utf-8') as f:
    data_38 = json.load(f)

for idx, p in enumerate(data_38):
    if p['id'] == 51 and 'when Mr.' in p['en']:
        next_p = data_38[idx+1]
        next_p['en'] = 'As if their estrangement were her fault, when Mr. Lorry knew for a fact years ago in London that this worthless brother had stolen all her savings and abandoned her!'
        next_p['ko'] = '마치 둘 사이가 멀어진 것이 그녀의 잘못인 것처럼 행동하다니, 로리 씨는 이미 수년 전 런던에서 이 쓸모없는 오빠가 그녀의 전 재산을 훔쳐서 그녀를 버렸다는 사실을 알고 있었는데도 말이다!'
        data_38.pop(idx)
        print("ch_38: Merged ID 51 into 52")
        break

for new_id, p in enumerate(data_38, 1):
    p['id'] = new_id

with open(fpath_38, 'w', encoding='utf-8') as f:
    json.dump(data_38, f, ensure_ascii=False, indent=2)

# 3. ch_18.json: Fix IDs 30, 35, 57, 76
fpath_18 = os.path.join(assets_dir, 'ch_18.json')
with open(fpath_18, encoding='utf-8') as f:
    data_18 = json.load(f)

for p in data_18:
    if p['id'] == 30 and p['en'].endswith('Mr.'):
        p['en'] = '"But—really, you know, Mr. Stryver—" Mr. Lorry began.'
        p['ko'] = '"하지만—정말이지, 스트라이버 씨—" 로리 씨가 말을 꺼냈다.'
        print("ch_18: Fixed ID 30")
    elif p['id'] == 35 and p['en'].endswith('Mr.'):
        p['en'] = 'You are a good match," Mr. Stryver insisted.'
        p['ko'] = '당신은 좋은 짝입니다," 스트라이버 씨가 주장했다.'
        print("ch_18: Fixed ID 35")
    elif p['id'] == 57 and p['en'].endswith('said Mr.'):
        p['en'] = '“I mean to tell you, Mr. Stryver,” said Mr. Lorry.'
        p['ko'] = '“내가 당신에게 하려는 말은 이겁니다, 스트라이버 씨,” 로리 씨가 말했다.'
        print("ch_18: Fixed ID 57")
    elif p['id'] == 76 and p['en'].endswith('said Mr.'):
        p['en'] = '“What I suppose, Mr. Stryver, I claim the right to describe for myself—and understand me, sir,” said Mr. Lorry.'
        p['ko'] = '“내가 추측하는 것은, 스트라이버 씨, 내 스스로 규정할 권리가 있습니다—그리고 내 말을 분명히 알아들으십시오, 선생,” 로리 씨가 말했다.'
        print("ch_18: Fixed ID 76")

with open(fpath_18, 'w', encoding='utf-8') as f:
    json.dump(data_18, f, ensure_ascii=False, indent=2)

# 4. ch_39.json: Fix ID 25
fpath_39 = os.path.join(assets_dir, 'ch_39.json')
with open(fpath_39, encoding='utf-8') as f:
    data_39 = json.load(f)

for p in data_39:
    if p['id'] == 25 and p['en'].endswith('said Mr.'):
        p['en'] = 'That, Mr. Lorry,” said Mr. Cruncher.'
        p['ko'] = '그것이 바로, 로리 나으리,” 크런처 씨가 말했다.'
        print("ch_39: Fixed ID 25")
        break

with open(fpath_39, 'w', encoding='utf-8') as f:
    json.dump(data_39, f, ensure_ascii=False, indent=2)

# 5. ch_44.json: Fix IDs 104 and 218
fpath_44 = os.path.join(assets_dir, 'ch_44.json')
with open(fpath_44, encoding='utf-8') as f:
    data_44 = json.load(f)

for p in data_44:
    if p['id'] == 104 and p['en'].endswith('Mrs.'):
        p['en'] = '“I will even go so far as to say, miss, furthermore,” continued Mr. Cruncher, with a most alarming tendency to preach as if from a pulpit—“and let my words be written down and delivered to Mrs. Cruncher.'
        p['ko'] = '“게다가 아가씨, 전 이렇게까지 말씀드리겠습니다,” 크런처 씨는 마치 설교단에서 설교하듯 몹시 불안한 기세로 말을 이었다. “—그리고 제 말을 받아적어 크런처 부인에게 전해 주십시오.'
        print("ch_44: Fixed ID 104")
    elif p['id'] == 218 and p['en'].endswith('thought Mr.'):
        p['en'] = '“I can’t hear you,” said Miss Pross. “What are you saying?” It was pointless for Mr. Cruncher to repeat what he had said; Miss Pross couldn’t hear him. ‘So I’ll nod my head,’ thought Mr. Cruncher.'
        p['ko'] = '“당신 말이 안 들려요.” 프로스 양이 말했다. “뭐라고 하는 건가요?” 크런처 씨가 했던 말을 되풀이해 보았지만 아무 소용이 없었다. 프로스 양은 그의 말이 들리지 않았다. ‘그러니 고개나 끄덕여야겠군,’ 하고 크런처 씨는 생각했다.'
        print("ch_44: Fixed ID 218")

with open(fpath_44, 'w', encoding='utf-8') as f:
    json.dump(data_44, f, ensure_ascii=False, indent=2)

# 6. ch_10.json: Fix ID 2
fpath_10 = os.path.join(assets_dir, 'ch_10.json')
with open(fpath_10, encoding='utf-8') as f:
    data_10 = json.load(f)

for p in data_10:
    if p['id'] == 2 and p['en'].endswith('counsel, Mr.'):
        p['en'] = 'From the dimly lit corridors of the courthouse, the last remnants of the human crowd that had been seething there all day were draining away, when Doctor Manette, his daughter Lucie Manette, Mr. Lorry, the defense solicitor, and its counsel, Mr. Stryver, stood talking together.'
        p['ko'] = '하루 종일 끓어오르던 인간 군상의 마지막 찌꺼기가 법원의 어둑한 복도에서 빠져나가고 있을 때, 마네트 박사와 그의 딸 루시 마네트, 로리 씨, 피고측 사무변호사, 그리고 법정변호사인 스트라이버 씨가 모여 이야기를 나누고 있었다.'
        print("ch_10: Fixed ID 2")
        break

with open(fpath_10, 'w', encoding='utf-8') as f:
    json.dump(data_10, f, ensure_ascii=False, indent=2)

print("\nAll approved positive fixes successfully applied!")

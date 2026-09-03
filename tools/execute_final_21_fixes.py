import json
import os

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

def update_file(filename, update_fn):
    fpath = os.path.join(assets_dir, filename)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)
    data = update_fn(data)
    for new_id, p in enumerate(data, 1):
        p['id'] = new_id
    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {filename}: {len(data)} paragraphs.")

# 1. ch_08.json
def fix_ch08(data):
    for p in data:
        if p['en'].endswith('will attract Mr.'):
            p['en'] = p['en'][:-len('will attract Mr.')] + "will attract Mr. Lorry's attention."
            p['ko'] = "문지기가 로리 씨에게 쪽지를 건넬 테니, 자네는 로리 씨의 주의를 끌 만한 몸짓을 하게."
        elif p['en'].endswith('making his way toward Mr.'):
            p['en'] = p['en'][:-len('making his way toward Mr.')] + "making his way toward Mr. Lorry."
            p['ko'] = "이때 크런처 씨의 주의는 문지기에게로 쏠렸는데, 문지기가 로리 씨를 향해 다가가는 것을 보았기 때문이었다."
        elif p['en'].endswith('whose whole attention, when Mr.'):
            p['en'] = p['en'][:-len('whose whole attention, when Mr.')] + "whose whole attention, when Mr. Cruncher looked at him, was directed to the ceiling."
            p['ko'] = p['ko'].rstrip('. ') + " 그의 모든 시선은 천장을 향해 있었다."
    return data

update_file('ch_08.json', fix_ch08)

# 2. ch_09.json
def fix_ch09(data):
    for p in data:
        if p['en'] == '"Yes, he was."' and '미스터' in p['ko']:
            p['ko'] = '"네, 그렇습니다."'
        elif p['en'].endswith('were next going to try Mr.'):
            p['en'] = p['en'][:-len('were next going to try Mr.')] + "were next going to try Mr. Carton."
            p['ko'] = "재판장은 (피고인의 변호인인) 스트라이버 씨에게, 다음에는 카턴 씨를 재판할 셈인지 물었다."
        elif p['en'].endswith('and touched Mr.'):
            p['en'] = p['en'][:-len('and touched Mr.')] + "and touched Mr. Lorry on the arm."
            p['ko'] = "카턴 씨가 바로 그 순간 다가와 로리 씨의 팔을 건드렸다."
    return data

update_file('ch_09.json', fix_ch09)

# 3. ch_10.json
def fix_ch10(data):
    for p in data:
        if p['en'].endswith('and had turned to Mr.'):
            p['en'] = p['en'][:-len('and had turned to Mr.')] + "and had turned to Mr. Stryver."
            p['ko'] = "다네이 씨는 그녀의 손에 열렬하고 감사한 마음으로 입을 맞춘 뒤, 스트라이버 씨를 향해 돌아섰다."
        elif p['en'].endswith('with honor, Mr.'):
            p['en'] = p['en'][:-len('with honor, Mr.')] + 'with honor, Mr. Darnay.”'
            p['ko'] = "그는 여전히 가발과 법복을 걸친 채, 죄 없는 로리 씨를 무리 밖으로 완전히 밀어낼 정도로 이전 의뢰인을 향해 당당하게 마주 서며 말했다. “명예롭게 무죄를 이끌어내어 기쁘군요, 다네이 씨.”"
        elif p['en'].endswith('“and for Mr.'):
            p['en'] = p['en'][:-len('“and for Mr.')] + '“and for Mr. Darnay.”'
            p['ko'] = "“제 자신을 위해서도 말하지만,” 로리 씨가 대답했다. “다네이 씨를 위해서도 말입니다.”"
        elif p['en'].endswith('where Mr. Lorry and Mr.'):
            p['en'] = p['en'][:-len('where Mr. Lorry and Mr.')] + 'where Mr. Lorry and Mr. Darnay stood.'
            p['ko'] = "그는 이제 로리 씨와 다네이 씨가 서 있는 곳으로 걸어갔다."
        elif p['en'].endswith("Don't be irritated, Mr.") or p['en'].endswith('Don’t be irritated, Mr.'):
            p['en'] = p['en'][:-len('Don\'t be irritated, Mr.')].rstrip() + ' "Don\'t be irritated, Mr. Lorry."'
            p['ko'] = '"*저도* 압니다, *저도* 알아요." 칼턴 씨가 무심하게 대꾸했다. "너무 언짢아하지 마십시오, 로리 씨."'
    return data

update_file('ch_10.json', fix_ch10)

# 4. ch_12.json
def fix_ch12(data):
    for p in data:
        if p['en'].endswith('sights, and Mr.'):
            p['en'] = p['en'][:-len('sights, and Mr.')] + "sights, and Mr. Lorry was glad of it."
            p['ko'] = p['ko'].replace('미스터', '').strip() + " 로리 씨는 그것을 다행스럽게 여겼다."
        elif p['en'].endswith('"Good night, Mr.'):
            p['en'] = p['en'][:-len('"Good night, Mr.')] + '"Good night, Mr. Lorry," Carton replied.'
            p['ko'] = '"안녕히 가십시오, 카턴 씨." 은행가가 말했다. "안녕히 가십시오, 로리 씨," 카턴이 대답했다.'
    return data

update_file('ch_12.json', fix_ch12)

# 5. ch_18.json
def fix_ch18(data):
    to_remove = None
    for idx, p in enumerate(data):
        if p['en'].endswith('"How do you do, Mr.'):
            p['en'] = 'The discreet Mr. Lorry said, in the measured tone he considered appropriate for the situation, "How do you do, Mr. Stryver? How do you do, sir?" and shook hands.'
            p['ko'] = '신중한 로리 씨는 그런 상황에 걸맞은 모범적인 어조로 말했다. "안녕하십니까, 스트라이버 씨? 안녕하십니까, 선생?" 그리고 악수했다.'
            if idx + 1 < len(data) and 'How do you do, sir?' in data[idx+1]['en']:
                to_remove = idx + 1
        elif p['en'].endswith('Miss Manette, Mr.'):
            p['en'] = p['en'][:-len('Miss Manette, Mr.')] + 'Miss Manette, Mr. Lorry."'
            p['ko'] = p['ko'].replace('미스터', '로리 씨."')
        elif p['en'].endswith('late as ten o’clock, Mr.') or p['en'].endswith("late as ten o'clock, Mr."):
            p['en'] = p['en'].rstrip('. ') + " Stryver was sitting alone."
            p['ko'] = "그리하여, 그날 밤 열 시나 되어 늦게 로리 씨가 방문했을 때, 스트라이버 씨는 혼자 앉아 있었다."
        elif p['en'].endswith('quite dumbfounded at Mr.'):
            p['en'] = p['en'][:-len('quite dumbfounded at Mr.')] + "quite dumbfounded at Mr. Stryver."
            p['ko'] = "로리 씨는 너무나 어안이 벙벙하여 멍하니 스트라이버 씨를 바라보았다."
    if to_remove:
        data.pop(to_remove)
    return data

update_file('ch_18.json', fix_ch18)

# 6. ch_24.json
def fix_ch24(data):
    for p in data:
        if p['en'].endswith('when they got upstairs, Mr.'):
            p['en'] = p['en'][:-len('when they got upstairs, Mr.')] + "when they got upstairs, Mr. Lorry was deeply troubled."
            p['ko'] = p['ko'].rstrip('. ') + " 씨는 깊은 시름에 잠겼다."
    return data

update_file('ch_24.json', fix_ch24)

# 7. ch_25.json
def fix_ch25(data):
    for p in data:
        if p['en'].endswith('gradual approach that Mr.'):
            p['en'] = p['en'][:-len('gradual approach that Mr.')] + "gradual approach that Mr. Lorry had planned."
            p['ko'] = "의사는 평소대로 불려 나와 아침 식사를 하러 왔다. 로리 씨가 세운 섬세하고 점진적인 접근 방식을 벗어나지 않는 한도 내에서."
    return data

update_file('ch_25.json', fix_ch25)

# 8. ch_27.json
def fix_ch27(data):
    for p in data:
        if p['en'].endswith('sleep at the bank," Mr.'):
            p['en'] = p['en'][:-len('sleep at the bank," Mr.')] + 'sleep at the bank," Mr. Lorry said.'
            p['ko'] = '"저는 은행에서 자야 할 줄 알았습니다," 로리 씨가 말했다.'
    return data

update_file('ch_27.json', fix_ch27)

# 9. ch_30.json
def fix_ch30(data):
    for p in data:
        if p['en'].endswith('little Lucie," said Mr.'):
            p['en'] = p['en'][:-len('little Lucie," said Mr.')] + 'little Lucie," said Mr. Lorry.'
            p['ko'] = p['ko'].rstrip('. ') + " 말했다."
    return data

update_file('ch_30.json', fix_ch30)

print("\nALL 21 FIXES APPLIED SUCCESSFULLY!")

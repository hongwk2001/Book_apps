import json
import os
import shutil

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"
fpath = os.path.join(assets_dir, 'ch_30.json')

with open(fpath, encoding='utf-8') as f:
    data = json.load(f)

# The block to replace is indices 19 through 50 (32 original items)
# They will be replaced with 14 perfectly aligned, natural speaker turns (IDs 20 to 33)

replacement_turns = [
    {
        "tag": "P008_3",
        "en": "The gloomy room once used for private meetings was now packed with people exchanging news. It was about half an hour before closing time.",
        "ko": "한때 사적인 모임에 쓰이던 어둑한 방은 이제 소식을 나누는 사람들로 가득 차 있었다. 마감 시간 약 삼십 분 전이었다.",
        "is_header": False,
        "raw_ref_id": 20
    },
    {
        "tag": "P009",
        "en": "“Even though you are the most youthful-spirited man alive,” Charles Darnay said, hesitating a bit, “I still have to suggest to you, bad weather, a long journey, unreliable transport, a chaotic country, and a city that might not even be safe for you.”",
        "ko": "“선생님께서 세상에서 가장 젊고 활기찬 분이시긴 하지만,” 찰스 다네이가 약간 머뭇거리며 말했다. “그래도 궂은 날씨와 긴 여정, 신뢰할 수 없는 교통수단, 혼란에 빠진 나라, 그리고 선생님께 결코 안전하지 않을지도 모르는 도시에 대해 조언을 드려야겠습니다.”",
        "is_header": False,
        "raw_ref_id": 22
    },
    {
        "tag": "P010",
        "en": "“I understand. That I am too old?” said Mr. Lorry. \"My dear Charles,\" he said with cheerful confidence, \"you are mentioning some of the reasons for me to go, not for staying away. I will be safe enough. No one will bother an old man of nearly eighty when there are so many other people worth targeting.”",
        "ko": "“이해하네. 내가 너무 늙었다는 말인가?” 로리 씨가 말했다. \"친애하는 찰스,\" 그가 유쾌한 자신감을 보이며 말했다. \"자네가 말한 것들은 내가 가야 할 이유이지, 가지 말아야 할 이유가 아니라네. 나는 충분히 안전할 걸세. 표적으로 삼을 가치가 있는 다른 사람들이 너무나 많은데, 여든 살이 다 된 노인을 누가 괴롭히겠나.”",
        "is_header": False,
        "raw_ref_id": 24
    },
    {
        "tag": "P012",
        "en": "“As for the chaos, if the city weren't chaotic, we wouldn't need to send someone from our London office to our Paris branch who knows the place and the business, and whom Tellson's trusts completely. As for the difficult travel, the long journey, and the winter weather, if I am not willing to face a few hardships for Tellson's after all these years, who should be?”",
        "ko": "“혼란에 관해서라면, 도시가 혼란스럽지 않다면 런던 본사에서 파리 지점으로 그곳의 상황과 사업을 알고 텔슨 은행이 온전히 신뢰하는 사람을 보낼 필요가 없을 걸세. 힘든 여행, 긴 여정, 그리고 겨울 날씨에 관해서라면, 지난 세월 텔슨 은행을 위해 일한 내가 약간의 고난을 기꺼이 마주하지 않는다면 대체 누가 해야겠는가?”",
        "is_header": False,
        "raw_ref_id": 28
    },
    {
        "tag": "P013",
        "en": "“I wish I were going myself,” Charles Darnay said restlessly, as if thinking aloud.",
        "ko": "“내가 직접 갈 수 있다면 좋을 텐데,” 찰스 다네이는 마치 혼잣말을 하듯 불안하게 말했다.",
        "is_header": False,
        "raw_ref_id": 30
    },
    {
        "tag": "P014",
        "en": "“Really! You are a fine one to object and give advice!” exclaimed Mr. Lorry. \"Do you wish you were going yourself? A born Frenchman? You are a very wise adviser indeed!”",
        "ko": "“정말인가! 반대하고 조언할 처지가 아니잖나!” 로리 씨가 외쳤다. \"자네가 직접 가고 싶기라도 한 건가? 프랑스에서 태어난 자네가? 참으로 현명한 조언자로군!”",
        "is_header": False,
        "raw_ref_id": 32
    },
    {
        "tag": "P015_1",
        "en": "\"My dear Mr. Lorry, it is because I was born a Frenchman that the thought (which I didn't mean to speak aloud here, though) has often crossed my mind. Having felt sympathy for the poor people and having given up my property to them,” he spoke thoughtfully, “I cannot help but think that they might listen to me. I might be able to persuade them to show some mercy.”",
        "ko": "\"친애하는 로리 씨, 비록 여기서 입 밖에 낼 생각은 아니었지만, 제가 태생이 프랑스인이기 때문에 그런 생각이 자주 머릿속을 스쳤던 것입니다. 가난한 사람들에게 동정심을 느껴왔고 그들에게 재산을 넘겨주었기에,” 그가 생각에 잠겨 말했다. “그들이 제 말에 귀를 기울여 줄지도 모른다는 생각을 떨칠 수가 없습니다. 자비를 베풀도록 그들을 설득할 수 있을지도 모릅니다.”",
        "is_header": False,
        "raw_ref_id": 35
    },
    {
        "tag": "P015_4",
        "en": "“Only last night, after you left, I was talking to Lucie—”",
        "ko": "“바로 어젯밤에도 선생님께서 떠나신 후 루시와 이야기를 나누었습니다만—”",
        "is_header": False,
        "raw_ref_id": 37
    },
    {
        "tag": "P016",
        "en": "\"When you were talking to Lucie,\" Mr. Lorry repeated. \"Yes. I'm surprised you're not ashamed to mention her name while wishing you were going to France at a time like this!”",
        "ko": "\"루시에게 이야기할 때라고,\" 로리 씨가 되풀이했다. \"그래. 이런 시국에 프랑스에 가고 싶다는 소리를 하면서 루시의 이름을 입에 올리는 것이 부끄럽지도 않단 말인가!”",
        "is_header": False,
        "raw_ref_id": 38
    },
    {
        "tag": "P017",
        "en": "“Well, I am not going,” Charles Darnay said with a smile. “It is more important that you are.”",
        "ko": "“글쎄요, 저는 가지 않습니다,” 찰스 다네이가 미소를 지으며 말했다. “선생님께서 가시는 것이 더 중요하니까요.”",
        "is_header": False,
        "raw_ref_id": 40
    },
    {
        "tag": "P018_1",
        "en": "“And I really am. The truth is, my dear Charles,” Mr. Lorry glanced at the distant bank partners and lowered his voice, \"you can have no conception of the difficulty with which our business is conducted, and of the peril in which our books and papers over there are involved. God only knows what terrible trouble it would cause for many people if our documents were seized or destroyed.”",
        "ko": "“그리고 나는 정말 갈 거라네. 실상은 말이네, 친애하는 찰스,” 로리 씨는 멀찍이 있는 동업자들을 흘끗 바라보고 목소리를 낮추었다. \"자네는 그곳에서 우리의 업무가 얼마나 어렵게 처리되고 있는지, 그리고 저곳에 있는 우리의 장부와 서류들이 얼마나 큰 위험에 처해 있는지 상상조차 못할 걸세. 만약 우리 서류들이 압류되거나 파기된다면 얼마나 많은 사람들에게 끔찍한 재앙이 닥칠지 신만이 아실 걸세.”",
        "is_header": False,
        "raw_ref_id": 42
    },
    {
        "tag": "P018_5",
        "en": "“Now, carefully choosing the important papers right away, and burying them or otherwise getting them out of harm's way, is something that hardly anyone but me can do without wasting precious time. Should I refuse, when Tellson's needs me, Tellson's, who has paid my salary for sixty years, just because my joints are a little stiff? Why, I'm a boy compared to half the old men working here!”",
        "ko": "“지금 지체 없이 중요한 서류들을 조심스럽게 골라내어 묻거나 달리 안전한 곳으로 옮기는 것은, 소중한 시간을 낭비하지 않고는 나 말고는 할 수 있는 사람이 거의 없는 일이네. 육십 년 동안 내게 급여를 준 텔슨 은행이 나를 필요로 할 때, 단지 내 관절이 조금 뻣뻣하다는 이유로 거절해야 한단 말인가? 뭐, 여기서 일하는 노인들 절반에 비하면 나는 어린아이나 다름없네!”",
        "is_header": False,
        "raw_ref_id": 44
    },
    {
        "tag": "P019",
        "en": "\"How I admire the gallantry of your youthful spirit, Mr. Lorry.\"",
        "ko": "\"로리 씨의 그 젊은 기백과 용기가 참으로 감탄스럽습니다.\"",
        "is_header": False,
        "raw_ref_id": 47
    },
    {
        "tag": "P020",
        "en": "\"Nonsense, sir! And, my dear Charles,\" said Mr. Lorry, glancing toward the partners again, \"you must remember that getting anything out of Paris right now, no matter what it is, is next to impossible. Just today, papers and valuables were brought to us here by the strangest messengers, who were in constant danger of losing their heads as they crossed the borders. Normally, our mail would come and go as easily as in England, but now, everything is blocked.”",
        "ko": "\"당치도 않네, 여보게! 그리고 친애하는 찰스,\" 로리 씨는 다시 동업자들을 바라보며 말했다. \"지금 당장은 그것이 무엇이든 파리 밖으로 빼내는 것이 거의 불가능에 가깝다는 점을 기억해야 하네. 바로 오늘만 해도, 국경을 넘으며 목숨을 잃을 뻔한 위험에 처했던 기묘한 전령들을 통해 서류와 귀중품들이 이곳으로 전달되었어. 평소라면 우편물이 영국에서처럼 쉽게 오갔겠지만, 지금은 모든 것이 막혀 있다네.”",
        "is_header": False,
        "raw_ref_id": 49
    }
]

# Verify slice
assert data[19]['id'] == 20
assert data[50]['id'] == 51
assert data[51]['id'] == 52

# Replace slice [19:51] with replacement_turns
data = data[:19] + replacement_turns + data[51:]

# Renumber IDs sequentially
for new_id, p in enumerate(data, 1):
    p['id'] = new_id

# Save
with open(fpath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: ch_30.json re-aligned! Total paragraphs now: {len(data)} (IDs 1 to {len(data)})")

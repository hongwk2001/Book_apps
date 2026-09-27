import json
import os

assets_dir = r"C:\git_repo\Book_apps\two_cities\src\main\assets\books"

splits = [
    # 1. ch_27.json ID 75 (Tag: P033)
    {
        "file": "ch_27.json",
        "match": lambda p: p.get("tag") == "P033" and p["en"].startswith("Just like a boiling whirlpool"),
        "tag1": "P033_1", "tag2": "P033_2",
        "en1": "Just like a boiling whirlpool has a center, all this raging chaos circled around Defarge's wine-shop.",
        "en2": "Everyone in the crowd was sucked toward the middle where Defarge himself, already covered in sweat and gunpowder, was shouting orders and handing out weapons. He pushed men back, dragged others forward, took weapons from some to give to others, and fought hard right in the middle of the madness.",
        "ko1": "끓어오르는 소용돌이에 중심이 있듯, 이 모든 격렬한 혼란은 드파르지의 와인 가게를 중심으로 돌고 있었습니다.",
        "ko2": "군중 속의 모든 사람이 한가운데로 빨려 들어갔고, 그곳에는 이미 땀과 화약으로 뒤덮인 드파르지 자신이 명령을 외치며 무기를 나눠주고 있었습니다. 그는 사람들을 뒤로 밀어내고, 다른 사람들을 앞으로 끌어당겼으며, 어떤 사람에게서 무기를 빼앗아 다른 사람에게 주기도 하며 그 광란의 한가운데서 맹렬히 싸웠습니다."
    },
    # 2. ch_30.json (Tag: P018_5)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P018_5" and p["en"].startswith("“Now, carefully choosing the important papers"),
        "tag1": "P018_5", "tag2": "P018_6",
        "en1": "“Now, carefully choosing the important papers right away, and burying them or otherwise getting them out of harm's way, is something that hardly anyone but me can do without wasting precious time.",
        "en2": "Should I refuse, when Tellson's needs me, Tellson's, who has paid my salary for sixty years, just because my joints are a little stiff? Why, I'm a boy compared to half the old men working here!”",
        "ko1": "“지금 지체 없이 중요한 서류들을 조심스럽게 골라내어 묻거나 달리 안전한 곳으로 옮기는 것은, 소중한 시간을 낭비하지 않고는 나 말고는 할 수 있는 사람이 거의 없는 일이네.",
        "ko2": "육십 년 동안 내게 급여를 준 텔슨 은행이 나를 필요로 할 때, 단지 내 관절이 조금 뻣뻣하다는 이유로 거절해야 한단 말인가? 뭐, 여기서 일하는 노인들 절반에 비하면 나는 어린아이나 다름없네!”"
    },
    # 3. ch_30.json (Tag: P018_1)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P018_1" and p["en"].startswith("“And I really am."),
        "tag1": "P018_1", "tag2": "P018_2",
        "en1": "“And I really am. The truth is, my dear Charles,” Mr. Lorry glanced at the distant bank partners and lowered his voice, \"you can have no conception of the difficulty with which our business is conducted, and of the peril in which our books and papers over there are involved.",
        "en2": "God only knows what terrible trouble it would cause for many people if our documents were seized or destroyed.”",
        "ko1": "“그리고 나는 정말 갈 거라네. 실상은 말이네, 친애하는 찰스,” 로리 씨는 멀찍이 있는 동업자들을 흘끗 바라보고 목소리를 낮추었다. \"자네는 그곳에서 우리의 업무가 얼마나 어렵게 처리되고 있는지, 그리고 저곳에 있는 우리의 장부와 서류들이 얼마나 큰 위험에 처해 있는지 상상조차 못할 걸세.",
        "ko2": "만약 우리 서류들이 압류되거나 파기된다면 얼마나 많은 사람들에게 끔찍한 재앙이 닥칠지 신만이 아실 걸세.”"
    },
    # 4. ch_30.json (Tag: P027_3)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P027_3" and p["en"].startswith("It was typical of the refugees,"),
        "tag1": "P027_3", "tag2": "P027_4",
        "en1": "It was typical of the refugees, and of the conservative English public, to talk about this terrible Revolution as if it were a disaster that had come out of nowhere, as if nothing had ever been done to cause it.",
        "en2": "They ignored the fact that anyone who had observed the starving millions in France and the greed of the rulers had seen it coming years ago and warned about it in plain words.",
        "ko1": "망명자들과 보수적인 영국 대중들이 이 끔찍한 혁명을 마치 아무 이유도 없이 갑자기 일어난 재앙인 양 이야기하는 것은 전형적인 모습이었다.",
        "ko2": "그들은 프랑스에서 굶주리는 수백만의 사람들과 지배자들의 탐욕을 관찰한 사람이라면 누구나 수년 전부터 그 사태를 예견하고 분명한 말로 경고해 왔다는 사실을 무시했다."
    },
    # 5. ch_34.json (Tag: P008_3)
    {
        "file": "ch_34.json",
        "match": lambda p: p.get("tag") == "P008_3" and p["en"].startswith("He could now tell Lucie"),
        "tag1": "P008_3", "tag2": "P008_4",
        "en1": "He could now tell Lucie that Charles was no longer in solitary confinement, but was with the other prisoners. The Doctor saw Charles every week and brought her messages directly from him.",
        "en2": "Sometimes Charles even sent letters, though never carried by the Doctor, but Lucie was not allowed to write back, because the authorities suspected that prisoners were plotting with friends abroad.",
        "ko1": "이제 그는 루시에게 찰스가 독방에 있지 않고 다른 죄수들과 함께 있다고 말할 수 있었다. 박사는 매주 찰스를 만났고 그가 전하는 메시지를 그녀에게 직접 가져왔다.",
        "ko2": "때로는 찰스가 편지를 보내기도 했지만, 박사가 전달한 적은 없었고, 당국이 죄수들이 해외의 친구들과 공모하고 있다고 의심했기 때문에 루시는 답장을 쓸 수 없었다."
    },
    # 6. ch_27.json (Tag: P003_3)
    {
        "file": "ch_27.json",
        "match": lambda p: p.get("tag") == "P003_3" and p["en"].startswith("Fluttering hopes and doubts"),
        "tag1": "P003_3", "tag2": "P003_4",
        "en1": "Fluttering hopes and doubts—hopes of a love as yet unknown to her, doubts about remaining on earth to enjoy that new delight—divided her heart.",
        "en2": "In those moments, among the echoes, the sound of footsteps at her own early grave would arise; and thoughts of the husband who would be left so desolate, and who would mourn for her so deeply, swelled to her eyes and broke like waves.",
        "ko1": "설레는 희망과 불안—아직 알지 못하는 사랑에 대한 희망과, 그 새로운 기쁨을 누리기 위해 자신이 세상에 살아남을 수 있을지에 대한 불안—이 그녀의 마음을 갈라놓았다.",
        "ko2": "그럴 때면 메아리 속에서 자신의 이른 무덤가에 울리는 발소리가 들려오는 듯했고, 홀로 쓸쓸히 남아 자신을 위해 깊이 애도할 남편에 대한 생각에 눈물이 차올라 파도처럼 흘러내렸다."
    },
    # 7. ch_12.json (Tag: P017_3)
    {
        "file": "ch_12.json",
        "match": lambda p: p.get("tag") == "P017_3" and p["en"].startswith("The first was the best room."),
        "tag1": "P017_3", "tag2": "P017_4",
        "en1": "The first was the best room. It contained Lucie's birds, flowers, books, desk, and watercolors. The second was the Doctor’s consulting room, which was also used for dining.",
        "en2": "The third, shaded by the leaves of the plane tree outside, was the Doctor’s bedroom. In the corner stood the unused shoemaker’s bench and tools, looking just as they had in the dark attic room in Paris.",
        "ko1": "첫 번째 방은 가장 좋은 방이었다. 그곳에는 루시의 새들, 꽃들, 책들, 책상, 그리고 수채화들이 있었다. 두 번째 방은 박사의 진찰실이었는데, 식당으로도 사용되었다.",
        "ko2": "세 번째 방은 밖의 플라타너스 잎사귀들로 그늘진 방으로 박사의 침실이었다. 구석에는 파리의 어두운 다락방에 있던 것과 똑같은 모습으로 사용하지 않는 구두장이의 작업대와 도구들이 놓여 있었다."
    },
    # 8. ch_12.json (Tag: P003_3)
    {
        "file": "ch_12.json",
        "match": lambda p: p.get("tag") == "P003_3" and p["en"].startswith("First, because on nice Sundays"),
        "tag1": "P003_3", "tag2": "P003_4",
        "en1": "First, because on nice Sundays he often walked before dinner with the Doctor and Lucie. Second, because on bad Sundays he spent the day with them as a family friend. They would talk, read, look out the window, and simply pass the time together.",
        "en2": "Third, because he had some small doubts he wanted to resolve, and he knew this was a good time to observe the Doctor's household.",
        "ko1": "첫째, 날씨가 좋은 일요일에는 저녁 식사 전에 박사와 루시와 함께 자주 산책을 했기 때문이다. 둘째, 날씨가 궂은 일요일에는 가족의 친구로서 그들과 하루를 보냈기 때문이다. 그들은 이야기하고, 책을 읽고, 창밖을 내다보며 그냥 함께 시간을 보내곤 했다.",
        "ko2": "셋째, 그에게는 해소하고 싶은 작은 의문들이 있었고, 이때가 박사의 가정을 관찰하기 좋은 시간이라는 것을 알았기 때문이다."
    },
    # 9. ch_29.json (Tag: P047_1)
    {
        "file": "ch_29.json",
        "match": lambda p: p.get("tag") == "P047_1" and p["en"].startswith("Within a hundred miles,"),
        "tag1": "P047_1", "tag2": "P047_2",
        "en1": "Within a hundred miles, by the light of other fires, other officials were not as lucky. That night and over the next few nights, the morning sun found many of them hanging dead over the streets where they had grown up.",
        "en2": "On the other side, some villagers were less fortunate than the road-mender and his friends, as soldiers and officials caught them and hanged them instead.",
        "ko1": "백 마일 이내의 다른 관리들은 다른 불빛 아래에서 그렇게 운이 좋지 않았다. 그날 밤과 이어진 며칠 밤 동안, 아침 해는 그들 중 많은 이들이 그들이 자란 거리 위에서 목매달려 죽어 있는 것을 발견했다.",
        "ko2": "반대편에서는 군인들과 관리들이 마을 사람들을 붙잡아 대신 교수형에 처했기 때문에, 도로 보수공과 그의 친구들보다 운이 나쁜 마을 사람들도 있었다."
    },
    # 10. ch_29.json (Tag: P042_3)
    {
        "file": "ch_29.json",
        "match": lambda p: p.get("tag") == "P042_3" and p["en"].startswith("The general scarcity of everything caused"),
        "tag1": "P042_3", "tag2": "P042_4",
        "en1": "The general scarcity of everything caused candles to be borrowed from Monsieur Gabelle in a rather forceful manner; and when that official hesitated and showed reluctance, the road-mender, once so submissive to authority, remarked that carriages were good for making bonfires and that post-horses would roast nicely.",
        "en2": "The chateau was left to blaze and burn away on its own.",
        "ko1": "모든 것이 전반적으로 부족하다 보니 가벨 씨에게서 다소 강압적인 태도로 양초를 빌려 가게 되었는데, 그 관리가 머뭇거리며 주저하자 한때 권력에 그토록 순종적이던 도로 보수공은 마차는 모닥불을 피우기에 안성맞춤이고 우편마차 말들은 통구이로 구워질 것이라고 한마디 던졌다.",
        "ko2": "성은 홀로 활활 타오르도록 내버려졌다."
    },
    # 11. ch_30.json (Tag: P012)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P012" and p["en"].startswith("“As for the chaos,"),
        "tag1": "P012_1", "tag2": "P012_2",
        "en1": "“As for the chaos, if the city weren't chaotic, we wouldn't need to send someone from our London office to our Paris branch who knows the place and the business, and whom Tellson's trusts completely.",
        "en2": "As for the difficult travel, the long journey, and the winter weather, if I am not willing to face a few hardships for Tellson's after all these years, who should be?”",
        "ko1": "“혼란에 관해서라면, 도시가 혼란스럽지 않다면 런던 본사에서 파리 지점으로 그곳의 상황과 사업을 알고 텔슨 은행이 온전히 신뢰하는 사람을 보낼 필요가 없을 걸세.",
        "ko2": "힘든 여행, 긴 여정, 그리고 겨울 날씨에 관해서라면, 지난 세월 텔슨 은행을 위해 일한 내가 약간의 고난을 기꺼이 마주하지 않는다면 대체 누가 해야겠는가?”"
    },
    # 12. ch_30.json (Tag: P087_1)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P087_1" and p["en"].startswith("That night, it was August fourteenth,"),
        "tag1": "P087_1", "tag2": "P087_2",
        "en1": "That night, it was August fourteenth, he stayed up late and wrote two emotional letters. One was to Lucie, explaining the heavy duty that forced him to go to Paris and explaining in detail why he was confident he would not be in any personal danger.",
        "en2": "The other was to the Doctor, entrusting Lucie and their child to his care and repeating the same strong reassurances.",
        "ko1": "그날 밤, 팔월 십사일, 그는 늦게까지 깨어 감동적인 편지 두 통을 썼다. 하나는 루시에게 자신이 파리로 가야만 하는 무거운 의무를 설명하고 개인적인 위험이 없을 것이라고 확신하는 이유를 자세히 설명하는 내용이었다.",
        "ko2": "다른 하나는 마네트에게 루시와 아이를 부탁하며 같은 강력한 안심의 말을 반복하는 내용이었다."
    },
    # 13. ch_30.json (Tag: P015_1)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P015_1" and p["en"].startswith('"My dear Mr. Lorry,'),
        "tag1": "P015_1", "tag2": "P015_2",
        "en1": '"My dear Mr. Lorry, it is because I was born a Frenchman that the thought (which I didn\'t mean to speak aloud here, though) has often crossed my mind.',
        "en2": 'Having felt sympathy for the poor people and having given up my property to them,” he spoke thoughtfully, “I cannot help but think that they might listen to me. I might be able to persuade them to show some mercy.”',
        "ko1": '"친애하는 로리 씨, 비록 여기서 입 밖에 낼 생각은 아니었지만, 제가 태생이 프랑스인이기 때문에 그런 생각이 자주 머릿속을 스쳤던 것입니다.',
        "ko2": '가난한 사람들에게 동정심을 느껴왔고 그들에게 재산을 넘겨주었기에,” 그가 생각에 잠겨 말했다. “그들이 제 말에 귀를 기울여 줄지도 모른다는 생각을 떨칠 수가 없습니다. 자비를 베풀도록 그들을 설득할 수 있을지도 모릅니다.”'
    },
    # 14. ch_13.json (Tag: P008_3)
    {
        "file": "ch_13.json",
        "match": lambda p: p.get("tag") == "P008_3" and p["en"].startswith("To find a promising cure"),
        "tag1": "P008_3", "tag2": "P008_4",
        "en1": "To find a promising cure for this exhaustion, three of these six gentlemen had joined a wild religious group called the Convulsionists.",
        "en2": "They were currently wondering if they should start foaming at the mouth, raging, roaring, and freezing in trances right then and there, hoping to provide a very clear sign pointing out the future for Monseigneur's guidance.",
        "ko1": "이 피로에 대한 유망한 치료법을 찾기 위해 이 여섯 명의 신사 중 세 명은 경련파라는 거친 종교 단체에 가입했다.",
        "ko2": "그들은 몽세뇌르의 지도를 위해 미래를 가리키는 매우 명확한 신호를 제공하기를 바라며, 그 자리에서 당장 입에 거품을 물고 분노하고 포효하며 무아지경에 빠져 얼어붙어야 할지 생각하고 있었다."
    },
    # 15. ch_30.json (Tag: P066_2)
    {
        "file": "ch_30.json",
        "match": lambda p: p.get("tag") == "P066_2" and p["en"].startswith("He had waited for the right moment"),
        "tag1": "P066_2", "tag2": "P066_3",
        "en1": "He had waited for the right moment to take action, but the situation had changed so fast that the opportunity had passed.",
        "en2": "Now, the nobles were fleeing France along every road, their properties were being seized and destroyed, and their very names were being erased, facts he knew just as well as the new French authorities who might accuse him of abandonment.",
        "ko1": "그는 행동할 적절한 순간을 기다렸지만 상황이 너무 빨리 변하여 기회를 놓쳐버렸다.",
        "ko2": "이제 귀족들은 사방의 길을 통해 프랑스를 탈출하고 있었고, 그들의 재산은 몰수당하고 파괴되었으며, 그들의 이름조차 지워지고 있다는 사실을 그도 알고 있었고, 그가 조국을 버렸다고 비난할지도 모르는 새로운 프랑스 당국도 똑같이 잘 알고 있었다."
    },
    # 16. ch_27.json (Tag: P007_2)
    {
        "file": "ch_27.json",
        "match": lambda p: p.get("tag") == "P007_2" and p["en"].startswith("The gentle breeze blowing"),
        "tag1": "P007_2", "tag2": "P007_3",
        "en1": "The gentle breeze blowing over a small garden grave also mixed with those sounds. Lucie could hear them in a soft whisper, like a calm summer sea against the sand.",
        "en2": "Meanwhile, little Lucie, looking very serious while doing her morning lessons or dressing her doll by her mother's feet, chattered away in the languages of the two cities that shaped her life.",
        "ko1": "정원의 작은 무덤 위로 부는 부드러운 산들바람 역시 그 소리들과 뒤섞였습니다. 루시는 모래사장에 부딪히는 잔잔한 여름 바다처럼 부드러운 속삭임 속에서 그 소리를 들을 수 있었습니다.",
        "ko2": "한편, 어린 루시는 매우 진지한 표정으로 아침 공부를 하거나 어머니의 발치에서 인형 옷을 입히며 그녀의 삶을 형성한 두 도시의 언어로 재잘거렸습니다."
    },
    # 17. ch_05.json (Tag: P008_12)
    {
        "file": "ch_05.json",
        "match": lambda p: p.get("tag") == "P008_12" and p["en"].startswith("Indeed they were lost at sea,"),
        "tag1": "P008_12", "tag2": "P008_13",
        "en1": "Indeed they were lost at sea, and the ship and crew were in danger of a storm.",
        "en2": "For the time was to come when the gaunt scarecrows of that region, having watched the lamplighter for so long in their idle hunger, would conceive the idea of improving on his method—and hauling up men by those ropes and pulleys, to flare upon the darkness of their condition.",
        "ko1": "실로 그들은 망망대해에 떠 있었고, 배와 선원들은 폭풍우의 위협에 처해 있었다.",
        "ko2": "왜냐하면 굶주림과 무기력 속에서 가로등 켜는 사람을 오랫동안 지켜보던 그 지역의 앙상한 허수아비 같은 자들이, 그 방식을 한 단계 발전시켜 사람들을 그 밧줄과 도르래로 끌어올려 매달아 자신들의 암담한 처지를 밝히겠다는 생각을 품게 될 날이 머지않았기 때문이었다."
    },
    # 18. ch_03.json (Tag: P009_2)
    {
        "file": "ch_03.json",
        "match": lambda p: p.get("tag") == "P009_2" and p["en"].startswith("He dozed in his seat,"),
        "tag1": "P009_2", "tag2": "P009_3",
        "en1": "He dozed in his seat, his arm hooked through the leather strap overhead to stop himself from slamming into the next passenger every time the coach jolted badly.",
        "en2": "The dim coach windows, the faint glow of the lamp, and the dark silhouette of the passenger across from him all slowly transformed in his half-sleeping mind into the familiar rooms of the bank.",
        "ko1": "그는 자리에 앉아 졸고 있었고, 마차가 심하게 덜컹거릴 때마다 옆 승객과 부딪히는 것을 막기 위해 머리 위의 가죽 끈에 팔을 걸고 있었다.",
        "ko2": "희미한 마차 창문과 램프의 옅은 불빛, 그리고 맞은편에 앉은 승객의 어두운 실루엣은 그의 반쯤 잠든 마음속에서 모두 텔슨 은행의 익숙한 방들로 천천히 변해갔다."
    },
    # 19. ch_27.json (Tag: P058_2)
    {
        "file": "ch_27.json",
        "match": lambda p: p.get("tag") == "P058_2" and p["en"].startswith("At first, the flooding crowd"),
        "tag1": "P058_2", "tag2": "P058_3",
        "en1": "At first, the flooding crowd would bump into them and sweep past, but by the time they finished going down and started winding their way up a tower, they were all alone.",
        "en2": "Surrounded by massive walls and arches, the crazy storm inside and outside the fortress sounded muffled. It was like the noise they had just escaped had almost ruined their hearing.",
        "ko1": "처음에는 쏟아져 들어오는 군중들이 그들과 부딪히며 지나갔지만, 그들이 아래로 내려가는 것을 마치고 탑을 향해 굽이쳐 올라가기 시작할 때쯤에는 그들뿐이었다.",
        "ko2": "거대한 벽과 아치로 둘러싸여, 요새 안팎의 미친 폭풍은 웅얼거리는 듯 들렸다. 마치 그들이 방금 벗어난 소음이 그들의 청력을 거의 앗아간 것 같았다."
    },
    # 20. ch_16.json (Tag: P002_6)
    {
        "file": "ch_16.json",
        "match": lambda p: p.get("tag") == "P002_6" and p["en"].startswith("As a tutor whose knowledge"),
        "tag1": "P002_6", "tag2": "P002_7",
        "en1": "As a tutor whose knowledge made learning remarkably pleasant and rewarding, and as a skilled translator who brought far more to his craft than simple dictionary definitions, young Mr. Darnay quickly gained recognition and support.",
        "en2": "Moreover, he possessed a deep understanding of affairs in his homeland, which were attracting ever-increasing interest.",
        "ko1": "학생들이 유쾌하고 유익하게 배울 수 있도록 이끌어 주는 뛰어난 식견을 지닌 가정교사이자, 단순한 사전적 지식을 넘어선 깊이를 작업에 불어넣는 훌륭한 번역가로서 젊은 다네이 씨는 곧 이름을 알리고 많은 격려를 받았다.",
        "ko2": "게다가 그는 나날이 관심이 높아지던 자기 조국의 사정에도 매우 밝았다."
    },
    # 21. ch_27.json (Tag: P060_1)
    {
        "file": "ch_27.json",
        "match": lambda p: p.get("tag") == "P060_1" and p["en"].startswith('"One hundred and five, North Tower!"'),
        "tag1": "P060_1", "tag2": "P060_2",
        "en1": '"One hundred and five, North Tower!" Inside, there was a small window high up on the wall with thick iron bars and no glass. It had a stone screen in front of it, so you had to stoop low and look up just to see the sky.',
        "en2": "A few feet away, there was a small chimney with heavy bars across it, and a pile of soft, old wood ashes sitting in the fireplace.",
        "ko1": '"북탑 일백오 호!" 안에는 유리가 없고 두꺼운 쇠창살이 있는 작은 창문이 벽 높은 곳에 있었다. 창문 앞에는 돌로 된 칸막이가 있어서, 허리를 숙이고 올려다보아야만 하늘을 볼 수 있었다.',
        "ko2": "몇 발자국 떨어진 곳에는 무거운 쇠창살이 가로질러진 작은 굴뚝이 있었고, 벽난로에는 부드럽고 오래된 나무 재 더미가 놓여 있었다."
    }
]

validation_report = []

from collections import defaultdict
splits_by_file = defaultdict(list)
for s in splits:
    splits_by_file[s['file']].append(s)

for filename, file_splits in splits_by_file.items():
    fpath = os.path.join(assets_dir, filename)
    with open(fpath, encoding='utf-8') as f:
        data = json.load(f)

    for s in file_splits:
        found = False
        for idx, p in enumerate(data):
            if s['match'](p):
                orig_en = p['en']
                orig_ko = p['ko']
                recombined_en = s['en1'] + ' ' + s['en2']
                recombined_ko = s['ko1'] + ' ' + s['ko2']

                assert orig_en.split() == recombined_en.split(), f"EN mismatch in {filename} tag {p.get('tag')}"
                assert orig_ko.split() == recombined_ko.split(), f"KO mismatch in {filename} tag {p.get('tag')}"

                chunk1 = {
                    "id": 0,
                    "tag": s['tag1'],
                    "en": s['en1'],
                    "ko": s['ko1'],
                    "is_header": False,
                    "raw_ref_id": p.get('raw_ref_id', p['id'])
                }
                chunk2 = {
                    "id": 0,
                    "tag": s['tag2'],
                    "en": s['en2'],
                    "ko": s['ko2'],
                    "is_header": False,
                    "raw_ref_id": p.get('raw_ref_id', p['id'])
                }

                data[idx] = chunk1
                data.insert(idx + 1, chunk2)
                found = True

                validation_report.append({
                    "file": filename,
                    "orig_id": p['id'],
                    "tag": p.get('tag'),
                    "orig_len": len(orig_en),
                    "chunk1_en_len": len(s['en1']),
                    "chunk1_ko_len": len(s['ko1']),
                    "chunk2_en_len": len(s['en2']),
                    "chunk2_ko_len": len(s['ko2']),
                    "chunk1_en": s['en1'],
                    "chunk1_ko": s['ko1'],
                    "chunk2_en": s['en2'],
                    "chunk2_ko": s['ko2']
                })
                break
        assert found, f"Could not find match for split in {filename}"

    for new_id, p in enumerate(data, 1):
        p['id'] = new_id

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Updated {filename}: Now {len(data)} paragraphs.")

with open('split_validation_report_tier350.txt', 'w', encoding='utf-8') as out:
    out.write("VALIDATION REPORT: 21 MULTI-SENTENCE PARAGRAPH SPLITS (350-399 TIER)\n")
    out.write(f"Total candidate paragraphs split: {len(validation_report)}\n")
    out.write("Invariant check: 100% character and word conservation verified for both EN and KO.\n")
    out.write("="*80 + "\n\n")

    for i, r in enumerate(validation_report, 1):
        out.write(f"[{i}] {r['file']} (Tag: {r['tag']}, Original Length: {r['orig_len']} chars)\n")
        out.write(f"  --> Chunk A ({r['chunk1_en_len']} EN ch / {r['chunk1_ko_len']} KO ch):\n")
        out.write(f"      EN: {r['chunk1_en']}\n")
        out.write(f"      KO: {r['chunk1_ko']}\n\n")
        out.write(f"  --> Chunk B ({r['chunk2_en_len']} EN ch / {r['chunk2_ko_len']} KO ch):\n")
        out.write(f"      EN: {r['chunk2_en']}\n")
        out.write(f"      KO: {r['chunk2_ko']}\n")
        out.write("-" * 80 + "\n\n")

print("SUCCESS: All 21 splits executed and verified! Report written to split_validation_report_tier350.txt")

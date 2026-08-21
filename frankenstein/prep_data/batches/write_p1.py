import json

data = [
  {
    "original_id": 0,
    "chunks": [
      {
        "tag": "P000-1",
        "en": "Chapter 5",
        "ko": "제5장"
      }
    ]
  },
  {
    "original_id": 1,
    "chunks": [
      {
        "tag": "P001-1",
        "en": "It was on a dreary night of November that I beheld the accomplishment of my toils. With an anxiety that almost amounted to agony, I collected the instruments of life around me, that I might infuse a spark of being into the lifeless thing that lay at my feet.",
        "ko": "음산한 11월의 어느 밤, 나는 마침내 내 노고의 결실을 목도하게 되었다. 거의 고통에 가까울 정도의 불안감 속에서 나는 생명의 도구들을 내 주변에 모아두었는데, 이는 내 발치에 놓인 생명 없는 형체에 존재의 불꽃을 불어넣기 위함이었다."
      },
      {
        "tag": "P001-2",
        "en": "It was already one in the morning; the rain pattered dismally against the panes, and my candle was nearly burnt out, when, by the glimmer of the half-extinguished light, I saw the dull yellow eye of the creature open;",
        "ko": "시간은 이미 새벽 1시를 가리키고 있었다. 빗방울이 창유리를 음산하게 두드렸고 촛불은 거의 다 타들어 가고 있었다. 바로 그때, 반쯤 꺼져가는 희미한 불빛 속에서 나는 그 피조물의 탁한 노란색 눈이 뜨이는 것을 보았다."
      },
      {
        "tag": "P001-3",
        "en": "it breathed hard, and a convulsive motion agitated its limbs.",
        "ko": "그것은 거칠게 숨을 쉬었고, 발작적인 경련이 그 사지를 뒤흔들었다."
      }
    ]
  },
  {
    "original_id": 2,
    "chunks": [
      {
        "tag": "P002-1",
        "en": "How can I describe my emotions at this catastrophe, or how delineate the wretch whom with such infinite pains and care I had endeavoured to form?",
        "ko": "이 참담한 순간의 내 감정을 어찌 말로 다 설명할 수 있겠는가. 그토록 무한한 수고와 정성을 들여 형상을 빚어내려 했던 그 비참한 존재를 어찌 묘사할 수 있겠는가?"
      },
      {
        "tag": "P002-2",
        "en": "His limbs were in proportion, and I had selected his features as beautiful. Beautiful! Great God!",
        "ko": "그 사지는 비율이 맞았고, 나는 아름답다고 생각되는 이목구비를 골라 그에게 부여했었다. 아름답다고! 위대하신 신이시여!"
      },
      {
        "tag": "P002-3",
        "en": "His yellow skin scarcely covered the work of muscles and arteries beneath; his hair was of a lustrous black, and flowing; his teeth of a pearly whiteness;",
        "ko": "그의 노란 피부는 그 아래의 근육과 동맥을 간신히 덮고 있을 뿐이었다. 머리카락은 윤기 나는 검은색에 찰랑거렸으며, 치아는 진주처럼 새하얬다."
      },
      {
        "tag": "P002-4",
        "en": "but these luxuriances only formed a more horrid contrast with his watery eyes, that seemed almost of the same colour as the dun-white sockets in which they were set, his shrivelled complexion and straight black lips.",
        "ko": "하지만 이러한 풍성함은 오히려 그의 물기 어린 눈동자와 더욱 끔찍한 대조를 이룰 뿐이었다. 그 눈동자는 그것이 박혀 있는 거무스름하고 하얀 눈구멍과 거의 같은 색으로 보였고, 그의 안색은 쪼그라들었으며 입술은 시커멓게 일자였다."
      }
    ]
  },
  {
    "original_id": 3,
    "chunks": [
      {
        "tag": "P003-1",
        "en": "The different accidents of life are not so changeable as the feelings of human nature. I had worked hard for nearly two years, for the sole purpose of infusing life into an inanimate body. For this I had deprived myself of rest and health.",
        "ko": "삶의 다양한 우연한 사건들도 인간의 감정만큼 변화무쌍하지는 않다. 나는 오로지 생명 없는 육체에 생명을 불어넣겠다는 목적 하나로 거의 2년 동안 고된 작업을 해왔다. 이를 위해 나는 휴식과 건강마저 포기했다."
      },
      {
        "tag": "P003-2",
        "en": "I had desired it with an ardour that far exceeded moderation; but now that I had finished, the beauty of the dream vanished, and breathless horror and disgust filled my heart.",
        "ko": "나는 절도를 훨씬 넘어서는 열정으로 그것을 갈망해 왔다. 하지만 막상 일을 끝내고 나니, 그 꿈의 아름다움은 신기루처럼 사라지고 숨 막히는 공포와 혐오감이 내 심장을 가득 채웠다."
      },
      {
        "tag": "P003-3",
        "en": "Unable to endure the aspect of the being I had created, I rushed out of the room and continued a long time traversing my bed-chamber, unable to compose my mind to sleep.",
        "ko": "내가 창조한 그 존재의 끔찍한 몰골을 차마 견딜 수 없어 나는 서둘러 방을 뛰쳐나왔다. 그리고 오랫동안 침실 안을 서성였지만 잠을 청할 만큼 마음을 가라앉힐 수 없었다."
      },
      {
        "tag": "P003-4",
        "en": "At length lassitude succeeded to the tumult I had before endured, and I threw myself on the bed in my clothes, endeavouring to seek a few moments of forgetfulness. But it was in vain; I slept, indeed, but I was disturbed by the wildest dreams.",
        "ko": "마침내 앞서 겪었던 극심한 혼란 뒤에 극도의 피로가 몰려왔고, 나는 옷을 입은 채로 침대에 몸을 던지며 잠시나마 잊기를 구했다. 그러나 헛된 일이었다. 잠이 들기는 했으나 가장 거칠고 기괴한 꿈들에 시달렸다."
      },
      {
        "tag": "P003-5",
        "en": "I thought I saw Elizabeth, in the bloom of health, walking in the streets of Ingolstadt. Delighted and surprised, I embraced her, but as I imprinted the first kiss on her lips, they became livid with the hue of death;",
        "ko": "꿈속에서 나는 건강하고 아름다운 엘리자베스가 잉골슈타트의 거리를 걷고 있는 것을 보았다. 기쁘고 놀라운 마음에 나는 그녀를 껴안았다. 그러나 내가 그녀의 입술에 첫 키스를 남기는 순간, 그녀의 입술은 죽음의 빛깔로 파랗게 질려갔다."
      },
      {
        "tag": "P003-6",
        "en": "her features appeared to change, and I thought that I held the corpse of my dead mother in my arms; a shroud enveloped her form, and I saw the grave-worms crawling in the folds of the flannel.",
        "ko": "그녀의 이목구비가 변하는 듯하더니, 어느새 나는 죽은 어머니의 시신을 품에 안고 있었다. 수의가 그녀의 몸을 감싸고 있었고, 덮인 플란넬의 주름 사이로 무덤의 구더기들이 기어 다니는 것이 보였다."
      },
      {
        "tag": "P003-7",
        "en": "I started from my sleep with horror; a cold dew covered my forehead, my teeth chattered, and every limb became convulsed; when, by the dim and yellow light of the moon, as it forced its way through the window shutters, I beheld the wretch—the miserable monster whom I had created.",
        "ko": "나는 공포에 질려 잠에서 깼다. 이마에는 차가운 식은땀이 맺혔고, 이가 부딪히며 온몸의 사지가 경련을 일으켰다. 그때, 창문을 통해 비쳐 드는 흐릿하고 누런 달빛 속에서 나는 보았다. 내가 창조해 낸 그 비참하고 가련한 괴물을."
      },
      {
        "tag": "P003-8",
        "en": "He held up the curtain of the bed; and his eyes, if eyes they may be called, were fixed on me. His jaws opened, and he muttered some inarticulate sounds, while a grin wrinkled his cheeks.",
        "ko": "그가 침대 커버를 들어 올렸고, 눈이라 부를 수 있다면 눈이라고 할 그것이 나를 빤히 응시하고 있었다. 그의 턱이 열리더니 알 수 없는 소리를 웅얼거렸고, 두 뺨은 미소로 주름져 있었다."
      },
      {
        "tag": "P003-9",
        "en": "He might have spoken, but I did not hear; one hand was stretched out, seemingly to detain me, but I escaped and rushed downstairs.",
        "ko": "어쩌면 그가 무슨 말을 했을지도 모르지만 나는 듣지 못했다. 한 손이 쭉 뻗어 나와 나를 붙잡으려는 듯했지만, 나는 빠져나와 아래층으로 서둘러 도망쳤다."
      },
      {
        "tag": "P003-10",
        "en": "I took refuge in the courtyard belonging to the house which I inhabited, where I remained during the rest of the night, walking up and down in the greatest agitation, listening attentively, catching and fearing each sound as if it were to announce the approach of the demoniacal corpse to which I had so miserably given life.",
        "ko": "나는 내가 머무는 집의 안뜰로 피신했고, 밤새도록 그곳에 머물렀다. 걷잡을 수 없는 흥분 속에서 위아래로 서성거리며, 귀를 기울이고 모든 소리에 신경을 곤두세웠다. 마치 내가 그렇게 비참하게 생명을 부여한 그 악마 같은 시체가 다가오는 것을 알리는 소리일까 두려워하면서 말이다."
      }
    ]
  },
  {
    "original_id": 4,
    "chunks": [
      {
        "tag": "P004-1",
        "en": "Oh! No mortal could support the horror of that countenance. A mummy again endued with animation could not be so hideous as that wretch.",
        "ko": "아! 어떤 인간도 그 끔찍한 얼굴을 견뎌내지는 못할 것이다. 다시 생명을 얻은 미라라 할지라도 그 괴물만큼 흉측하지는 않을 것이다."
      },
      {
        "tag": "P004-2",
        "en": "I had gazed on him while unfinished; he was ugly then, but when those muscles and joints were rendered capable of motion, it became a thing such as even Dante could not have conceived.",
        "ko": "나는 아직 완성되지 않았을 때도 그를 응시했었다. 그때도 그는 흉측했지만, 근육과 관절이 움직일 수 있게 되자 단테조차 상상하지 못할 만큼 끔찍한 존재가 되어버렸다."
      }
    ]
  },
  {
    "original_id": 5,
    "chunks": [
      {
        "tag": "P005-1",
        "en": "I passed the night wretchedly. Sometimes my pulse beat so quickly and hardly that I felt the palpitation of every artery; at others, I nearly sank to the ground through languor and extreme weakness.",
        "ko": "나는 그 밤을 비참하게 보냈다. 때로는 맥박이 너무 빠르고 강하게 뛰어 모든 동맥의 박동이 느껴질 정도였고, 때로는 나른함과 극도의 쇠약함으로 땅에 쓰러질 뻔했다."
      },
      {
        "tag": "P005-2",
        "en": "Mingled with this horror, I felt the bitterness of disappointment; dreams that had been my food and pleasant rest for so long a space were now become a hell to me; and the change was so rapid, the overthrow so complete!",
        "ko": "이 공포와 더불어 나는 깊은 절망의 쓴맛을 느꼈다. 그토록 오랜 시간 나의 양식이요 달콤한 안식처였던 꿈이 이제는 내게 지옥이 되어버린 것이다. 변화는 너무도 급작스러웠고, 몰락은 너무도 완벽했다!"
      }
    ]
  },
  {
    "original_id": 6,
    "chunks": [
      {
        "tag": "P006-1",
        "en": "Morning, dismal and wet, at length dawned and discovered to my sleepless and aching eyes the church of Ingolstadt, its white steeple and clock, which indicated the sixth hour.",
        "ko": "마침내 음산하고 축축한 아침이 밝았고, 잠들지 못해 욱신거리는 내 눈앞에 잉골슈타트 교회의 모습이 드러났다. 하얀 첨탑과 6시를 가리키는 시계가 보였다."
      },
      {
        "tag": "P006-2",
        "en": "The porter opened the gates of the court, which had that night been my asylum, and I issued into the streets, pacing them with quick steps, as if I sought to avoid the wretch whom I feared every turning of the street would present to my view.",
        "ko": "그날 밤 나의 피난처였던 뜰의 문을 문지기가 열었고, 나는 거리로 나섰다. 거리를 돌 때마다 내가 두려워하는 그 괴물이 나타날까 봐 두려워 잰걸음으로 서둘렀다."
      },
      {
        "tag": "P006-3",
        "en": "I did not dare return to the apartment which I inhabited, but felt impelled to hurry on, although drenched by the rain which poured from a black and comfortless sky.",
        "ko": "내가 살던 방으로 돌아갈 엄두가 나지 않아 발걸음을 재촉할 수밖에 없었다. 어둡고 삭막한 하늘에서 쏟아지는 비에 온몸이 흠뻑 젖었음에도 불구하고 말이다."
      }
    ]
  }
]

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_9.ch5_done.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

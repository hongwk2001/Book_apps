import json

data4 = [
  {
    "original_id": 20,
    "chunks": [
      {
        "tag": "P020-1",
        "en": "By very slow degrees, and with frequent relapses that alarmed and grieved my friend, I recovered.",
        "ko": "아주 서서히, 그리고 친구를 놀라게 하고 슬프게 만든 잦은 재발을 거치면서 나는 회복되어 갔다."
      },
      {
        "tag": "P020-2",
        "en": "I remember the first time I became capable of observing outward objects with any kind of pleasure, I perceived that the fallen leaves had disappeared and that the young buds were shooting forth from the trees that shaded my window.",
        "ko": "내가 다시 어떤 즐거움을 가지고 외부의 사물들을 관찰할 수 있게 된 첫날을 기억한다. 나는 떨어졌던 낙엽들이 사라지고 내 창문을 가려주던 나무에서 어린 새싹들이 돋아나는 것을 보았다."
      },
      {
        "tag": "P020-3",
        "en": "It was a divine spring, and the season contributed greatly to my convalescence.",
        "ko": "그것은 성스러운 봄이었고, 계절의 변화는 내 회복에 큰 도움을 주었다."
      },
      {
        "tag": "P020-4",
        "en": "I felt also sentiments of joy and affection revive in my bosom; my gloom disappeared, and in a short time I became as cheerful as before I was attacked by the fatal passion.",
        "ko": "내 가슴속에는 다시 기쁨과 애정의 감정이 피어났고, 우울함은 사라져 버렸다. 그리고 얼마 지나지 않아 나는 그 치명적인 열정에 사로잡히기 전처럼 쾌활해졌다."
      }
    ]
  },
  {
    "original_id": 21,
    "chunks": [
      {
        "tag": "P021-1",
        "en": "“Dearest Clerval,” exclaimed I, “how kind, how very good you are to me. This whole winter, instead of being spent in study, as you promised yourself, has been consumed in my sick room.",
        "ko": "\"가장 사랑하는 클러벌,\" 나는 외쳤다. \"자네는 내게 얼마나 친절하고 얼마나 좋은 사람인가. 올겨울 내내 자네가 약속했던 학업에 몰두하는 대신 내 병실에서 시간을 허비해 버렸네."
      },
      {
        "tag": "P021-2",
        "en": "How shall I ever repay you? I feel the greatest remorse for the disappointment of which I have been the occasion, but you will forgive me.”",
        "ko": "내가 이 은혜를 어떻게 다 갚을 수 있겠는가? 나 때문에 자네가 겪은 실망감에 큰 죄책감을 느끼네. 하지만 나를 용서해 주게.\""
      }
    ]
  },
  {
    "original_id": 22,
    "chunks": [
      {
        "tag": "P022-1",
        "en": "“You will repay me entirely if you do not discompose yourself, but get well as fast as you can; and since you appear in such good spirits, I may speak to you on one subject, may I not?”",
        "ko": "\"자네가 불안해하지 않고 최대한 빨리 건강을 되찾는다면 내게 온전히 다 갚는 거라네. 그리고 자네가 이렇게 기분이 좋아 보이니, 한 가지 주제에 대해 이야기해도 되겠지?\""
      }
    ]
  },
  {
    "original_id": 23,
    "chunks": [
      {
        "tag": "P023-1",
        "en": "I trembled. One subject! What could it be? Could he allude to an object on whom I dared not even think?",
        "ko": "나는 몸을 떨었다. 한 가지 주제라니! 그게 대체 무엇일까? 설마 내가 감히 생각조차 할 수 없는 그 끔찍한 존재를 암시하는 것일까?"
      }
    ]
  },
  {
    "original_id": 24,
    "chunks": [
      {
        "tag": "P024-1",
        "en": "“Compose yourself,” said Clerval, who observed my change of colour, “I will not mention it if it agitates you; but your father and cousin would be very happy if they received a letter from you in your own handwriting.",
        "ko": "\"진정하게,\" 안색이 변하는 것을 본 클러벌이 말했다. \"자네를 동요하게 한다면 언급하지 않겠네. 하지만 자네 아버지와 사촌은 자네가 직접 쓴 편지를 받는다면 매우 기뻐하실 걸세."
      },
      {
        "tag": "P024-2",
        "en": "They hardly know how ill you have been and are uneasy at your long silence.”",
        "ko": "두 분은 자네가 얼마나 아팠는지 잘 모르시고, 자네의 오랜 침묵에 불안해하고 계시네.\""
      }
    ]
  },
  {
    "original_id": 25,
    "chunks": [
      {
        "tag": "P025-1",
        "en": "“Is that all, my dear Henry? How could you suppose that my first thought would not fly towards those dear, dear friends whom I love and who are so deserving of my love?”",
        "ko": "\"그게 전부인가, 사랑하는 헨리? 내 첫 생각이 내가 사랑하고, 또 내 사랑을 받기에 충분한 사랑하는 나의 가족과 친구들에게 향하지 않았으리라 어떻게 짐작할 수 있단 말인가?\""
      }
    ]
  },
  {
    "original_id": 26,
    "chunks": [
      {
        "tag": "P026-1",
        "en": "“If this is your present temper, my friend, you will perhaps be glad to see a letter that has been lying here some days for you; it is from your cousin, I believe.”",
        "ko": "\"자네가 지금 그런 마음이라면, 며칠 전부터 이곳에 자네를 기다리고 있던 편지 한 통을 보면 기뻐할지도 모르겠군. 내 생각엔 자네 사촌이 보낸 것 같아.\""
      }
    ]
  }
]

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_9.ch5_done.json', 'r', encoding='utf-8') as f:
    existing_data = json.load(f)

existing_data.extend(data4)

with open(r'c:\git_repo\Book_apps\frankenstein\prep_data\batches\batch_9.ch5_done.json', 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, ensure_ascii=False, indent=2)

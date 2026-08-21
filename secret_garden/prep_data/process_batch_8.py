import json
import re

# Sentence counter
def count_sentences(text):
    sentences = re.split(r'[.!?]+["\']?(?=\s|$)', text)
    return len([s for s in sentences if s.strip()])

output_data = [
  {
    "original_id": 132,
    "chunks": [
      {
        "tag": "P132-1",
        "en": "\"I have no friends at all,\" Mary said.",
        "ko": "\"난 친구가 한 명도 없어요.\" 메리가 말했다."
      },
      {
        "tag": "P132-2",
        "en": "\"I never had any. My Ayah didn't like me, and I never played with anyone.\"",
        "ko": "\"원래부터 없었어요. 내 인도인 유모 아야도 날 좋아하지 않았고, 난 누구랑 놀아 본 적도 없거든요.\""
      }
    ]
  },
  {
    "original_id": 134,
    "chunks": [
      {
        "tag": "P134-1",
        "en": "\"You and me are quite a bit alike,\" he said. \"We were cut from the same cloth.\"",
        "ko": "\"너랑 나는 결이 참 많이 닮았구먼.\" 노인이 말했다. \"한통속이란 말일세.\""
      },
      {
        "tag": "P134-2",
        "en": "\"Neither of us is good-looking, and we're both as sour as we look. We've got the same bad tempers, the both of us, I'd bet.\"",
        "ko": "\"둘 다 인물이 잘난 것도 아니고, 겉보기만큼이나 속이 뒤틀려 있지. 성깔도 더러운 게 아주 판박일 거다, 내 장담하건대.\""
      }
    ]
  },
  {
    "original_id": 135,
    "chunks": [
      {
        "tag": "P135-1",
        "en": "This was blunt honesty, and Mary Lennox had never heard the truth about herself in her entire life. Indian servants always bowed and submitted to whatever she did.",
        "ko": "참으로 뼈아픈 직설이었다. 메리 레녹스는 평생 자신에 대한 진실을 단 한 번도 들어 본 적이 없었다. 인도의 하인들은 메리가 무슨 짓을 하든 늘 머리를 굽신거리며 복종할 뿐이었다."
      },
      {
        "tag": "P135-2",
        "en": "She had never thought much about her own appearance, but now she wondered if she was as unattractive as Ben Weatherstaff. She also wondered if she looked as sour as he had before the robin arrived.",
        "ko": "메리는 제 외모에 대해 별달리 신경을 쓴 적이 없었지만, 이제 자신이 벤 웨더스태프만큼이나 못생겼는지 생각해보게 되었다. 그리고 붉은가슴울새가 날아오기 전 노인의 얼굴처럼 자신도 그렇게 심술이 가득한 표정인지 궁금해졌다."
      },
      {
        "tag": "P135-3",
        "en": "She even began to wonder if she really was bad-tempered. The thoughts made her feel uncomfortable.",
        "ko": "급기야 자신이 정말로 성깔이 고약한 것은 아닌가 하는 의구심마저 들었다. 이런 생각들에 메리는 마음이 영 가시방석 같았다."
      }
    ]
  },
  {
    "original_id": 138,
    "chunks": [
      {
        "tag": "P138-1",
        "en": "\"He's made up his mind to be friends with you,\" Ben replied.",
        "ko": "\"너랑 친구가 되기로 결심한 게야.\" 벤이 대답했다."
      },
      {
        "tag": "P138-2",
        "en": "\"Well, I'll be. He's taken a real liking to you.\"",
        "ko": "\"허어, 참나. 녀석이 널 아주 마음에 들어 하는구먼.\""
      }
    ]
  },
  {
    "original_id": 140,
    "chunks": [
      {
        "tag": "P140-1",
        "en": "\"Would you be friends with me?\" she said to the robin, just as if she were speaking to a person.",
        "ko": "\"나랑 친구 해 줄래?\" 메리가 마치 사람에게 말을 건네듯 붉은가슴울새에게 속삭였다."
      },
      {
        "tag": "P140-2",
        "en": "\"Would you?\"",
        "ko": "\"응? 그럴 거지?\""
      },
      {
        "tag": "P140-3",
        "en": "She didn't say it in her usual hard little voice or in her bossy Indian tone, but in a voice so soft, eager, and coaxing that Ben Weatherstaff was just as surprised as she had been when he whistled.",
        "ko": "평소처럼 날카롭고 앙칼진 목소리도, 인도에서 쓰던 위압적인 말투도 아니었다. 어찌나 상냥하고 간절하게 어르는 목소리였는지, 벤 웨더스태프 역시 조금 전 자신이 불었던 감미로운 휘파람 소리에 메리가 놀랐던 것만큼이나 깜짝 놀랐다."
      }
    ]
  },
  {
    "original_id": 143,
    "chunks": [
      {
        "tag": "P143-1",
        "en": "\"Everybody knows him. Dickon wanders around everywhere.\"",
        "ko": "\"모르는 사람이 없지. 디콘 녀석은 안 쑤시고 다니는 데가 없거든.\""
      },
      {
        "tag": "P143-2",
        "en": "\"The very blackberries and heather-bells know him. I'd bet the foxes show him where their cubs are sleeping, and the skylarks don't hide their nests from him.\"",
        "ko": "\"들판의 블랙베리랑 헤더 꽃망울들까지 그 애를 알아볼 정도니까. 여우들이 자기 새끼가 어디 누워 자는지 알려 주고, 종다리들도 그 녀석 앞에선 둥지를 숨기지 않을 게다, 내 장담하지.\""
      }
    ]
  },
  {
    "original_id": 144,
    "chunks": [
      {
        "tag": "P144-1",
        "en": "Mary would have liked to ask more questions. She was almost as curious about Dickon as she was about the locked garden.",
        "ko": "메리는 묻고 싶은 말이 더 많았다. 닫힌 정원만큼이나 디콘에 대해서도 호기심이 무척 솟구쳤기 때문이다."
      },
      {
        "tag": "P144-2",
        "en": "But just then, the robin, who had finished his song, gave his wings a little shake, spread them, and flew away. He had finished his visit and had other things to do.",
        "ko": "그러나 바로 그때 노래를 마친 붉은가슴울새가 날개를 가볍게 털더니 날개를 활짝 펴고 날아가 버렸다. 방문을 마치고 제 할 일을 하러 간 것이다."
      }
    ]
  },
  {
    "original_id": 145,
    "chunks": [
      {
        "tag": "P145-1",
        "en": "\"He has flown over the wall!\" Mary cried, watching him.",
        "ko": "\"담장 너머로 날아가 버렸어요!\" 메리가 새를 쫓으며 소리쳤다."
      },
      {
        "tag": "P145-2",
        "en": "\"He has flown into the orchard—and now across the other wall—into the garden where there is no door!\"",
        "ko": "\"과수원으로 날아가더니, 이제 다른 담장을 넘어가네요. 문이 없는 정원으로 들어갔어요!\""
      }
    ]
  },
  {
    "original_id": 146,
    "chunks": [
      {
        "tag": "P146-1",
        "en": "\"He lives there,\" old Ben said.",
        "ko": "\"거기 살아서 그렇다네.\" 늙은 벤이 말했다."
      },
      {
        "tag": "P146-2",
        "en": "\"He hatched from his egg there. If he's courting, he's looking for some young lady robin who lives among the old rosebushes in there.\"",
        "ko": "\"거기 둥지 틀고 알 깨고 나온 놈이니. 짝을 구하는 중이라면 저 안에 오래된 장미 덩굴 사이에 사는 처녀 새를 찾고 있겠지.\""
      }
    ]
  },
  {
    "original_id": 150,
    "chunks": [
      {
        "tag": "P150-1",
        "en": "\"I should like to see them,\" Mary said.",
        "ko": "\"나도 보고 싶어요.\" 메리가 말했다."
      },
      {
        "tag": "P150-2",
        "en": "\"Where is the green door? There must be a door somewhere.\"",
        "ko": "\"초록색 문은 어디 있어요? 분명 어디가 문이 있을 텐데요.\""
      }
    ]
  },
  {
    "original_id": 154,
    "chunks": [
      {
        "tag": "P154-1",
        "en": "\"None that anyone can find, and none that is anyone's business. Don't be a meddling girl, poking your nose where it doesn't belong.\"",
        "ko": "\"아무도 찾을 수 없고, 알 바도 아니오. 참견쟁이 계집애처럼 쓸데없이 남의 일에 참견하려 들지 마시오.\""
      },
      {
        "tag": "P154-2",
        "en": "\"Now, I have to get on with my work. Go on and play. I have no more time.\"",
        "ko": "\"이제 난 일해야 하오. 가서 놀기나 하시오. 난 바쁜 몸이오.\""
      }
    ]
  },
  {
    "original_id": 2,
    "chunks": [
      {
        "tag": "P002-1",
        "en": "At first, every day that passed for Mary Lennox was exactly like the last. Every morning, she woke up in her tapestried room to find Martha kneeling by the hearth building her fire. Every morning, she ate her breakfast in the nursery, which had nothing entertaining in it.",
        "ko": "처음에 메리 레녹스에게 지나가는 하루하루는 전날과 완전히 똑같았다. 매일 아침 그녀는 태피스트리가 걸린 방에서 눈을 떴고, 마사가 벽난로 앞에 무릎을 꿇고 불을 피우고 있는 모습을 보았다. 매일 아침 그녀는 아무런 즐길 거리도 없는 유아실에서 아침 식사를 했다."
      },
      {
        "tag": "P002-2",
        "en": "After breakfast, she gazed out of the window at the vast moor that seemed to spread out in all directions and climb up to the sky. After staring for a while, she realized that if she didn't go outside, she would have to stay indoors and do nothing—so she went out. She didn't know that this was the best thing she could have done.",
        "ko": "아침을 먹고 나면 그녀는 창밖으로 사방으로 뻗어 나가 하늘까지 닿을 듯한 넓은 황무지를 바라보았다. 한참 동안 밖을 바라보다가, 그녀는 밖으로 나가지 않으면 실내에 머물며 아무것도 하지 않아야 한다는 것을 깨달았고, 그래서 밖으로 나갔다. 그녀는 이것이 자신이 할 수 있는 최선의 행동이었다는 것을 알지 못했다."
      },
      {
        "tag": "P002-3",
        "en": "She also didn't realize that when she began to walk quickly, or even run along the paths and down the avenue, she was stimulating her sluggish circulation and growing stronger by fighting the wind that swept down from the moor. She only ran to keep warm, and she hated the wind that rushed at her face, roaring and holding her back like an invisible giant.",
        "ko": "또한 오솔길과 대로를 따라 빠르게 걷거나 달리기 시작했을 때, 황무지에서 불어오는 바람과 싸우며 정체되어 있던 혈액 순환이 촉진되고 몸이 더 튼튼해지고 있다는 사실도 깨닫지 못했다. 그녀는 그저 몸을 따뜻하게 하려고 달렸을 뿐이었고, 보이지 않는 거인처럼 으르렁거리며 자신을 가로막고 얼굴로 세차게 몰아치는 바람이 싫었다."
      },
      {
        "tag": "P002-4",
        "en": "Yet the deep breaths of crisp, fresh air blowing over the heather filled her lungs. It was wonderful for her thin body, bringing a flush of red to her cheeks and brightening her dull eyes without her even realizing it.",
        "ko": "하지만 히더 꽃밭 위로 불어오는 맑고 신선한 공기를 깊이 들이마시자 그녀의 폐가 채워졌다. 그것은 그녀의 야윈 몸에 아주 좋았으며, 자신도 모르는 사이에 뺨에 붉은 생기를 돌게 하고 흐릿하던 눈을 반짝이게 해 주었다."
      }
    ]
  },
  {
    "original_id": 6,
    "chunks": [
      {
        "tag": "P006-1",
        "en": "\"It's the air of the moor that's giving you an appetite for your food,\" answered Martha. \"It's lucky for you that you've got food as well as an appetite.\"",
        "ko": "\"황무지 바람을 맞아서 입맛이 도는 거구먼유.\" 마사가 대답했다. \"입맛이 도는데 먹을 음식까지 있으니 아가씨는 참 운이 좋으셔유.\""
      },
      {
        "tag": "P006-2",
        "en": "\"There's been twelve of us in our cottage who had the appetite and nothing to put in our stomachs. You keep on playing outdoors every day, and you'll get some weight on your bones and you won't look so yellow.\"",
        "ko": "\"저희 오두막집에는 입맛은 꿀떡 같은데 뱃속에 채워 넣을 게 없는 식구가 열둘이나 되거든유. 매일 밖에서 놀다 보면 뼈에 살도 좀 붙고 얼굴에 누런 기운도 가실 거예유.\""
      }
    ]
  },
  {
    "original_id": 8,
    "chunks": [
      {
        "tag": "P008-1",
        "en": "\"Nothing to play with!\" exclaimed Martha.",
        "ko": "\"가지고 놀 게 없다고유!\" 마사가 외쳤다."
      },
      {
        "tag": "P008-2",
        "en": "\"Our children play with sticks and stones. They just run about, shout, and look at things.\"",
        "ko": "\"우리 동생들은 나뭇가지랑 돌멩이를 갖고 놀아유. 그냥 뛰어댕기고, 소리 지르고, 구경하면서 노는 거쥬.\""
      },
      {
        "tag": "P008-3",
        "en": "Mary did not shout, but she did look at things. There was nothing else to do. She walked round and round the gardens and wandered along the paths in the park.",
        "ko": "메리는 소리를 지르지는 않았지만, 구경은 했다. 달리 할 일이 없었기 때문이다. 그녀는 정원 주변을 돌고 또 돌며 공원의 오솔길을 거닐었다."
      },
      {
        "tag": "P008-4",
        "en": "Sometimes she looked for Ben Weatherstaff, but though she saw him at work several times, he was either too busy to look at her or too grumpy. Once, when she was walking toward him, he picked up his spade and turned away as if he did it on purpose.",
        "ko": "때로는 벤 웨더스태프를 찾아보기도 했지만, 그가 일하는 모습을 여러 번 보았음에도 그는 메리를 쳐다보지도 못할 만큼 너무 바쁘거나 혹은 심술이 나 있었다. 한번은 메리가 그를 향해 걸어가고 있을 때, 그는 마치 일부러 그러는 것처럼 삽을 집어 들고 몸을 돌려 버렸다."
      }
    ]
  },
  {
    "original_id": 9,
    "chunks": [
      {
        "tag": "P009-1",
        "en": "There was one place she visited more often than any other. It was the long walk outside the walled gardens. There were bare flowerbeds on either side of the path, and ivy grew thickly against the walls.",
        "ko": "그녀가 다른 어떤 곳보다 자주 찾는 곳이 한 군데 있었다. 담장으로 둘러싸인 정원 바깥쪽으로 길게 뻗은 산책로였다. 길 양옆에는 꽃이 없는 화단이 있었고, 담장에는 담쟁이덩굴이 무성하게 자라나 있었다."
      },
      {
        "tag": "P009-2",
        "en": "On one section of the wall, the creeping, dark green leaves were much bushier than anywhere else. It looked as though that part had been neglected for a very long time. The rest of the ivy had been clipped and kept neat, but at this lower end of the walk, it had not been trimmed at all.",
        "ko": "담장의 한 구역에는 짙은 초록색 담쟁이 잎사귀가 다른 어느 곳보다 훨씬 더 더부룩하게 덤불을 이루고 있었다. 그 부분은 오랫동안 방치된 것처럼 보였다. 나머지 담쟁이덩굴은 보기 좋게 다듬어져 있었지만, 산책로 아래쪽 끝부분은 전혀 손질이 되어 있지 않았다."
      }
    ]
  }
]

# Validation
with open(r'c:\git_repo\Book_apps\secret_garden\batches\batch_8.json', 'r', encoding='utf-8') as f:
    input_data = json.load(f)

assert len(output_data) == len(input_data), f"Count mismatch: {len(output_data)} vs {len(input_data)}"

for orig, processed in zip(input_data, output_data):
    assert orig['id'] == processed['original_id'], f"ID mismatch: {orig['id']} vs {processed['original_id']}"
    for chunk in processed['chunks']:
        en_cnt = count_sentences(chunk['en'])
        ko_cnt = count_sentences(chunk['ko'])
        assert en_cnt <= 3, f"EN sentences > 3 in {chunk['tag']}: {en_cnt} -> {chunk['en']}"
        assert ko_cnt <= 3, f"KO sentences > 3 in {chunk['tag']}: {ko_cnt} -> {chunk['ko']}"
        assert chunk['tag'].startswith(orig['tag']), f"Tag mismatch: {chunk['tag']} does not start with {orig['tag']}"
        assert len(chunk['en'].strip()) > 0
        assert len(chunk['ko'].strip()) > 0
        print(f"{chunk['tag']}: EN sents={en_cnt}, KO sents={ko_cnt} OK")

out_path = r'c:\git_repo\Book_apps\secret_garden\batches\batch_8_done.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print("\nValidation passed and file written successfully to:", out_path)

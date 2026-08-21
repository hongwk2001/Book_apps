import json
import re

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

def split_en(text):
    text = re.sub(r'\b(Dr|Mr|Mrs|Ms|Prof)\.', r'\1<DOT>', text)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9\"\'\u201c\u2018])', text.strip())
    sentences = [s.replace('<DOT>', '.') for s in sentences if s]
    return sentences

def split_ko(text):
    sentences = re.split(r'(?<=[.!?])\s+(?=[가-힣\"\'\u201c\u2018a-zA-Z0-9])', text.strip())
    sentences = [s for s in sentences if s]
    return sentences

# Pre-processing loop
for item in data:
    tag = item.get('tag')
    if tag == 'P003d':
        item['en'] = item['en'].replace(' Dr.', '').strip()
    elif tag == 'P003e':
        if not item['en'].startswith('Dr.'):
            item['en'] = 'Dr. ' + item['en']
    elif tag == 'P036':
        item['ko'] = item['ko'].replace("멀리서 늑대들의 울음소리가 들려옵니다. 눈 때문에", "멀리서 늑대들의 울음소리가 들려옵니다; 눈 때문에")
    elif tag == 'P053a':
        item['ko'] = item['ko'].replace('교수님은 내 손을 이끌어 안으로 들이며 말씀하셨습니다. "자, 보시오!', '교수님은 내 손을 이끌어 안으로 들이며 말씀하셨습니다, "자, 보시오!')

output = []
new_id = 1
for item in data:
    if 'en' not in item or not item['en']:
        output.append({
            "id": new_id,
            "original_id": item.get('id'),
            "tag": item.get('tag'),
            "en": item.get('en', ''),
            "ko": item.get('ko', ''),
            "is_header": item.get('is_header', False)
        })
        new_id += 1
        continue
    
    tag = item.get('tag', 'unknown')
    
    if tag == 'P020a':
        chunks_obj = [
            {"tag": "P020a-1", "en": "All day yesterday, we delved deep into the rugged mountain range and entered an endlessly rough and desolate land. Massive, menacing cliffs and countless roaring waterfalls were scattered about like the aftermath of a wild party thrown by Mother Nature. Madam Mina slept like the dead.", "ko": "어제 하루 종일 우리는 험준한 산맥 깊숙이 파고들며 끝없이 거칠고 황량한 땅으로 들어섰다. 거대하고 위협적인 절벽과 굉음을 내는 수많은 폭포들이 마치 대자연이 광란의 파티를 벌인 흔적처럼 널려 있었다. 미나 부인은 죽은 듯이 잠만 잤다."},
            {"tag": "P020a-2", "en": "Even as I satisfied my hunger alone, I couldn't bear to wake her up to feed her. I was suddenly terrified that the fatal curse harbored by this demonic place was seeping into the lady, who had shared the Count's terrible blood.", "ko": "나는 혼자 허기를 달래면서도 차마 밥을 먹이려고 부인을 깨울 수가 없었다. 나는 백작의 끔찍한 피를 나눠 마신 부인에게 이 마의 장소가 품은 치명적인 저주가 스며들고 있는 것은 아닌지 덜컥 겁이 났다."}
        ]
    elif tag == 'P020b':
        chunks_obj = [
            {"tag": "P020b-1", "en": "'Alright,' I muttered to myself. If she sleeps all day, I will definitely stay awake all night tonight.' Running along the rough, ancient dirt road, I unwittingly dropped my head and fell into a deep sleep.", "ko": "'좋아,' 나는 혼잣말을 되뇌었다. '부인이 하루 종일 잔다면, 나는 오늘 밤 기필코 뜬눈으로 밤을 새우겠어.' 거칠게 파인 고대의 낡은 흙길을 달리며, 나도 모르게 고개를 떨구고 깊은 잠에 빠져들었다."},
            {"tag": "P020b-2", "en": "When I opened my eyes with a start, overcome by terrible guilt once again, quite some time had already passed. Madam Mina was still asleep, and the sun was beginning to set. But the surrounding scenery had completely changed.", "ko": "또다시 지독한 죄책감에 번쩍 눈을 떴을 때는 이미 시간이 꽤 흘러 있었고, 미나 부인은 여전히 잠들어 있었으며 해는 뉘엿뉘엿 저물어가고 있었다. 하지만 주변 풍경은 완전히 달라져 있었다."}
        ]
    elif tag == 'P052a':
        chunks_obj = [
            {"tag": "P052a-1", "en": "November 6.—Knowing that Jonathan and the others were chasing us, it was around late afternoon when the Professor and I set out on the road heading east. The path was a steep downhill, but we couldn't hurry our steps because we had to carry a bunch of heavy blankets and coats. We couldn't risk being isolated without winter clothes in this biting blizzard.", "ko": "11월 6일.—조나단 일행이 쫓아오고 있다는 것을 알고 있었기에, 교수님과 내가 동쪽을 향해 길을 나선 것은 늦은 오후 무렵이었습니다. 길은 가파른 내리막이었지만 무거운 담요며 겉옷들을 잔뜩 짊어져야 했기에 걸음을 재촉할 수가 없었습니다. 이 매서운 눈보라 속에서 방한복도 없이 고립되는 위험을 감수할 수는 없었으니까요."},
            {"tag": "P052a-2", "en": "It was a complete wasteland with no trace of human presence, and not even a sign of people living beyond the pouring snow, so we also had to pack plenty of food.", "ko": "인적이라고는 찾아볼 수 없는 완벽한 황무지였고, 쏟아지는 눈발 너머로 사람이 사는 흔적조차 보이지 않아 식량도 단단히 챙겨야 했습니다."}
        ]
    elif tag == 'P052b':
        chunks_obj = [
            {"tag": "P052b-1", "en": "When we had walked down about a mile, exhausted from carrying the heavy load, I sat down to rest. When I looked back, the distinct silhouette of Dracula's castle touching the pitch-black sky came into view. Because we had come so deep down below the hill where the castle sat, even the Carpathian Mountains looked much lower than the castle.", "ko": "1마일쯤 걸어 내려왔을 때, 무거운 짐을 지고 걷느라 기진맥진한 나는 쉬기 위해 자리에 주저앉았습니다. 그때 뒤를 돌아보니, 시커먼 하늘과 맞닿은 드라큘라 성의 뚜렷한 실루엣이 시야에 들어왔습니다. 성이 자리 잡은 언덕 아래로 너무 깊숙이 내려온 탓에 카르파티아 산맥마저 성보다 훌쩍 낮아 보였습니다."}
        ]
    elif tag == 'P052c':
        chunks_obj = [
            {"tag": "P052c-1", "en": "Towering a full thousand feet high at the top of a sheer cliff, completely cut off from the surrounding mountains by massive, deeply carved valleys, the magnificent figure of that bizarre castle caught my eye at a glance. An indescribably rough and eerie aura lingered there. From far away, the sound of starving wolves howling could be heard.", "ko": "깎아지른 듯한 절벽 꼭대기에서 무려 1천 피트나 우뚝 솟아오른 채, 깊게 팬 거대한 골짜기들로 주변 산맥들과 완전히 단절된 그 기괴한 성의 웅장한 자태가 한눈에 들어왔습니다. 그곳에는 말로 다 할 수 없이 거칠고 섬뜩한 기운이 맴돌았습니다. 저 멀리서 굶주린 늑대들이 울부짖는 소리가 들려왔습니다."},
            {"tag": "P052c-2", "en": "Although it sounded somewhat muffled because it came from very far away and the pouring snow swallowed the sound, it was full of chilling terror. Seeing Dr. Van Helsing scanning the surroundings with sharp eyes, it was clear he was looking for a good strategic point to defend against a possible attack. The roughly carved road continued endlessly downhill, and we carefully felt our way along that blurry trail, pushing through the piled-up snow.", "ko": "아주 먼 곳에서 들려오는 데다 쏟아지는 눈이 소리를 삼켜버려 다소 둔탁하게 들렸음에도, 그 소리는 소름 끼치는 공포로 가득했습니다. 반 헬싱 박사님이 날카로운 눈으로 주변을 살피는 모습을 보니, 혹시 모를 습격에 대비해 방어하기 좋은 전략적 요충지를 찾고 계신 것이 분명했습니다. 거칠게 팬 도로는 끝없이 내리막으로 이어졌고, 우리는 소복이 쌓인 눈을 헤치며 그 흐릿한 흔적을 조심스레 더듬어 나갔습니다."}
        ]
    else:
        en_sents = split_en(item['en'])
        ko_sents = split_ko(item['ko'])
        
        if len(en_sents) != len(ko_sents):
            print(f"Mismatched: {tag} EN({len(en_sents)}) KO({len(ko_sents)})")
            chunks_obj = [{
                "tag": f"{tag}-1",
                "en": item['en'],
                "ko": item['ko']
            }]
        else:
            chunks_obj = []
            chunk_idx = 1
            for i in range(0, len(en_sents), 3):
                en_chunk = " ".join(en_sents[i:i+3])
                ko_chunk = " ".join(ko_sents[i:i+3])
                chunks_obj.append({
                    "tag": f"{tag}-{chunk_idx}",
                    "en": en_chunk,
                    "ko": ko_chunk
                })
                chunk_idx += 1
    
    out_item = {
        "id": new_id,
        "original_id": item.get('id'),
        "chunks": chunks_obj
    }
    output.append(out_item)
    new_id += 1

with open(r'C:\git_repo\Book_apps\dracula\src\main\assets\books\ch_27.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)


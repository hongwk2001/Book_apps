# Book Paragraph Splitting & Integrity Audit Log

This document logs every paragraph split operation across all book assets. It provides a complete audit trail including original text, split chunks, character invariant verification, and ID shift tracking.


## Audit Entry: 2026-09-02 16:19:57
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_01.json`
- **Original Target**: ID 3 (`P003_1`)
- **Reason for Split**: Opening paragraph was 8 sentences (578 chars EN, 326 chars KO).
- **Split Strategy**: 4 symmetric 2-sentence bite-sized chunks.
- **Verification Status**: PASSED (100% character-level invariant preserved, 0 missing/added characters).
- **Total Chapter Paragraphs**: Shifted from 35 to 38. Sequential IDs cleanly updated from 1 to 38.

### Split Details:

#### Chunk 1 (`P003_1` / ID 3)
- **EN**: `It was the best of times and the worst of times. It was the age of wisdom and the age of foolishness.`
- **KO**: `최고의 시절이자 최악의 시절이었다. 지혜의 시대이자 어리석음의 시대였다.`

#### Chunk 2 (`P003_2` / ID 4)
- **EN**: `It was the century of belief and the century of disbelief. It was the season of light and the season of darkness.`
- **KO**: `믿음의 세기이자 불신의 세기였다. 빛의 계절이자 어둠의 계절이었다.`

#### Chunk 3 (`P003_3` / ID 5)
- **EN**: `It was the spring of hope and the winter of despair. We had everything before us, yet we had nothing.`
- **KO**: `희망의 봄이자 절망의 겨울이었다. 우리 앞에는 모든 것이 있었지만 또 아무것도 없었다.`

#### Chunk 4 (`P003_4` / ID 6)
- **EN**: `We were all going straight to heaven, yet we were also going straight in the opposite direction. In short, that period was so similar to the present that even the loudest authorities of the time insisted it be judged, for better or worse, only in superlatives.`
- **KO**: `우리 모두 천국으로 곧장 가고 있었지만, 또 반대 방향으로 곧장 가고 있기도 했다. 요컨대, 그 시대는 지금의 시대와 너무도 비슷해서, 당시 가장 목소리 큰 권위자들조차 좋든 나쁘든 오직 최상급으로만 그 시대를 평가해야 한다고 주장했다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_04.json`
- **Original Target**: ID 149 (`P070`)
- **Reason for Split**: Paragraph was 9 sentences (758 chars EN).
- **Split Strategy**: Split into 3 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P070_1`)
- **EN**: `"As I was saying: suppose Monsieur Manette did not die. Suppose he simply vanished one day, silently and without a trace. Suppose he was taken away.`
- **KO**: `"제가 말씀드리고 있었듯이: 마네트 씨가 죽지 않았다고 가정해 보십시오. 그가 어느 날 조용히 흔적도 없이 사라졌다고 가정해 봅시다. 그가 어디론가 끌려갔다고 가정해 봅시다.`
#### Chunk 2 (`P070_2`)
- **EN**: `It would be easy enough to guess which terrible place he had been sent to, even if no one could prove it. Suppose he had an enemy, someone with the power to sign blank arrest warrants and lock anyone away in a silent prison forever. That power was so feared in France that even the bravest people refused to whisper about it.`
- **KO**: `비록 아무도 그것을 증명할 수 없었더라도, 그가 어떤 끔찍한 곳으로 보내졌는지 짐작하기란 충분히 쉬웠을 것입니다. 그에게 백지 체포 영장에 서명하여 누구든 영원히 소리 없는 감옥에 가둘 수 있는 권력을 가진 적이 있었다고 가정해 봅시다. 그 권력은 프랑스에서 너무나 두려운 것이어서 가장 용감한 사람들조차 그것에 대해 속삭이기를 거부했습니다.`
#### Chunk 3 (`P070_3`)
- **EN**: `Suppose his wife went to the king, the queen, the court, and the church, begging for any news of her husband. All of that begging would come to nothing. If all of this were true, then the story of your father would be the story of this unfortunate gentleman, the Doctor of Beauvais."`
- **KO**: `그의 아내가 남편의 소식을 조금이라도 얻기 위해 왕과 왕비, 궁정, 교회에 찾아가 애원했다고 가정해 봅시다. 그 모든 애원은 수포로 돌아갔을 것입니다. 이 모든 것이 사실이라면, 아가씨 아버님의 이야기는 바로 이 불행한 신사, 보베의 의사 이야기일 것입니다."`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_05.json`
- **Original Target**: ID 19 (`P007_1`)
- **Reason for Split**: Paragraph was 3 sentences (625 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P007_1`)
- **EN**: `And now that the cloud settled once more on Saint Antoine—which a fleeting gleam of joy had temporarily driven from its gloomy face—the darkness grew heavy again.`
- **KO**: `잠깐의 빛줄기로 잠시 걷혔던 구름이 생 앙투안 위에 다시 드리우자, 그 어둠은 몹시 무거웠다.`
#### Chunk 2 (`P007_2`)
- **EN**: `Cold, dirt, sickness, ignorance, and poverty were the attendants in waiting on this holy presence—all of them nobles of great power, but most especially poverty. Samples of a people who had undergone terrible grinding and regrinding in the mill—and certainly not in the mythical mill that ground old people young—shivered at every corner, passed in and out of every doorway, looked from every window, and fluttered in every shred of clothing that the wind shook.`
- **KO**: `추위, 오물, 질병, 무지, 그리고 빈곤은 그 거룩한 존재를 모시는 시종들이었으며, 그들 모두 막강한 권력을 지닌 귀족들이었지만 특히나 마지막 존재인 빈곤이 그러했다. 맷돌에 들어가 무시무시하게 갈리고 또 갈린—노인을 젊게 만들어준다는 전설 속의 방앗간이 결코 아닌—사람들의 표본들이 골목 구석마다 웅크려 떨고 있었고, 문간마다 드나들었으며, 창문마다 내다보았고, 바람에 나부끼는 누더기 옷자락마다 퍼덕거렸다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_07.json`
- **Original Target**: ID 13 (`P005_2`)
- **Reason for Split**: Paragraph was 4 sentences (507 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P005_1`)
- **EN**: `After pushing open a stubborn door that shook with a weak rattle, you fell down two steps into the bank. There you found yourself in a miserable little shop with two small counters.`
- **KO**: `약하게 덜거덕거리며 흔들리는 뻑뻑한 문을 밀고 들어가면, 계단 두 개를 내려가 은행 안으로 들어가게 된다. 그곳에는 작은 카운터 두 개가 있는 초라하고 작은 상점이 있다.`
#### Chunk 2 (`P005_2`)
- **EN**: `The oldest clerks working there would take your check with hands that shook so much the paper rustled like leaves, while they examined your signature by the dirtiest windows. These windows were constantly sprayed with mud from Fleet Street and made even darker by heavy iron bars and the shadow of the nearby Temple Bar gate.`
- **KO**: `그곳에서 일하는 가장 나이 많은 직원들은 당신의 수표를 종이가 나뭇잎처럼 바스락거릴 정도로 손을 심하게 떨며 받을 것이고, 가장 더러운 창문 옆에서 당신의 서명을 확인할 것이다. 이 창문들은 항상 플리트 스트리트에서 튄 진흙으로 뒤덮여 있었고, 무거운 철창과 근처의 템플 바 게이트의 그림자 때문에 훨씬 더 어두웠다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_09.json`
- **Original Target**: ID 12 (`P002_11`)
- **Reason for Split**: Paragraph was 3 sentences (598 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P002_1`)
- **EN**: `That the noble example of this flawless and unimpeachable witness for the Crown—to refer to whom, however unworthily, was an honor—had communicated itself to the prisoner’s servant, and had engendered in him a holy determination to examine his master’s table drawers and pockets, and secrete his papers.`
- **KO**: `국왕 측의 이 티 없고 흠잡을 데 없는 증인—아무리 보잘것없는 표현으로 언급하더라도 영광일 따름인 그 증인—의 숭고한 본보기가 피고인의 하인에게도 전해져, 주인의 서랍과 주머니를 뒤져 서류를 몰래 빼돌려야겠다는 거룩한 결의를 품게 만들었다는 것.`
#### Chunk 2 (`P002_2`)
- **EN**: `That he (Mr. Attorney-General) was prepared to hear some attempts to disparage this admirable servant; but that, in a general way, he preferred him to his own brothers and sisters, and honored him more than his own father and mother. And that he confidently called upon the jury to do likewise.`
- **KO**: `그리고 자신(검찰총장)은 이 훌륭한 하인을 깎아내리려는 시도가 있으리라는 점을 각오하고 있으나, 대체로 자신은 자기 친형제자매보다 이 하인을 더 아끼며, 자기 친부모보다 그를 더 존경한다는 것. 그러므로 배심원 여러분도 기꺼이 자신과 같은 마음을 품어줄 것을 확신을 갖고 촉구한다는 내용이었다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_13.json`
- **Original Target**: ID 44 (`P010_3`)
- **Reason for Split**: Paragraph was 3 sentences (755 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P010_1`)
- **EN**: `This obsession with dressing up like it was a costume party trickled all the way down from the royal Palace of the Tuileries, past Monseigneur and the entire Court, through the government chambers, the courts of justice, and all of high society (ignoring the poor people in rags), until it reached the common executioner.`
- **KO**: `마치 가장무도회인 것처럼 차려입는 것에 대한 이 집착은 왕궁인 튈르리 궁전에서부터 시작되어, 몽세뇌르와 궁정 전체를 지나, 정부 기관들, 사법 재판소들, 그리고 상류 사회 전체(누더기를 입은 가난한 사람들은 무시한 채)로 흘러내려 와, 마침내 흔한 사형 집행인에게까지 이르렀다.`
#### Chunk 2 (`P010_2`)
- **EN**: `To keep the glamorous illusion going, the executioner had to do his grim job with curled and powdered hair, wearing a gold-laced coat, dress shoes, and white silk stockings. At the gallows and the breaking wheel—the executioner's axe was rarely used—Monsieur Paris, which is what his fellow executioners from the provinces like Monsieur Orleans respectfully called him, presided over the executions in this delicate and fancy outfit.`
- **KO**: `그 화려한 환상을 유지하기 위해 사형 집행인은 구부러지고 분칠된 머리에 금색 끈이 달린 코트, 정장 구두, 그리고 하얀 실크 스타킹을 신고 그의 끔찍한 직무를 수행해야 했다. 교수대와 수레바퀴 처형대에서—사형 집행인의 도끼는 거의 사용되지 않았다—지방에서 온 오를레앙 씨와 같은 그의 동료 사형 집행인들이 정중하게 파리 씨라고 불렀던 그는, 이 섬세하고 화려한 복장으로 처형을 주재했다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_21.json`
- **Original Target**: ID 178 (`P084_2`)
- **Reason for Split**: Paragraph was 4 sentences (608 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P084_1`)
- **EN**: `If he needed a King and Queen to recover, he was lucky to have his cure nearby. Soon, the large-faced King and the fair-faced Queen arrived in their golden coach, accompanied by the shining stars of their Court—a glittering crowd of laughing ladies and elegant lords.`
- **KO**: `만약 그가 기력을 회복하기 위해 국왕과 왕비가 필요했다면, 가까운 곳에 그 치유책이 있어서 다행이었다. 곧, 큰 얼굴의 국왕과 고운 얼굴의 왕비가 궁정의 빛나는 별들—웃고 있는 귀부인들과 우아한 귀족들의 화려한 무리—을 동반하고 황금 마차를 타고 도착했다.`
#### Chunk 2 (`P084_2`)
- **EN**: `The road-mender soaked in the jewels, silks, powder, splendor, and the gracefully snobby figures and handsome, arrogant faces of both sexes. He became so temporarily intoxicated by it all that he shouted, "Long live the King, long live the Queen, long live everybody and everything!" as if he had never even heard of the mysterious Jacques.`
- **KO**: `도로 보수공은 보석, 비단, 분, 화려함, 그리고 남녀 모두의 우아하게 거만한 자태와 잘생기고 오만한 얼굴들에 흠뻑 빠져들었다. 그는 그 모든 것에 일시적으로 몹시 취한 나머지, 마치 미스터리한 자크에 대해 들어본 적도 없는 것처럼 "국왕 만세, 왕비 만세, 모든 사람과 모든 것들 만세!"라고 소리쳤다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 117 (`P058`)
- **Reason for Split**: Paragraph was 6 sentences (686 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P058_1`)
- **EN**: `They rushed through dark, gloomy vaults that had never seen sunlight, passing awful doors to dark cages. They ran down huge flights of stairs and then climbed up steep, rough brick and stone steps that looked more like dry waterfalls than staircases. Defarge, the jailer, and Jacques Three linked arms and moved as fast as they could.`
- **KO**: `그들은 햇빛을 본 적 없는 어둡고 우울한 지하 저장고를 서둘러 지나며 끔찍한 문들을 거쳐 어두운 철창으로 향했다. 그들은 거대한 계단을 뛰어내려간 다음, 계단이라기보다는 마른 폭포에 가까워 보이는 가파르고 거친 벽돌과 돌계단을 기어올랐다. 드파르지, 간수, 그리고 자크 삼세는 팔을 끼고 가능한 한 빨리 움직였다.`
#### Chunk 2 (`P058_2`)
- **EN**: `At first, the flooding crowd would bump into them and sweep past, but by the time they finished going down and started winding their way up a tower, they were all alone. Surrounded by massive walls and arches, the crazy storm inside and outside the fortress sounded muffled. It was like the noise they had just escaped had almost ruined their hearing.`
- **KO**: `처음에는 쏟아져 들어오는 군중들이 그들과 부딪히며 지나갔지만, 그들이 아래로 내려가는 것을 마치고 탑을 향해 굽이쳐 올라가기 시작할 때쯤에는 그들뿐이었다. 거대한 벽과 아치로 둘러싸여, 요새 안팎의 미친 폭풍은 웅얼거리는 듯 들렸다. 마치 그들이 방금 벗어난 소음이 그들의 청력을 거의 앗아간 것 같았다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 144 (`P074`)
- **Reason for Split**: Paragraph was 6 sentences (673 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P074_1`)
- **EN**: `In the screaming, angry chaos surrounding the grim old officer in his gray coat and red medal, only one figure stood perfectly steady: a woman. "Look, there's my husband!" she yelled, pointing at him. "See Defarge!" She stood firmly next to the grim old officer and stayed glued to him as Defarge and the crowd dragged him through the streets.`
- **KO**: `회색 코트를 입고 붉은 훈장을 단 무뚝뚝한 노장교를 둘러싼 비명 지르고 분노하는 혼돈 속에서, 오직 단 한 사람, 한 여자만이 완벽하게 흔들림 없이 서 있었다. "보라, 저기 내 남편이 있다!" 그녀가 그를 가리키며 소리쳤다. "드파르지를 보라!" 그녀는 무뚝뚝한 노장교 옆에 굳건히 서서, 드파르지와 군중이 그를 거리를 통해 끌고 갈 때 그에게 딱 붙어 연이어 있었다.`
#### Chunk 2 (`P074_2`)
- **EN**: `She stayed right next to him as they neared City Hall and people started hitting him from behind. She didn't budge even when a rain of stabs and heavy blows fell on him. She was so close that when he finally dropped dead, she suddenly sprang into action, stepped on his neck, and used her cruel, ready knife to hack off his head.`
- **KO**: `그들이 시청에 가까워지고 사람들이 뒤에서 그를 때리기 시작했을 때도 그녀는 그의 바로 옆에 머물렀다. 수많은 찌름과 거친 구타가 그에게 쏟아질 때조차 그녀는 꿈쩍도 하지 않았다. 그녀는 너무나 가까이 있어서, 마침내 그가 쓰러져 죽었을 때 갑자기 행동에 나서 그의 목을 밟고 잔인하게 준비된 칼로 그의 머리를 베어냈다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_31.json`
- **Original Target**: ID 200 (`P111_2`)
- **Reason for Split**: Paragraph was 5 sentences (541 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P111_1`)
- **EN**: `There was one woman dressed in black, leaning near a window, with light shining on her golden hair, and she looked like... Let's ride on again, for God's sake, through the lit-up villages where everyone is awake!`
- **KO**: `검은 옷을 입고 창가 근처에 기대어 금발 머리에 빛이 비치는 한 여자가 있었는데, 그녀는 마치... 제발, 모두가 깨어 있는 불이 켜진 마을들을 지나 다시 말을 달려가자!`
#### Chunk 2 (`P111_2`)
- **EN**: `He made shoes, he made shoes, he made shoes. Five paces by four and a half.” With these random thoughts spinning in his mind, the prisoner walked faster and faster, stubbornly counting his steps. The roar of the city outside still sounded like muffled drums, but now he imagined hearing the cries of voices he knew in the noise.`
- **KO**: `그는 신발을 만들었다, 그는 신발을 만들었다, 그는 신발을 만들었다. 다섯 걸음에 네 걸음 반.” 이런 무작위적인 생각들이 그의 마음속에서 맴도는 가운데, 수감자는 점점 더 빨리 걸으며, 고집스럽게 발걸음을 세었다. 밖에서 들리는 도시의 굉음은 여전히 둔탁한 북소리처럼 들렸지만, 이제 그는 소음 속에서 자신이 아는 목소리들의 외침이 들린다고 상상했다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_34.json`
- **Original Target**: ID 32 (`P010_2`)
- **Reason for Split**: Paragraph was 7 sentences (819 chars EN).
- **Split Strategy**: Split into 3 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P010_1`)
- **EN**: `The new era had begun. The king was put on trial, condemned, and beheaded. The new Republic of Liberty, Equality, Fraternity, or Death declared that it would fight for victory or death against the entire armed world.`
- **KO**: `새로운 시대가 시작되었다. 왕은 재판을 받고, 유죄 판결을 받고, 참수되었다. '자유, 평등, 박애, 아니면 죽음'이라는 새로운 공화국은 무장한 전 세계에 맞서 승리 아니면 죽음을 걸고 싸우겠다고 선언했다.`
#### Chunk 2 (`P010_2`)
- **EN**: `A black flag waved day and night from the massive towers of Notre Dame. Three hundred thousand men were called up to rise against the earth's tyrants, and they sprang up from every corner of France.`
- **KO**: `노트르담의 거대한 탑에서는 밤낮으로 검은 깃발이 나부꼈다. 지구의 폭군들에 맞서 봉기할 30만 명의 병사들이 소집되었고, 그들은 프랑스 전역에서 솟아올랐다.`
#### Chunk 3 (`P010_3`)
- **EN**: `It was as if dragon's teeth had been scattered everywhere and sprouted soldiers equally on hills and plains, on rocky ground, in gravel, and in rich mud. They rose under the bright southern skies and the cloudy northern skies, in wild moors and forests, in vineyards and olive groves, among short grass and leftover cornstalks, along the fertile banks of wide rivers, and in the sand along the seashore.`
- **KO**: `마치 용의 이빨이 사방에 뿌려져 언덕과 평원, 바위투성이 땅, 자갈밭, 비옥한 진흙 위에서 똑같이 병사들로 싹을 틔운 것 같았다. 그들은 눈부신 남쪽 하늘과 구름 낀 북쪽 하늘 아래에서, 황량한 황무지와 숲, 포도밭과 올리브 숲에서, 짧은 풀밭과 남은 옥수수 줄기 사이에서, 넓은 강가의 비옥한 둑을 따라, 그리고 해변의 모래사장에서 일어났다.`

---

## Audit Entry: 2026-09-02 16:22:24
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_38.json`
- **Original Target**: ID 11 (`P004`)
- **Reason for Split**: Paragraph was 6 sentences (436 chars EN).
- **Split Strategy**: Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P004_1`)
- **EN**: `The room was thick with smoky lamplight. Customers sat smoking pipes and fiddling with worn cards and yellow dominoes. A shirtless, soot-covered worker read a newspaper aloud to a small crowd.`
- **KO**: `방 안은 연기 자욱한 램프 불빛으로 탁했다. 손님들은 파이프를 피우고 낡은 카드와 누런 도미노를 만지작거리며 앉아 있었다. 셔츠를 벗은 채 그을음을 뒤집어쓴 노동자가 작은 무리에게 큰 소리로 신문을 읽어주고 있었다.`
#### Chunk 2 (`P004_2`)
- **EN**: `Weapons lay scattered around the tables. Two or three customers were slumped asleep, looking like sleeping bears in their heavy black coats. Taking all of this in, the two English customers walked up to the counter and showed what they wanted.`
- **KO**: `테이블 주변에는 무기들이 널려 있었다. 서너 명의 손님들은 무거운 검은 코트를 입고 잠을 자는 곰처럼 축 늘어져 잠들어 있었다. 이 모든 것을 눈에 담으며, 두 명의 영국인 손님은 카운터로 걸어가서 자신들이 원하는 것을 가리켰다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_02.json`
- **Original Target**: ID 18 (`P006`)
- **Category**: Category 2 (Asymmetric)
- **Reason for Split**: Paragraph was 338 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P006_1`)
- **EN**: `The Dover mail was running normally. The guard suspected the passengers. The passengers suspected each other and the guard. They all suspected everyone else. The only person who wasn't suspicious was the coachman.`
- **KO**: `도버 우편물은 정상적으로 운행되고 있었습니다. 호위병은 승객들을 의심했습니다. 승객들은 서로와 호위병을 의심했습니다. 그들은 모두 다른 모든 사람을 의심했습니다. 유일하게 의심하지 않은 사람은 마부였습니다.`
#### Chunk 2 (`P006_2`)
- **EN**: `He was simply certain about one thing: the horses were not fit for this journey. He could have sworn that on the Holy Bible.`
- **KO**: `그는 단 한 가지에 대해 확신하고 있었습니다. 말들이 이 여행에 적합하지 않다는 것이었습니다. 그는 성경에 대고 그것을 맹세할 수 있었습니다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_03.json`
- **Original Target**: ID 61 (`P028`)
- **Category**: Category 2 (Asymmetric)
- **Reason for Split**: Paragraph was 310 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P028_1`)
- **EN**: `Dig. Dig. Dig. Until one of the other passengers shifted restlessly, snapping him back to reality.`
- **KO**: `파고, 파고, 또 팠다. 다른 승객들 중 한 명이 쉴 새 없이 뒤척이며 그를 다시 현실로 끌어올릴 때까지.`
#### Chunk 2 (`P028_2`)
- **EN**: `He would roll the window back up. He would hook his arm through the strap again. He would try to focus on the two sleeping figures nearby. But soon his mind would drift away. Back to the bank. Back to the grave.`
- **KO**: `그는 창문을 다시 올리곤 했다. 그는 팔을 가죽 끈에 다시 걸었다. 그는 근처에서 잠든 두 형체에 집중하려고 애썼다. 그러나 곧 그의 마음은 멀리 떠내려갔다. 다시 은행으로. 다시 무덤으로.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_13.json`
- **Original Target**: ID 38 (`P008_4`)
- **Category**: Category 2 (Asymmetric)
- **Reason for Split**: Paragraph was 637 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P008_1`)
- **EN**: `Besides these fanatics, there were three others who had joined a different sect that resolved matters with mystical jargon about "the Center of Truth." They held that Man had strayed from the Center of Truth—which required little proof—but had not yet escaped its Circumference, and that he must be kept from flying beyond this perimeter and even pushed back into the Center through fasting and spiritual visions.`
- **KO**: `이들 광신도들 외에도 또 다른 종파에 뛰어든 세 사람이 있었는데, 그 종파는 '진리의 중심'에 관한 횡설수설로 문제를 얼버무렸다. 그들은 인간이 진리의 중심에서 벗어났으나—이는 굳이 증명할 필요도 없었지만—그 원주 밖으로까지 벗어난 것은 아니며, 단식과 영혼과의 접신을 통해 원주 밖으로 날아가지 못하게 막고 중심부로 다시 밀어 넣어야 한다고 주장했다.`
#### Chunk 2 (`P008_2`)
- **EN**: `Naturally, there was much conversing with spirits among them, producing a great deal of good that remained entirely invisible. But the comforting part was that everyone in Monseigneur's grand mansion was impeccably dressed.`
- **KO**: `따라서 그들 사이에서는 영혼들과의 대화가 활발히 이어졌고, 그 덕에 엄청난 효험이 있었으나 그것이 겉으로 드러나는 일은 결코 없었다. 그러나 다행스러운 것은 몽세뇌르의 웅장한 저택에 모인 모든 이들이 완벽하게 차려입고 있었다는 점이었다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 30 (`P011_1`)
- **Category**: Category 3A (2-Sentence Mega)
- **Reason for Split**: Paragraph was 567 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P011_1`)
- **EN**: `Mr. Stryver, exuding the most offensive kind of condescension from every pore, had marched these three young gentlemen before him like sheep to the quiet corner in Soho and offered them as pupils to Lucie’s husband, delicately saying, "Hello! Here are three lumps of bread and cheese for your marriage picnic, Darnay!"`
- **KO**: `온몸의 땀구멍마다 가장 불쾌한 오만함을 풍기던 스트라이버 씨는 이 세 젊은 신사를 양 떼처럼 몰고 소호의 한적한 구석으로 데려가 루시의 남편에게 제자로 삼으라며 제안했었다. 그는 '고상하게' 말하기를, "이보게! 자네의 결혼 소풍에 보탬이 될 빵과 치즈 세 덩이라네, 다네이!"라고 했다.`
#### Chunk 2 (`P011_2`)
- **EN**: `The polite rejection of these three lumps of bread and cheese had inflated Mr. Stryver with indignation, which he later turned to advantage when training the young gentlemen by warning them to beware of the pride of beggars, like that tutor fellow.`
- **KO**: `이 세 덩이의 빵과 치즈에 대한 정중한 거절은 스트라이버 씨를 분노로 잔뜩 부풀어 오르게 만들었고, 그는 나중에 이 젊은 신사들을 교육할 때 그 가정교사 녀석 같은 거지들의 오만함을 조심하라고 훈계함으로써 그 분노를 유용하게 써먹었다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 31 (`P011_3`)
- **Category**: Category 3A (2-Sentence Mega)
- **Reason for Split**: Paragraph was 572 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P011_1`)
- **EN**: `Over his rich wine, he was also in the habit of boasting to Mrs. Stryver about the tricks Mrs. Darnay had once used to "catch" him, and about his own equally sharp tricks that had kept him from being caught.`
- **KO**: `그는 또한 진한 와인을 마시며 아내 스트라이버 부인에게, 다네이 부인이 한때 자신을 '낚기' 위해 썼던 술수들과, 자신이 '낚이지' 않도록 맞받아친 빼어난 술수들에 대해 열변을 토하곤 했다.`
#### Chunk 2 (`P011_2`)
- **EN**: `Some of his King's Bench acquaintances, who occasionally shared the wine and heard the lie, excused him by saying that he had told it so often he actually believed it himself—which is certainly such an incorrigible worsening of an already bad offense that it would justify hauling such an offender off to some suitably secluded spot and hanging him out of the way.`
- **KO**: `때때로 그 진한 와인을 함께 마시며 거짓말을 듣던 왕좌재판소의 지인들은, 그가 하도 자주 그 이야기를 하다 보니 스스로도 그것을 믿게 된 것이라며 변명해 주었다—하지만 이는 원래 나쁜 잘못을 도저히 구제할 수 없을 정도로 악화시키는 일이라, 그런 자를 한적한 곳으로 끌고 가 목을 매달아 치워버려도 마땅할 정도였다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_28.json`
- **Original Target**: ID 39 (`P021_1`)
- **Category**: Category 3A (2-Sentence Mega)
- **Reason for Split**: Paragraph was 518 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P021_1`)
- **EN**: `The men were terrifying in the bloodthirsty anger with which they looked from windows, seized whatever weapons they had, and came pouring down into the streets; but the women were a sight to chill the bravest heart.`
- **KO**: `창밖을 내다보며 손에 잡히는 무기를 들고 거리로 쏟아져 나오는 남자들의 잔혹한 분노도 끔찍했지만, 여자들의 모습은 가장 용감한 사람의 간담도 서늘하게 할 정도였다.`
#### Chunk 2 (`P021_2`)
- **EN**: `Leaving behind what little household work their extreme poverty allowed, leaving their children, and leaving their sick and elderly crouching famished and naked on the bare ground, they rushed out with disheveled hair, driving one another and themselves into madness with the wildest cries and actions.`
- **KO**: `지독한 빈곤이 허락한 보잘것없는 집안일도 팽개치고, 굶주리고 헐벗은 채 맨땅에 웅크리고 있는 자식들과 노인, 병자들을 뒤로한 채, 여자들은 머리를 풀어헤치고 뛰쳐나와 거친 비명과 광란의 몸짓으로 서로를, 그리고 스스로를 미치도록 부추겼다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_40.json`
- **Original Target**: ID 7 (`P004_1`)
- **Category**: Category 3A (2-Sentence Mega)
- **Reason for Split**: Paragraph was 510 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P004_1`)
- **EN**: `“One cloudy, moonlit night, in the third week of December (I think the twenty-second of the month) in the year 1757, I was walking along a secluded part of the quay by the Seine to refresh myself in the frosty air, an hour’s distance from my residence in the Street of the School of Medicine, when a carriage approached rapidly behind me.`
- **KO**: `“1757년 12월 셋째 주(내 생각으로는 그달 22일이었던 것 같다), 구름 낀 달밤에 나는 의과대학 거리에 있는 거처에서 한 시간쯤 떨어진 센강 변의 호젓한 부둣가를 거닐며 차가운 공기로 머리를 식히고 있었다. 그때 뒤쪽에서 마차 한 대가 아주 빠른 속도로 달려왔다.`
#### Chunk 2 (`P004_2`)
- **EN**: `As I stepped aside to let that carriage pass, apprehensive that it might otherwise run me down, a head was put out at the window, and a voice called to the driver to stop.`
- **KO**: `마차에 치일까 염려되어 비켜서자, 창밖으로 머리를 내민 누군가가 마부에게 멈추라고 소리쳤다.`

---

## Audit Entry: 2026-09-02 16:28:37
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_40.json`
- **Original Target**: ID 114 (`P055`)
- **Category**: Category 2 (Asymmetric)
- **Reason for Split**: Paragraph was 791 chars EN.
- **Split Strategy**: Sliced via Substring Anchor into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P055_1`)
- **EN**: `“‘We were robbed so badly by that man standing there, just as all of us common dogs are by those superior Beings, taxed by him without mercy, forced to work for him without pay, forced to grind our grain at his mill, forced to feed dozens of his tame birds on our poor crops, while we were forbidden under pain of death to keep a single tame bird of our own.`
- **KO**: `“‘우리 평범한 개들 모두가 저 우월한 존재들에게 당하는 것처럼, 우리는 저기 서 있는 자에게 지독하게 약탈당했습니다. 무자비하게 세금을 뜯기고, 돈도 받지 못하고 억지로 일해야 했으며, 저 자의 방앗간에서 곡식을 빻아야 했고, 우리의 초라한 농작물로 저 자의 수십 마리 길들인 새들을 먹여야 했습니다. 그러면서 정작 우리는 죽음의 고통을 무릅쓰지 않고는 단 한 마리의 새도 기를 수 없었습니다.`
#### Chunk 2 (`P055_2`)
- **EN**: `We were plundered to the point that if we happened to have a piece of meat, we ate it in fear with the door locked and the shutters closed so his servants wouldn't see it and take it from us. I tell you, we were so robbed and hunted, and made so poor, that our father told us it was a terrible thing to bring a child into the world. He said we should pray that our women would be barren and our miserable family line would die out!’`
- **KO**: `우리는 고기 한 점이라도 생기면 행여나 하인들이 보고 빼앗아갈까 봐 문을 잠그고 덧문을 닫은 채 두려움 속에서 먹어야 할 정도로 수탈당했습니다. 정말이지 우리는 너무도 빼앗기고, 쫓기고, 가난해져서, 아버지께서는 이 세상에 아이를 낳는 것은 끔찍한 일이라고 말씀하셨습니다. 우리 여인들이 불임이 되어 이 비참한 가문이 끊어지게 해달라고 기도해야 한다고 하셨습니다!’`

---

## Audit Entry: 2026-09-02 16:44:42
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_04.json`
- **Original Target**: ID 209 (`P090_1`)
- **Category**: Category 3B (ESL Learner Optimized Split)
- **Split Strategy**: Miss Pross entrance (ESL split adding 'She' / '그녀는')
- **Verification Status**: PASSED (Smooth bilingual sentence alignment, 0 broken fragments).
### Split Chunks:
#### Chunk 1 (`P090_1`)
- **EN**: `A wild-looking woman—whom even in his agitation Mr. Lorry observed to be entirely dressed in red, with red hair, wearing remarkably tight-fitting clothes, and having on her head a most wonderful bonnet like a Grenadier wooden measure (and a generous measure at that) or a great Stilton cheese—came running into the room ahead of the inn servants.`
- **KO**: `로리 씨가 경황없는 와중에도 온통 붉은빛 옷차림에 붉은 머리칼, 기묘할 정도로 몸에 꽉 끼는 옷을 입고 머리에는 근위병의 나무 됫박(그것도 아주 큼직한 됫박)이나 커다란 스틸턴 치즈 같은 기이한 보닛 모자를 쓰고 있음을 알아챌 만큼 거친 용모의 한 여인이 여관 하인들보다 앞서 방으로 뛰어 들어왔다.`
#### Chunk 2 (`P090_2`)
- **EN**: `She soon settled the matter of his detachment from the poor young lady by slamming a brawny hand against his chest and sending him flying back against the nearest wall.`
- **KO**: `그녀는 그의 가슴팍에 우람한 손을 얹어 가까운 벽 쪽으로 날려버림으로써 가엾은 숙녀에게서 그를 떼어놓는 문제를 단숨에 해결해 버렸다.`

---

## Audit Entry: 2026-09-02 16:44:42
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_09.json`
- **Original Target**: ID 210 (`P095_3`)
- **Category**: Category 3B (ESL Learner Optimized Split)
- **Split Strategy**: Sydney Carton in court (ESL smooth English & Korean split)
- **Verification Status**: PASSED (Smooth bilingual sentence alignment, 0 broken fragments).
### Split Chunks:
#### Chunk 1 (`P095_1`)
- **EN**: `His learned colleague, Mr. Stryver, gathered his papers before him, whispered with those sitting nearby, and from time to time glanced anxiously at the jury. All the spectators shifted around and formed new groups, and even the judge himself rose from his seat and slowly paced up and down his dais, looking agitated.`
- **KO**: `동료 변호사인 스트라이버 씨는 서류를 모으고 곁에 앉은 이들과 귓속말을 나누며 때때로 불안한 눈빛으로 배심원단을 힐끔거렸다. 모든 방청객들이 저마다 술렁이며 삼삼오오 흩어졌다 모였고, 심지어 판사조차 자리에서 일어나 단상을 천천히 서성이며 초조한 기색을 내비쳤다.`
#### Chunk 2 (`P095_2`)
- **EN**: `Yet this one man sat leaning back, with his torn robe half falling off him, his untidy wig sitting on his head however it had happened to land when he put it back on, his hands in his pockets, and his eyes fixed on the ceiling just as they had been all day.`
- **KO**: `하지만 이 한 남자만은 찢어진 법복을 반쯤 걸친 채, 아무렇게나 얹어놓은 듯한 헝클어진 가발을 쓰고, 두 손을 주머니에 찌른 채 하루 종일 그랬듯 천장을 응시하며 뒤로 기대앉아 있었다.`

---

## Audit Entry: 2026-09-02 16:44:42
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_31.json`
- **Original Target**: ID 173 (`P097_2`)
- **Category**: Category 3B (ESL Learner Optimized Split)
- **Split Strategy**: Jailers vs Ghostly women + punchline split
- **Verification Status**: PASSED (Smooth bilingual sentence alignment, 0 broken fragments).
### Split Chunks:
#### Chunk 1 (`P097_1`)
- **EN**: `The jailer standing beside him and the other jailers moving about, who would have looked normal enough while performing their ordinary duties, appeared outrageously coarse compared to the grieving mothers and blooming daughters who were there—to the ghostly figures of the flirt, the young beauty, and the delicately raised mature woman—so much so that the total reversal of all normal experience and expectation presented by this shadowy scene was heightened to the extreme.`
- **KO**: `그의 곁에 서 있는 간수와 주위를 돌아다니는 다른 간수들은 평상시의 직무를 수행할 때라면 겉모습이 그럭저럭 무난해 보였겠지만, 그곳에 있는 슬픔에 잠긴 어머니들과 피어나는 딸들—교태를 부리는 여인, 젊은 미녀, 그리고 고상하게 자란 원숙한 여인의 유령 같은 모습들—과 대조되어 터무니없이 거칠어 보였기에, 그림자 같은 그 광경이 보여 주는 온갖 경험과 상식의 전도는 극에 달해 있었다.`
#### Chunk 2 (`P097_2`)
- **EN**: `Surely, they were all ghosts.`
- **KO**: `분명 그들은 모두 유령이었다.`

---

## Audit Entry: 2026-09-02 16:44:42
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_34.json`
- **Original Target**: ID 16 (`P005_4`)
- **Category**: Category 3B (ESL Learner Optimized Split)
- **Split Strategy**: Dr. Manette & Samaritans split
- **Verification Status**: PASSED (Smooth bilingual sentence alignment, 0 broken fragments).
### Split Chunks:
#### Chunk 1 (`P005_1`)
- **EN**: `Being besought to go to him and dress the wound, the Doctor had passed out at the same gate, and had found him in the arms of a company of Samaritans, who were seated on the bodies of their victims.`
- **KO**: `부상자에게 가서 상처를 치료해 달라는 간청을 받은 박사는 같은 문을 통해 밖으로 나갔고, 희생자들의 시신 위에 걸터앉은 한 무리의 ‘사마리아인들’ 품에 안겨 있는 그를 발견했다.`
#### Chunk 2 (`P005_2`)
- **EN**: `With an inconsistency as monstrous as anything in this awful nightmare, they had helped the healer and tended the wounded man with the gentlest solicitude—had made a litter for him and escorted him carefully from the spot—had then caught up their weapons and plunged anew into a butchery so dreadful that the Doctor had covered his eyes with his hands, and swooned away in the midst of it.`
- **KO**: `이 끔찍한 악몽 속 그 어떤 것보다도 기괴한 모순 속에서, 그들은 의사를 도왔고 지극한 정성으로 부상자를 돌보았으며, 그를 위해 들것을 만들어 현장에서 조심스럽게 호송해 갔다. 그러고 나서는 다시 무기를 쥐고 너무나 끔찍한 도살극에 뛰어들었기에, 박사는 두 손으로 눈을 가리고 그 한가운데서 정신을 잃고 말았다.`

---

## Audit Entry: 2026-09-02 16:44:42
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_34.json`
- **Original Target**: ID 40 (`P012_1`)
- **Category**: Category 3B (ESL Learner Optimized Split)
- **Split Strategy**: Time contradiction & Reign of Terror machinery split
- **Verification Status**: PASSED (Smooth bilingual sentence alignment, 0 broken fragments).
### Split Chunks:
#### Chunk 1 (`P012_1`)
- **EN**: `And yet, observing the strange law of contradiction which obtains in all such cases, the time was long, while it flamed by so fast.`
- **KO**: `하지만 그러한 모든 상황에 적용되는 기묘한 모순의 법칙에 따라, 시간은 불길처럼 빠르게 지나가면서도 길게 느껴졌다.`
#### Chunk 2 (`P012_2`)
- **EN**: `A revolutionary tribunal in the capital, and forty or fifty thousand revolutionary committees all over the land; a law of the Suspected, which struck away all security for liberty or life, and delivered over any good and innocent person to any bad and guilty one; prisons gorged with people who had committed no offence, and could obtain no hearing; these things became the established order and nature of appointed things, and seemed to be ancient usage before they were many weeks old.`
- **KO**: `수도의 혁명재판소와 전국 각지의 사오만 개에 달하는 혁명위원회, 자유와 생명에 대한 모든 안전장치를 박탈하고 선량하고 무고한 사람을 악하고 죄 있는 자의 손에 넘겨버린 용의자법, 아무런 죄도 짓지 않고 재판조차 받지 못하는 사람들로 가득 찬 감옥들. 이러한 것들이 정해진 일상의 질서이자 본질이 되었고, 불과 몇 주가 지나기도 전에 아주 오래된 관습처럼 여겨졌다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_04.json`
- **Original Target**: ID 20 (`P008_2`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Hotel staff watching Mr. Lorry go to breakfast
- **Reason for Split**: Paragraph was 455 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P008_1`)
- **EN**: `Consequently, another waiter, two porters, several maids, and the landlady were all lingering casually at various points along the corridor between the Concord room and the coffee room, when a gentleman of sixty, formally dressed in a brown suit that was quite worn but very well-maintained—with large square cuffs and large pocket flaps—walked past on his way to breakfast.`
- **KO**: `그리하여 또 다른 웨이터 한 명과 두 명의 짐꾼, 몇몇 하녀들과 여주인은 모두 우연을 가장해 '콩코드' 방과 다실 사이의 복도 곳곳에 서성거리고 있었는데, 그때 넓은 사각 소맷단과 커다란 주머니 덮개가 달린 꽤 낡았지만 아주 잘 관리된 갈색 정장을 단정하게 차려입은 예순 살가량의 신사가 아침 식사를 하러 지나갔다.`
#### Chunk 2 (`P008_2`)
- **EN**: `That morning, the coffee room had no other guest besides the gentleman in brown.`
- **KO**: `그날 오전 다실에는 갈색 옷을 입은 그 신사 외에는 아무도 없었다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_05.json`
- **Original Target**: ID 7 (`P003_4`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: People scooping up spilled wine in Saint Antoine
- **Reason for Split**: Paragraph was 481 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P003_1`)
- **EN**: `Others dipped into the puddles with chipped clay mugs, or even with scarves taken from women's heads, which they squeezed dry into babies' mouths.`
- **KO**: `다른 이들은 이가 빠진 점토 머그잔으로 웅덩이를 떠내거나, 심지어 여자들의 머리에서 풀어낸 스카프를 적셔 아기들의 입에 짜 넣어주기도 했다.`
#### Chunk 2 (`P003_2`)
- **EN**: `Some made small mud walls to block the wine as it flowed, while others, directed by neighbors looking out from high windows, ran around to block small streams of wine branching off in new directions. A few focused on the wine-soaked wood from the broken barrel, licking and even chewing the wet, wine-stained fragments with enjoyment.`
- **KO**: `어떤 사람들은 흐르는 와인을 막기 위해 작은 진흙 둑을 만들었고, 높은 창문에서 내다보는 이웃들의 지시를 받아 새롭게 갈라져 나가는 작은 와인 줄기들을 막으려 뛰어다니는 사람들도 있었다. 몇몇은 부서진 통에서 나온 와인에 흠뻑 젖은 나무에 매달려, 와인 얼룩이 진 젖은 나뭇조각들을 핥고 씹으며 즐기기까지 했다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_05.json`
- **Original Target**: ID 13 (`P004_5`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Street returning to dark gloom after wine is gone
- **Reason for Split**: Paragraph was 463 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P004_1`)
- **EN**: `The woman who had left a small pot of hot ashes on a doorstep, trying to warm her own frozen fingers and toes or those of her child, returned to it. Men with bare arms and messy hair walked back down to their rooms.`
- **KO**: `문간에 작은 뜨거운 잿불 단지를 놓아두고 자신이나 아이의 얼어붙은 손발을 녹이려던 여자는 다시 그곳으로 돌아갔다. 맨팔에 헝클어진 머리를 한 남자들은 다시 그들의 방으로 걸어 내려갔다.`
#### Chunk 2 (`P004_2`)
- **EN**: `Their faces were pale and ghost-like. They had come up into the winter light from dark cellars, and now they disappeared back into them. A dark gloom settled over the street once more, looking far more natural to the street than sunshine ever did.`
- **KO**: `그들의 얼굴은 창백하고 유령 같았다. 그들은 어두운 지하실에서 겨울 햇살 속으로 올라왔다가, 이제 다시 그 안으로 사라졌다. 햇살이 비추던 때보다 훨씬 자연스러워 보이는 어두운 우울함이 다시 한 번 거리 위로 내려앉았다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_05.json`
- **Original Target**: ID 20 (`P007_2`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Cold, sickness, and poverty attendants
- **Reason for Split**: Paragraph was 462 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P007_1`)
- **EN**: `Cold, dirt, sickness, ignorance, and poverty were the attendants in waiting on this holy presence—all of them nobles of great power, but most especially poverty.`
- **KO**: `추위, 오물, 질병, 무지, 그리고 빈곤은 그 거룩한 존재를 모시는 시종들이었으며, 그들 모두 막강한 권력을 지닌 귀족들이었지만 특히나 마지막 존재인 빈곤이 그러했다.`
#### Chunk 2 (`P007_2`)
- **EN**: `Samples of a people who had undergone terrible grinding and regrinding in the mill—and certainly not in the mythical mill that ground old people young—shivered at every corner, passed in and out of every doorway, looked from every window, and fluttered in every shred of clothing that the wind shook.`
- **KO**: `맷돌에 들어가 무시무시하게 갈리고 또 갈린—노인을 젊게 만들어준다는 전설 속의 방앗간이 결코 아닌—사람들의 표본들이 골목 구석마다 웅크려 떨고 있었고, 문간마다 드나들었으며, 창문마다 내다보았고, 바람에 나부끼는 누더기 옷자락마다 퍼덕거렸다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_09.json`
- **Original Target**: ID 168 (`P072_2`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Lucie's anxious testimony & spectator reactions
- **Reason for Split**: Paragraph was 474 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P072_1`)
- **EN**: `Her brow was painfully tense and anxious as she gave this testimony, and during the pauses when she waited for the judge to write it down, she watched its effect on both the prosecution and the defense counsel.`
- **KO**: `그녀가 이 증언을 하는 동안 그녀의 이마에는 뼈아픈 불안과 긴장감이 서려 있었고, 판사가 기록할 수 있도록 말을 멈춘 사이사이에 변호인과 검사에게 미치는 영향을 살폈다.`
#### Chunk 2 (`P072_2`)
- **EN**: `Among the spectators, the same expression was seen throughout the courtroom; so much so that most of their foreheads could have been mirrors reflecting the witness when the judge looked up from his notes to glare at that outrageous heresy about George Washington.`
- **KO**: `방청객들 사이에서도 법정 곳곳에서 똑같은 표정이 나타났다. 판사가 조지 워싱턴에 관한 그 엄청난 이단적 발언에 노기를 띠며 메모에서 고개를 들었을 때, 법정에 모인 대다수의 이마는 마치 증인을 비추는 거울과도 같았을 정도였다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 96 (`P043_3`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Bastille storming & Defarge at his cannon
- **Reason for Split**: Paragraph was 458 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P043_1`)
- **EN**: `There were flashing weapons, blazing torches, and smoking wagons full of wet straw. People fought hard at barricades in every direction amid screams, gunshots, curses, and endless bravery. It was all booming, smashing, and rattling like a furious sea.`
- **KO**: `번쩍이는 무기, 활활 타오르는 횃불, 그리고 젖은 짚을 실은 연기 나는 마차들이 있었습니다. 비명, 총성, 저주, 그리고 끝없는 용기 속에서 사방의 바리케이드에서 사람들은 격렬하게 싸웠습니다. 그 모든 것이 분노한 바다처럼 쾅쾅 울리고 부서지고 덜컥거렸습니다.`
#### Chunk 2 (`P043_2`)
- **EN**: `But through it all stood the deep ditch, the single drawbridge, the massive stone walls, and the eight huge towers. And there was Defarge at his cannon, now twice as hot after four fierce hours of fighting.`
- **KO**: `그러나 그 모든 것 속에서도 깊은 해자, 단일 도개교, 거대한 돌 성벽, 그리고 여덟 개의 거대한 탑은 굳건히 서 있었습니다. 그리고 그곳에는 네 시간의 치열한 전투 후 이제 두 배로 뜨거워진 대포 앞에 드파르지가 있었습니다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_27.json`
- **Original Target**: ID 150 (`P075_2`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Spilled blood at City Hall & hanging the guard
- **Reason for Split**: Paragraph was 486 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P075_1`)
- **EN**: `Saint Antoine's blood was boiling, while the blood of tyranny and cruel control spilled out—down on the steps of the City Hall where the governor's body lay, and down on Madame Defarge's shoe where she had stepped to steady the body while cutting it.`
- **KO**: `생탕투안의 피가 끓고 있었고, 그동안 폭정과 잔인한 통제의 피가 쏟아져 나왔다. 총독의 시신이 누워 있는 시청 계단으로, 그리고 머리를 베기 위해 몸을 고정시키려 밟고 있던 마담 드파르지의 신발 위로 말이다.`
#### Chunk 2 (`P075_2`)
- **EN**: `"Lower that lamp over there!" yelled the crowd of Saint Antoine, looking for another way to kill. "Here's one of his soldiers to leave on guard!" The dead guard was strung up to swing from the lamppost, and the massive crowd rushed on.`
- **KO**: `"저기 저 가로등을 내려!" 생탕투안의 군중이 또 다른 살인 방법을 찾으며 소리쳤다. "여기 경비를 서게 할 그의 병사가 있다!" 죽은 병사는 가로등에 매달려 흔들거렸고, 거대한 군중은 계속해서 몰려갔다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_28.json`
- **Original Target**: ID 50 (`P021_12`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Women screaming for the blood of Foulon
- **Reason for Split**: Paragraph was 482 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P021_1`)
- **EN**: `Husbands, brothers, and young men, give us the blood of Foulon, give us the head of Foulon, give us the heart of Foulon, give us the body and soul of Foulon! Tear Foulon to pieces, and bury him in the ground so that grass can grow from him!`
- **KO**: `남편, 형제, 청년들이여, 풀롱의 피를 우리에게 주오, 풀롱의 머리를 우리에게 주오, 풀롱의 심장을 우리에게 주오, 풀롱의 몸과 영혼을 우리에게 주오! 풀롱을 갈기갈기 찢어 땅에 묻어 그에게서 풀이 자라게 하라!`
#### Chunk 2 (`P021_2`)
- **EN**: `Shouting these cries, many of the women were driven into a blind frenzy. They spun around, striking and scratching at their own friends until they collapsed in an exhausted faint, only saved from being trampled by the men who cared for them.`
- **KO**: `이 외침을 지르며 많은 여성들이 맹목적인 광란에 빠져들었다. 그들은 빙빙 돌며 친구들을 때리고 할퀴다가 지쳐 쓰러졌고, 그들을 돌보는 남자들 덕분에 짓밟히는 것을 간신히 면했다.`

---

## Audit Entry: 2026-09-02 16:49:10
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_28.json`
- **Original Target**: ID 69 (`P028_1`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: The mob dragging Foulon to the lamppost
- **Reason for Split**: Paragraph was 492 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P028_1`)
- **EN**: `Dragged up and down the steps, now on his knees, now on his back, beaten and choked with grass and straw stuffed into his face, the old man begged for mercy. The crowd drew back to watch him struggle.`
- **KO**: `계단을 오르내리며 끌려다니고, 때로는 무릎을 꿇거나 등에 업힌 채, 맞고 얼굴에 쑤셔 넣어진 풀과 짚으로 숨이 막혀 늙은이는 자비를 구걸했다. 군중은 그가 발버둥 치는 것을 보려고 뒤로 물러섰다.`
#### Chunk 2 (`P028_2`)
- **EN**: `They dragged him to the nearest street corner where a lamp post hung. Madame Defarge let him go like a cat releasing a mouse, watching quietly while they prepared the rope, as he begged her for help. The women screamed at him, and the men called for him to be hanged with grass in his mouth.`
- **KO**: `그들은 가로등 기둥이 매달려 있는 가장 가까운 길모퉁이로 그를 끌고 갔다. 마담 드파르지는 고양이가 쥐를 놓아주듯 그를 풀어주었고, 그가 도와달라고 애원하는 동안 그들이 밧줄을 준비하는 것을 조용히 지켜보았다. 여자들은 그에게 소리를 질렀고, 남자들은 입에 풀을 물린 채 그를 교수형에 처하라고 외쳤다.`

---

## Audit Entry: 2026-09-02 16:49:33
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_31.json`
- **Original Target**: ID 5 (`P003_3`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Citizen-patriots checking travelers at town gates
- **Reason for Split**: Paragraph was 451 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P003_1`)
- **EN**: `Every town gate and village tollhouse was guarded by a band of citizen-patriots holding loaded muskets, ready to shoot at any moment. They stopped everyone. They cross-examined travelers, checked papers, and searched for names on custom lists.`
- **KO**: `모든 성문과 마을 요금소에는 장전된 머스킷 총을 들고 언제든 쏠 준비가 된 시민 애국자 무리가 경비를 서고 있었다. 그들은 모든 사람을 멈춰 세웠다. 그들은 여행자를 심문하고, 서류를 확인하며, 세관 명단에서 이름을 찾았다.`
#### Chunk 2 (`P003_2`)
- **EN**: `Then they turned people back, sent them forward, or arrested them outright. It all depended on whatever their random judgment decided was best for the new Republic of Liberty, Equality, Fraternity, or Death.`
- **KO**: `그런 다음 사람들을 돌려보내거나, 통과시키거나, 그 자리에서 체포했다. 모든 것은 그들의 자의적인 판단이 자유, 평등, 박애, 혹은 죽음이라는 새로운 공화국에 무엇이 최선이라고 결정하느냐에 달려 있었다.`

---

## Audit Entry: 2026-09-02 16:49:33
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_31.json`
- **Original Target**: ID 200 (`P111_1`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Darnay pacing cell repeating 'Five paces by four and a half'
- **Reason for Split**: Paragraph was 453 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P111_1`)
- **EN**: `“"Five paces by four and a half, five paces by four and a half, five paces by four and a half." The prisoner paced back and forth in his cell, measuring the room over and over. Outside, the distant roar of the city sounded like muffled drums mixed with shouting voices.`
- **KO**: `“다섯 걸음에 네 걸음 반, 다섯 걸음에 네 걸음 반, 다섯 걸음에 네 걸음 반." 수감자는 방을 계속해서 측량하며 감방 안을 왔다 갔다 했다. 밖에서는, 도시의 먼 굉음이 고함 소리와 섞인 둔탁한 북소리처럼 들렸다.`
#### Chunk 2 (`P111_2`)
- **EN**: `“He made shoes, he made shoes, he made shoes.” Darnay measured the cell again, walking faster to try to block out that repetitive thought. “The ghosts who vanished when the gate shut.`
- **KO**: `“그는 신발을 만들었다, 그는 신발을 만들었다, 그는 신발을 만들었다.” 다네이는 그 반복되는 생각을 막으려고 더 빨리 걸으며 감방을 다시 측량했다. “문이 닫힐 때 사라졌던 유령들.`

---

## Audit Entry: 2026-09-02 16:49:33
- **Book**: Two Cities (`two_cities`)
- **File**: `ch_39.json`
- **Original Target**: ID 175 (`P090`)
- **Category**: Phase 4 Polish (Paragraphs >= 450 chars)
- **Description**: Sydney Carton walking through city of death at night
- **Reason for Split**: Paragraph was 493 chars EN.
- **Split Strategy**: Substring Anchor Split into 2 bite-sized chunks.
- **Verification Status**: PASSED (100% character invariant preserved, 0 missing/added chars).
### Split Chunks:
#### Chunk 1 (`P090_1`)
- **EN**: `He looked at the lit windows where people were going to sleep, escaping the day's horrors for a few hours. He saw the dark church towers where no one prayed anymore, because the people had rejected religion after years of corrupt priests.`
- **KO**: `그는 사람들이 몇 시간 동안이나마 그날의 공포에서 벗어나 잠자리에 들려 하는 불 켜진 창문들을 바라보았다. 그는 수년 동안의 타락한 사제들 이후 사람들이 종교를 거부했기 때문에 더 이상 아무도 기도하지 않는 어두운 교회 탑들을 보았다.`
#### Chunk 2 (`P090_2`)
- **EN**: `He thought of the cemeteries with signs reading "Eternal Sleep," the crowded jails, and the streets where cartloads of people rode to their deaths daily. Walking through this city of death as it quieted down for the night, Carton crossed the river again.`
- **KO**: `그는 "영원한 수면"이라는 팻말이 붙은 공동묘지들, 붐비는 감옥들, 그리고 마차에 실려 죽음을 향해 가는 사람들의 행렬이 매일 지나가는 거리들을 생각했다. 밤을 맞아 고요해져 가는 이 죽음의 도시를 걸으며, 카턴은 다시 강을 건넸다.`

---

## Batch 5: 23 Multi-Sentence Mega-Paragraphs (400–499 Characters) Split (2026-09-02 17:18:34)
- **Scope**: All 23 multi-sentence paragraphs $\ge 400$ characters in *A Tale of Two Cities*.
- **Splitting Strategy**: 1-to-1 Bilingual Sentence Boundary Matching.
- **Invariant Checking**: 100% character and word conservation verified for both English and Korean.
- **Result**: Zero multi-sentence paragraphs $\ge 400$ characters remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $ightarrow$ `BUILD SUCCESSFUL`.

```
VALIDATION REPORT: 23 MULTI-SENTENCE MEGA-PARAGRAPH SPLITS
Total candidate paragraphs split: 23
Invariant check: 100% character and word conservation verified for both EN and KO.
================================================================================

[1] ch_30.json (Tag: P020, Original Length: 460 chars)
  --> Chunk A (200 EN ch / 108 KO ch):
      EN: "Nonsense, sir! And, my dear Charles," said Mr. Lorry, glancing toward the partners again, "you must remember that getting anything out of Paris right now, no matter what it is, is next to impossible.
      KO: "당치도 않네, 여보게! 그리고 친애하는 찰스," 로리 씨는 다시 동업자들을 바라보며 말했다. "지금 당장은 그것이 무엇이든 파리 밖으로 빼내는 것이 거의 불가능에 가깝다는 점을 기억해야 하네.

  --> Chunk B (259 EN ch / 116 KO ch):
      EN: Just today, papers and valuables were brought to us here by the strangest messengers, who were in constant danger of losing their heads as they crossed the borders. Normally, our mail would come and go as easily as in England, but now, everything is blocked.”
      KO: 바로 오늘만 해도, 국경을 넘으며 목숨을 잃을 뻔한 위험에 처했던 기묘한 전령들을 통해 서류와 귀중품들이 이곳으로 전달되었어. 평소라면 우편물이 영국에서처럼 쉽게 오갔겠지만, 지금은 모든 것이 막혀 있다네.”
------------------------------------------------------------------------------... [Full report saved in split_validation_report.txt]
```


## Batch 6: 21 Multi-Sentence Paragraphs (350–399 Characters) Split (2026-09-02 17:23:06)
- **Scope**: All 21 multi-sentence paragraphs in the 350–399 character tier in *A Tale of Two Cities*.
- **Splitting Strategy**: 1-to-1 Bilingual Sentence Boundary Matching.
- **Invariant Checking**: 100% character and word conservation verified for both English and Korean.
- **Result**: Zero multi-sentence paragraphs $\ge 350$ characters remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $ightarrow$ `BUILD SUCCESSFUL`.

```
VALIDATION REPORT: 21 MULTI-SENTENCE PARAGRAPH SPLITS (350-399 TIER)
Total candidate paragraphs split: 21
Invariant check: 100% character and word conservation verified for both EN and KO.
================================================================================

[1] ch_27.json (Tag: P033, Original Length: 398 chars)
  --> Chunk A (101 EN ch / 60 KO ch):
      EN: Just like a boiling whirlpool has a center, all this raging chaos circled around Defarge's wine-shop.
      KO: 끓어오르는 소용돌이에 중심이 있듯, 이 모든 격렬한 혼란은 드파르지의 와인 가게를 중심으로 돌고 있었습니다.

  --> Chunk B (296 EN ch / 172 KO ch):
      EN: Everyone in the crowd was sucked toward the middle where Defarge himself, already covered in sweat and gunpowder, was shouting orders and handing out weapons. He pushed men back, dragged others forward, took weapons from some to give to others, and fought hard right in the middle of the madness.
      KO: 군중 속의 모든 사람이 한가운데로 빨려 들어갔고, 그곳에는 이미 땀과 화약으로 뒤덮인 드파르지 자신이 명령을 외치며 무기를 나눠주고 있었습니다. 그는 사람들을 뒤로 밀어내고, 다른 사람들을 앞으로 끌어당겼으며, 어떤 사람에게서 무기를 빼앗아 다른 사람에게 주기도 하며 그 광란의 한가운데서 맹렬히 싸웠습니다.
--------------------------------------------------------------------------------

[2] ch_27.json (Tag: P003_3, Original Len... [Full report saved in split_validation_report_tier350.txt]
```


## Batch 7: 16 Single-Sentence Paragraphs (350–399 Characters) ESL-Friendly Split (2026-09-02 17:26:28)
- **Scope**: All 16 single-sentence paragraphs in the 350–399 character tier in *A Tale of Two Cities*.
- **Splitting Strategy**: Clause boundary and ESL-optimized natural thought splitting (Categories A, B, and C).
- **Result**: Zero paragraphs in the 350–399 tier remain in *Two Cities*!
- **Build Status**: `:shared:testDebugUnitTest` $ightarrow$ `BUILD SUCCESSFUL`.

```
VALIDATION REPORT: 16 SINGLE-SENTENCE PARAGRAPH ESL SPLITS (350-399 TIER)
Total candidate paragraphs split: 16
Quality check: Smooth, bite-sized English and natural Korean validated for all 16 items.
================================================================================

[1] ch_35.json (Tag: P002_4, Original Length: 397 chars)
  --> Chunk A (265 EN ch / 143 KO ch):
      EN: Lovely girls, bright women, youths, stalwart men and old, gentle born and peasant born—all red wine for La Guillotine, all daily brought into light from the dark cellars of the loathsome prisons, and carried to her through the streets to slake her devouring thirst.
      KO: 사랑스러운 소녀들, 활기찬 여인들, 젊은이들, 건장한 사내들과 노인들, 귀족 출신과 농민 출신—이 모든 이들이 단두대를 위한 붉은 포도주가 되어 매일같이 음산한 감옥의 어두운 지하 독방에서 끌려 나와, 단두대의 갈증을 채워주기 위해 거리를 지나 실려 갔다.

  --> Chunk B (95 EN ch / 63 KO ch):
      EN: Liberty, equality, fraternity, or death! The last was much the easiest to bestow, O Guillotine!
      KO: 자유, 평등, 박애, 그렇지 않으면 죽음을! 오 단두대여, 그중 죽음이야말로 네가 베풀기에 가장 쉬운 것이었구나!
--------------------------------------------------------------------------------

[2] ch_26.json (Tag: P045_1, Original Length: 394 chars)
  --> Chunk A (83 EN ch / 36 KO ch)... [Full report saved in split_validation_report_singles16.txt]
```


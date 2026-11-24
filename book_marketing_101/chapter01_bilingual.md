# Chapter 1 — Know Your Book and Your Reader
# 1장 — 내 책과 독자 알기

## Lab 1 — Find your 3 comps
## 실습 1 — 비교 도서 3권 찾기

Goal: end with 3 comparable books and one reader profile you can use in every later chapter.

목표: 이후 모든 장에서 쓸 비교 도서 3권과 독자 프로필 하나를 만듭니다.

1. Write your shelf in one line: genre + subgenre + the promise (for example, "cozy fantasy with found family, a happy ending guaranteed").
1. 서가를 한 줄로 적으십시오: 장르 + 하위 장르 + 약속(예: "가족을 찾아가는 따뜻한 판타지, 해피엔딩 보장").
2. Find 4–6 recent books that share your reader. Use the store's "readers also bought" list and BookBub or Goodreads lists.
2. 같은 독자를 가진 최근 책 4~6권을 찾으십시오. 서점의 "함께 구매한 책" 목록과 BookBub, Goodreads 목록을 쓰십시오.
3. Put them into `labs/ch01_comps.py` (the `COMPS` list), set `MY_GENRE`, and run the script.
3. `labs/ch01_comps.py`의 `COMPS` 목록에 넣고, `MY_GENRE`를 정한 뒤 스크립트를 실행하십시오.
4. Keep the titles marked KEEP. If fewer than 3 pass, search again. Do not lower the rules.
4. KEEP으로 표시된 책을 남기십시오. 3권보다 적으면 다시 찾으십시오. 기준을 낮추지 마십시오.
5. Write your reader profile in the table below, then your hook (one sentence) and comp pitch ("A meets B").
5. 아래 표에 독자 프로필을 쓰고, 훅(한 문장)과 비교 피치("A와 B를 합친 책")를 쓰십시오.

```
$ python labs/ch01_comps.py
Title A  KEEP
Title B  DROP: too old
Title C  DROP: different genre
Title D  DROP: giant
1 of 4 comps kept
```

Checkpoint: you have at least 3 KEEP titles, and your hook passes this test: a person who has never seen the book asks one follow-up question.

확인: KEEP 책이 3권 이상이고, 훅을 한 번도 본 적 없는 사람이 후속 질문을 한 번 하면 통과합니다.

| Question | Your answer / 여러분의 답 |
|---|---|
| Who are they? / 어떤 사람입니까? | |
| What else do they read? / 다른 어떤 책을 읽습니까? | |
| Where do they find books? / 어디서 책을 찾습니까? | |
| What do they want? / 무엇을 원합니까? | |
| What turns them off? / 무엇이 그들을 떠나게 합니까? | |

## Concept — why this works
## 개념 — 왜 이렇게 하는가

Readers shop by category. "Fantasy" is too broad; "cozy fantasy with found family" tells a reader in seconds whether the book is for them. Nonfiction works the same way: "personal finance" versus "personal finance for freelancers."

독자는 카테고리로 책을 고른다. "판타지"는 너무 넓다. "가족을 찾아가는 따뜻한 판타지"라고 하면 독자는 몇 초 만에 그 책이 자기 취향인지 안다. 논픽션도 같다. "개인 재무"보다 "프리랜서를 위한 개인 재무"가 훨씬 분명하다.

Comps ("comparable titles") are recent books that share your reader. They show you what covers work, what readers expect, which keywords to use and which ads to target. A good comp is recent, successful but not a giant bestseller, and genuinely similar in tone, not just plot.

비교 도서(comps)는 여러분의 독자를 가진 최근 책이다. 어떤 표지가 통하는지, 독자가 무엇을 기대하는지, 어떤 키워드와 광고를 쓸지 알려 준다. 좋은 비교 도서는 최신이고, 성공했지만 거대한 베스트셀러가 아니며, 줄거리뿐 아니라 톤과 독자가 실제로 비슷하다.

There are three pitches, and you need all three: the hook (one line that makes someone say "tell me more"), the elevator pitch (hook, stakes and tone in 2–3 sentences), and the comp pitch ("Book A meets Book B").

피치는 세 가지가 필요하다. 훅(한 줄로 "더 알려 주세요"라는 말을 끌어내는 문장), 엘리베이터 피치(훅에 걸린 것과 분위기를 더한 2~3문장), 비교 피치("A와 B를 합친 책")다.

Real-world example: in 2021, Keila Shaheen self-published *The Shadow Work Journal*, a guided workbook built on Carl Jung's idea of the "shadow self." It was a specific tool for a specific reader, and many of them were on TikTok. It sold more than a million copies, nearly 700,000 through TikTok Shop, promoted by creators who earned a commission on each sale (Boston Globe / New York Times). The lesson is that the narrower your reader profile, the easier it is for the right people to recognize your book as "for me."

실제 사례: 2021년 케일라 셰이헌(Keila Shaheen)은 칼 융의 "그림자 자아" 개념을 바탕으로 한 가이드 워크북 *The Shadow Work Journal*을 직접 출간했다. 넓은 자기계발서가 아니라 특정 독자를 위한 구체적인 도구였고, 그 독자 중 많은 수가 틱톡 이용자였다. 100만 부가 넘게 팔렸고, 그중 거의 70만 부가 TikTok Shop을 통해 팔렸다. 판매마다 수수료를 받은 크리에이터들이 홍보했다(보스턴 글로브 / 뉴욕 타임스). 교훈은 독자 프로필이 좁을수록 맞는 사람들이 여러분의 책을 "나를 위한 책"으로 알아보기 쉽다는 것이다.

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **"comps" → 비교 도서.** Korean readers will not know the slang, so the first use is the translation. After that, "비교 도서" alone is enough.
   "comps"는 업계 줄임말이라 한국 독자에게는 낯섭니다. 처음에 번역어를 쓰고, 이후에는 "비교 도서"만 씁니다.
2. **"Keila Shaheen" and "Simon & Schuster" spellings are unverified.** Check them before publishing (glossary decision 2).
   "Keila Shaheen", "Simon & Schuster"의 한국어 표기는 아직 확인하지 않았습니다. 출간 전에 확인하십시오(용어집 결정 2).
3. **Unverified sales figures.** The one-million-copy and 700,000 TikTok Shop figures come from the English draft. Verify them before publishing.
   판매 수치(100만 부, 약 70만 부)는 영어 원고에서 가져온 것으로 검증하지 않았습니다. 출간 전에 확인하십시오.

**Glossary terms used in this chapter:** 비교 도서 (comps), 독자 프로필 (reader profile), 훅 (hook), 엘리베이터 피치 (elevator pitch), 비교 피치 (comp pitch), 서가 (shelf), 장르 (genre), 하위 장르 (subgenre), 카테고리 (category).

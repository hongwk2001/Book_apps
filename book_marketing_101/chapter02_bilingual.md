# Chapter 2 — Get Your Book Ready to Sell
# 2장 — 판매할 준비 갖추기

## Lab 2 — Price the book, then write its listing
## 실습 2 — 가격을 계산하고 판매 페이지 쓰기

Goal: choose a price by its royalty, not by a guess, and draft the listing data a store will read.

목표: 짐작이 아니라 로열티를 계산해서 가격을 고르고, 서점이 읽을 판매 정보를 초안으로 씁니다.

1. Open `labs/ch02_royalty.py`. Change the price list to your three candidate ebook prices and run it.
1. `labs/ch02_royalty.py`를 여세요. 전자책 후보 가격 세 개로 목록을 바꾸고 실행하십시오.
2. Compare each price: royalty per sale, and whether the price falls in the 70% band ($2.99–$12.99).
2. 가격마다 판매당 로열티와 70% 구간($2.99~$12.99) 안에 드는지 비교하십시오.
3. Run the paperback line with your page count's print cost. Note the $9.99 boundary: below it the rate drops from 60% to 50%.
3. 쪽수에 맞는 인쇄 비용으로 종이책 줄을 실행하십시오. $9.99 경계를 기억하십시오. 그 아래에서는 요율이 60%에서 50%로 내려갑니다.
4. Fill the metadata table below with your title, 3 categories and 7 keyword phrases. Check each category has real bestsellers.
4. 아래 메타데이터 표에 제목, 카테고리 3개, 키워드 구문 7개를 채우십시오. 각 카테고리에 실제 베스트셀러가 있는지 확인하십시오.
5. Write your blurb in 150–250 words using the fiction or nonfiction template in Appendix C. Count the words with `len(text.split())` in Python.
5. 부록 C의 소설 또는 논픽션 템플릿으로 책 소개문을 150~250단어로 쓰십시오. Python의 `len(text.split())`로 단어 수를 세십시오.

```
$ python labs/ch02_royalty.py
== Ebook ==
price $2.99 -> royalty $2.09
price $4.99 -> royalty $3.49
price $9.99 -> royalty $6.99
price $12.99 -> royalty $9.09
price $13.99 -> royalty $4.90
== Paperback ==
list $9.99, print $3.50 -> royalty $2.49
list $8.99, print $3.50 -> royalty $1.00
```

Checkpoint: your price gives you the royalty you want per sale, and every category and keyword in your table has been checked against real books.

확인: 선택한 가격이 원하는 판매당 로열티를 주고, 표의 모든 카테고리와 키워드를 실제 책으로 확인했습니다.

| Element / 항목 | Your entry / 여러분의 입력 |
|---|---|
| Title and subtitle / 제목과 부제 | |
| Categories (up to 3) / 카테고리(최대 3개) | |
| Keywords (up to 7) / 키워드(최대 7개) | |
| Series info / 시리즈 정보 | |

## Concept — why this works
## 개념 — 왜 이렇게 하는가

The cover is your most important ad. Readers judge a book in about a second, usually as a phone thumbnail. Its job is to signal genre and tone so the right reader stops scrolling, not to illustrate a scene.

표지는 가장 중요한 광고다. 독자는 약 1초 만에, 보통 휴대폰의 작은 썸네일로 책을 판단한다. 표지의 역할은 장면을 그리는 것이 아니라, 장르와 분위기를 알려서 맞는 독자가 스크롤을 멈추게 하는 것이다.

Price signals value and changes how stores treat your book. Check what readers in your genre already pay, then use the royalty rules to decide. Ebooks outside the $2.99–$12.99 band earn 35%. Paperbacks at or above $9.99 earn 60% of list price, and those below earn 50%, both minus printing cost.

가격은 가치를 드러내고, 서점이 책을 다루는 방식을 바꾼다. 장르 독자가 이미 내는 가격대를 확인한 뒤, 로열티 규칙으로 결정하십시오. $2.99~$12.99 구간 밖의 전자책은 35%를 받는다. 종이책은 $9.99 이상이면 정가의 60%, 그 아래면 50%를 받으며, 둘 다 인쇄 비용을 뺀다.

Metadata is the information behind your listing, which store search engines rely on. For AI shoppers, be plain: say who the book is for, the genre and the experience it delivers. Amazon's assistant answers questions like "a cozy mystery set in a bakery," so the description has to name those things in the reader's own words.

메타데이터는 판매 페이지 뒤에 있는 정보이며, 서점 검색 엔진이 이에 의존한다. AI 쇼핑 도우미를 위해서는 분명하게 쓰십시오. 누구를 위한 책인지, 장르, 어떤 경험을 주는지 말하십시오. 아마존의 도우미는 "빵집을 배경으로 한 코지 미스터리" 같은 질문에 답하므로, 소개문이 독자의 말로 그 내용을 담고 있어야 합니다.

Amazon rules as of late 2026: KDP allows up to three categories per format and up to seven keyword boxes (Bookishelf guide; KDP Help). Amazon may add categories it judges relevant. Many newly added categories are nearly empty.

2026년 말 기준 아마존 규칙: KDP는 형식별로 카테고리를 최대 3개, 키워드 칸을 최대 7개까지 허용한다(Bookishelf 가이드, KDP 도움말). 아마존은 관련이 있다고 판단하는 카테고리를 추가할 수 있다. 새로 추가된 카테고리 중 많은 수가 거의 비어 있다(ScribeCount).

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **"blurb" → 책 소개문.** Korean publishers say 책 소개문. The first time it appears, 블러브 is in parentheses as a reading aid.
   "blurb"는 한국 출판계에서 "책 소개문"이라고 합니다. 처음 나올 때만 발음 표기 "블러브"를 괄호에 넣었습니다.
2. **Royalty rules are time-sensitive.** The $12.99 band edge (changed July 7, 2026) and the category counts come from the English draft. Check KDP's help pages before you set a real price.
   로열티 구간 경계($12.99, 2026년 7월 7일 변경)와 카테고리 수는 영어 원고에서 왔습니다. 실제 가격을 정하기 전에 KDP 도움말에서 확인하십시오.
3. **The script skips fees.** `labs/ch02_royalty.py` leaves out delivery fees and file costs so you see the core math. Real royalties will be a little lower.
   스크립트는 전송 수수료와 파일 비용을 뺍니다. 핵심 계산을 보기 위해서이며, 실제 로열티는 조금 더 낮습니다.

**Glossary terms used in this chapter:** 책 소개문 (blurb), 메타데이터 (metadata), 키워드 (keywords), 카테고리 (categories), 작가 소개 (author bio), 시리즈 정보 (series info), 로열티 (royalty), 정가 (list price), 앞부분 (front matter), 뒷부분 (back matter), 표지 (cover), 썸네일 (thumbnail).

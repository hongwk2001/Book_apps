# Chapter 6 — Long-Term Marketing
# 6장 — 장기 마케팅

## Lab 6 — Decide if an ad can pay, before you spend
## 실습 6 — 돈을 쓰기 전에 광고가 남는지 계산하기

Goal: compute ROAS and the break-even cost per click from a small test, and set a fixed test budget.

목표: 작은 테스트 결과로 ROAS와 손익분기 클릭당 비용을 계산하고, 고정된 테스트 예산을 정합니다.

1. Use your royalty per sale from Lab 2 and your conversion guess (2% is a common starting point). Put the numbers in `labs/ch06_ads.py` and run it.
1. 실습 2에서 구한 판매당 로열티와 전환율 추정치(2%부터 시작하는 것이 흔합니다)를 `labs/ch06_ads.py`에 넣고 실행하십시오.
2. If your break-even CPC is below what the ad platform charges per click, do not start. Improve the cover or blurb first.
2. 손익분기 클릭당 비용이 광고 플랫폼의 클릭당 요금보다 낮으면 시작하지 마십시오. 먼저 표지나 책 소개문을 고치십시오.
3. Plan one small test: a fixed budget you can lose, two ad versions (different image or headline), and a check date one or two weeks away.
3. 작은 테스트를 계획하십시오. 잃어도 괜찮은 고정 예산, 광고 버전 두 개(다른 이미지나 제목), 1~2주 뒤 확인 날짜.
4. Write your series plan: book 2 date, and one back-matter link to book 2 in book 1.
4. 시리즈 계획을 쓰십시오. 2권의 출간일과 1권 뒷부분에 넣을 2권 링크.

```
$ python labs/ch06_ads.py
Spend $60.00, royalties $31.50
ROAS: 0.53
Break-even CPC at 2% conversion: $0.07
Break-even CPC at 5% conversion: $0.18
Read-through: 40%
```

Checkpoint: you can state the ROAS of your test, and you have a fixed budget and a check date.

확인: 테스트의 ROAS를 말할 수 있고, 고정 예산과 확인 날짜가 있습니다.

## Concept — why this works
## 개념 — 왜 이렇게 하는가

Ads can scale what already works, but they cannot fix a weak cover or blurb. Before spending money, check that readers who land on the page buy the book. A ROAS below 1.0 means the ads returned less than they cost in royalties, as the example shows.

광고는 이미 효과가 있는 것을 키울 수는 있지만, 약한 표지나 책 소개문을 고쳐 주지는 못한다. 돈을 쓰기 전에 페이지에 들어온 독자가 실제로 구매하는지 확인해야 한다. ROAS가 1.0보다 낮으면, 위 예시처럼 광고가 로열티로 번 금액이 광고비보다 적다는 뜻이다.

Ad products change often. Amazon Sponsored Products shows your book in search and on other books' pages and charges per click. Sponsored Brands shows several books or a video. Amazon audiobook ads are US only since August 2026 (PPC Land), and Meta and BookBub ads target fans of comp authors. Check Amazon's KDP advertising help before you start.

광고 상품은 자주 바뀐다. Amazon Sponsored Products는 검색과 다른 책의 상세 페이지에 책을 노출하며 클릭당 요금을 받는다. Sponsored Brands는 여러 책이나 동영상을 보여 준다. 아마존 오디오북 광고는 2026년 8월부터 미국에서만 가능하다(PPC Land). Meta와 BookBub 광고는 비교 도서 작가의 팬을 겨냥한다. 시작하기 전에 KDP 광고 도움말을 확인하십시오.

Series and backlist give the best long-term return. A reader who enjoys book 1 often buys books 2, 3 and 4 (read-through). Since one reader may be worth several sales, you can spend more to find each new reader. The back matter of each book is prime space for the next-book link, the newsletter sign-up and a review request.

시리즈와 기존 도서가 장기적으로 가장 좋은 수익을 준다. 1권을 즐긴 독자는 종종 2, 3, 4권도 산다(연속 구매). 독자 한 명이 여러 번의 판매 가치를 가질 수 있으므로, 새 독자를 찾는 데 더 많이 쓸 수 있다. 각 책의 뒷부분은 다음 권 링크, 뉴스레터 구독 신청, 리뷰 요청을 넣기에 좋은 자리다.

Collaboration and direct sales also help. Newsletter swaps work less well than they used to, so pick partners whose readers overlap with yours. Selling from your own store keeps more of each sale and shows you who your readers are; BookFunnel delivers files and handles reader support (ScribeCount).

협업과 직접 판매도 도움이 된다. 뉴스레터 교환은 예전만 못하니, 독자가 겹치는 파트너를 고르십시오. 자신의 판매 페이지에서 팔면 판매마다 더 많이 남고 독자가 누구인지 알 수 있다. BookFunnel은 파일을 전달하고 독자 지원을 처리한다(ScribeCount).

Real-world example: a special edition sells. The *Onyx Storm* "Wing and Claw" edition sold nearly 1.7 million print copies in 2025 (Publishers Weekly). The figure is unverified in the English draft; check it before you quote it.

실제 사례: 특별판은 팔린다. *Onyx Storm*의 "Wing and Claw" 특별판은 2025년 종이책이 거의 170만 부 팔렸다(Publishers Weekly). 이 수치는 영어 원고에서 왔고 검증하지 않았으니, 인용하기 전에 확인하십시오.

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **"Read-through" → 연속 구매.** Korean has no common word for it, so 연속 구매 is used, and 연속 구매율 is the rate.
   "read-through"에 쓰이는 일상적인 한국어가 없어서 "연속 구매"로 옮겼습니다. "연속 구매율"은 비율입니다.
2. **"Backlist" → 기존 도서.** Korean publishers say 기존 도서 for older titles.
   출판 영어 "backlist"는 한국 출판계에서 "기존 도서"라고 합니다.
3. **Unverified claims.** The Sponsored Brands change, the audiobook ad date, the Onyx Storm figure, and the newsletter-swap comment come from the English draft. Ad products change often, so check KDP's help pages.
   Sponsored Brands 변경, 오디오북 광고 날짜, Onyx Storm 수치, 뉴스레터 교환 내용은 영어 원고에서 왔습니다. 광고 상품은 자주 바뀌므로 KDP 도움말을 확인하십시오.

**Glossary terms used in this chapter:** 유료 광고 (paid ads), 연속 구매 (read-through), 기존 도서 (backlist), 번들 (bundle), 박스 세트 (box set), 앤솔러지 (anthology), 공동 프로모션 (group promotion), 판매 페이지 (storefront), 주문 제작 인쇄 (print on demand), 특별판 (special edition).

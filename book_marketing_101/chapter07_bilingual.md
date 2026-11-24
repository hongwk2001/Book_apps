# Chapter 7 — Measure What Works
# 7장 — 효과 있는 것 측정하기

## Lab 7 — Run the monthly check in 15 minutes
## 실습 7 — 15분 안에 월간 점검하기

Goal: compare your ad dashboard with your KDP report week by week, flag the weeks that do not match, and compute read-through from your sales.

목표: 광고 대시보드와 KDP 보고서를 주 단위로 비교하고, 맞지 않는 주를 표시하며, 판매 데이터로 연속 구매율을 계산합니다.

1. Open `labs/ch07_monthly_check.py`. Replace the `WEEKS` rows with your last four weeks: ad spend, ad-dashboard royalties, KDP royalties.
1. `labs/ch07_monthly_check.py`를 여십시오. `WEEKS` 행을 최근 4주의 광고비, 광고 대시보드 로열티, KDP 로열티로 바꾸십시오.
2. Run it. Any week marked CHECK differs by more than 20%. Find out why before you trust the dashboard.
2. 실행하십시오. CHECK로 표시된 주는 차이가 20%를 넘습니다. 대시보드를 믿기 전에 이유를 찾으십시오.
3. Calculate read-through for book 1 to book 2 with `read_through()` in `labs/ch06_ads.py`.
3. `labs/ch06_ads.py`의 `read_through()`로 1권에서 2권으로 가는 연속 구매율을 계산하십시오.
4. Write three lines in your spreadsheet: what worked, what did not, and what you will test next month.
4. 스프레드시트에 세 줄을 쓰십시오. 무엇이 효과가 있었나, 무엇이 없었나, 다음 달에 무엇을 시험할까.

```
$ python labs/ch07_monthly_check.py
W1: spend $20.00  dash $14.00  kdp $13.50  gap +4%  ok
W2: spend $20.00  dash $18.00  kdp $16.00  gap +12%  ok
W3: spend $20.00  dash $15.00  kdp $11.00  gap +36%  CHECK
W4: spend $20.00  dash $22.00  kdp $12.50  gap +76%  CHECK
Total spend $80.00, KDP royalties $53.00, ROAS (KDP) 0.66
```

Checkpoint: you have a flagged list of weeks, one explanation for each flagged week, and the read-through number.

확인: 표시된 주의 목록, 표시된 주마다 하나씩 설명, 연속 구매율 숫자가 있습니다.

## Concept — why this works
## 개념 — 왜 이렇게 하는가

You cannot improve what you do not measure. A few numbers checked once a month show which marketing to keep, which to fix and which to drop. Do not watch the daily sales rank; it moves constantly. Look for trends over weeks and months.

측정하지 않으면 개선할 수 없다. 한 달에 한 번 몇 가지 숫자만 확인해도, 어떤 마케팅을 유지하고 무엇을 고치고 무엇을 그만둘지 알 수 있다. 일일 판매 순위는 끊임없이 움직이므로 보지 않는다. 몇 주, 몇 달에 걸친 추세를 본다.

The core habit is checking one number against another. Compare the ad dashboard with the KDP report. As of November 2026, Amazon Ads no longer shows KDP authors an estimate of Kindle Unlimited page-read royalties after an ad click (PPC Land). For books in Kindle Unlimited, the KDP report is the number to trust, and a three-column spreadsheet (ad spend, sales royalties, page-read royalties) is enough.

핵심 습관은 숫자 하나를 다른 숫자와 맞춰 보는 것이다. 광고 대시보드를 KDP 보고서와 비교한다. 2026년 11월 기준, 아마존 광고는 광고 클릭 후 읽은 킨들 언리미티드 페이지 로열티의 추정치를 더 이상 KDP 작가에게 보여 주지 않는다(PPC Land). 킨들 언리미티드 책이라면 KDP 보고서를 믿어야 하며, 광고비, 판매 로열티, 페이지 읽기 로열티의 세 열짜리 스프레드시트면 충분하다.

Read-through is the share of book 1 readers who go on to book 2. If 1,000 readers buy book 1 and 400 buy book 2, read-through is 40%. High read-through means each new reader is worth more than one sale. Low read-through suggests checking the ending of book 1 and the link to book 2 in its back matter.

연속 구매율은 1권 독자 중 2권으로 이어 읽는 비율이다. 1권을 산 독자가 1,000명이고 그중 400명이 2권을 샀다면, 연속 구매율은 40%다. 연속 구매율이 높으면 새 독자 한 명의 가치가 한 번의 판매보다 크다. 낮다면 1권의 결말과 뒷부분의 2권 링크를 확인해야 한다.

Real-world check: a monthly routine takes about an hour, with three questions each month: what worked, what did not, and what to try next. Write the next book, since it is the best marketing.

실제 점검: 월간 루틴은 약 한 시간이 걸리며, 매달 세 가지 질문을 한다. 무엇이 효과가 있었나, 무엇이 없었나, 다음 달에는 무엇을 시도할까. 그리고 다음 책을 쓴다. 다음 책이 가장 좋은 마케팅이다.

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **"Metric" → 지표.** The standard Korean business term for a measured number.
   "metric"은 측정한 숫자를 뜻하는 한국어 비즈니스 용어 "지표"입니다.
2. **"ROAS" in brackets.** 광고 수익률 with ROAS in brackets, because ROAS is the term on ad dashboards.
   "광고 수익률"에 "ROAS"를 괄호로 붙였습니다. 광고 대시보드에서 이 약어를 보게 됩니다.
3. **Unverified claim.** The November 2026 Amazon Ads change comes from the English draft. Check it in Amazon Ads before you rely on it.
   2026년 11월 아마존 광고 변경은 영어 원고에서 왔습니다. 믿기 전에 아마존 광고에서 직접 확인하십시오.

**Glossary terms used in this chapter:** 지표 (metric), 판매 순위 (sales rank), 리뷰와 평점 (reviews and rating), 이메일 구독자 (email subscribers), 오픈율 (open rate), 클릭률 (click rate), 연속 구매율 (read-through rate), 광고비 (ad spend), 광고 수익률 (ROAS), 로열티 (royalty).

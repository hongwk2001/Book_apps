# Chapter 3 — Build Your Author Platform
# 3장 — 작가 플랫폼 만들기

## Lab 3 — Model your email list before you need it
## 실습 3 — 필요하기 전에 이메일 리스트 모델 만들기

Goal: know how many signups per month your list needs to reach a target, and set one reader magnet and a 3-email welcome sequence.

목표: 목표 구독자 수에 도달하려면 매달 몇 명이 가입해야 하는지 알고, 리더 마그넷(독자에게 주는 무료 선물) 하나와 3통짜리 환영 메일을 정합니다.

1. Write your starting subscriber count, your target, and an honest guess of monthly signups and unsubscribes.
1. 현재 구독자 수, 목표 구독자 수, 매달 가입자와 탈퇴자 수에 대한 솔직한 추정치를 적으십시오.
2. Put those numbers into `labs/ch03_list_growth.py` and run it. Try 10, 20 and 30 signups per month.
2. 그 숫자를 `labs/ch03_list_growth.py`에 넣고 실행하십시오. 매달 가입자를 10명, 20명, 30명으로 바꿔 보십시오.
3. Choose one reader magnet that fits your book: a bonus story (fiction) or a checklist or worksheet (nonfiction).
3. 책에 맞는 리더 마그넷을 하나 고르십시오. 소설이라면 보너스 단편, 논픽션이라면 체크리스트나 워크시트가 좋습니다.
4. Write three emails: the gift and thank-you, your story, and one question that starts a conversation. Schedule them over about two weeks.
4. 이메일 세 통을 쓰십시오. 첫 번째는 선물과 감사 인사, 두 번째는 여러분의 이야기, 세 번째는 대화를 시작하는 질문입니다. 약 2주에 걸쳐 보내도록 예약하십시오.

```
$ python labs/ch03_list_growth.py
Start 40, net +21/month
Months to reach 500: 22
Pace check:
  signups 10/month -> 77 months
  signups 20/month -> 29 months
  signups 30/month -> 18 months
```

Checkpoint: you can say, from the output, how many signups per month your target needs, and your magnet and three emails exist as drafts.

확인: 출력을 보고 목표를 이루려면 매달 몇 명이 가입해야 하는지 말할 수 있고, 리더 마그넷과 이메일 세 통의 초안이 있습니다.

## Concept — why this works
## 개념 — 왜 이렇게 하는가

Your website is your permanent home online. It needs to answer a visitor's questions fast: your latest book, a one-line description of what you write, a newsletter signup, your books with buy links, and a contact or media page. Buy your own domain (yourname.com) so the address survives a change of website builder.

웹사이트는 온라인에서 여러분의 영구적인 집입니다. 방문자의 질문에 빠르게 답해야 합니다. 최신작, 여러분이 쓰는 글을 한 줄로 설명한 문장, 뉴스레터 구독 신청, 구매 링크가 있는 책 페이지, 연락처와 미디어 페이지가 필요합니다. 자신의 도메인(yourname.com)을 사 두면, 웹사이트 제작 도구를 바꿔도 주소가 그대로 유지됩니다.

The email list is the channel you own. Social platforms change their rules and can shrink your reach overnight. Subscribers have asked to hear from you, so an email list is usually the most reliable way to sell on launch day. A welcome sequence of 3–5 emails over about two weeks delivers the gift, shares your story, introduces your books and asks a question.

이메일 리스트는 여러분이 직접 가진 채널입니다. 소셜 플랫폼은 규칙을 바꾸고, 하룻밤 사이에 도달 범위를 줄일 수 있습니다. 구독자는 여러분의 소식을 듣기로 직접 요청한 사람들입니다. 그래서 출간일에 책을 파는 가장 믿을 만한 방법인 경우가 많습니다. 약 2주 동안 3~5통의 환영 메일을 보내면 선물을 전하고, 이야기를 나누고, 책을 소개하고, 질문을 던질 수 있습니다.

Choose one or two social platforms, not all of them. Pick where your reader profile from Chapter 1 spends time. Facebook (62%) and Instagram (51%) were the most-used weekly platforms in a recent BookBub author survey, with Bluesky third at 21% (BookBub Insights). Always point people back to your newsletter.

소셜 플랫폼은 모두 쓰지 말고 한두 곳만 고르십시오. 1장에서 정한 독자 프로필이 시간을 보내는 곳을 고르면 됩니다. 최근 BookBub 작가 설문에서 주간 사용률이 가장 높은 곳은 Facebook(62%)과 Instagram(51%)이었습니다. Bluesky는 21%로 3위였습니다(BookBub Insights). 사람들을 늘 뉴스레터로 다시 안내하십시오.

Written Word Media's survey of 1,346 indie authors found that authors with an email list earned a median of about $300 a month, versus about $15 for those without one. The figures are self-reported and show a link, not proof that the list causes the income.

Written Word Media가 독립 작가 1,346명을 대상으로 한 설문에서, 이메일 리스트가 있는 작가의 월 중앙값 수입은 약 $300이었습니다. 없는 작가는 약 $15였습니다. 이 수치는 작가들이 직접 응답한 값입니다. 리스트와 수입이 관련 있다는 것은 보여 주지만, 리스트가 수입을 만든다는 증거는 아닙니다.

Real-world example: Mel Robbins's *The Let Them Theory* was the bestselling print book in the US in 2025, at more than 2.8 million copies (Publishers Weekly). The idea started as a podcast episode and social posts before the book went on sale (publisher's sell sheet). Test your core idea in public first.

실제 사례: 멜 로빈스(Mel Robbins)의 *The Let Them Theory*는 2025년 미국에서 가장 많이 팔린 종이책이었고, 280만 부가 넘게 팔렸습니다(Publishers Weekly). 이 아이디어는 책이 나오기 전에 팟캐스트 에피소드와 소셜 게시물로 먼저 시작되었습니다(출판사 제품 소개지). 핵심 아이디어는 먼저 공개적으로 시험해 보십시오.

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **"platform" has two meanings.** 플랫폼 can mean an app or service, so the title says "작가 플랫폼" to make it clear.
   "플랫폼"은 앱이나 서비스를 뜻하기도 하므로, 제목에 "작가 플랫폼"이라고 썼습니다.
2. **"reader magnet" → 리더 마그넷.** No common Korean word exists, so the English stays, with 무료 증정물 on first use.
   한국어로 굳어진 말이 없어서 영어를 그대로 쓰고, 처음에만 "무료 증정물"을 붙였습니다.
3. **Unverified figures.** The platform percentages, the Written Word Media numbers and the Mel Robbins sales come from the English draft. Check the original sources before publishing.
   플랫폼 비율, Written Word Media 수치, Mel Robbins 판매량은 영어 원고에서 왔고 검증하지 않았습니다. 출간 전에 원자료를 확인하십시오.

**Glossary terms used in this chapter:** 작가 플랫폼 (author platform), 이메일 리스트 (email list), 뉴스레터 (newsletter), 리더 마그넷 (reader magnet), 환영 메일 시리즈 (welcome sequence), 소셜 미디어 (social media), 독자 그룹 (reader groups), 미디어 키트 (media kit).

# Bonus Chapter — Case Study: Marketing This Book
# 보너스 챕터 — 사례 연구: 이 책을 홍보하기

The best proof that a system works is to use it in public. This chapter applies Chapters 1–7 to *Book Marketing 101* itself, with the way the book was made as the main hook. Treat it as a worked example you can copy for your own book.

시스템이 효과가 있다는 가장 좋은 증거는 공개적으로 써 보는 것이다. 이 장은 1~7장을 *Book Marketing 101*에 직접 적용한다. 책이 만들어진 방식을 핵심 훅으로 삼았다. 여러분의 책에 그대로 옮겨 쓸 수 있는 실습 예시로 읽어 주십시오.

## Lab B — Run this book's own launch
## 실습 B — 이 책의 출간을 직접 실행하기

Goal: track this book's launch with the same checklist you would use for your own, and see where it stands today.

목표: 여러분 책에 쓸 것과 같은 체크리스트로 이 책의 출간을 추적하고, 지금 어디에 있는지 봅니다.

1. Open `labs/bonus_launch_check.py`. Change a `False` to `True` for each task this book has finished.
1. `labs/bonus_launch_check.py`를 여십시오. 이 책에서 끝낸 작업마다 `False`를 `True`로 바꾸십시오.
2. Run it. The script reports progress by stage, the same way Appendix A is organized.
2. 실행하십시오. 부록 A와 같은 단계별로 진행률이 나옵니다.
3. Pick the stage with the lowest progress and write its next action on one line.
3. 진행률이 가장 낮은 단계를 고르고, 다음에 할 일을 한 줄로 쓰십시오.

```
$ python labs/bonus_launch_check.py
Book ready: 0/4
Platform ready: 0/3
Pre-launch done: 0/3
Overall: 0/10 (0%)
```

Checkpoint: the output matches the state of this book today, and you have one next action written.

확인: 출력이 오늘 이 책의 상태와 같고, 다음 할 일이 한 줄로 적혀 있습니다.

### Step 1 — Know the book and the reader (Chapter 1)
### 1단계 — 책과 독자 알기 (1장)

- Shelf: nonfiction → business and writing → book marketing for self-published and first-time authors.
- 서가: 논픽션 → 비즈니스와 글쓰기 → 독립 출간 작가와 초보 작가를 위한 도서 마케팅.
- Reader profile: a first-time author, finished or nearly finished with a book, overwhelmed by marketing advice, curious about AI tools but unsure whether to trust them.
- 독자 프로필: 첫 책을 쓰는 작가. 원고를 끝냈거나 거의 끝냈고, 마케팅 조언에 압도되어 있으며, AI 도구에 호기심이 있지만 믿어도 될지 확신이 없다.
- Comps: established book-marketing guides for indie authors. Before using any as comps, check that they are recent and still selling, as Chapter 1 recommends. [Add your 3–5 comps here.]
- 비교 도서: 독립 작가를 위한 검증된 도서 마케팅 가이드. 1장의 권고대로, 비교 도서로 쓰기 전에 최신이고 여전히 팔리는지 확인하십시오. [여기에 비교 도서 3~5권을 추가하십시오.]

Hook options. Test these on people who have not seen the book and keep the one that gets the most follow-up questions:

훅 후보. 책을 본 적 없는 사람에게 테스트하고, 후속 질문을 가장 많이 받는 것을 고르십시오:

- The book-marketing guide that markets itself.
- 스스로를 홍보하는 도서 마케팅 가이드.
- I wrote a book about book marketing with AI, then used it to launch the book. Here is everything that happened.
- AI와 함께 도서 마케팅에 관한 책을 썼고, 그 방법으로 이 책을 출간했습니다. 일어난 모든 일을 공개합니다.
- A beginner's book-marketing system, built with AI and tested on its own launch.
- AI와 함께 만들고, 자기 출간으로 시험해 본 초보자용 도서 마케팅 시스템.

Comp pitch: "A beginner's book-marketing guide meets a behind-the-scenes AI experiment."

비교 피치: "초보자를 위한 도서 마케팅 가이드와 AI 실험 비하인드 스토리의 만남."

### Step 2 — Get the book ready to sell (Chapter 2)
### 2단계 — 판매 준비 (2장)

- Subtitle idea: Book Marketing 101: A Step-by-Step System to Find Readers, Built with AI and Tested on Its Own Launch.
- 부제 아이디어: *Book Marketing 101: A Step-by-Step System to Find Readers, Built with AI and Tested on Its Own Launch* (영문 부제는 그대로 두고, 한국어판 부제는 별도로 정한다).
- Cover: follow the look of the nonfiction marketing shelf (bold title, clean design). Any AI visual should stay subtle; the hook is in the subtitle and blurb.
- 표지: 논픽션 마케팅 서가의 분위기를 따르십시오(굵은 제목, 깔끔한 디자인). AI로 만든 이미지는 눈에 띄지 않게 두십시오. 훅은 부제와 책 소개문에 있다.
- Draft blurb (using the nonfiction template in Appendix C):
- 책 소개문 초안(부록 C의 논픽션 템플릿 사용):

> You wrote a book. Now how do you get anyone to read it?
> 책을 썼습니다. 이제 어떻게 독자에게 닿게 할까요?
>
> Most marketing advice is either too vague to use or too overwhelming to start. Book Marketing 101 gives you one clear system, from knowing your reader to launch week and beyond. You'll learn:
> 대부분의 마케팅 조언은 너무 막연해서 쓸 수 없거나, 너무 벅차서 시작하기 어렵다. *Book Marketing 101*은 독자를 아는 것부터 출간 주간과 그 이후까지, 하나의 분명한 시스템을 준다. 이 책에서 배울 내용:
>
> - How to package your book so the right readers stop scrolling
> - 맞는 독자가 스크롤을 멈추게 하는 방식으로 책을 포장하는 법
> - How to build an email list and a launch team before release day
> - 출간일 전에 이메일 리스트와 출간 팀을 만드는 법
> - How to plan a launch week and keep selling for years
> - 출간 주간을 계획하고 몇 년 동안 계속 파는 법
>
> And this book does not just give advice. It was written with AI, then marketed using its own methods, and the Bonus Chapter shows you exactly how.
> 그리고 이 책은 조언만 주지 않는다. AI와 함께 쓰였고, 그 방법 그대로 홍보되었다. 보너스 챕터가 정확히 어떻게 했는지 보여 준다.

### Step 3 — Build the platform (Chapter 3)
### 3단계 — 플랫폼 만들기 (3장)

- Reader magnet: the Launch Checklist and 90-Day Calendar from the appendices, offered as a free printable download.
- 리더 마그넷: 부록의 출간 체크리스트와 90일 달력을 무료 인쇄용 다운로드로 제공한다.
- Content angle: a behind-the-scenes series, such as "How I wrote a book with AI, and what it got wrong." Honest stories about limits build more trust than hype.
- 콘텐츠 방향: "AI와 함께 책을 쓴 과정, 그리고 AI가 틀린 것들"처럼 비하인드 시리즈로 만든다. 한계를 솔직하게 말하는 이야기가 과장된 광고보다 더 큰 신뢰를 쌓는다.
- Platforms: go where authors gather. For a nonfiction book about publishing, the 2026 platform guide in Chapter 3 points to Substack (a newsletter plus Notes), YouTube for teaching videos, Bluesky for writing-community conversation, and Facebook author groups. Start with two, following the Mel Robbins model: publish the ideas from each chapter as free posts first and turn the best-performing ones into launch content.
- 플랫폼: 작가들이 모이는 곳에 가십시오. 출판에 관한 논픽션이라면, 3장의 2026년 플랫폼 가이드는 Substack(뉴스레터와 Notes), 교육용 영상을 위한 YouTube, 글쓰기 커뮤니티 대화를 위한 Bluesky, 페이스북 작가 그룹을 가리킨다. 멜 로빈스 방식을 따라 두 곳부터 시작하십시오. 각 장의 아이디어를 먼저 무료 게시물로 올리고, 반응이 좋은 것을 출간 콘텐츠로 키운다.

### Step 4 — Pre-launch (Chapter 4)
### 4단계 — 출간 전 (4장)

- ARC readers: recruit from writing groups and your newsletter; invite readers who are skeptical of AI too, because their honest reviews will be the most convincing.
- ARC 독자: 글쓰기 모임과 뉴스레터에서 모집하십시오. AI에 회의적인 독자도 초대하십시오. 그들의 솔직한 리뷰가 가장 설득력이 있을 것이다.
- Podcast pitch angle: "What happens when you write a book with AI, and what AI still cannot do in book marketing." Target podcasts about self-publishing, writing craft and AI tools.
- 팟캐스트 제안 방향: "AI와 함께 책을 쓰면 무슨 일이 생기는가, 그리고 AI가 도서 마케팅에서 여전히 못 하는 것은 무엇인가." 독립 출판, 글쓰기 기술, AI 도구를 다루는 팟캐스트를 겨냥하십시오.
- Cover reveal: share the hook alongside the cover.
- 표지 공개: 표지와 함께 훅을 공유하십시오.

### Step 5 — Launch week (Chapter 5)
### 5단계 — 출간 주간 (5장)

Use the day-by-day plan, with a behind-the-scenes theme each day: Day 2 shares how the book was made, and Day 4 might be a live session showing how a chapter was drafted and edited.

날짜별 계획을 쓰되, 매일 비하인드 주제를 하나씩 넣으십시오. 2일차에는 책이 어떻게 만들어졌는지 공유하고, 4일차에는 한 장이 어떻게 초안에서 편집까지 갔는지 보여 주는 라이브 세션을 할 수 있다.

### Step 6 — Long-term (Chapter 6)
### 6단계 — 장기 (6장)

- Turn the experiment into a series: a workbook, an updated edition, or a follow-up book on AI tools for authors.
- 실험을 시리즈로 만드십시오. 워크북, 개정판, 또는 작가를 위한 AI 도구에 관한 후속작.
- Swap newsletters with authors who write about craft, publishing or productivity.
- 글쓰기, 출판, 생산성에 대해 쓰는 작가와 뉴스레터를 교환하십시오.

### Step 7 — Measure and share the results (Chapter 7)
### 7단계 — 결과 측정하고 공유하기 (7장)

Track the numbers in Chapter 7 and publish them in your newsletter: sales, subscribers, what worked and what flopped. A launch reported honestly becomes its own marketing: "Month 3 results from the book that markets itself." Future editions can update this chapter with real numbers.

7장의 숫자를 추적하고, 뉴스레터에 공개하십시오. 판매량, 구독자, 효과가 있었던 것과 실패한 것을 함께 쓴다. 솔직하게 보고한 출간은 그 자체가 마케팅이 된다. "스스로를 홍보하는 책의 3개월 결과." 앞으로의 판에서는 이 장을 실제 수치로 업데이트할 수 있다.

### Handle the AI angle with care
### AI 이야기는 신중하게 다루기

AI is a powerful hook, but it divides readers. Some authors are excited by it; others feel strongly that AI harms writers. Keep the hook honest and useful:

AI는 강력한 훅이지만, 독자를 둘로 나눈다. 어떤 작가는 흥분하고, 다른 작가는 AI가 글 쓰는 사람을 해친다고 강하게 느낀다. 훅은 솔직하고 쓸모 있게 유지하십시오:

- Be transparent. Say plainly what the AI did and what you did. Never present AI-drafted text as entirely your own.
- 투명하게 하십시오. AI가 무엇을 했고 여러분이 무엇을 했는지 분명히 말하십시오. AI가 초안을 쓴 글을 전부 여러분이 쓴 것처럼 내놓지 마십시오.
- Disclose to the store. Amazon KDP requires publishers to say whether a book contains AI-generated text, images or translations; AI-assisted work (your own writing that AI helped edit or refine) does not need disclosure. Text that an AI drafted counts as AI-generated, so this book should be disclosed. Check each store's current rules before you publish.
- 서점에 고지하십시오. 아마존 KDP는 출간자가 책에 AI 생성 텍스트, 이미지, 번역이 포함되는지 밝히도록 요구한다. AI가 편집하거나 다듬은 여러분 자신의 글(AI 보조 작업)은 고지가 필요 없다. AI가 초안을 쓴 텍스트는 AI 생성으로 간주되므로, 이 책은 고지해야 한다. 출간 전에 각 서점의 최신 규칙을 확인하십시오.
- Know the copyright question. In some countries, including the US, text generated by AI without enough human authorship may have limited copyright protection. Your own edits, additions and stories strengthen your claim; check current guidance or ask a publishing lawyer.
- 저작권 문제를 알아 두십시오. 미국을 포함한 일부 국가에서는 인간의 저작성이 충분하지 않은 AI 생성 텍스트는 저작권 보호가 제한될 수 있다. 여러분의 편집, 추가 내용, 이야기는 권리 주장을 강화한다. 최신 지침을 확인하거나 출판 전문 변호사에게 문의하십시오.
- Lead with the reader's benefit. The hook gets attention; the useful system is what earns reviews.
- 독자에게 돌아가는 이익을 앞세우십시오. 훅은 관심을 끌고, 쓸모 있는 시스템이 리뷰를 얻는다.

---

## Learning notes (for you)
## 학습 노트 (읽는 분을 위한 설명)

1. **Placeholder kept on purpose.** "[Add your 3–5 comps here.]" is still a placeholder. It is translated so you can fill it in, not because it is part of the finished text.
   "[여기에 비교 도서 3~5권을 추가하십시오.]"는 아직 채워지지 않은 자리표시자입니다. 완성된 본문이 아니라, 여러분이 채울 수 있도록 번역해 두었습니다.
2. **Subtitle left as English.** The English subtitle is the book's selling line. Decide later whether the Korean edition needs its own subtitle, following the title decision you made.
   영문 부제는 책의 판매 문구이므로 우선 영어로 두었습니다. 제목에 대한 결정처럼, 한국어판에 별도 부제가 필요한지는 나중에 정하면 됩니다.
3. **Blockquote for the blurb.** The sample blurb is set as a quote so it reads as a separate piece of copy. Notice how the English and Korean sit in pairs even inside the quote.
   샘플 책 소개문은 인용문으로 따로 표시했습니다. 인용문 안에서도 영어와 한국어가 짝을 이루는 것을 확인해 보십시오.
4. **Unverified claims.** The platform guide references, the Mel Robbins model, and the KDP disclosure rules are from the English draft. The KDP AI-disclosure rule is important for this book; verify it on KDP's current content guidelines before you publish.
   플랫폼 가이드 참조, 멜 로빈스 방식, KDP 고지 규칙은 영어 원고에서 왔습니다. KDP의 AI 고지 규칙은 이 책에 특히 중요하므로, 출간 전에 KDP 최신 콘텐츠 가이드라인에서 확인하십시오.

**Glossary terms used in this chapter:** 리더 마그넷 (reader magnet), 비교 도서 (comps), 훅 (hook), 책 소개문 (blurb), 표지 (cover), 부제 (subtitle), 출간 주간 (launch week), 비하인드 (behind-the-scenes), 저작권 (copyright), AI 생성 (AI-generated).

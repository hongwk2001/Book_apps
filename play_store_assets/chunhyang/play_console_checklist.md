# 춘향전 — Play Console checklist (first release)

AAB: `chunhyang/build/outputs/bundle/release/chunhyang-release.aab` (versionCode 1, versionName "1.0")
Screenshots to upload: `play_store_assets/chunhyang/upload/` (24-bit PNG, alpha removed)

> ⚠ Heads-up first: if your developer account is a **personal** account created after Nov 2023,
> Google requires a **closed test with ≥12 testers for 14 days** before each app can go to Production
> (Dashboard shows "Apply for production access"). If Dracula went straight to Production, ignore this.

---

## 1. Create app
All apps → **Create app**
- App name: `춘향전 Chunhyang: Korean-English`
- Default language: **English (United States) – en-US** (same as Dracula; Korean added as a translation in step 3)
- App or game: **App** · Free or paid: **Free** (can't be changed later)
- Tick the two declarations → Create app

## 2. App content (Policy → App content) — do these before the release can be sent for review
| Item | Answer |
|---|---|
| Privacy policy | Same URL pattern as Dracula, e.g. `…/chunhyang-privacy` (copy Dracula's policy text, change the app name) |
| Ads | **No, my app does not contain ads** |
| App access | **All functionality is available without special access** |
| Content rating | see 2a |
| Target audience | **13–15, 16–17 and 18+**. "Could appeal to children?" → **No** |
| News app | No |
| Data safety | see 2b |
| Government app | No |
| Financial features | **My app doesn't provide any financial features** |
| Health | No |
| Foreground service permissions | The app declares `FOREGROUND_SERVICE_MEDIA_PLAYBACK` → choose **Media playback**; describe: "Reads the book aloud with text-to-speech; playback continues with the screen off and is controlled from the media notification." Reuse Dracula's demo video link (same shared code). |

### 2a. Content rating (IARC questionnaire)
- Email: tkprof.ai@gmail.com · Category: **Reference, News, or Educational**
- Violence: **Yes** — realistic violence described in text (a beating/punishment scene), **no** blood/gore detail, not glorified
- Sexuality: **Yes** → tick only *Suggestive/Sexual Themes or References* → *Suggestive references and innuendo in text*. Sexual situations involving under-18s: **not ticked** (no ages are stated and nothing sexual is described)
- Language: crude humor/innuendo **Yes** if asked (the bawdy jokes); no strong profanity
- Controlled substances: references to **alcohol** (drinking at the feast) → Yes, references only
- Gambling: No · User interaction/sharing: No · Shares location: No
- **Digital purchases: Yes** (optional tips)
- Expected result: Teen / 12+ (GRAC 12세, PEGI 12). If it comes out 15+/16, that's fine too.

### 2b. Data safety
- Does your app collect or share any required user data types? → **No**
  (No accounts, no analytics, no ads SDK; reading progress stays on the device; purchases are processed by Google Play Billing.)
- Then confirm "No data collected" summary → Save. (If Dracula's form says otherwise, copy Dracula's answers — the code is shared.)

## 3. Store listing (Grow → Store presence → Main store listing)
Play does **not** render Markdown. Paste the text below (uses `<b>` and `•`, which Play accepts).

**App name (30):** `춘향전 Chunhyang: Korean-English`
**Short description (80):** `Korea's great love story in modern Korean and simple English, with read-aloud.`

**Full description (en-US):**
```
Chunhyang, a gisaeng's daughter, falls in love with Master Yi, the magistrate's son, on a spring day by a swing. They marry in secret, he must leave for Seoul, and a cruel new magistrate demands that she become his. She refuses, and pays for it. This is Korea's best-loved love story, told in full.

<b>What makes this edition different</b>
• <b>From the original woodblock.</b> Translated from the 1911 Wanpan woodblock edition (열녀춘향수절가), the classic version of the tale, using images held by the National Museum of Korea.
• <b>Two languages, line by line.</b> Every line appears in natural modern Korean and in simple, clear English (about B1 level), so you can read either one and check the other.
• <b>Read-aloud in both languages.</b> Listen in English, Korean, or both, with adjustable speed and pitch.
• <b>Wordplay made readable.</b> The famous songs and jokes, including the love song, the Thousand Character Classic puns, and the ten-stroke song, are explained so learners can enjoy them.
• <b>About three hours long.</b> 21 short chapters, each 5–14 minutes.
• <b>Free to read to the end.</b> No ads, and every chapter can be read for free. Now and then the app asks if you'd like to buy the developer a coffee; tap "Not now" and keep reading. Tips are optional.

Good for Korean learners of English, English speakers learning Korean, and anyone who wants to meet a great Korean classic.

Note: the story includes romance with playful innuendo and a punishment scene. Suitable for ages 13 and up.

Source images: "Yeollyeo Chunhyang Sujeolga" (신수15187), National Museum of Korea, used under KOGL Type 1 (공공누리 제1유형).
```

Graphics: App icon `play_store_icon.png` · Feature graphic `feature_graphic.png` · Phone screenshots `upload/1_reader.png … 4_tts_settings.png` (if Play rejects the 1080×2400 aspect ratio, use the `*_9x16.png` versions instead).

**Add Korean translation:** Manage translations → Add your own → **Korean – ko-KR**:
- App name: `춘향전 Chunhyang: 한영 대역`  (or keep the English one)
- Short description: `한국인이 가장 사랑하는 사랑 이야기를 현대 한국어와 쉬운 영어로, 읽어 주기까지.`
- Full description:
```
봄날 광한루 그네 아래에서 시작된 춘향과 이몽룡의 사랑, 그리고 변 사또의 수청 요구에 맞선 춘향의 절개. 한국인이 가장 사랑하는 고전 『춘향전』을 처음부터 끝까지 담았습니다.

<b>이 책의 특징</b>
• <b>완판 84장본 원전 번역.</b> 국립중앙박물관 소장 완판본 「열녀춘향수절가」(1911) 이미지를 바탕으로 새로 옮겼습니다.
• <b>한 줄씩 한국어와 영어.</b> 자연스러운 현대 한국어와 쉬운 영어(B1 수준)를 나란히 보여 줍니다.
• <b>두 언어로 읽어 주기.</b> 영어, 한국어, 또는 둘 다 들을 수 있고 속도와 높낮이를 조절할 수 있습니다.
• <b>말놀이까지 쉽게.</b> 사랑가, 천자풀이, 십장가 같은 노래와 말장난을 학습자도 즐길 수 있게 풀었습니다.
• <b>약 3시간 분량.</b> 21개의 짧은 장, 한 장에 5~14분.
• <b>끝까지 무료.</b> 광고 없이 모든 장을 무료로 읽을 수 있습니다. 가끔 "개발자에게 커피 한 잔" 후원 안내가 나오지만 "나중에 하기"를 누르고 계속 읽으시면 됩니다. 후원은 선택입니다.

※ 사랑 이야기의 재치 있는 농담과 형벌 장면이 포함되어 있습니다. 13세 이상 권장.

원문 이미지: 국립중앙박물관 소장 「열녀춘향수절가」(신수15187), 공공누리 제1유형
```
(Korean screenshots: optional; the English ones are used if none are added.)

**Store settings:** Category **Books & Reference** · Tags: Books, Education, Language learning · Contact email tkprof.ai@gmail.com · Website (optional).

## 4. Upload the AAB (creates the app's billing link)
Test and release → **Production** → Countries/regions tab first: **Add countries** → South Korea + others (e.g. United States, Canada, UK, Australia, Japan, Singapore… or "Select all")
→ Releases tab → **Create new release** → accept **Play App Signing** (Google-managed key) → upload `chunhyang-release.aab`
- Release name: `1 (1.0)`
- Release notes:
```
<en-US>
First release: the full Tale of Chunhyang in modern Korean and simple English, with read-aloud.
</en-US>
<ko-KR>
첫 출시: 『춘향전』 전체를 현대 한국어와 쉬운 영어로, 읽어 주기 기능과 함께.
</ko-KR>
```
→ **Save** (don't send for review yet if the tips aren't set up).

## 5. In-app tip products (Monetize → Products → In-app products / One-time products)
Available only after an AAB with the billing library is uploaded (step 4). Create, set **Active**:

| Product ID | Name (en) | Name (ko) | Description | Price (KRW default) |
|---|---|---|---|---|
| `tip_small_1500` | Small Coffee Tip | 작은 커피 후원 | Buy the developer a small coffee. Thank you! / 개발자에게 작은 커피 한 잔. 감사합니다! | ₩1,500 |
| `tip_medium_3000` | Big Coffee Tip | 큰 커피 후원 | Buy the developer a big coffee. Thank you! / 개발자에게 큰 커피 한 잔. 감사합니다! | ₩3,000 |

Set price in KRW, then "Update exchange rates" for other countries. (Code also lists `tip_large_5000`, but no button uses it — optional.)
Product IDs can never be reused, so type them exactly.

## 6. Send for review
Publishing overview → **Send changes for review**. Typical first review: a few days (up to ~7).
Once live, https://play.google.com/store/apps/details?id=com.tkprof.chunhyang will work and the Google Ads App campaign can target it.

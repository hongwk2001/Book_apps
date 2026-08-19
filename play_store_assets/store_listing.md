# Google Play Store Release Kit

All your visual assets (512x512 Icon & 1024x500 Feature Graphic) have been successfully generated and saved to `C:\git_repo\Book_apps\play_store_assets`.

Here is the finalized Store Listing text and Privacy Policy to copy-paste into the Google Play Console.

---

## 1. Store Listing Text (English)

**App Name (Max 30 chars):**
`Dracula: Bilingual TTS Reader`

**Short Description (Max 80 chars):**
`Read and listen to Dracula in English with full Korean translations and TTS!`

**Full Description:**
```text
Immerse yourself in Bram Stoker's classic masterpiece, Dracula, while mastering your English reading and listening skills! 

Designed specifically for Korean speakers, this bilingual reader provides a seamless experience for both casual reading and language study. 

Key Features:
🦇 Bilingual Text: Read the original English text alongside high-quality Korean translations.
🎧 Built-in TTS Audio: Listen to the story using native Android Text-to-Speech.
⚙️ Adjustable Speed: Slow down for practice or speed up to 3.0x for a challenge.
📖 Auto-scrolling: Never lose your place—the text automatically highlights and scrolls as you listen.
📞 Smart Audio Focus: The app intelligently pauses playback when you receive a phone call and resumes when you're done.
🌙 Dark Mode Support: Read comfortably at night with a beautiful, eye-friendly dark theme.

Start your journey into Transylvania today! Chapters 1 & 2 are completely free. Unlock the rest of the book to continue the adventure.
```

---

## 2. Store Listing Text (Korean)

**App Name (Max 30 chars):**
`드라큘라: 영한 쌍방향 오디오북`

**Short Description (Max 80 chars):**
`드라큘라 영문 원서와 한국어 번역을 동시에! TTS 오디오 기능으로 영어 듣기 연습까지 완벽하게.`

**Full 정식 설명 (Long Description):**
```text
브램 스토커의 고전 명작 '드라큘라'를 읽으며 영어 원서 읽기와 듣기 실력을 동시에 향상시켜 보세요!

한국어 사용자를 위해 특별히 설계된 이 앱은 원서 읽기의 장벽을 낮추고, 몰입감 넘치는 오디오북 경험을 제공합니다.

주요 기능:
🦇 영한 쌍방향 텍스트: 영어 원문과 매끄러운 한국어 번역을 함께 비교하며 읽을 수 있습니다.
🎧 내장 TTS 오디오: 안드로이드 기본 텍스트 음성 변환(TTS)을 통해 정확한 발음으로 이야기를 들려줍니다.
⚙️ 속도 조절: 내 실력에 맞게 오디오 속도를 세밀하게 조절하세요 (최대 3.0x 지원).
📖 자동 스크롤: 음성에 맞춰 텍스트가 자동으로 따라가며 하이라이트 되므로 길을 잃을 염려가 없습니다.
📞 스마트 오디오 포커스: 전화가 오면 오디오가 자동으로 일시 정지되며, 통화가 끝나면 읽던 곳에서 자연스럽게 다시 시작됩니다.
🌙 다크 모드 지원: 어두운 곳에서도 눈이 편안한 다크 모드 테마를 완벽하게 지원합니다.

트랜실바니아로의 오싹한 여행을 지금 시작해 보세요! 1장과 2장은 완전 무료로 제공됩니다. 

언어 학습과 독서의 즐거움을 한 번에 경험하세요!
```

---

## 3. Privacy Policy (개인정보 처리방침)

Google requires a privacy policy URL. Here is a clean, compliant policy you can use:

**Text to copy:**
```text
Privacy Policy for TKProf Dracula Bilingual Reader

TKProf built the Dracula Bilingual Reader app as a Freemium app. This SERVICE is provided by TKProf at no cost for the initial chapters and is intended for use as is.

Information Collection and Use:
Our app does NOT actively collect, store, or transmit any personally identifiable information (PII). The app utilizes the device's built-in Android Text-to-Speech (TTS) engine, which processes text locally on your device.

Permissions:
The app may require standard permissions (like internet access for billing) to process in-app purchases through the Google Play Billing Library. We do not store or process your payment details on our own servers.

Changes to This Privacy Policy:
We may update our Privacy Policy from time to time. Thus, you are advised to review this page periodically for any changes.

Contact Us:
If you have any questions or suggestions about our Privacy Policy, do not hesitate to contact us.
```

### Recommendation on Hosting:
Since you already have **jigsawpuzzlehelper**, I highly recommend hosting it there! Creating a simple page like `jigsawpuzzlehelper.com/dracula-privacy` looks incredibly professional and builds strong brand trust. 
Alternatively, **Google Docs** is perfectly fine and heavily used by indie developers—just paste the text above into a Google Doc, click "Share," set it to "Anyone with the link can view," and paste that URL into the Play Console!

---

## 4. Final Step: Generating the App Bundle (.aab)

To upload the app to Google Play, you need a signed `.aab` file. 

1. Open **Android Studio**.
2. In the top menu, click **Build > Generate Signed Bundle / APK...**
3. Select **Android App Bundle** and click Next.
4. Under **Key store path**, click **Create new...**
   * Choose a safe place on your PC (e.g., your Documents folder). **Never lose this file or password!** You need it for all future updates.
   * Fill in the passwords and your name in the certificate info.
5. Select the `dracula` module.
6. Select the **release** build variant and click **Create**.
7. Android Studio will generate an `.aab` file in `dracula/release/`. This is the file you upload to the Google Play Console!

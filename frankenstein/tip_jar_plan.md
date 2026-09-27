# Free + Tip Jar Implementation Plan

This plan details how to transition your book apps to a completely free model with voluntary "Tip" options, utilizing a "soft paywall".

## 1. Google Play Console Changes
1. Go to **Google Play Console** -> **Monetize** -> **In-app products**
2. Create 3 new products (we will make these standard one-time purchases since it unlocks the rest of the book without interruptions):
   - **Product ID:** `tip_small_1500` | Name: "Small Coffee Tip" | Price: 1,500 KRW
   - **Product ID:** `tip_medium_3000` | Name: "Big Coffee Tip" | Price: 3,000 KRW
   - **Product ID:** `tip_large_5000` | Name: "Lunch Tip" | Price: 5,000 KRW

## 2. Changes to `BillingManager.kt`
- Modify `BillingManager` to accept multiple Product IDs (e.g., `tip_small_1500`, `tip_medium_3000`, `tip_large_5000`).
- Update `launchPurchaseFlow` to take a specific `productId` as a parameter.
- Update `restorePurchases()` so that if the user has purchased *any* of the three tip options, `isFullUnlocked` becomes true.

## 3. UI Changes (The "Soft Paywall" Screen)

### A. The Soft Paywall Logic (Every 3 Chapters)
- Whether the user hits "Next Chapter" to reach Chapter 3/6/9, or if they select those locked chapters directly from the **Table of Contents**, they will be presented with a full-screen support page.
- If the user purchases any of the tip options, **all future chapters are permanently unlocked** and they will never see this screen again.
- If the user clicks **"Not Now"**, the next 3 chapters unlock for free, and they can continue reading immediately. The screen will simply appear again in another 3 chapters.

### B. The Polite Message
The screen will have a friendly, honest message in both English and Korean depending on their device language:

**English (`strings.xml`):**
> "I'm a solo developer and put a lot of effort into creating this bilingual reading experience. If you are enjoying the book so far, a small tip would mean the world to me and help me create more apps!"

**Korean (`strings.xml` in `values-ko`):**
> "1인 개발자로서 많은 정성을 들여 만든 앱입니다. 지금까지 책을 즐겁게 읽으셨다면, 작은 후원 부탁드립니다. 앞으로 더 좋은 앱을 만드는 데 큰 힘이 됩니다!"

### C. Menu Button
- We will add a persistent "☕ Support Developer" (개발자 후원하기) button in the Top App Bar or Navigation Drawer so users can tip at any time without waiting for the paywall.

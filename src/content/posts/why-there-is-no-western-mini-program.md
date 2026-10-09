---
title: Why there is no Western mini program
description: A mini program inherits its identity and its payment rail from the app hosting it. Here is that mechanism, and what the four Western equivalents do instead.
date: 2026-10-09
lang: en
topic: ai-and-engineering
tags: [rails-and-infrastructure]
---

The usual version of this question is about super apps, and it has been answered at length by people with better data than mine; mine is narrower. A mini program is a small bundle of code that runs inside somebody else's application, and the question is which parts of that arrangement exist in what Apple and Google ship.

I read the vendors' own documentation for WeChat Mini Programs, Apple App Clips, Google Play Instant and Progressive Web Apps, and compared them on five dimensions: install and size, identity, payment, entry point, distribution and review.

One mechanism carries most of the answer. A mini program brings neither its own user account nor its own checkout. It borrows both from the application hosting it.

## The five dimensions, side by side

| | WeChat Mini Program | Progressive web app | Native app (iOS/Android) | App Clip (iOS) |
| --- | --- | --- | --- | --- |
| Install and size | Runs inside WeChat. Main package 2 MB maximum, all packages together 30 MB (20 MB for programs developed by a third-party provider) ([WeChat subpackages](https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html), read 2026-10-09) | No package at all. Chrome offers install after HTTPS plus a manifest carrying a name, 192 px and 512 px icons, `start_url` and a display mode ([web.dev install criteria](https://web.dev/articles/install-criteria), read 2026-10-09) | Full binary from the store. Apple states the App Store limits the size of apps installable over a mobile connection and gives no number on that page ([Apple](https://developer.apple.com/documentation/xcode/reducing-your-app-s-size), read 2026-10-09); Google states a compressed download limit of 200 MB for apps published as app bundles ([Google](https://developer.android.com/topic/performance/reduce-apk-size), read 2026-10-09) | 10 MB uncompressed on iOS 15 and earlier, 15 MB on iOS 16 and earlier, 100 MB on iOS 17 or later under conditions ([Apple](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip), read 2026-10-09) |
| Identity | `openid` per mini program, `unionid` shared across every app under one Open Platform account. Both come from `wx.login` plus `code2Session`, which WeChat documents as returning the UnionID "without user authorization" ([login](https://developers.weixin.qq.com/miniprogram/en/dev/framework/open-ability/login.html), [UnionID](https://developers.weixin.qq.com/miniprogram/en/dev/framework/open-ability/union-id.html), read 2026-10-09) | Each origin keeps its own account. The browser hands nothing to a site silently | Account per app. Sign in with Apple where the app offers it, as an explicit step by the user ([Apple](https://developer.apple.com/sign-in-with-apple), read 2026-10-09) | Sign in with Apple, the keychain and CloudKit, shared with the parent app ([Apple](https://developer.apple.com/documentation/appclip/sharing-data-between-your-app-clip-and-your-full-app), read 2026-10-09) |
| Payment | WeChat Pay. A merchant number is bound to the mini program's AppID, at most 50 AppIDs per merchant number ([WeChat Pay](https://pay.weixin.qq.com/doc/v3/merchant/4013287504), page updated 2025-07-02). Virtual goods must go through the mini program virtual-payment channel, where "the platform charges a technical service fee" ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/en/business-capabilities/virtual-payment.html), read 2026-10-09) | Card and wallet APIs called by the merchant, on the merchant's own acquiring contract | In-app purchase is required to unlock features. Apple's guidelines name QR codes among the mechanisms that may not be used instead ([Apple](https://developer.apple.com/app-store/review/guidelines/), read 2026-10-09) | Apple's in-app purchase. Hosts in the Mini Apps Partner Program "earn 85% of qualifying In-App Purchase sales within qualifying mini apps" ([Apple](https://developer.apple.com/programs/mini-apps-partner/), read 2026-10-09) |
| Entry | Documented entry paths carry IDs: 1011 scan a QR code, 1012 long-press an image, 1013 pick a code from the album, 1023 the Android home-screen icon, 1005 and 1006 search boxes, 1026 the nearby list, 1183 search inside the PC WeChat mini program panel ([WeChat scene values](https://developers.weixin.qq.com/miniprogram/dev/reference/scene-list.html), read 2026-10-09) | A URL, a search result, or a home-screen shortcut the user adds by hand. On iOS there is no install prompt at all ([web.dev](https://web.dev/learn/pwa/installation/), read 2026-10-09) | Store search and the home-screen icon | An App Clip Code, NFC tag or QR code at a physical location; Siri suggestions; Maps; Messages; a Smart App Banner on a website in Safari ([Apple](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip), read 2026-10-09) |
| Distribution and review | Published from the mini program console. Virtual payment requires a certified entity: an enterprise, institution or individual merchant ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/en/business-capabilities/virtual-payment.html), read 2026-10-09) | Nothing is submitted. It is HTTPS plus a manifest | Store review against the App Review Guidelines | No listing of its own. It ships inside a full app, which the App Clip documentation says "must include the same functionality as the App Clip" ([Apple](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip), read 2026-10-09); Guideline 2.5.16(a) adds that all App Clip features must be in the main app binary and that "App Clips cannot contain advertising" ([Apple](https://developer.apple.com/app-store/review/guidelines/), read 2026-10-09) |

The Android equivalent is gone. "Starting December 2025, Instant Apps cannot be published through Google Play, and all Google Play services Instant APIs will no longer work" ([Google Play Instant](https://developer.android.com/topic/google-play-instant), last updated 2026-06-24).

## Identity arrives before the first screen

The WeChat login flow is one call on the client and one on the server. `wx.login` returns a code, the server exchanges it through `code2Session`, and the reply carries an `openid` for that user in that mini program, a `unionid` and a session key ([WeChat](https://developers.weixin.qq.com/miniprogram/en/dev/framework/open-ability/login.html), read 2026-10-09).

The UnionID page says what this costs the user: the developer gets it "without user authorization" ([WeChat](https://developers.weixin.qq.com/miniprogram/en/dev/framework/open-ability/union-id.html), read 2026-10-09). No phone number, no password, no consent sheet. The `openid` is scoped to one mini program; the `unionid` is identical across every mobile app, website app, official account and mini program bound to the same Open Platform account, so a merchant with several surfaces sees one person.

Compare the alternatives. On the web, an origin cannot read an identifier out of the browser; it asks the user to sign in and then owns a credential to protect. On iOS, an App Clip can use Sign in with Apple and the keychain, which Apple's documentation points developers at sharing with the full app, but those are technologies an app opts into rather than an identifier handed over at launch.

That is why the first screen of a mini program is the product. Onboarding was paid for at install time, by the host.

## Payment is a binding between two accounts

Paying inside a mini program does not mean the mini program holds money. WeChat Pay binds a merchant number to the mini program's AppID. One merchant number can bind at most 50 AppIDs, the binding starts on the merchant side and is confirmed from the mini program side, and once established cannot be unbound ([WeChat Pay](https://pay.weixin.qq.com/doc/v3/merchant/4013287504), page updated 2025-07-02). The rail and the code package are joined by an account relationship neither side can create alone.

Virtual goods get a second layer. The documentation is blunt: virtual currency, unlocked features, subscription content, paid services, tips and virtual gifts "require integration with Mini Program's virtual payment system for both purchase and payment", and the platform charges a technical service fee on the amount ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/en/business-capabilities/virtual-payment.html), read 2026-10-09). Physical goods go through ordinary WeChat Pay; digital ones go through the host's channel, with the host's cut.

Apple's version of that cut is recent and documented. The Mini Apps Partner Program was announced on 13 November 2025 ([Apple](https://developer.apple.com/news/?id=xcz1s7cz), 2025-11-13): host apps carrying mini apps can join, earn 85 percent of qualifying in-app purchase sales inside those mini apps, and must use Apple's in-app purchase system for them ([Apple](https://developer.apple.com/programs/mini-apps-partner/), read 2026-10-09). Admission is not automatic: a host needs the Advanced Commerce API and a manifest describing itself and its mini apps.

Apple's App Review Guidelines still require in-app purchase to unlock features or functionality, and the same sentence lists QR codes among the mechanisms that cannot substitute for it ([Apple](https://developer.apple.com/app-store/review/guidelines/), read 2026-10-09). What changed, on 1 May 2025, is that Guidelines 3.1.1, 3.1.1(a), 3.1.3 and 3.1.3(a) were updated for the United States storefront after a court decision about buttons and external links ([Apple](https://developer.apple.com/news/?id=9txfddzf), 2025-05-01).

## The QR code is the offline switch

A WeChat developer does not have to choose between a printed code and a link shared in a chat. The official scene-value table lists both, with IDs: 1011 scanning a QR code, 1012 long-pressing an image, 1013 picking one from the album, 1023 the Android home-screen icon, 1005 and 1006 the two search boxes, 1026 the nearby list, 1183 search inside the PC WeChat mini program panel ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/reference/scene-list.html), read 2026-10-09).

Two details make the printed code cheap. Codes come from an API, and WeChat states every generated mini program code is permanently valid. The "one item, one code" interface has no quantity limit and needs a smaller printed area than an ordinary URL code ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/qr-code.html), read 2026-10-09). A code already printed and pointing at a URL can be configured to open a chosen page inside a mini program ([WeChat](https://developers.weixin.qq.com/miniprogram/introduction/qrcode.html), read 2026-10-09). The person scans what is already on the table.

App Clips have the same physical invocations: an App Clip Code, an NFC tag, a QR code at a physical location ([Apple](https://developer.apple.com/documentation/appclip/configuring-the-launch-experience-of-your-app-clip), read 2026-10-09). Two constraints pull the other way.

The first constraint trades size against physical entry. The 100 MB ceiling for iOS 17 or later carries four conditions: the App Clip "only supports digital invocations" and not "physical invocations such as App Clip Codes, QR codes, or NFC tags" ([Apple](https://developer.apple.com/documentation/appclip/choosing-the-right-functionality-for-your-app-clip), read 2026-10-09), it is used where a reliable connection is likely, and it "doesn't support iOS 16 and earlier". The exception Apple names is a demo link from App Store Connect, which may use the 100 MB limit and still support App Clip Codes, NFC tags and QR codes. An App Clip with a counter code stays inside the smaller limit.

The second concerns persistence. Apple's Human Interface Guidelines say App Clips "remain on the device for a limited amount of time", and that only App Clip Codes produced in App Store Connect or with Apple's own code generator are approved for use ([Apple](https://developer.apple.com/design/human-interface-guidelines/app-clips), read 2026-10-09). A merchant cannot print its own.

## Who reviews it, and who is answerable

Reviews differ in kind as well as in strictness. A PWA is submitted to nobody; Chrome installs it once its manifest and HTTPS satisfy the criteria ([web.dev](https://web.dev/articles/install-criteria), read 2026-10-09). An App Clip cannot be submitted alone. It ships inside a full app that must already contain the same functionality, cannot carry advertising, and is reviewed as part of that app ([Apple](https://developer.apple.com/app-store/review/guidelines/), read 2026-10-09). A mini program is submitted inside WeChat, and the entity requirement arrives with payment rather than with the code: to sell virtual items, the program must be a certified enterprise, institution or individual merchant ([WeChat](https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/en/business-capabilities/virtual-payment.html), read 2026-10-09).

The commercial consequence: in the App Store, a mini-app-like product reaches users through a host that already has an account relationship and a reviewed app behind it. In WeChat, the party needing the corporate identity, the certification and the merchant binding is the mini program author.

## Where the four pieces sit

In WeChat, four things a mini program depends on sit with one owner: the identity system, the payment rail, the entry surface (camera, search, chat, home screen, desktop) and the distribution channel with its review. An author plugs into a host that has all four and pays for the parts it uses.

In the Apple and Google stacks those four are held by parties with different interests. The operating system vendor issues the platform account and runs the payment system; the browser owns the entry surface for web content; the stores own distribution and review; the rail for physical goods sits with the merchant's bank relationship.

No single party there can hand all four to a third party. Apple's answer in November 2025 was to supply the missing pieces itself and keep the commission: hosts get Apple's in-app purchase for mini apps and keep 85 percent of qualifying sales, in exchange for approval, a manifest and Apple's review.

The mechanism that makes mini programs work is therefore an ownership arrangement rather than a technology gap. Reproducing it outside WeChat means finding one party that holds the users, the identity, the payment rail and the entry surface, and getting it to open all four to third-party code at a price the third party will pay. In the West, the two parties that hold those pieces chose to be the host themselves.

## How I checked this

- Every figure and quote comes from documentation published by the vendor it describes: WeChat's mini program and WeChat Pay docs, Apple's developer documentation, guidelines and news items, Google's Android documentation, and web.dev.
- All pages were fetched on 2026-10-09. Most carry no publication date, so a date beside a source is my reading date unless the page states its own: the WeChat Pay AppID binding page (updated 2025-07-02), the Google Play Instant page (last updated 2026-06-24), Apple's updated-guidelines news item (2025-05-01), Apple's Mini Apps Partner Program news item (2025-11-13) and Tencent's write-up of the 2022 WeChat Open Class (2022-01-07).
- Size limits and scene-value IDs come from the pages that state them: WeChat's subpackage page for 2 MB and 30 MB, Apple's App Clip page for the 10/15/100 MB table, WeChat's scene-value table for the ID numbers.
- Google Play Instant's page would not load in a plain HTTP client, so I read it through the Internet Archive and then through a rendering fetch that returned the live page.

## What I could not check

- **The fee WeChat charges on virtual payments.** The page says a fee is charged on the payment amount and gives no percentage.
- **The standard WeChat Pay rate for physical goods.** I found no official rate page; what I reached describes partner fee schemes and refers to a merchant rate without the base number.
- **The extra steps for virtual payment on iOS.** WeChat's virtual payment page says iOS "requires additional activation and adaptation procedures" and points at separate documentation; I could not load that page, so I do not know whether an Apple-side charge is involved.
- **Whether an App Clip can take payment for physical goods through Apple Pay.** Not stated on the App Clip pages I read.
- **Any current count of mini programs or mini-program daily users.** Tencent's release discloses Weixin monthly accounts and names Mini Games and Mini Shops, but carries no mini-program count. The most recent first-party figure I found: more than 450 million daily users at the end of 2021, from Tencent's write-up of the 2022 WeChat Open Class ([Tencent](https://www.tencent.com/zh-cn/articles/2201267.html), 2022-01-07). That figure is four years old.
- **What "certified Mini Program" requires in practice**, beyond the entity types named on the virtual payment page, and how long WeChat's review takes.
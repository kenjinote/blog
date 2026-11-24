---
title: "Hugo PaperMod में Twitter Card (X Card) कैसे सेट करें"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "PaperMod के दस्तावेज़ित विकल्पों से X कार्ड छवि सेट करें और बने हुए HTML तथा X पोस्ट कंपोज़र में पूर्वावलोकन जाँचें।"
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod Open Graph और Twitter Card मेटाडेटा बना सकता है। आउटपुट थीम संस्करण और कस्टम लेआउट के अनुसार बदल सकता है, इसलिए किसी उदाहरण पर निर्भर रहने के बजाय प्रकाशित HTML जाँचें।

## पूरी साइट की सेटिंग

PaperMod का SEO मेटाडेटा production बिल्ड में सक्रिय होता है। साइट का वातावरण production सेट करें।

```toml
[params]
  env = "production"
```

पूरी साइट के डिफ़ॉल्ट चित्र के लिए फ़ाइल `static` में रखें और यहाँ उसका पथ दें। जब किसी पोस्ट में अलग चित्र न हो, तब यह विकल्प हो सकता है। प्रकाशित साइट पर बनी URL भी जाँचें।

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## प्रति पोस्ट छवि

किसी पोस्ट का अपना चित्र देने के लिए Page Bundle की छवि को `cover.image` में रखें। `relative: true` Bundle के भीतर का सापेक्ष पथ बताता है। PaperMod के अनुसार कवर छवि पहले उपयोग होती है; उसके अभाव में पोस्ट की `images` सूची और फिर उपयुक्त Bundle चित्र देखे जा सकते हैं।

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## लेख में कवर छिपाएँ

PaperMod की variables reference के अनुसार `cover.hidden: true` लेख में कवर दिखाना बंद करता है, पर उसे structured metadata में रखता है। सोशल कार्ड के लिए ही छवि चाहिए तो यह उपयोगी है। थीम fork या अपने template होने पर HTML अवश्य जाँचें।

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## कार्ड प्रकार और छवि आकार

पुराने दावे कि PaperMod केवल `summary_large_image` देता है और 800×418 तय आकार है, हर संस्करण पर लागू नहीं होते। कार्ड प्रकार थीम या साइट template पर निर्भर हो सकता है। चौड़ी साझा छवि के लिए 1200×630 (लगभग 1.90:1) व्यावहारिक सुझाव है, X की गारंटीशुदा आवश्यकता नहीं।

## HTML और preview जाँचें

production बिल्ड करें और लेख के HTML में `twitter:card`, `twitter:image`, `og:image`, शीर्षक और विवरण देखें। चित्र HTTPS पर बिना लॉगिन सीधे सार्वजनिक रूप से उपलब्ध होना चाहिए। X ने 2022 में Card Validator का preview हटाकर पोस्ट कंपोज़र में जाँचने की सलाह दी। लिंक कंपोज़र में डालकर पोस्ट किए बिना preview देखें। कैश अपडेट होने में समय लग सकता है।

24 नवंबर 2026 को लिंक किए गए PaperMod स्रोतों और X डेवलपर फ़ोरम से जाँचा गया। Fork, template बदलाव और X में परिवर्तन से आउटपुट बदल सकता है।

## संदर्भ

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)

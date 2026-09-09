---
title: 'Hugo में HTML टैग को कैसे सक्षम करें (config.toml सेटिंग्स)'
slug: "hugo-में-html-टैग-का-उपयोग-करना"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["ब्लॉग प्रबंधन"]
description: 'हम बताएंगे कि स्टेटिक साइट जनरेटर Hugo के मार्कडाउन लेखों के भीतर HTML टैग को सीधे कैसे लिखा और उपयोग किया जा सकता है। बस config.toml में markup.goldmark.renderer की असुरक्षित (unsafe) सेटिंग जोड़ें और यह हो गया。'
---

डिफ़ॉल्ट रूप से, HUGO लेखों में HTML टैग के उपयोग की अनुमति नहीं देता है, लेकिन आप config.toml में निम्नलिखित विवरण जोड़कर इसे सक्षम कर सकते हैं।

```toml
[markup.goldmark.renderer]
    unsafe = true
```

संदर्भ: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)

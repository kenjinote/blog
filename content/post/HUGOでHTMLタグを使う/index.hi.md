---
title: "HUGO में HTML टैग का उपयोग करना"
slug: "hugo-में-html-टैग-का-उपयोग-करना"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["ब्लॉग प्रबंधन"]
---

डिफ़ॉल्ट रूप से, HUGO लेखों में HTML टैग के उपयोग की अनुमति नहीं देता है, लेकिन आप config.toml में निम्नलिखित विवरण जोड़कर इसे सक्षम कर सकते हैं।

```toml
[markup.goldmark.renderer]
    unsafe = true
```

संदर्भ: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)

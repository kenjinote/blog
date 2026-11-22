---
title: "Hugo Markdown में Raw HTML चालू करें"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "YAML, TOML और JSON उदाहरणों के साथ Hugo Markdown में raw HTML चालू करना सीखें। इसमें सुरक्षा जोखिम और किन स्थितियों में यह विकल्प चालू नहीं करना चाहिए, यह भी बताया गया है।"
---

Hugo का Goldmark Markdown रेंडरर डिफ़ॉल्ट रूप से raw HTML को रेंडर नहीं करता। इसकी आवश्यकता हो तो साइट कॉन्फ़िगरेशन में `markup.goldmark.renderer.unsafe` को `true` करें। Hugo YAML, TOML और JSON कॉन्फ़िगरेशन फ़ाइलें स्वीकार करता है। उदाहरण के लिए, `hugo.yaml` में:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

`hugo.toml` में:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

या `hugo.json` में:

```json
{
  "markup": {
    "goldmark": {
      "renderer": {
        "unsafe": true
      }
    }
  }
}
```

डिफ़ॉल्ट मान `false` है। `unsafe: true` Markdown में raw HTML को आउटपुट में आने देता है और Hugo की content trust boundary को कमज़ोर करता है। यदि साइट अविश्वसनीय योगदानकर्ताओं या बाहरी स्रोतों से Markdown प्रोसेस करती है, तो इसे सक्षम न करें। इसका उपयोग केवल ऐसी सामग्री के लिए करें जिसे आप नियंत्रित और जाँच सकते हैं, और जिसके परिणाम आप समझते हों। जटिल लेआउट के लिए shortcode या HTML content फ़ाइल बेहतर विकल्प हो सकती है।

संदर्भ: [Markup कॉन्फ़िगर करें](https://gohugo.io/configuration/markup/) · [Hugo का सुरक्षा मॉडल](https://gohugo.io/about/security/)

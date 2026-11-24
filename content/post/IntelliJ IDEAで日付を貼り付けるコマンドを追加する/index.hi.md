---
title: 'IntelliJ IDEA में वर्तमान दिनांक सम्मिलित करने के लिए शॉर्टकट कैसे बनाएं'
slug: "IntelliJ IDEAでतिथिを貼り付けるकमांडを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'IntelliJ IDEA Live Template बनाएँ जो स्थानीय टाइम ज़ोन ऑफ़सेट सहित ISO 8601 टाइमस्टैम्प डालता है। यह गाइड सेटिंग पथ, दिनांक एक्सप्रेशन और विस्तार कुंजी के लिए JetBrains के वर्तमान दस्तावेज़ों का पालन करती है।'
---

# परिचय

यदि लिखते समय आपको बार-बार टाइमस्टैम्प डालना पड़ता है, तो IntelliJ IDEA Live Template छोटे संक्षिप्त रूप से इसे डाल सकता है। यह उदाहरण कंप्यूटर के स्थानीय समय और टाइम ज़ोन ऑफ़सेट सहित ISO 8601 टाइमस्टैम्प बनाता है।

## Live Template बनाएँ

1. **Settings > Editor > Live Templates** खोलें। Windows या Linux पर **File > Settings** से और macOS पर **IntelliJ IDEA > Settings** से खोलें।
2. कोई टेम्पलेट समूह चुनें (जैसे **other**) और **+ > Live Template** क्लिक करें।
3. **Abbreviation** में `date` और **Description** में छोटा विवरण लिखें।
4. **Template text** में `$date$` लिखें।
5. **Edit Variables** क्लिक करें। `date` वेरिएबल के **Expression** में `date("yyyy-MM-dd'T'HH:mm:ssXXX")` डालें। टेम्पलेट विस्तार के समय मान अपने-आप निकालने के लिए **Skip if defined** चालू करें।
6. **Define** क्लिक करें और वे संदर्भ चुनें जहाँ टेम्पलेट चाहिए (उपयुक्त होने पर **Everywhere** चुनें)। सेटिंग सहेजें।

## टेम्पलेट का उपयोग करें

एडिटर में `date` लिखें और डिफ़ॉल्ट विस्तार कुंजी **Tab** दबाएँ। IntelliJ IDEA मौजूदा सिस्टम तारीख और समय को `2026-11-24T09:30:00+09:00` जैसे प्रारूप में डालेगा। समय और ऑफ़सेट कंप्यूटर के मौजूदा टाइम ज़ोन के अनुसार होंगे। यदि आपने विस्तार कुंजी बदली है, तो Live Templates सेटिंग में जाँचें।

`XXX` पैटर्न ISO 8601 टाइम ज़ोन ऑफ़सेट देता है। एक्सप्रेशन `+09:00` को स्थायी रूप से नहीं जोड़ता, इसलिए यह प्रत्येक पाठक के स्थानीय टाइम ज़ोन का उपयोग करता है। जाँचें कि बना हुआ टाइमस्टैम्प आपके इच्छित प्रकाशन समय से मेल खाता है।

## संदर्भ

- [Live Template बनाएँ और संपादित करें](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template वेरिएबल और date फ़ंक्शन](https://www.jetbrains.com/help/idea/template-variables.html)
- [Live Template विस्तार कुंजी सेट करें](https://www.jetbrains.com/help/idea/settings-live-templates.html)

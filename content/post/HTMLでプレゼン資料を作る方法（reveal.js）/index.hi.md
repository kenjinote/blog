---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'reveal.js का उपयोग: HTML और Markdown के साथ प्रेजेंटेशन सामग्री बनाएं'
slug: "HTMLでप्रस्तुति資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "प्रेजेंटेशन"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'हम "reveal.js" के इंस्टॉलेशन और बुनियादी उपयोग की व्याख्या करेंगे, एक टूल जो आपको HTML और Markdown के साथ सहज रूप से प्रेजेंटेशन बनाने की अनुमति देता है। हम ऐसे उपयोग पेश करेंगे जो एनीमेशन और PDF आउटपुट का समर्थन करते हैं और Git जैसे संस्करण नियंत्रण (Version Control) के साथ संगत हैं。'
---

# HTML के साथ प्रेजेंटेशन कैसे बनाएं

reveal.js, HTML और Markdown का उपयोग करने वाला एक प्रेजेंटेशन निर्माण उपकरण है, जिसमें निम्नलिखित विशेषताएं हैं:

- गणितीय सूत्र, एनिमेशन और स्वाइप संचालन जैसी विभिन्न प्रेजेंटेशन विशेषताएं
- अनुकूलन योग्य थीम और लेआउट
- माउस, कीबोर्ड और टचपैड जैसे कई उपकरणों के लिए नेविगेशन समर्थन
- स्लाइड ऑटो-प्ले और एम्बेडेड वीडियो जैसी उन्नत विशेषताएं प्रदान करता है
- PDF प्रारूप में निर्यात किया जा सकता है

इन सुविधाओं के साथ, उपयोगकर्ता आसानी से इंटरैक्टिव और आकर्षक प्रेजेंटेशन बना सकते हैं।

# reveal.js की स्थापना और उपयोग

इसे उपयोग करने का सबसे आसान तरीका निम्नलिखित पृष्ठ से संपूर्ण ZIP डाउनलोड करना और उसे निकालना है।

1. [https://revealjs.com/installation](https://revealjs.com/installation) खोलें और लिंक से `master.zip` डाउनलोड करें
2. निकाले गए फ़ोल्डर में मौजूद index.html को ब्राउज़र में खोलें
3. अपनी खुद की प्रेजेंटेशन सामग्री बनाने के लिए index.html को फिर से लिखें

※ चूंकि डेमो HTML कोड demo.html में लिखा गया है, आप इसे संदर्भ के रूप में उपयोग कर सकते हैं।

# कैसे उपयोग करें

आपके द्वारा बनाए गए प्रेजेंटेशन को वेब पेजों के रूप में प्रकाशित किया जा सकता है या PDF के रूप में निर्यात किया जा सकता है।
इसके अलावा, चूंकि प्रेजेंटेशन का स्रोत पाठ है, इसलिए इसे संस्करण नियंत्रण प्रणाली के साथ प्रबंधित करना आसान है।

Markdown प्रारूप में प्रेजेंटेशन सामग्री बनाना भी संभव लगता है।

# मूल स्लाइड बनाएं

सबसे आसान तरीका नवीनतम Basic Setup ZIP डाउनलोड करना, उसे निकालना और `index.html` संपादित करना है। नीचे दिए HTML उदाहरण की तरह हर स्लाइड को `<section>` में रखें। Basic Setup की नमूना फ़ाइल में आवश्यक शैलियाँ और आरंभीकरण कोड पहले से शामिल हैं।

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Markdown में स्लाइड लिखें

साथ आने वाला Markdown प्लगइन HTML फ़ाइल में Markdown लिखने देता है। क्षैतिज स्लाइडों को `---` से अलग करें और नीचे का उदाहरण `index.html` में जोड़ें। बाहरी Markdown फ़ाइल लोड करने के लिए स्थानीय वेब सर्वर चाहिए।

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# विकास सेटअप

स्थानीय सर्वर या स्रोत-विकास टूल चाहिए तो आधिकारिक Full Setup चुनें। ये कमांड चलाएँ और फिर ब्राउज़र में `http://localhost:8000` खोलें।

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# PDF में निर्यात

URL के अंत में `?print-pdf` जोड़ें। Chrome या Chromium के प्रिंट संवाद में PDF के रूप में सहेजें, लैंडस्केप, बिना मार्जिन और बैकग्राउंड ग्राफ़िक्स सक्षम करें। आधिकारिक मार्गदर्शिका Chrome और Chromium की पुष्टि करती है।

# वक्ता नोट्स

अलग विंडो में वक्ता दृश्य खोलने के लिए `S` दबाएँ। स्लाइड के `<aside class="notes">` में नोट लिखें। स्थानीय वक्ता दृश्य के लिए वेब सर्वर आवश्यक है।

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# आधिकारिक दस्तावेज़

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。

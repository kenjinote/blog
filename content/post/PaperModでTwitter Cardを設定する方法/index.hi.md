---
title: "PaperMod में Twitter Card कैसे सेट करें"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["ブログ運営"]
---
# परिचय
PaperMod थीम Twitter Card का समर्थन करती है।
हालाँकि, Twitter Card सेटिंग्स को `config.toml` में या प्रत्येक लेख के `*.md` की हेडर जानकारी में लिखा जाना चाहिए।
यदि आप प्रत्येक लेख और `config.toml` दोनों में सेट करते हैं, तो प्रत्येक लेख की हेडर जानकारी को प्राथमिकता दी जाएगी।

# सेट कैसे करें
## config.toml
`config.toml` में, `[params]` के तहत `images` नामक एक आइटम जोड़ें।
`images` में, Twitter Card पर प्रदर्शित होने वाली छवि का पथ लिखें।
यदि आप छवि को `static` फ़ोल्डर में रखते हैं, तो केवल फ़ाइल नाम निर्दिष्ट करना ठीक है।

```
[params]
  images = ["twitter_card.jpg"]
```

फ़ोल्डर संरचना
```
root
│  config.toml (यहाँ लिखें)
├─content
│  └─posts
│      └─लेख फ़ोल्डर
│         │  index.md (यहाँ लिखें)
│         └─images
│             cover.png (यहाँ रखें)
└─static
    twitter_card.jpg (यहाँ रखें)
```

## प्रत्येक लेख की हेडर जानकारी
प्रत्येक लेख की हेडर जानकारी में, `cover` के तहत `image` नामक एक आइटम जोड़ें।
यदि आप `relative` को `true` पर सेट करते हैं, तो आप इसे लेख के `*.md` से सापेक्ष पथ के रूप में निर्दिष्ट कर सकते हैं।

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### यदि आप इसे लेख के शीर्ष पर प्रदर्शित नहीं करना चाहते हैं
यदि आप लेख के शीर्ष पर कवर छवि प्रदर्शित नहीं करना चाहते हैं, तो `cover` के तहत `hidden` नामक एक आइटम जोड़ें और इसे `true` पर सेट करें।
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# छवि आकार के बारे में

वर्तमान PaperMod विनिर्देश में, ऐसा लगता है कि Twitter Card आकार केवल `summary_large_image` का समर्थन करता है।
`summary_large_image` के लिए उपयुक्त आकार (रिज़ॉल्यूशन) के कई सिद्धांत हैं, लेकिन `800 x 418` (छवि अनुपात 1.91:1) के आसपास अच्छा लगता है।

[संदर्भ साइट 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[संदर्भ साइट 2](https://developers.facebook.com/docs/sharing/best-practices)


यदि संभव हो, तो हम पोस्ट करने से पहले छवि का आकार बदलने की सलाह देते हैं।

# सेटिंग्स की जांच कैसे करें
Twitter Card सेटिंग्स की जांच करने के लिए, [Twitter Card Validator](https://cards-dev.twitter.com/validator) का उपयोग करें।
हालाँकि, चूंकि मेरे वातावरण में पूर्वावलोकन ठीक से प्रदर्शित नहीं हुआ था, यदि पूर्वावलोकन प्रदर्शित नहीं होता है, तो मैं पोस्ट करने से पहले एक बार निजी खाते आदि का उपयोग करके इसकी जांच करने की सलाह देता हूं।

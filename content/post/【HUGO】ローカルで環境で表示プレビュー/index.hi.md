---
title: "【HUGO】स्थानीय वातावरण में पूर्वावलोकन प्रदर्शित करें"
slug: "【HUGO】स्थानीय वातावरण में पूर्वावलोकन प्रदर्शित करें"
date: 2022-09-05T12:28:01+09:00
tags: ["HUGO"]
draft: false
image: "img.png"
categories: ["ब्लॉग संचालन"]
---
# HUGO की स्थापना

## डाउनलोड
[HUGO डाउनलोड करें](https://github.com/gohugoio/hugo/releases)

उपरोक्त वेबसाइट से, अपने वातावरण के अनुकूल Windows मॉड्यूल डाउनलोड करें और उसे निकालें।
मेरे मामले में, मैंने "hugo_0.102.3_Windows-64bit.zip" डाउनलोड किया।

## निकालना
डाउनलोड की गई zip फ़ाइल को निकालें, और उसके अंदर स्थित hugo.exe को आपके द्वारा बनाए गए फ़ोल्डर में कॉपी करें, उदाहरण के लिए C:\bin।

## पर्यावरण चर में पंजीकृत करें
इसे पर्यावरण चर में पंजीकृत करें ताकि आप कहीं से भी hugo.exe को चला सकें।
निम्नलिखित क्रियाएँ Windows 11 के लिए हैं, लेकिन आपको समान चरणों के साथ पंजीकरण करने में सक्षम होना चाहिए:

1. संस्करण जानकारी खोलने के लिए Win+Pause बटन दबाएँ
2. उन्नत सिस्टम सेटिंग्स पर क्लिक करें
3. पर्यावरण चर पर क्लिक करें
4. Path चुनें और संपादित करें पर क्लिक करें
5. नया पर क्लिक करें, नई लाइन में "C:\bin" दर्ज करें और डायलॉग बंद करने के लिए ठीक पर क्लिक करें
 
# ब्लॉग का पूर्वावलोकन करें
कमांड प्रॉम्प्ट में, HUGO ब्लॉग फ़ोल्डर में जाएँ और नीचे दिए गए कमांड को चलाएँ।

`hugo server -D`

निष्पादन परिणाम नीचे दिया गया है। (-D ड्राफ्ट लेखों को प्रदर्शित करने का विकल्प है।)

```
C:\Users\win11\IdeaProjects\kenji.blog>hugo server -D
Start building sites …
hugo v0.102.3-b76146b129d7caa52417f8e914fc5b9271bf56fc windows/amd64 BuildDate=2022-09-01T10:16:19Z VendorInfo=gohugoio

                   | JA
-------------------+-----
  Pages            | 39
  Paginator pages  |  0
  Non-page files   |  7
  Static files     |  0
  Processed images |  0
  Aliases          | 13
  Sitemaps         |  1
  Cleaned          |  0

Built in 161 ms
Watching for changes in C:\Users\win11\IdeaProjects\kenji.blog\{archetypes,content,themes}
Watching for config changes in C:\Users\win11\IdeaProjects\kenji.blog\config.toml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

चूंकि निष्पादन के दौरान पता प्रदर्शित होता है (उपरोक्त उदाहरण में `http://localhost:1313/`), उस पते को अपने ब्राउज़र में कॉपी करें।
हर बार फ़ाइल सहेजने पर पूर्वावलोकन स्वचालित रूप से अपडेट हो जाता है।
पूर्वावलोकन समाप्त करने के लिए, कमांड प्रॉम्प्ट में Ctrl+C दर्ज करें।

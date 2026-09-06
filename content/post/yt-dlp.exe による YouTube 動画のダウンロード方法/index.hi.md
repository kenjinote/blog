---
title: "yt-dlp.exe से YouTube वीडियो कैसे डाउनलोड करें"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "डाउनलोड"]
draft: false
image: "img_1.png"
categories: ["IT/प्रौद्योगिकी"]
---
# yt-dlp क्या है

`yt-dlp` YouTube वीडियो डाउनलोड करने के लिए एक कमांड-लाइन टूल है।
वीडियो डाउनलोड करने के अलावा, आप इसे mp3 फ़ॉर्मेट में संगीत फ़ाइल के रूप में भी डाउनलोड कर सकते हैं।

## डाउनलोड और इंस्टॉलेशन

1. [yt-dlp रिलीज़ पेज](https://github.com/yt-dlp/yt-dlp/releases) से नवीनतम yt-dlp.exe डाउनलोड करें।
2. yt-dlp.exe को किसी भी फ़ोल्डर में रखें।
3. yt-dlp.exe के फ़ोल्डर पथ को पर्यावरण चर Path में जोड़ें।

## उपयोग कैसे करें

कमांड प्रॉम्प्ट में yt-dlp.exe चलाएँ और YouTube वीडियो का URL निर्दिष्ट करें।

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ आप तर्क (argument) के रूप में केवल VIDEO_ID का उपयोग भी कर सकते हैं।

इसे mp3 संगीत फ़ाइल के रूप में डाउनलोड करने के लिए, निम्न कमांड चलाएँ:

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

इसके साथ, वीडियो उस वर्तमान निर्देशिका में डाउनलोड हो जाएगा जहाँ कमांड निष्पादित किया गया था।

बस इतना ही।

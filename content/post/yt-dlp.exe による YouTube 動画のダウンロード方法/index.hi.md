---
title: 'yt-dlp का उपयोग कैसे करें: YouTube वीडियो और ऑडियो डाउनलोड और सेव करने का तरीका'
date: "2026-09-24T19:44:38+09:00"
slug: "yt-dlp.exe による YouTube वीडियोのडाउनलोड方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "डाउनलोड"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: 'कमांड लाइन टूल ''yt-dlp'' का उपयोग करके उच्च गुणवत्ता में YouTube वीडियो डाउनलोड और सेव करने का तरीका, और उन्हें mp3 ऑडियो फ़ाइल के रूप में निकालने और सेव करने की प्रक्रिया को आसानी से समझाया गया है। इंस्टॉलेशन से लेकर उपयोग तक पूरी जानकारी शामिल है।'
---
# yt-dlp क्या है

`yt-dlp` YouTube वीडियो डाउनलोड करने के लिए एक कमांड-लाइन टूल है।
वीडियो डाउनलोड करने के अलावा, आप इसे mp3 फ़ॉर्मेट में संगीत फ़ाइल के रूप में भी डाउनलोड कर सकते हैं।

## डाउनलोड और इंस्टॉलेशन

1. [yt-dlp रिलीज़ पेज](https://github.com/yt-dlp/yt-dlp/releases) से नवीनतम yt-dlp[.exe](/hi/p/%E0%A4%A8%E0%A4%BF%E0%A4%B7%E0%A5%8D%E0%A4%AA%E0%A4%BE%E0%A4%A6%E0%A4%A8-%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A5%8D%E0%A4%AF-%E0%A4%AB%E0%A4%BC%E0%A4%BE%E0%A4%87%E0%A4%B2exe%E3%81%AE%E4%B8%AD%E8%BA%AB%E3%82%92%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%87%E0%A4%B7%E0%A4%A3%E3%81%99%E3%82%8B%E0%A4%9F%E0%A5%82%E0%A4%B2/) डाउनलोड करें।
2. yt-dlp[.exe](/hi/p/%E0%A4%A8%E0%A4%BF%E0%A4%B7%E0%A5%8D%E0%A4%AA%E0%A4%BE%E0%A4%A6%E0%A4%A8-%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A5%8D%E0%A4%AF-%E0%A4%AB%E0%A4%BC%E0%A4%BE%E0%A4%87%E0%A4%B2exe%E3%81%AE%E4%B8%AD%E8%BA%AB%E3%82%92%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%87%E0%A4%B7%E0%A4%A3%E3%81%99%E3%82%8B%E0%A4%9F%E0%A5%82%E0%A4%B2/) को किसी भी फ़ोल्डर में रखें।
3. yt-dlp[.exe](/hi/p/%E0%A4%A8%E0%A4%BF%E0%A4%B7%E0%A5%8D%E0%A4%AA%E0%A4%BE%E0%A4%A6%E0%A4%A8-%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A5%8D%E0%A4%AF-%E0%A4%AB%E0%A4%BC%E0%A4%BE%E0%A4%87%E0%A4%B2exe%E3%81%AE%E4%B8%AD%E8%BA%AB%E3%82%92%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%87%E0%A4%B7%E0%A4%A3%E3%81%99%E3%82%8B%E0%A4%9F%E0%A5%82%E0%A4%B2/) के फ़ोल्डर पथ को पर्यावरण चर Path में जोड़ें।

## उपयोग कैसे करें

कमांड प्रॉम्प्ट में yt-dlp[.exe](/hi/p/%E0%A4%A8%E0%A4%BF%E0%A4%B7%E0%A5%8D%E0%A4%AA%E0%A4%BE%E0%A4%A6%E0%A4%A8-%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A5%8D%E0%A4%AF-%E0%A4%AB%E0%A4%BC%E0%A4%BE%E0%A4%87%E0%A4%B2exe%E3%81%AE%E4%B8%AD%E8%BA%AB%E3%82%92%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%8D%E0%A4%B2%E0%A5%87%E0%A4%B7%E0%A4%A3%E3%81%99%E3%82%8B%E0%A4%9F%E0%A5%82%E0%A4%B2/) चलाएँ और YouTube वीडियो का URL निर्दिष्ट करें।

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

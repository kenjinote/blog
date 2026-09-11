---
title: 'curl कमांड का उपयोग करके Gmail से ईमेल कैसे भेजें'
slug: "Gmailをcurlから送る"
date: 2025-02-27T02:13:31+09:00
tags: ["gmail", "curl"]
draft: false
image: "img.webp"
categories: ["AI और प्रौद्योगिकी"]
description: 'हम बताएंगे कि कमांड लाइन टूल "curl" का उपयोग करके Gmail खाते के माध्यम से ईमेल कैसे भेजें। Google के ऐप पासवर्ड प्राप्त करने की प्रक्रिया से लेकर curl के विकल्प निर्दिष्ट करने और ईमेल मुख्य फ़ाइल बनाने और भेजने के कमांड तक, हम सब कुछ विस्तार से पेश करेंगे。'
---

# curl के साथ Gmail भेजें

## 1. ऐप पासवर्ड प्राप्त करें
https://myaccount.google.com/apppasswords
उपरोक्त लिंक पर क्लिक करें और ऐप का नाम दर्ज करें।
जेनरेट किए गए पासवर्ड को सेव करें।

## 2. curl कमांड के साथ ईमेल भेजें
निम्नलिखित कमांड निष्पादित करें।

नीचे दिए गए उदाहरण में, ईमेल की सामग्री mail.txt में लिखी गई है।

```mail.txt
From: from@gmail.com
To: to@gmail.com
Subject: टेस्ट ईमेल
Content-Type: text/plain; charset="UTF-8"

यह एक टेस्ट ईमेल है।
```

उपरोक्त फ़ाइल बनाएं और निम्न कमांड चलाएं।

```bash
curl --url "smtps://smtp.gmail.com:465" --ssl-reqd --mail-from "from@gmail.com" --mail-rcpt "to@gmail.com" --user "from@gmail.com:xxxxxxxxxxxxxxxx" --upload-file mail.txt
```
※ कृपया xxxxxxxxxxxxxxxx को अपने ऐप पासवर्ड से बदलें।

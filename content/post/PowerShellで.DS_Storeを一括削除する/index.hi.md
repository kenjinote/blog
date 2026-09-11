---
title: 'PowerShell से .DS_Store फ़ाइलों को एक साथ हटाने के लिए आसान कमांड'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["प्रोग्रामिंग"]
description: 'हम बताते हैं कि PowerShell का उपयोग करके Windows वातावरण में परेशान करने वाली Mac की .DS_Store फ़ाइलों को उप-फ़ोल्डरों सहित एक साथ कैसे हटाएं। आप केवल एक छोटे कमांड से अनावश्यक फ़ाइलों को आसानी से साफ़ कर सकते हैं।'
---

वर्तमान निर्देशिका को लक्ष्य फ़ोल्डर में ले जाएँ और सबफ़ोल्डर सहित .DS_Store फ़ाइलों को एक साथ हटाने के लिए निम्नलिखित कमांड चलाएँ।

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

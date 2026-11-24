---
title: "Windows कमांड प्रॉम्प्ट से बड़ा फ़ोल्डर हटाना: चरण और जोखिम"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["कमांड प्रॉम्प्ट"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "DEL और RMDIR से फ़ोल्डर हटाने की Microsoft-दस्तावेज़ित विधि, साथ में शांत पुनरावर्ती हटाने, पथ-जाँच और बैकअप की चेतावनी।"
---
ये कमांड लक्ष्य के अंदर की फ़ाइलों और उप-फ़ोल्डरों को पुनरावर्ती रूप से हटाते हैं। `/Q` पुष्टि नहीं दिखाता। गलत लक्ष्य चुनने से डेटा हमेशा के लिए खो सकता है, इसलिए ज़रूरी डेटा का बैकअप लें और हटाने से पहले पैरेंट पथ तथा फ़ोल्डर नाम जाँचें। गति फ़ाइलों की संख्या और स्टोरेज पर निर्भर करती है; तेज़ी की गारंटी नहीं है।

## चरण

इस उदाहरण में `C:\Parent` पैरेंट फ़ोल्डर है और `Large Folder` हटाया जाने वाला फ़ोल्डर है। पहले लक्ष्य की सूची देखें और पुष्टि करें, फिर हटाएँ।

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

`DEL /F /Q /S` लक्ष्य के भीतर की फ़ाइलें हटाता है (`/F` केवल-पढ़ने योग्य फ़ाइलें भी, `/Q` बिना पुष्टि, और `/S` उप-फ़ोल्डरों सहित)। इसके बाद `RMDIR /S /Q` बिना पुष्टि पूरी डायरेक्टरी ट्री हटाता है। `C:\Parent` और `Large Folder` को वास्तविक मानों से बदलें और हटाने की कमांड चलाने से पहले `dir` का परिणाम जाँचें।

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)

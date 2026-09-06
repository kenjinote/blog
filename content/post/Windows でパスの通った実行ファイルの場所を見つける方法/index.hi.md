---
title: "Windows में PATH में मौजूद एक्ज़ीक्यूटेबल फ़ाइल का स्थान कैसे खोजें"
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "पाथ", "एक्ज़ीक्यूटेबल फ़ाइल", "कमांड प्रॉम्प्ट"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# Windows में PATH में मौजूद एक्ज़ीक्यूटेबल फ़ाइल का स्थान कैसे खोजें

जब आप किसी एक्ज़ीक्यूटेबल फ़ाइल को निर्दिष्ट करके कमांड चलाते हैं, तो कभी-कभी आप जानना चाहते हैं कि वह एक्ज़ीक्यूटेबल फ़ाइल कहाँ स्थित है। ऐसे मामलों में, आप निम्न कमांड से एक्ज़ीक्यूटेबल फ़ाइल का स्थान जान सकते हैं।

```powershell
where <एक्ज़ीक्यूटेबल_फ़ाइल_का_नाम>
```

उदाहरण के लिए, यदि आप पेंट (mspaint.exe) का स्थान जानना चाहते हैं, तो आप निम्न कार्य कर सकते हैं:

```powershell
where mspaint.exe
```

# संदर्भ

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)

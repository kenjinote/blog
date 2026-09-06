---
title: "'hide' कमांड के साथ हिदेमारू एडिटर (Hidemaru Editor) कैसे शुरू करें"
slug: "hide-command-ke-saath-hidemaru-editor-kaise-shuru-karein"
date: 2024-03-29T23:45:37+09:00
tags: ["कमांड", "हिदेमारू एडिटर", "रजिस्ट्री"]
draft: false
image: "img_2.png"
categories: ["उपकरण और विकास पर्यावरण"]
---

## यहाँ 'hide' कमांड के साथ हिदेमारू एडिटर (Hidemaru Editor) को शुरू करने का तरीका बताया गया है।

नोट: इस तरीके का परीक्षण `Windows 10/11` पर किया गया है।

1. रजिस्ट्री एडिटर (Registry Editor) खोलें।
2. `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` पर जाएँ।
3. `App Paths` के अंतर्गत `hide.exe` नामक एक कुंजी (key) बनाएँ। **इस कुंजी के नाम में `.exe` से पहले का भाग कमांड का नाम बन जाता है।**
4. `hide.exe` कुंजी के `(Default)` मान को हिदेमारू एडिटर की निष्पादन योग्य फ़ाइल (executable file) के पथ (path) पर सेट करें। मेरे वातावरण में, यह `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"` था।
5. `hide.exe` कुंजी में `Path` नामक एक स्ट्रिंग (String) मान बनाएँ।
6. `Path` के डेटा को उस फ़ोल्डर के पथ पर सेट करें जिसमें हिदेमारू एडिटर की निष्पादन योग्य फ़ाइल है। मेरे वातावरण में, यह `"C:\Program Files (x86)\Hidemaru"` था।
7. अब, **Run** डायलॉग बॉक्स में (जिसे `Win` + `R` दबाकर खोला जाता है), आप `hide` कमांड टाइप करके हिदेमारू एडिटर को शुरू कर सकते हैं। इसके अलावा, कमांड प्रॉम्प्ट (Command Prompt) में, आप इसे `start hide` कमांड के साथ शुरू कर सकते हैं।

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
यदि आप उपरोक्त सामग्री को `.reg` फ़ाइल के रूप में सहेजते हैं और इसे चलाते हैं, तो सेटिंग्स रजिस्ट्री में जोड़ दी जाएंगी।

![img_1.png](img_1.png)

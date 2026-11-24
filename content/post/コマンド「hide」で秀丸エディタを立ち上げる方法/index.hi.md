---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: '''hide'' कमांड से Hidemaru Editor को तुरंत शुरू करें! Windows में सुविधाजनक सेटिंग का तरीका'
slug: "कमांड「hide」でहिडेमारू एडिटरを立ち上げる方法"
tags: ["कमांड", "हिदेमारू एडिटर", "रजिस्ट्री"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "Windows 10/11 में App Paths नाम पंजीकृत करके Run संवाद या start hide से Hidemaru Editor शुरू करें।"
---

## यहाँ 'hide' कमांड के साथ हिदेमारू एडिटर (Hidemaru Editor) को शुरू करने का तरीका बताया गया है।

नोट: इस तरीके का परीक्षण `Windows 10/11` पर किया गया है।

1. रजिस्ट्री एडिटर (Registry Editor) खोलें।
2. `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths` पर जाएँ।
3. `App Paths` के अंतर्गत `hide.exe` नामक एक कुंजी (key) बनाएँ। **इस कुंजी के नाम में `.exe` से पहले का भाग कमांड का नाम बन जाता है।**
4. `hide.exe` कुंजी के `(Default)` मान को हिदेमारू एडिटर की निष्पादन योग्य फ़ाइल (executable file) के पथ (path) पर सेट करें। मेरे वातावरण में, यह `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"` था।
5. Path मान वैकल्पिक है। अतिरिक्त DLL खोज निर्देशिकाएँ आवश्यक हों तभी सेट करें; ShellExecuteEx उन्हें प्रक्रिया के PATH में जोड़ता है।
6. Run (Win + R) में hide लिखें। Command Prompt में start hide उपयोग करें; केवल hide लिखना यहाँ बताई गई विधि नहीं है।

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
यदि आप उपरोक्त सामग्री को `.reg` फ़ाइल के रूप में सहेजते हैं और इसे चलाते हैं, तो सेटिंग्स रजिस्ट्री में जोड़ दी जाएंगी।

यह .reg उदाहरण केवल वर्तमान उपयोगकर्ता के लिए है। पथ को वास्तविक Hidemaru निष्पादन फ़ाइल पथ से बदलें। सभी उपयोगकर्ताओं के लिए HKEY_CURRENT_USER को HKEY_LOCAL_MACHINE करें और व्यवस्थापक अधिकारों से आयात करें।


## संदर्भ

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)

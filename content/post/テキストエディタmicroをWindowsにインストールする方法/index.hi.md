---
title: 'Windows पर उपलब्ध! हल्के टेक्स्ट एडिटर ''micro'' की इंस्टॉलेशन प्रक्रिया'
slug: "टेक्स्ट एडिटरmicroをWindowsにइंस्टॉलする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "टेक्स्ट एडिटर"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'कमांड प्रॉम्प्ट में सुचारू रूप से काम करने वाले टर्मिनल-आधारित टेक्स्ट एडिटर ''micro'' को Windows में इंस्टॉल करने और पर्यावरण चर सेट करके इसका उपयोग करने की प्रक्रिया को आसानी से समझाया गया है।'
---

## micro डाउनलोड करें
https://github.com/micro-editor/micro/releases/latest
नवीनतम रिलीज़ के Assets में से Windows x64 आर्काइव (उदाहरण: `micro-<version>-win64.zip`) डाउनलोड करें और उसे अपनी पसंद के फ़ोल्डर में निकालें।

Windows ARM पर संबंधित ARM64 आर्काइव चुनें।

## पर्यावरण चर (Environment Variables) सेट करें
कमांड प्रॉम्प्ट से `micro.exe` का उपयोग करने के लिए, आपको पर्यावरण चर सेट करने की आवश्यकता है।

1. `Win` + `R` दबाएँ, `sysdm.cpl` लिखें और `Enter` दबाएँ।
2. Advanced टैब खोलें और Environment Variables पर क्लिक करें।
3. अपने खाते के User variables में `Path` चुनें और Edit पर क्लिक करें। सूची में न हो तो `Path` बनाएँ।
4. New पर क्लिक करके `micro.exe` वाले फ़ोल्डर का पथ जोड़ें।
5. डायलॉग बंद करने के लिए OK पर क्लिक करें।
6. Command Prompt फिर से खोलें और `micro` चलाकर देखें कि यह शुरू होता है।

## micro का उपयोग कैसे करें

जब आप कमांड प्रॉम्प्ट में `micro` टाइप करते हैं और इसे निष्पादित करते हैं, तो निम्नलिखित स्क्रीन दिखाई देगी।
![img_3.png](img_3.webp)

मुख्य संचालन और शॉर्टकट कुंजियाँ इस प्रकार हैं:

| शॉर्टकट कुंजी | संचालन | 
|--------|-----| 
| Ctrl+Q | मौजूदा फ़ाइल बंद करें (अंतिम फ़ाइल होने पर micro बंद हो जाता है) |
| Ctrl+S | फ़ाइल सहेजें | 
| Ctrl+O | फ़ाइल खोलें | 
| Ctrl+A | सभी का चयन करें | 
| Ctrl+X | चयन को काटें (Cut) | 
| Ctrl+C | चयन की प्रतिलिपि बनाएँ (Copy) | 
| Ctrl+V | चिपकाएँ (Paste) | 
| Ctrl+Z | पूर्ववत करें (Undo) | 
| Ctrl+Y | फिर से करें (Redo) | 
| Ctrl+E | एडिटर कमांड निष्पादित करें | 

## संदर्भ
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)

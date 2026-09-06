---
title: "Windows 11 में क्लासिक राइट-क्लिक मेनू को कैसे पुनर्स्थापित करें"
slug: "how-to-restore-classic-context-menu-windows-11"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "फ़ाइल एक्सप्लोरर"]
draft: false
image: "img.png"
categories: ["PC और गैजेट्स"]
---

# Windows 11 में क्लासिक राइट-क्लिक मेनू को कैसे पुनर्स्थापित करें

यहाँ बताया गया है कि Windows 11 में क्लासिक राइट-क्लिक मेनू को कैसे पुनर्स्थापित किया जाए।

1. रजिस्ट्री संपादक खोलें।

`Win कुंजी` + `R कुंजी` दबाएँ, `regedit` टाइप करें और `Enter कुंजी` दबाएँ।
![img_1.png](img_1.png)　

2. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` पर जाएँ। यदि यह कुंजी मौजूद नहीं है, तो इसे बनाएँ।


4. `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32` पर जाएँ। यदि यह कुंजी मौजूद नहीं है, तो इसे बनाएँ।
5. पुष्टि करें कि `InprocServer32` में `(डिफ़ॉल्ट)` का कोई मान नहीं है।

![img_2.png](img_2.png)

6. कंप्यूटर को पुनरारंभ करें।
7. पुष्टि करें कि राइट-क्लिक मेनू क्लासिक संस्करण में वापस आ गया है।

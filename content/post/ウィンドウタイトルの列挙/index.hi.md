---
title: "PowerShell से प्रक्रियाओं की मुख्य विंडो के शीर्षक दिखाएँ"
slug: "विंडोタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "जानें कि Get-Process और MainWindowTitle से हर प्रक्रिया की मुख्य विंडो का शीर्षक कैसे दिखाएँ, परिणाम की सीमा क्या है और शीर्षक में संवेदनशील जानकारी क्यों हो सकती है।"
---
PowerShell के `Get-Process` से मिले प्रक्रिया ऑब्जेक्ट में से केवल वे दिखाएँ जिनका `MainWindowTitle` (मुख्य विंडो का शीर्षक) खाली नहीं है:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

यह हर प्रक्रिया की **मुख्य विंडो का शीर्षक** दिखाता है। यह किसी प्रक्रिया की सभी विंडो या डेस्कटॉप की हर विंडो की सूची नहीं बनाता। जिन प्रक्रियाओं की मुख्य विंडो नहीं है या जिनका शीर्षक खाली है, वे परिणाम में नहीं आतीं। प्रक्रियाएँ शुरू या बंद होने पर परिणाम बदल सकता है।

विंडो शीर्षक में खुले दस्तावेज़ों के नाम या अन्य निजी जानकारी हो सकती है। परिणाम को लॉग में सहेजने या साझा करने से पहले उसकी जाँच करें।

Microsoft दस्तावेज़ देखें: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) और [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle)।

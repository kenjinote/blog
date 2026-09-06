---
title: "PowerShell के साथ .DS_Store को एक साथ हटाएं"
slug: "PowerShell के साथ .DS_Store को एक साथ हटाएं"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["प्रोग्रामिंग"]
---

वर्तमान निर्देशिका को लक्ष्य फ़ोल्डर में ले जाएँ और सबफ़ोल्डर सहित .DS_Store फ़ाइलों को एक साथ हटाने के लिए निम्नलिखित कमांड चलाएँ।

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

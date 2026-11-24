---
title: "WinGet से PowerToys इंस्टॉल और अनइंस्टॉल करें"
slug: "PowerToysのइंस्टॉल"
tags: ["cmd", "कमांड प्रॉम्प्ट", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Microsoft के पैकेज ID से WinGet द्वारा PowerToys इंस्टॉल या अनइंस्टॉल करें और मौजूदा सिस्टम आवश्यकताएँ देखें।"
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys, Windows को अनुकूलित करने के लिए Microsoft की यूटिलिटीज़ का संग्रह है। Microsoft GitHub या Microsoft Store से इंस्टॉल करने की सलाह देता है; इस मार्गदर्शिका में WinGet तरीका दिया गया है।

## सिस्टम आवश्यकताएँ

PowerToys की मौजूदा आवश्यकताएँ Windows 11 या Windows 10 संस्करण 2004 (20H1, बिल्ड 19041) या नया, और 64-bit x64 या ARM64 प्रोसेसर हैं। सेटअप के दौरान Microsoft Edge WebView2 Runtime का नवीनतम स्थिर संस्करण इंस्टॉल होता है। आवश्यकताएँ और उपलब्धता बदल सकती हैं, इसलिए इंस्टॉल करने से पहले आधिकारिक दस्तावेज़ देखें।

## WinGet से इंस्टॉल करें

पहले Command Prompt या PowerShell में `winget --version` चलाकर पुष्टि करें कि WinGet उपलब्ध है। यह कमांड winget source से Microsoft.PowerToys पैकेज ID चुनता है। आगे बढ़ने से पहले किसी भी सूचना या सहमति अनुरोध को पढ़ें।

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## अनइंस्टॉल करें

अनइंस्टॉल कमांड में भी ID और winget source दिया गया है। आगे बढ़ने से पहले पुष्टि करें कि चुना गया पैकेज PowerToys है और दिखाई देने वाले पुष्टि संदेश को पढ़ें।

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Microsoft के आधिकारिक संदर्भ

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)

---
title: 'Windows 11 के WinGet कमांड से ऐप्स को आसानी से इंस्टॉल और प्रबंधित करने का तरीका'
slug: "WinGet を使ってकमांडでऐपをइंस्टॉलする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Windows 11 के पैकेज मैनेजर ''WinGet'' का उपयोग करके कमांड लाइन से ऐप्स इंस्टॉल करने का तरीका समझाया गया है। Chrome, VSCode, Slack जैसे प्रमुख सॉफ़्टवेयर को कमांड लाइन से जल्दी से इंस्टॉल और प्रबंधित करने की प्रक्रिया प्रस्तुत की गई है।'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# WinGet से ऐप इंस्टॉल करें

WinGet (Windows Package Manager) Windows कमांड लाइन से ऐप खोजने, इंस्टॉल, अपडेट और हटाने देता है। Microsoft के अनुसार यह Windows 11, Windows 10 संस्करण 1809 या बाद के संस्करण, और Windows Server 2025 पर समर्थित है; डेस्कटॉप पर यह सामान्यतः App Installer में शामिल होता है।

## जाँचें और उपयोग करें

`winget --version` चलाएँ। कमांड न मिले तो Windows अपडेट लगाएँ और Microsoft Store से App Installer इंस्टॉल या अपडेट करें। नए खाते में पहली बार साइन इन के बाद Store पंजीकरण पूरा होने दें।

नाम से खोजें, ID और प्रकाशक जाँचें, फिर इंस्टॉल करें:

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` सटीक ID मिलान और `--source winget` WinGet Community Repository चुनता है। स्रोत की शर्तें व ऐप लाइसेंस पढ़कर ही स्वीकारें। Microsoft `Microsoft.PowerToys`, `Microsoft.PowerShell`, `Git.Git`, `Docker.DockerDesktop` के उदाहरण भी देता है। ID/संस्करण बदल सकते हैं; पहले `winget show` से जाँचें और कई स्रोत हों तो `--source` दें।

## Paint.NET अब WinGet पर उपलब्ध है

वर्तमान कम्युनिटी सूची में ID `dotPDN.PaintDotNet` है:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

उपलब्धता बदल सकती है; वर्तमान मैनिफ़ेस्ट देखें।

## संदर्भ

- [Microsoft Learn: WinGet परिचय](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [install कमांड](https://learn.microsoft.com/en-us/windows/package-manager/winget/install) · [search कमांड](https://learn.microsoft.com/en-us/windows/package-manager/winget/search)
- [Paint.NET मैनिफ़ेस्ट](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)

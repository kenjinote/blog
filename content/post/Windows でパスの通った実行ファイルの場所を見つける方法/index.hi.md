---
title: "Windows में where.exe और PowerShell से executable ढूँढ़ें"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でपथの通ったनिष्पादन योग्य फ़ाइलの場所を見つける方法"
tags: ["Windows", "पाथ", "एक्ज़ीक्यूटेबल फ़ाइल", "कमांड प्रॉम्प्ट"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Command Prompt में where और PowerShell में where.exe तथा Get-Command से PATH पर executable ढूँढ़ें; alias और खोज-सीमा भी समझें।"
---
## Command Prompt

कमांड के रूप में चलने वाली executable का स्थान जानने के लिए Command Prompt में `where` चलाएँ। PowerShell में `where`, `Where-Object` का alias है; बाहरी प्रोग्राम चलाने के लिए स्पष्ट रूप से `where.exe` लिखें।

```cmd
where mspaint.exe
```

`where` मौजूदा फ़ोल्डर और `PATH` पर्यावरण चर में सूचीबद्ध फ़ोल्डरों को खोजकर मेल खाने वाले स्थान दिखाता है। एक से अधिक पथ मिल सकते हैं। यह कंप्यूटर के हर फ़ोल्डर को नहीं खोजता और उन स्थानों से बाहर के ऐप नहीं ढूँढ़ता।

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

PowerShell में `Get-Command` यह दिखाता है कि PowerShell कौन-सा कमांड चलाएगा और उसका executable path क्या है।

## आधिकारिक संदर्भ

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)

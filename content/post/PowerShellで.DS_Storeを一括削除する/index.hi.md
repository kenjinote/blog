---
title: "PowerShell से .DS_Store फ़ाइलें सुरक्षित रूप से हटाएँ"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "स्पष्ट root folder चुनें, छिपी हुई मेल खाने वाली फ़ाइलें देखें और हटाने से पहले WhatIf preview जाँचें।"
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

यदि macOS द्वारा बनाई गई `.DS_Store` फ़ाइलें Windows फ़ोल्डरों में रह गई हों, तो PowerShell से हटाई जा सकती हैं। हटाने का दायरा स्पष्ट रखने के लिए target folder चुनें, मेल खाने वाले पूरे paths देखें और हटाने से पहले `-WhatIf` से preview करें।

## मिलान सूचीबद्ध करें और preview देखें

`$root` को उस फ़ोल्डर के absolute path से बदलें जिसे साफ़ करना है। `-LiteralPath` root path के अक्षरों को wildcard नहीं मानता; `-Filter` केवल `.DS_Store` नाम वाली entries चुनता है। `-File` उसी नाम के फ़ोल्डरों को बाहर रखता है। `-Recurse` subfolders खोजता है और `-Force` hidden items भी शामिल करता है।

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## जाँच के बाद ही हटाएँ

पहले output में candidate फ़ाइलों के पूरे paths दिखते हैं। उसके बाद `-WhatIf` बिना हटाए प्रस्तावित कार्रवाई दिखाता है। सूची और preview सही होने की पुष्टि के बाद ही उसी `Remove-Item` पंक्ति से `-WhatIf` हटाकर चलाएँ।

## दायरा और अनुमतियाँ

यह उदाहरण चुने गए root के नीचे `.DS_Store` नाम वाली फ़ाइलों को लक्षित करता है। गलत root चुनने पर उसके नीचे की अन्य फ़ाइलें भी शामिल हो सकती हैं। `-Force` access permissions को नहीं हटाता। अनुमति त्रुटि पर path और अपने अधिकार जाँचें।

## Microsoft संदर्भ

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)

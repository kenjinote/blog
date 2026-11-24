---
title: "حذف ملفات .DS_Store دفعة واحدة بأمان باستخدام PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "حدد مجلداً جذرياً صريحاً، وراجع الملفات المخفية المطابقة، ثم عاين الحذف باستخدام WhatIf قبل التنفيذ."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

إذا بقيت ملفات `.DS_Store` التي أنشأها macOS في مجلدات Windows، فيمكن حذفها باستخدام PowerShell. لحصر النطاق، حدد المجلد المستهدف، وراجع المسارات الكاملة المطابقة، ثم عاين العملية باستخدام `-WhatIf` قبل حذف أي شيء.

## عرض المطابقات ومعاينة العملية

استبدل `$root` بالمسار المطلق للمجلد الذي تريد تنظيفه. يمنع `-LiteralPath` تفسير أحرف المسار الجذري كأنماط بدل، ويحدد `-Filter` العناصر التي اسمها `.DS_Store`. يستبعد `-File` المجلدات التي تحمل الاسم نفسه. يبحث `-Recurse` في المجلدات الفرعية، ويضمّن `-Force` العناصر المخفية.

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

## لا تحذف إلا بعد المراجعة

يعرض الناتج الأول المسارات الكاملة للملفات المرشحة. ويعرض `-WhatIf` التالي عمليات الحذف المقترحة دون تنفيذها. لا تزل `-WhatIf` من سطر `Remove-Item` نفسه وتشغّله إلا بعد التأكد من صحة القائمة والمعاينة.

## النطاق والأذونات

يستهدف المثال الملفات التي تحمل الاسم `.DS_Store` تحت الجذر المحدد. وقد يؤدي اختيار جذر خاطئ إلى إدراج ملفات ضمن كامل نطاقه. لا يتجاوز `-Force` أذونات الوصول. عند رفض الوصول، راجع المسار والأذونات.

## مراجع Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)

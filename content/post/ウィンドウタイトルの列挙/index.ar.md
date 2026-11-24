---
title: "عرض عناوين النوافذ الرئيسية للعمليات باستخدام PowerShell"
slug: "نافذةタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "تعرّف على عرض عنوان النافذة الرئيسية لكل عملية باستخدام Get-Process وMainWindowTitle، وعلى نطاق النتائج واحتمال احتواء العناوين على معلومات حساسة."
---
يمكنك تصفية كائنات العمليات التي يعيدها `Get-Process` لعرض العناصر التي لا تكون فيها قيمة `MainWindowTitle` (عنوان النافذة الرئيسية) فارغة:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

يعرض الأمر **عنوان النافذة الرئيسية لكل عملية**. ولا يسرد كل النوافذ التابعة لعملية واحدة أو كل النوافذ على سطح المكتب. تُستبعد العمليات التي لا تملك نافذة رئيسية أو يكون عنوانها فارغًا. وقد تتغير النتائج عند بدء العمليات أو انتهائها.

قد تتضمن عناوين النوافذ أسماء مستندات مفتوحة أو معلومات شخصية أخرى. راجع النتائج قبل حفظها في سجل أو مشاركتها.

راجع وثائق Microsoft: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) و[.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).

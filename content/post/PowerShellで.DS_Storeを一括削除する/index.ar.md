---
title: "حذف ملفات .DS_Store دفعة واحدة باستخدام PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["برمجة"]
---

انقل الدليل الحالي إلى المجلد المستهدف وقم بتشغيل الأمر التالي لحذف ملفات .DS_Store دفعة واحدة، بما في ذلك المجلدات الفرعية.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

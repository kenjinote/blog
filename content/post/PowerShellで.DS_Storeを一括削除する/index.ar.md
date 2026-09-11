---
title: 'أمر بسيط لحذف ملفات .DS_Store دفعة واحدة باستخدام PowerShell'
slug: "PowerShellで.DS_Storeを一括削除する"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["برمجة"]
description: 'نشرح كيفية استخدام PowerShell لحذف ملفات .DS_Store الخاصة بـ Mac (والتي غالباً ما تكون مزعجة في بيئات Windows) دفعة واحدة، بما في ذلك المجلدات الفرعية. يمكنك بسهولة تنظيف الملفات غير الضرورية بأمر واحد قصير.'
---

انقل الدليل الحالي إلى المجلد المستهدف وقم بتشغيل الأمر التالي لحذف ملفات .DS_Store دفعة واحدة، بما في ذلك المجلدات الفرعية.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

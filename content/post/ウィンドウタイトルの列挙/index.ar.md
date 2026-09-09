---
title: 'كيفية سرد واسترجاع عناوين النوافذ المفتوحة حالياً باستخدام PowerShell'
slug: "سرد عناوين النوافذ"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["البرمجة"]
description: 'نشرح كيفية سرد واسترجاع عناوين جميع النوافذ المفتوحة حالياً على جهاز الكمبيوتر بسهولة باستخدام PowerShell. نقدم أمثلة على الأوامر الفعلية ونماذج المخرجات بطريقة سهلة الفهم للمبتدئين.'
---
# سرد عناوين النوافذ

طريقة لسرد عناوين النوافذ المفتوحة حاليًا باستخدام PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

نموذج الإخراج

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
بدون عنوان - الرسام
بدون عنوان - المفكرة
مدير المهام
تجربة إدخال Windows
مستند - الدفتر
```

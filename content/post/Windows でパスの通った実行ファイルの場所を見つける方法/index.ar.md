---
title: "العثور على ملف تنفيذي في Windows باستخدام where.exe وPowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でمسارの通ったملف تنفيذيの場所を見つける方法"
tags: ["Windows", "مسار", "ملف تنفيذي", "موجه الأوامر"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "شرح العثور على الملفات التنفيذية في PATH باستخدام where في موجه الأوامر أو where.exe وGet-Command في PowerShell، مع توضيح الاسم المستعار ونطاق البحث."
---
## موجه الأوامر

للعثور على مسار ملف تنفيذي يمكن تشغيله كأمر، استخدم `where` في موجه الأوامر. في PowerShell، الاسم `where` هو اسم مستعار لـ`Where-Object`؛ اكتب `where.exe` لاستدعاء البرنامج الخارجي صراحةً.

```cmd
where mspaint.exe
```

يبحث `where` في المجلد الحالي والمجلدات المدرجة في متغير البيئة `PATH` ويعرض النتائج المطابقة. قد يظهر أكثر من مسار. لا يبحث في جميع مجلدات الكمبيوتر ولا يعثر على التطبيقات خارج هذه المواقع.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

في PowerShell، يعرض `Get-Command` الأمر الذي سيختاره PowerShell ومسار ملفه التنفيذي.

## مراجع رسمية

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)

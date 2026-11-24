---
title: "حذف مجلد كبير من موجه أوامر Windows: الخطوات والمخاطر"

slug: "大きなフォルダーを高速一括削除"
date: 2022-09-20T16:04:02+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["موجه الأوامر"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "طريقة موثقة من Microsoft لحذف المجلدات باستخدام DEL وRMDIR، مع تنبيه إلى الحذف التكراري الصامت والتحقق من المسار والنسخ الاحتياطي."
---
تحذف هذه الأوامر الملفات والمجلدات الفرعية في الهدف بشكل تكراري. يمنع الخيار `/Q` ظهور طلب التأكيد. قد يؤدي اختيار هدف خاطئ إلى فقدان بيانات لا يمكن استعادتها؛ لذا انسخ البيانات المهمة احتياطيًا وتحقق من مسار المجلد الأب واسمه قبل التنفيذ. تختلف السرعة حسب عدد الملفات ووسيط التخزين، ولا يوجد ضمان بأنها ستكون أسرع.

## الخطوات

في هذا المثال، `C:\Parent` هو المجلد الأب و`Large Folder` هو المجلد المراد حذفه. اعرض محتويات الهدف للتحقق منه أولًا، ثم احذفه.

```bat
cd /d "C:\Parent"
dir /a "Large Folder"
DEL /F /Q /S "Large Folder\*" > NUL
RMDIR /S /Q "Large Folder"
```

يحذف `DEL /F /Q /S` الملفات الموجودة في الهدف (`/F` يشمل الملفات للقراءة فقط، و`/Q` يمنع طلب التأكيد، و`/S` يشمل المجلدات الفرعية). ثم يحذف `RMDIR /S /Q` شجرة المجلد كاملة من دون تأكيد. استبدل `C:\Parent` و`Large Folder` بالقيم الفعلية، وتحقق من مخرجات `dir` قبل تنفيذ أوامر الحذف.

## Microsoft documentation

- [del command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/del)
- [rmdir command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rmdir)

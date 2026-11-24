---
title: 'يمكن استخدامه على Windows! طريقة تثبيت محرر النصوص الخفيف "micro"'
slug: "محرر نصوصmicroをWindowsにتثبيتする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "محرر نصوص"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'نشرح بوضوح خطوات تثبيت محرر النصوص الموجه للطرفية "micro" الذي يعمل بسلاسة في موجه الأوامر على نظام Windows، وإعداد متغيرات البيئة لجعله جاهزاً للاستخدام.'
---

## تنزيل micro
https://github.com/micro-editor/micro/releases/latest
من قسم Assets في أحدث إصدار، نزّل أرشيف Windows x64 (مثل `micro-<version>-win64.zip`) وفك ضغطه في مجلد تختاره.

إذا كان جهازك يعمل بنظام Windows على ARM، فاختر أرشيف ARM64 المطابق بدلًا منه.

## تعيين متغيرات البيئة
لاستخدام `micro.exe` من موجه الأوامر، ستحتاج إلى تعيين متغيرات البيئة.

1. اضغط `Win` + `R`، واكتب `sysdm.cpl`، ثم اضغط `Enter`.
2. افتح علامة التبويب Advanced ثم انقر على Environment Variables.
3. ضمن متغيرات المستخدم لحسابك، اختر `Path` وانقر على Edit. أنشئ `Path` إذا لم يكن موجودًا.
4. انقر على New وأضف مسار المجلد الذي يحتوي على `micro.exe`.
5. انقر على OK لإغلاق مربعات الحوار.
6. أعد فتح موجه الأوامر وشغّل `micro` للتحقق من بدء تشغيله.

## كيفية استخدام micro

عند كتابة `micro` في موجه الأوامر وتشغيله، ستظهر لك شاشة مشابهة لهذه:
![img_3.png](img_3.webp)

تتضمن طرق التشغيل الرئيسية واختصارات لوحة المفاتيح ما يلي:

| اختصار لوحة المفاتيح | العملية | 
|--------|-----| 
| Ctrl+Q | إغلاق الملف الحالي (ينتهي micro إذا كان هذا آخر ملف) |
| Ctrl+S | حفظ الملف | 
| Ctrl+O | فتح ملف | 
| Ctrl+A | تحديد الكل | 
| Ctrl+X | قص التحديد | 
| Ctrl+C | نسخ التحديد | 
| Ctrl+V | لصق | 
| Ctrl+Z | تراجع | 
| Ctrl+Y | إعادة | 
| Ctrl+E | تنفيذ أمر المحرر | 

## مراجع
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)

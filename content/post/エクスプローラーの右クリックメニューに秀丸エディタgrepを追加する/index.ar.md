---
title: 'كيفية إضافة ميزة grep الخاصة بمحرر Hidemaru إلى قائمة النقر بزر الماوس الأيمن في Windows'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "مستكشف الملفاتのقائمة النقر الأيمنにمحرر هيديماروgrepを追加する"
tags: ["Hidemaru Editor", "File Explorer", "Right-click menu", "grep", "Registry"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'نقدم خطوات إعداد مفيدة لإضافة ميزة grep الخاصة بمحرر Hidemaru إلى قائمة النقر بزر الماوس الأيمن في مستكشف Windows 10/11. نشرح بوضوح الطريقة السهلة باستخدام ملف تسجيل السجل.'
---
نقدم لكم طريقة لإضافة grep الخاص بـ Hidemaru Editor إلى قائمة النقر بزر الماوس الأيمن في مستكشف الملفات في Windows 10/11.

**※ يرجى ملاحظة أن الخطوات التالية تتضمن تعديل السجل (الريجستري)، لذا يرجى القيام بذلك على مسؤوليتك الخاصة.**

يضيف هذا الملف أوامر لقائمة المجلدات للمستخدم الحالي فقط؛ ولا يضيف خيار الفتح باستخدام Hidemaru إلى كل الملفات أو يغيّر إعدادات النظام بأكمله. قبل الاستيراد، افتحه في المفكرة وتحقق من مسار البرنامج أو عدّله. إذا كانت المفاتيح موجودة، فصدّرها أولًا من محرر السجل عبر «ملف» > «تصدير». في Windows 11 قد تظهر الأوامر القديمة ضمن «إظهار المزيد من الخيارات». انتهى دعم Windows 10 في 14 أكتوبر 2025. يحذف ملف الإزالة المرفق إدخالات المستخدم الحالي فقط، ولا يلغي التسجيل القديم على مستوى النظام. إذا استوردت الملف السابق، فتحقق من مفاتيحه وأزلها بشكل منفصل في محرر السجل.
## الخطوات

1. افتح الرابط التالي واحفظ الملف في أي مجلد تريده.

[تسجيل_ريجستري_هيديمارو.reg](秀丸レジストリ登録.reg)

[إزالة إدخالات Hidemaru من السجل](秀丸レジストリ解除.reg)

2. انقر نقراً مزدوجاً على ملف `تسجيل_ريجستري_هيديمارو.reg` لإضافته إلى السجل.

## المراجع

- [تنفيذ Hidemaru grep من قائمة النقر بزر الماوس الأيمن للمجلد](https://aimek-developer.blogspot.com/2019/02/grep.html)

## مراجع رسمية

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)

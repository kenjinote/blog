---
title: "Windows 11: فحص بدء التشغيل السريع عند تغيّر تحجيم العرض"

slug: "شاشات متعددةで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["شاشات متعددة", "DPI", "لوحة التحكم"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "خطوة استكشاف أعطال حذرة في Windows 11: عطّل بدء التشغيل السريع مؤقتًا، واختبر الإيقاف والتشغيل، ثم أعد تفعيله إذا لم يساعد."
---
يحفظ بدء التشغيل السريع جلسة النواة وحالة برامج تشغيل الأجهزة في ملف الإسبات عند إيقاف التشغيل لتسريع الإقلاع التالي. وقد يؤدي تعطيله إلى إبطاء الإقلاع. لا تحدد وثائق Microsoft هذه الميزة سببًا لإعادة ضبط التحجيم على شاشات متعددة؛ لذا اعتبر الخطوات اختبارًا مؤقتًا لا إصلاحًا مؤكدًا.

## تغيير الإعداد مؤقتًا

1. افتح لوحة التحكم واختر **خيارات الطاقة**.
2. افتح **اختيار ما تفعله أزرار الطاقة**.
3. انقر **تغيير الإعدادات غير المتاحة حاليًا** (قد تحتاج إلى صلاحيات المسؤول).
4. أزل تحديد **تشغيل بدء التشغيل السريع (مستحسن)** ثم انقر **حفظ التغييرات**.
5. اختر **إيقاف التشغيل** ثم شغّل الكمبيوتر وتحقق من بقاء التحجيم. يجب أن يكون الاختبار بالإيقاف ثم التشغيل؛ خيار **إعادة التشغيل** لا يستخدم بدء التشغيل السريع.

إذا لم يساعد ذلك، فأعد تفعيل بدء التشغيل السريع من الصفحة نفسها. قد تختلف أسماء القوائم حسب لغة Windows وتحديثاته.

## مراجع Microsoft

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)

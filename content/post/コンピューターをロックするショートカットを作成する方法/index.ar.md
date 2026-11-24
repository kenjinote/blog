---
title: 'قفل جهاز الكمبيوتر الذي يعمل بنظام Windows في ثانية واحدة! طريقة إنشاء واستخدام اختصار مفيد'
slug: "قفل الكمبيوترするاختصارを作成する方法"
tags: ["Windows", "قفل الكمبيوتر", "اختصار"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'نشرح بوضوح بالصور كيفية إنشاء اختصار لقفل جهاز كمبيوتر يعمل بنظام Windows بنقرة واحدة. كما نقدم طريقة القفل الفوري باستخدام مفاتيح Win+L، والتي تُعد مفيدة كتدبير أمني عند ترك المقعد.'
date: "2024-04-01T01:37:49+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

إليك كيفية إنشاء اختصار لقفل الكمبيوتر.

يعد ذلك مفيدًا لأنه يمكنك قفل الكمبيوتر عن طريق النقر المزدوج فوق الاختصار الذي تم إنشاؤه على سطح المكتب.

## طريقة الإنشاء

#### 1. انقر بزر الماوس الأيمن على سطح المكتب وحدد `جديد` > `اختصار`

![img_2.png](img_2.webp)
#### 2. ستظهر شاشة إنشاء الاختصار، أدخل `rundll32.exe user32.dll,LockWorkStation` وانقر على `التالي`

![img_1.png](img_1.webp)

#### 3. أدخل اسم الاختصار `قفل الكمبيوتر` وانقر على `إنهاء`

![img_3.png](img_3.webp)

#### 4. تغيير أيقونة الاختصار الذي تم إنشاؤه

انقر بزر الماوس الأيمن على الاختصار الذي تم إنشاؤه وحدد `خصائص`

![img_4.png](img_4.webp)

انقر على `تغيير الأيقونة`

![img_6.png](img_6.webp)

حدد الأيقونة المربعة الصفراء وانقر على `موافق` ، ثم انقر على `موافق` مرة أخرى لإغلاق الخصائص

![img_5.png](img_5.webp)

هذا كل شيء.

![img_7.png](img_7.webp)

النقر المزدوج على الاختصار الذي تم إنشاؤه سيؤدي إلى قفل الكمبيوتر.

يمكنك أيضًا قفل الكمبيوتر بالضغط على `مفتاح Win` + `مفتاح L`.

※ ملاحظة: لن يتم عرض مربع حوار تأكيد قفل الكمبيوتر.

عند قفل Windows تظل التطبيقات مفتوحة، ويلزم تسجيل الدخول مجددًا للمتابعة. تعرض لقطات الشاشة واجهة Windows اليابانية، لذلك قد تختلف التسميات والتخطيط باختلاف الإصدار ولغة العرض.

## References

- [Microsoft Support: Lock your Windows device](https://support.microsoft.com/en-us/accounts-billing/security/user-account-access-in-windows)
- [Microsoft Learn: LockWorkStation function](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-lockworkstation)
- [Microsoft Learn: Changing computer state with PowerShell](https://learn.microsoft.com/en-us/powershell/scripting/samples/changing-computer-state)
- [Microsoft Learn: rundll32 command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/rundll32)

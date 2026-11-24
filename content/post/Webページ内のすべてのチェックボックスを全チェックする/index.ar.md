---
title: "تحديد كل مربعات الاختيار في صفحة ويب أو إلغاء تحديدها"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "استخدم JavaScript أو إشارة مرجعية لتنفيذ تحديد أو إلغاء تحديد مربعات الاختيار المفعّلة في الصفحة الحالية. تحقّق من سلوك الصفحة قبل تشغيل الرمز."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# تحديد كل مربعات الاختيار في صفحة ويب أو إلغاء تحديدها

ينقر هذا البرنامج النصي على مربعات الاختيار المفعّلة في الصفحة الحالية لتغييرها دفعة واحدة.

## تنبيه قبل التشغيل

شغّله على الصفحات الموثوقة فقط. قد تستجيب الصفحة للنقر بتغيير الإعدادات أو إرسال طلبات. راجع الاختيارات قبل الإرسال أو الحفظ.

## التشغيل في DevTools

افتح الصفحة المطلوبة وشغّل الرمز أدناه في وحدة تحكم DevTools. إذا لم يفتح F12 أدوات DevTools، فاستخدم قائمة المتصفح.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

لإلغاء تحديد جميع المربعات المفعّلة، استخدم هذا الرمز.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## إنشاء إشارة مرجعية

أنشئ إشارة مرجعية والصق الرمز ذي السطر الواحد في حقل URL باستخدام محرر الإشارات المرجعية. لا تكتبه في شريط العناوين. اختر الإشارة المرجعية في الصفحة المطلوبة لتحديد المربعات المفعّلة.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

لإلغاء التحديد، استخدم المثال الثاني أو إشارة إلغاء تحديد الكل. يعمل البرنامج النصي في المستند الحالي فقط ويتجاوز مربعات الاختيار المعطّلة.

قد لا يؤدي تغيير الخاصية `.checked` وحدها إلى إرسال الأحداث المعتادة عند النقر إلى رمز الصفحة. تستدعي `.click()` سلوك النقر، لكن معالجة الصفحة نفسها قد تمنع بعض التغييرات.

## المراجع

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)

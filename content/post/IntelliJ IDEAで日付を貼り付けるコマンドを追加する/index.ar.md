---
title: 'كيفية إنشاء اختصار لإدراج التاريخ الحالي في IntelliJ IDEA'
slug: "IntelliJ IDEAでتاريخを貼り付けるأمرを追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: 'أنشئ قالباً مباشراً في IntelliJ IDEA لإدراج طابع زمني بتنسيق ISO 8601 يتضمن إزاحة المنطقة الزمنية المحلية. يتبع هذا الدليل وثائق JetBrains الحالية لإعداد التعبير ومفتاح التوسيع.'
---

# مقدمة

إذا كنت تدخل الطوابع الزمنية كثيراً أثناء الكتابة، فيمكن لقالب مباشر في IntelliJ IDEA إدراجها باستخدام اختصار قصير. ينشئ هذا المثال طابعاً زمنياً بتنسيق ISO 8601 مع الوقت المحلي وإزاحة المنطقة الزمنية للكمبيوتر.

## إنشاء القالب المباشر

1. افتح **Settings > Editor > Live Templates**. في Windows أو Linux افتحه من **File > Settings**، وفي macOS من **IntelliJ IDEA > Settings**.
2. اختر مجموعة قوالب (مثل **other**) وانقر **+ > Live Template**.
3. أدخل `date` في **Abbreviation** واكتب وصفاً موجزاً في **Description**.
4. أدخل `$date$` في **Template text**.
5. انقر **Edit Variables**. للمتغير `date` أدخل `date("yyyy-MM-dd'T'HH:mm:ssXXX")` في **Expression**. فعّل **Skip if defined** ليتم حساب القيمة تلقائياً عند توسيع القالب.
6. انقر **Define** وحدد السياقات التي تريد استخدام القالب فيها (اختر **Everywhere** إذا كان ذلك مناسباً). احفظ الإعدادات.

## استخدام القالب

اكتب `date` في المحرر واضغط مفتاح التوسيع الافتراضي **Tab**. يُدرج IntelliJ IDEA تاريخ النظام ووقته الحاليين بصيغة مثل `2026-11-24T09:30:00+09:00`. يعتمد الوقت والإزاحة على المنطقة الزمنية الحالية للكمبيوتر. إذا غيّرت مفتاح التوسيع، فتحقق منه في إعدادات Live Templates.

ينشئ النمط `XXX` إزاحة منطقة زمنية بتنسيق ISO 8601. لا يثبت التعبير القيمة `+09:00`، بل يستخدم المنطقة الزمنية المحلية لكل قارئ. تحقق من أن الطابع الزمني الناتج يطابق وقت النشر المقصود.

## مراجع

- [إنشاء القوالب المباشرة وتحريرها](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [متغيرات القوالب المباشرة ودالة date](https://www.jetbrains.com/help/idea/template-variables.html)
- [إعداد مفتاح توسيع القالب المباشر](https://www.jetbrains.com/help/idea/settings-live-templates.html)

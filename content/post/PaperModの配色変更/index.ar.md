---
title: "تخصيص ألوان Hugo PaperMod باستخدام متغيرات CSS"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "استبدل متغيرات ألوان PaperMod للسمتين الفاتحة والداكنة عبر CSS الموسع، ثم افحص تباين النص."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

يمكن تخصيص ألوان PaperMod باستخدام خصائص CSS المخصصة (المتغيرات). ضع التعديلات في `assets/css/extended/` الخاص بموقعك بدلاً من تحرير ملفات القالب، لتسهيل الاحتفاظ بها عند التحديث. يوضح المثال لوحة فاتحة دافئة وأخرى داكنة؛ عدّل القيم لتناسب موقعك.

## الوضع الداكن والمتغيرات الحالية

يبدّل PaperMod الحالي إلى الوضع الداكن بتعيين `data-theme="dark"` على عنصر `html`. قد لا تنطبق الأمثلة القديمة التي تستهدف `.dark` وحده على هذا المحدد. كما أن `--hljs-bg` لم يعد متغير خلفية كتلة الشيفرة الحالي؛ الاسم المستخدم الآن هو `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## تباين النص

في المثال، تتباين ألوان النص العادي `--primary` و`--content` بوضوح مع الخلفيات. تبلغ نسبة تباين `--primary` مع `--theme` نحو 10.4:1 في الوضع الفاتح و13.4:1 في الداكن. يطلب WCAG 2.2 AA نسبة 4.5:1 للنص العادي؛ افحص ألوان تمييز الشيفرة والروابط والحدود والحالات الأخرى بشكل منفصل.

## إضافة CSS الموسع وفحصه

احفظ ورقة الأنماط باسم `assets/css/extended/theme-colors.css` في جذر الموقع. توضح FAQ الخاصة بـ PaperMod أن CSS داخل `assets/css/extended/` يُدمج مع أنماط القالب. شغّل Hugo وافحص التبديل بين الفاتح والداكن والبطاقات والنص والشيفرة المضمنة وكتل الشيفرة والروابط.

## النطاق

هذه لوحة ألوان توضيحية ولا تضمن إمكانية الوصول لكل نص أو صورة أو عنصر تفاعلي. ألوان تمييز بناء الجملة معرفة بصورة منفصلة عن `--code-block-bg`؛ أعد فحص وضوح الشيفرة بعد تغيير خلفية الكتلة.

## المراجع

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)

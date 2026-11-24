---
title: "تغيير حجم صور الغلاف وموضعها في قوائم Hugo PaperMod"
slug: "PaperModのصورةの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "استخدم CSS الموسع في PaperMod وCSS Grid لتصغير صور أغلفة البطاقات ووضعها بجانب الملخص."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

يقلل هذا المثال حجم صور الغلاف في بطاقات قوائم PaperMod ويضعها أسفل العنوان بجانب الملخص. يستخدم CSS الموسع الخاص بالموقع بدلاً من تعديل ملفات الأنماط أو القوالب المرفقة بالثيم. تعتمد المحددات على فئات PaperMod، لذا افحص النتيجة في المتصفح بعد تحديث الثيم.

## إضافة CSS موسع

أنشئ `assets/css/extended/custom.css` في جذر الموقع. يضم PaperMod ملفات CSS من هذا المجلد إلى أنماط الثيم. يغيّر CSS Grid الترتيب المرئي مع الإبقاء على بنية HTML الحالية.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## الضبط للشاشات الضيقة

قلل عرض العمود والمسافة على الشاشات الضيقة كي يظل الملخص مقروءاً. عدّل 150px ونقطة التوقف بما يناسب التصميم. تحافظ `height: auto` على نسبة الصورة. أضف `aspect-ratio` و`object-fit: cover` فقط إذا أردت قص الصور بأبعاد موحدة.

## تجنب تعديل ملفات الثيم مباشرة

تصف وثائق PaperMod ملف `blank.css` بأنه عنصر نائب يُستخدم عندما يكون مجلد CSS الموسع فارغاً. لا حاجة لتعديل `post-entry.css` المرفق بالثيم أو حذف السطر المعلّق `/* width: 100%; */`؛ فحذف تعليق CSS لا يغيّر النمط. إذا أردت تغيير بنية HTML نفسها، انسخ القالب إلى مجلد `layouts/` في موقعك واستبدله، لكن حافظ على النسخة عند تحديث الثيم.

## فحص التخطيط

شغّل Hugo وافحص قوائم الصفحة الرئيسية والوسوم والتصنيفات على الشاشات الواسعة والضيقة. تأكد من عدم تداخل الصورة والعنوان والملخص والبيانات الوصفية، ومن عمل الرابط الذي يغطي البطاقة كلها. عدّل CSS إذا غيّر تحديث الثيم الفئات أو HTML. يخص هذا المثال أغلفة بطاقات القوائم، ولا يغيّر الصور داخل المقالات.

## المراجع

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

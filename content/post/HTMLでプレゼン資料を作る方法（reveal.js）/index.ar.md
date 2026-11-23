---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'كيفية استخدام reveal.js: إنشاء عروض تقديمية باستخدام HTML و Markdown'
slug: "HTMLでعرض تقديمي資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "عرض تقديمي"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'نشرح تثبيت والاستخدام الأساسي لأداة ''reveal.js'' التي تتيح لك إنشاء عروض تقديمية بشكل بديهي باستخدام HTML و Markdown. نقدم أيضاً كيفية الاستفادة منها مع دعم الرسوم المتحركة وإخراج ملفات PDF، وتوافقها الممتاز مع أنظمة التحكم في الإصدارات مثل Git.'
---

# طريقة إنشاء عرض تقديمي باستخدام HTML

أداة reveal.js هي أداة لإنشاء العروض التقديمية باستخدام HTML و Markdown، وتحتوي على الميزات التالية:

- ميزات عرض تقديمي متنوعة مثل المعادلات الرياضية، الرسوم المتحركة، وعمليات السحب
- إمكانية تخصيص السمة والتخطيط
- ميزات تنقل تدعم أجهزة متعددة مثل الماوس، لوحة المفاتيح، ولوحة اللمس
- توفير ميزات متقدمة مثل التشغيل التلقائي للشرائح وتضمين الفيديو
- إمكانية التصدير بصيغة PDF

من خلال هذه الميزات، يمكن للمستخدمين بسهولة إنشاء عروض تقديمية تفاعلية وجذابة.

# تثبيت واستخدام reveal.js

أسهل طريقة للاستخدام هي تنزيل ملف ZIP بالكامل من الصفحة التالية وفك ضغطه.

1. افتح [https://revealjs.com/installation](https://revealjs.com/installation) وقم بتنزيل `master.zip` من الرابط
2. افتح ملف index.html الموجود في المجلد المستخرج باستخدام المتصفح
3. قم بتعديل index.html لإنشاء العرض التقديمي الخاص بك

※ تمت كتابة كود HTML تجريبي في demo.html لذا يمكنك استخدامه كمرجع.

# طرق الاستفادة

يمكنك نشر العرض التقديمي الذي قمت بإنشائه كصفحة ويب كما هو، أو تصديره كملف PDF.
أيضًا، نظرًا لأن مصدر العرض التقديمي عبارة عن نص، فمن السهل إدارته باستخدام أنظمة التحكم في الإصدار.

يبدو أنه يمكنك أيضًا إنشاء عروض تقديمية بتنسيق Markdown.

# إنشاء شرائح أساسية

أسهل طريقة هي تنزيل أحدث ملف ZIP من Basic Setup وفك ضغطه ثم تحرير `index.html`. كما في مثال HTML أدناه، ضع كل شريحة داخل `<section>`. يتضمن ملف Basic Setup التجريبي الأنماط وشيفرة التهيئة اللازمة.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# كتابة الشرائح بصيغة Markdown

تتيح إضافة Markdown المرفقة كتابة Markdown داخل ملف HTML. افصل الشرائح الأفقية باستخدام `---` وأضف المثال أدناه إلى `index.html`. يتطلب تحميل ملف Markdown خارجي خادم ويب محليًا.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# إعداد التطوير

إذا احتجت إلى خادم محلي أو أدوات تطوير المصدر، فاستخدم Full Setup الرسمي. نفّذ الأوامر التالية ثم افتح `http://localhost:8000` في المتصفح.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# التصدير إلى PDF

أضف `?print-pdf` إلى نهاية عنوان URL. في نافذة الطباعة في Chrome أو Chromium اختر الحفظ بصيغة PDF، والاتجاه الأفقي، ومن دون هوامش، مع تفعيل رسومات الخلفية. يؤكد الدليل الرسمي Chrome وChromium.

# ملاحظات المتحدث

اضغط `S` لفتح عرض المتحدث في نافذة منفصلة. أضف الملاحظات داخل `<aside class="notes">` في الشريحة. يحتاج عرض المتحدث محليًا إلى خادم ويب.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# الوثائق الرسمية

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

スライドに使う画像・動画の利用条件を確認し、公開資料に機密情報や非公開の発表者ノートが含まれていないか確認してください。

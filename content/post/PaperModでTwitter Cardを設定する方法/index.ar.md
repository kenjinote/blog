---
title: "كيفية إعداد Twitter Card (X Card) في Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "اضبط صور بطاقات X وفق إعدادات PaperMod الموثقة، ثم افحص HTML الناتج والمعاينة في محرر منشورات X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

يمكن لـ PaperMod إنشاء بيانات Open Graph وTwitter Card. وقد يختلف الناتج حسب إصدار القالب والتخطيطات المخصصة؛ لذا افحص HTML المنشور ولا تفترض أن مثال الإعداد يضمن بطاقة بعينها.

## إعداد الموقع بالكامل

تُفعّل بيانات SEO في PaperMod عند البناء لبيئة production. اضبط بيئة الموقع على production.

```toml
[params]
  env = "production"
```

لصورة افتراضية على مستوى الموقع، ضع الملف داخل `static` وحدده هنا. وقد تُستخدم عند عدم تعيين صورة خاصة للمقال. تحقق أيضاً من URL الناتج على الموقع المنشور.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## صورة خاصة بالمقال

لتعيين صورة لمقال بعينه، اجعل `cover.image` يشير إلى صورة داخل Page Bundle. يشير `relative: true` إلى مسار نسبي داخل الحزمة. تذكر وثائق PaperMod أن صورة الغلاف لها الأولوية؛ وعند غيابها قد تُستخدم قائمة `images` في الصفحة ثم صور الحزمة المطابقة للشروط.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## إخفاء الغلاف في المقال

وفق مرجع متغيرات PaperMod، يخفي `cover.hidden: true` الغلاف من عرض المقال مع إبقائه في البيانات الوصفية المنظمة. يفيد ذلك عندما تكون الصورة مخصصة للبطاقات الاجتماعية فقط. افحص HTML عند استخدام fork للقالب أو قوالب بديلة.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## نوع البطاقة وأبعاد الصورة

لا يصح تعميم الادعاءين القديمين بأن PaperMod لا يدعم إلا `summary_large_image` وأن 800×418 مقاس ثابت. فقد يعتمد نوع البطاقة على إصدار القالب أو تخطيطات الموقع. للصورة العريضة، يعد 1200×630 (نحو 1.90:1) هدفاً عملياً للتصميم، لا ضماناً لمتطلبات العرض لدى X.

## فحص HTML والمعاينة

ابنِ الموقع بإعداد production ثم افحص HTML للمقال بحثاً عن `twitter:card` و`twitter:image` و`og:image` والعنوان والوصف. يجب أن يكون رابط الصورة متاحاً للعامة مباشرة عبر HTTPS دون تسجيل دخول. أزالت X معاينة Card Validator في 2022 وأحالت المطورين إلى محرر المنشورات. ألصق الرابط هناك وعاين البطاقة دون نشر المنشور. قد يتأخر تحديث التخزين المؤقت.

تمت المراجعة في 24-11-2026 بالاستناد إلى مراجع PaperMod ومنتدى مطوري X المرتبطين. وقد يؤثر fork القالب أو تخصيص التخطيطات أو تغييرات X في الناتج.

## المراجع

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)

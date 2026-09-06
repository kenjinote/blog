---
title: "كيفية إعداد Twitter Card في PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["إدارة المدونة"]
---
# مقدمة
يدعم قالب PaperMod ميزة Twitter Card.
ومع ذلك، يجب كتابة إعدادات Twitter Card في `config.toml` أو في معلومات رأس `*.md` لكل مقال.
إذا تم تعيينها في كل من المقال و `config.toml`، فستكون الأولوية لمعلومات رأس كل مقال.

# طريقة الإعداد
## config.toml
في `config.toml`، أضف عنصرًا يسمى `images` ضمن `[params]`.
في `images`، اكتب مسار الصورة التي سيتم عرضها في Twitter Card.
إذا كنت ستضع الصورة في مجلد `static`، فيكفي تحديد اسم الملف فقط.

```
[params]
  images = ["twitter_card.jpg"]
```

هيكل المجلد
```
root
│  config.toml (اكتب هنا)
├─content
│  └─posts
│      └─مجلد المقال
│         │  index.md (اكتب هنا)
│         └─images
│             cover.png (ضع هنا)
└─static
    twitter_card.jpg (ضع هنا)
```

## معلومات رأس كل مقال
في معلومات رأس كل مقال، أضف عنصرًا يسمى `image` تحت `cover`.
إذا قمت بتعيين `relative` إلى `true`، يمكنك تحديده بمسار نسبي من `*.md` للمقال.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### إذا كنت لا ترغب في عرضها أعلى المقال
إذا كنت لا ترغب في عرض صورة الغلاف أعلى المقال، أضف عنصرًا يسمى `hidden` تحت `cover` وقم بتعيينه إلى `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# حول حجم الصورة

حاليًا، يبدو أن حجم Twitter Card في مواصفات PaperMod يدعم فقط `summary_large_image`.
الحجم المناسب (الدقة) لـ `summary_large_image` مختلف عليه، ولكن يبدو أن `800 x 418` (نسبة الصورة 1.91:1) جيدة.

[الموقع المرجعي 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[الموقع المرجعي 2](https://developers.facebook.com/docs/sharing/best-practices)

إذا أمكن، نوصي بتغيير حجم الصورة قبل النشر.

# كيفية التحقق من الإعدادات
للتحقق من إعدادات Twitter Card، استخدم [Twitter Card Validator](https://cards-dev.twitter.com/validator).
ومع ذلك، في بيئتي لم يتم عرض المعاينة بشكل صحيح، لذلك إذا لم يتم عرض المعاينة، نوصي بالتحقق منها مرة واحدة قبل النشر باستخدام حساب خاص أو ما شابه.

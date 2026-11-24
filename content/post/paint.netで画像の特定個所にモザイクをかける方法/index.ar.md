---
title: 'شرح بسيط لكيفية وضع فسيفساء (Mosaic) على جزء معين من الصورة في paint.net'
slug: "paint.netでصورةの特定個所にモザイクをかける方法"
tags: ["paint.net", "البكسلة", "تحرير الصور", "الخصوصية"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "طريقة تطبيق تأثير Pixelate في paint.net على تحديد وضبط Cell Size وطرق تغيير الحجم. لا تضمن البكسلة إخفاء المعلومات بأمان؛ وتوضح المقالة بديلاً أكثر أماناً."
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


في هذه المقالة، سنشرح كيفية تطبيق الفسيفساء على جزء معين من الصورة باستخدام paint.net.

عند تحميل الصور على الإنترنت، قد ترغب في بعض الأحيان في إخفاء أجزاء معينة بوضع فسيفساء عليها، وباستخدام paint.net يمكنك تعديل الصور بسهولة وسرعة.

## الخطوات

#### 1. افتح الصورة التي تريد تعديلها في paint.net
#### 2. استخدم أداة التحديد لاختيار الجزء الذي تريد تغطيته بالفسيفساء (يمكن التحديد المتعدد)

![img_2.png](img_2.webp)

#### 3. اختر من القائمة: تأثيرات (Effects) > تشويه (Distort) > فسيفساء (Pixelate)

![img_1.png](img_1.webp)

- يتحكم Cell Size في حجم البكسلات بعد تكبيرها. تؤدي القيم الأعلى إلى مربعات أكبر، لكنها لا تضمن إخفاء المعلومات بأمان.
- للحصول على مربعات بكسلية واضحة، اختر `Multisample Bilinear` في [Scale Down] و`Nearest Neighbor` في [Scale Up].

انقر على OK لإغلاق النافذة.

#### 4. سيتم تطبيق الفسيفساء، قم بحفظ الصورة بعد ذلك.

![img.png](img.webp)

## تنبيه بشأن الخصوصية

إذا كان يجب إخفاء بيانات شخصية أو معلومات أخرى بشكل موثوق، فلا تعتمد على البكسلة أو التمويه وحدهما. غطِّ المحتوى بالكامل بلون موحد معتم، وصدّر الصورة بصيغة PNG أو JPEG من دون طبقات أو سجل تعديلات، ثم افحص الملف الناتج. احتفظ بالنسخة القابلة للتحرير في مكان آمن منفصل.

هذا كل شيء.

## المراجع

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)

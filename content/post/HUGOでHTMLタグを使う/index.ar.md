---
title: 'كيفية تفعيل وسوم HTML في Hugo (إعدادات config.toml)'
slug: "HUGOでHTMLタグを使う"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["إدارة المدونة"]
description: 'نشرح كيفية تمكين كتابة وسوم HTML واستخدامها مباشرة داخل مقالات Markdown في مُنشئ المواقع الثابتة Hugo. يكتمل الأمر بمجرد إضافة إعداد ''unsafe'' إلى ''markup.goldmark.renderer'' في ملف config.toml.'
---

افتراضيًا، لا يسمح HUGO باستخدام علامات HTML في المقالات، ولكن بإضافة الكود التالي إلى ملف config.toml، سيصبح ذلك ممكنًا.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

المرجع: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)

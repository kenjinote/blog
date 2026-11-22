---
title: "السماح بـ HTML الخام في Markdown ضمن Hugo"
date: "2023-01-17T19:20:32+09:00"
lastmod: 2026-11-23
slug: "HUGOでHTMLタグを使う"
tags: ["HUGO", "HTML"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "تعرّف على كيفية السماح بعرض HTML الخام في Markdown ضمن Hugo، مع أمثلة YAML وTOML وJSON وشرح للمخاطر الأمنية والحالات التي لا ينبغي فيها تفعيل هذا الخيار."
---

لا يعرض محرّك Goldmark في Hugo وسوم HTML الخام داخل Markdown افتراضيًا. إذا احتجت إلى ذلك، فاضبط `markup.goldmark.renderer.unsafe` على `true` في إعدادات الموقع. يدعم Hugo ملفات إعداد YAML وTOML وJSON. مثال في `hugo.yaml`:

```yaml
markup:
  goldmark:
    renderer:
      unsafe: true
```

وفي `hugo.toml`:

```toml
[markup.goldmark.renderer]
  unsafe = true
```

أو في `hugo.json`:

```json
{
  "markup": {
    "goldmark": {
      "renderer": {
        "unsafe": true
      }
    }
  }
}
```

القيمة الافتراضية هي `false`. يسمح `unsafe: true` بتمرير HTML الخام في Markdown إلى المخرجات، ويضعف حدّ الثقة الذي يطبقه Hugo على المحتوى. لا تفعّله إذا كان الموقع يعالج Markdown من مساهمين غير موثوقين أو من مدخلات خارجية. استخدمه فقط مع محتوى تتحكم فيه وتراجعه، وبعد فهم العواقب. وقد يكون shortcode أو ملف محتوى HTML أنسب للتخطيطات المعقدة.

مراجع: [إعداد markup](https://gohugo.io/configuration/markup/) · [نموذج الأمان في Hugo](https://gohugo.io/about/security/)

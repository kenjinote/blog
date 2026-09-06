---
title: "استخدام علامات HTML في HUGO"
slug: "استخدام-علامات-html-في-hugo"
date: 2023-01-17T19:20:32+09:00
tags: ["HUGO", "HTML"]
draft: false
image: "img.png"
categories: ["إدارة المدونة"]
---

افتراضيًا، لا يسمح HUGO باستخدام علامات HTML في المقالات، ولكن بإضافة الكود التالي إلى ملف config.toml، سيصبح ذلك ممكنًا.

```toml
[markup.goldmark.renderer]
    unsafe = true
```

المرجع: [Configure Markup](https://gohugo.io/getting-started/configuration-markup)

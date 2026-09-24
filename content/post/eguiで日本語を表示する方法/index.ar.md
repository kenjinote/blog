---
title: 'كيفية تحميل وعرض الخطوط اليابانية في مكتبة واجهة المستخدم الرسومية ''egui'' الخاصة بـ Rust'
slug: "eguiでاللغة اليابانيةを表示する方法"
date: "2026-09-24T16:08:36+09:00"
tags: ["rust", "egui", "مكتبة-واجهة-المستخدم", "ياباني"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'نشرح كيفية تنفيذ عرض اللغة اليابانية بشكل صحيح في مكتبة واجهة المستخدم الرسومية (GUI) الخفيفة ''egui'' للغة Rust. نعرض أمثلة برمجية محددة لتحميل خط (Meiryo) في نظام Windows وتطبيقه على التطبيقات.'
---

## الحصول على مثال egui

يمكنك تشغيل مثال egui بالأوامر التالية.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## تحميل خط يدعم اليابانية

لعرض اللغة اليابانية، تحتاج إلى تحميل خط يدعمها.

في `src/app.rs`، أضف الأسطر التالية داخل طريقة `pub fn new`.

```rust
// تحميل خط يدعم اللغة اليابانية
let mut fonts = egui::FontDefinitions::default();
fonts.font_data.insert(
    "Meiryo".to_owned(),
    egui::FontData::from_static(include_bytes!("C:/Windows/Fonts/Meiryo.ttc")),
);
fonts
    .families
    .entry(egui::FontFamily::Proportional)
    .or_default()
    .insert(0, "Meiryo".to_owned());
cc.egui_ctx.set_fonts(fonts);
```

## الآن يمكنك عرض اللغة اليابانية.

![img.png](img.webp)

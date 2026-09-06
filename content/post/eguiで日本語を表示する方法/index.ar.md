---
title: "كيفية عرض اللغة اليابانية في egui"
slug: "how-to-display-japanese-in-egui-ar"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "مكتبة-واجهة-المستخدم", "ياباني"]
draft: false
image: "img.png"
categories: ["تكنولوجيا-المعلومات"]
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

![img.png](img.png)

---
title: 'How to Display Japanese in egui'
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI library", "Japanese"]
draft: false
image: "img.png"
categories: ["IT / Technology"]
---

## Get the egui sample

You can run the egui sample using the following commands:

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Load a Japanese-compatible font

To display Japanese, you need to load a Japanese-compatible font.

Add the following lines inside the `pub fn new` method in `src/app.rs`.

```rust
// Load a Japanese-compatible font
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

## Now you can display Japanese.

![img.png](img.png)

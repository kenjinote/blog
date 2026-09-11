---
title: '在Rust的GUI库“egui”中加载并显示中文字体（日语字体）的方法'
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI库", "日语"]
draft: false
image: "img.webp"
categories: ["IT与技术"]
description: '本文讲解在Rust的轻量级GUI库“egui”中正确显示日语（及中文等）的实现方法。介绍加载Windows的微软雅黑（或Meiryo）字体并应用于应用程序的具体代码示例。'
---

## 获取egui示例

可以使用以下命令运行egui的示例。

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## 加载支持日语的字体

要显示日语，必须加载支持日语的字体。

在 `src/app.rs` 中的 `pub fn new` 方法中添加以下代码行。

```rust
// 加载支持日语的字体
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

## 现在就可以显示日语了。

![img.png](img.webp)

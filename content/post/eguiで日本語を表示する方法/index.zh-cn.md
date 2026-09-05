---
title: '如何在egui中显示日语'
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI库", "日语"]
draft: false
image: "img.png"
categories: ["IT与技术"]
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

![img.png](img.png)

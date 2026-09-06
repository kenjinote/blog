---
title: "如何在 egui 中顯示日文"
slug: "how-to-display-japanese-in-egui"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI 函式庫", "日文"]
draft: false
image: "img.png"
categories: ["IT・科技"]
---

## 取得 egui 範例

您可以使用以下指令執行 egui 範例。

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## 載入支援日文的字型

要顯示日文，您必須載入支援日文的字型。

在 `src/app.rs` 中，將以下行新增至 `pub fn new` 方法內。

```rust
// 載入支援日文的字型
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

## 現在您可以顯示日文了。

![img.png](img.png)

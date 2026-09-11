---
title: '在Rust的GUI函式庫「egui」中載入並顯示日文字型的方法'
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI 函式庫", "日文"]
draft: false
image: "img.webp"
categories: ["IT・科技"]
description: '為您解說如何在Rust的輕量GUI函式庫「egui」中，正確顯示日文的實作方法。我們將介紹載入Windows的Meiryo（メイリオ）字型並應用於應用程式的具體程式碼範例。'
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

![img.png](img.webp)

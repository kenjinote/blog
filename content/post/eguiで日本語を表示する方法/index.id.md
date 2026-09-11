---
title: 'Cara Memuat dan Menampilkan Font Bahasa Jepang di Library GUI Rust ''egui'''
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "pustaka-GUI", "jepang"]
draft: false
image: "img.webp"
categories: ["Teknologi-TI"]
description: 'Menjelaskan metode implementasi untuk menampilkan bahasa Jepang dengan benar di ''egui'', library GUI yang ringan untuk Rust. Memperkenalkan sampel kode konkret untuk memuat font Meiryo Windows dan menerapkannya pada aplikasi.'
---

## Mendapatkan Contoh egui

Anda dapat menjalankan contoh egui dengan perintah berikut.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Memuat Font yang Mendukung Bahasa Jepang

Untuk menampilkan bahasa Jepang, Anda perlu memuat font yang mendukungnya.

Di `src/app.rs`, tambahkan baris berikut di dalam metode `pub fn new`.

```rust
// Memuat font yang mendukung bahasa Jepang
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

## Sekarang Anda Dapat Menampilkan Bahasa Jepang.

![img.png](img.webp)

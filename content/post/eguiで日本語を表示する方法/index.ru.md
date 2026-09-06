---
title: "Как отобразить японский язык в egui"
slug: "how-to-display-japanese-in-egui-ru"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "библиотека-GUI", "японский"]
draft: false
image: "img.png"
categories: ["IT-технологии"]
---

## Получение примера egui

Вы можете запустить пример egui с помощью следующих команд.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Загрузка шрифта с поддержкой японского языка

Чтобы отобразить японский язык, необходимо загрузить соответствующий шрифт.

В `src/app.rs` добавьте следующие строки в метод `pub fn new`.

```rust
// Загрузка шрифта с поддержкой японского языка
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

## Теперь вы можете отображать японский язык.

![img.png](img.png)

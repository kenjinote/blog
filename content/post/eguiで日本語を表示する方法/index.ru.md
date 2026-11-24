---
title: "Отображение японского текста в egui с подходящим шрифтом"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでЯпонский языкを表示する方法"
tags: ["rust", "egui", "библиотека-GUI", "японский"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Чтобы отображать японский текст в GUI-библиотеке egui для Rust, добавьте в `FontDefinitions` шрифт с японскими глифами. В этом примере используется переменный файл `.ttf` шрифта Noto Sans JP из Google Fonts. Сохраните файл шрифта в каталоге проекта `assets/fonts/`."
---
## Adding and applying a font

Чтобы отображать японский текст в GUI-библиотеке egui для Rust, добавьте в `FontDefinitions` шрифт с японскими глифами. В этом примере используется переменный файл `.ttf` шрифта Noto Sans JP из Google Fonts. Сохраните файл шрифта в каталоге проекта `assets/fonts/`.

В текущем шаблоне eframe настройте шрифты внутри `TemplateApp::new` в файле `src/app.rs`. Добавьте следующий код в этот метод. Windows-файл `Meiryo.ttc` — это коллекция TrueType, а не формат `.ttf` или `.otf`, указанный в документации `FontData` для egui, поэтому в примере он не используется.

```rust
let mut fonts = egui::FontDefinitions::default();
fonts.font_data.insert(
    "Noto Sans JP".to_owned(),
    std::sync::Arc::new(egui::FontData::from_static(include_bytes!(
        "../assets/fonts/NotoSansJP[wght].ttf"
    ))),
);
fonts
    .families
    .entry(egui::FontFamily::Proportional)
    .or_default()
    .insert(0, "Noto Sans JP".to_owned());
cc.egui_ctx.set_fonts(fonts);
```

Noto Sans JP распространяется по лицензии SIL Open Font License. При распространении шрифта вместе с приложением включите файл лицензии и соблюдайте её условия.

## Источники

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

---
title: "Japanisch in egui mit einer passenden Schrift anzeigen"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでJapanischを表示する方法"
tags: ["rust", "egui", "GUI-Bibliothek", "Japanisch"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Um Japanisch in der Rust-GUI-Bibliothek egui darzustellen, fügen Sie `FontDefinitions` eine Schriftart mit japanischen Glyphen hinzu. Dieses Beispiel verwendet die variable `.ttf`-Datei von Noto Sans JP aus Google Fonts. Speichern Sie die Schriftdatei im Projektordner `assets/fonts/`."
---
## Adding and applying a font

Um Japanisch in der Rust-GUI-Bibliothek egui darzustellen, fügen Sie `FontDefinitions` eine Schriftart mit japanischen Glyphen hinzu. Dieses Beispiel verwendet die variable `.ttf`-Datei von Noto Sans JP aus Google Fonts. Speichern Sie die Schriftdatei im Projektordner `assets/fonts/`.

In der aktuellen eframe-Vorlage richten Sie Schriftarten in `TemplateApp::new` in `src/app.rs` ein. Fügen Sie den folgenden Code in diese Methode ein. Windows-`Meiryo.ttc` ist eine TrueType Collection und nicht das von eguis `FontData` dokumentierte `.ttf`- oder `.otf`-Format; daher wird es in diesem Beispiel nicht verwendet.

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

Noto Sans JP wird unter der SIL Open Font License verbreitet. Wenn Sie die Schriftart mit Ihrer Anwendung weitergeben, fügen Sie die Lizenzdatei bei und halten Sie deren Bedingungen ein.

## Referenzen

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

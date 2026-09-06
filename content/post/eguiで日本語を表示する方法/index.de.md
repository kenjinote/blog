---
title: "Wie man Japanisch in egui anzeigt"
slug: "wie-man-japanisch-in-egui-anzeigt"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "GUI-Bibliothek", "Japanisch"]
draft: false
image: "img.png"
categories: ["IT und Technologie"]
---

## Holen Sie sich das egui Beispiel

Sie können das egui-Beispiel mit dem folgenden Befehl ausführen.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Laden Sie eine japanisch-kompatible Schriftart

Um Japanisch anzuzeigen, müssen Sie eine Schriftart laden, die die japanische Sprache unterstützt.

Fügen Sie in `src/app.rs` die folgenden Zeilen in die Methode `pub fn new` ein.

```rust
// Laden Sie eine japanisch-kompatible Schriftart
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

## Jetzt können Sie Japanisch anzeigen.

![img.png](img.png)

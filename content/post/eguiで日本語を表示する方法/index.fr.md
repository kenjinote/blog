---
title: "Comment afficher du japonais dans egui"
slug: "comment-afficher-japonais-egui"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "Bibliothèque GUI", "Japonais"]
draft: false
image: "img.png"
categories: ["Informatique et Technologie"]
---

## Obtenir l'exemple egui

Vous pouvez exécuter l'exemple egui avec la commande suivante.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Charger une police compatible avec le japonais

Pour afficher du japonais, vous devez charger une police qui le prend en charge.

Dans `src/app.rs`, ajoutez les lignes suivantes à l'intérieur de la méthode `pub fn new`.

```rust
// Charger une police compatible avec le japonais
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

## Vous pouvez maintenant afficher du japonais.

![img.png](img.png)

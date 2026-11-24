---
title: "Afficher le japonais dans egui avec une police adaptée"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでJaponaisを表示する方法"
tags: ["rust", "egui", "Bibliothèque GUI", "Japonais"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Pour afficher le japonais dans la bibliothèque graphique Rust egui, ajoutez à `FontDefinitions` une police contenant les glyphes japonais. Cet exemple utilise le fichier `.ttf` variable de Noto Sans JP distribué par Google Fonts. Enregistrez ce fichier dans le dossier `assets/fonts/` du projet."
---
## Adding and applying a font

Pour afficher le japonais dans la bibliothèque graphique Rust egui, ajoutez à `FontDefinitions` une police contenant les glyphes japonais. Cet exemple utilise le fichier `.ttf` variable de Noto Sans JP distribué par Google Fonts. Enregistrez ce fichier dans le dossier `assets/fonts/` du projet.

Dans le modèle eframe actuel, configurez les polices dans `TemplateApp::new`, dans `src/app.rs`. Ajoutez le code ci-dessous à cette méthode. `Meiryo.ttc` sous Windows est une collection TrueType, et non le format `.ttf` ou `.otf` documenté pour `FontData` d’egui ; cet exemple ne l’utilise donc pas.

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

Noto Sans JP est distribué sous la SIL Open Font License. Si vous redistribuez la police avec votre application, joignez le fichier de licence et respectez ses conditions.

## Références

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

---
title: "Mostrar japonés en egui con una fuente compatible"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでJaponésを表示する方法"
tags: ["rust", "egui", "biblioteca GUI", "japonés"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Para mostrar japonés en la biblioteca GUI egui para Rust, añade a `FontDefinitions` una fuente que contenga glifos japoneses. Este ejemplo usa el archivo `.ttf` variable de Noto Sans JP distribuido por Google Fonts. Guarda el archivo de fuente en `assets/fonts/` dentro del proyecto."
---
## Adding and applying a font

Para mostrar japonés en la biblioteca GUI egui para Rust, añade a `FontDefinitions` una fuente que contenga glifos japoneses. Este ejemplo usa el archivo `.ttf` variable de Noto Sans JP distribuido por Google Fonts. Guarda el archivo de fuente en `assets/fonts/` dentro del proyecto.

En la plantilla actual de eframe, configura las fuentes dentro de `TemplateApp::new`, en `src/app.rs`. Añade el código siguiente dentro de ese método. `Meiryo.ttc` de Windows es una colección TrueType, no el formato `.ttf` u `.otf` indicado por `FontData` de egui; por eso este ejemplo no lo utiliza.

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

Noto Sans JP se distribuye con la SIL Open Font License. Si redistribuyes la fuente con tu aplicación, incluye el archivo de licencia y respeta sus condiciones.

## Referencias

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

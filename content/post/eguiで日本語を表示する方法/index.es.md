---


title: "Cómo mostrar japonés en egui"
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "biblioteca GUI", "japonés"]
draft: false
image: "img.png"
categories: ["TI y Tecnología"]
---



## Obtener el ejemplo de egui

Puedes ejecutar el ejemplo de egui con los siguientes comandos.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Cargar una fuente compatible con japonés

Para mostrar japonés, es necesario cargar una fuente compatible con este idioma.

En `src/app.rs`, dentro del método `pub fn new`, añade las siguientes líneas:

```rust
// Cargar fuente compatible con japonés
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

## Ahora podrás mostrar texto en japonés.

![img.png](img.png)

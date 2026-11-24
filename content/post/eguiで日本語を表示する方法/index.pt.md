---
title: "Exibir japonês no egui com uma fonte compatível"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでJaponêsを表示する方法"
tags: ["rust", "egui", "Biblioteca GUI", "Japonês"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Para exibir japonês na biblioteca GUI egui para Rust, adicione a `FontDefinitions` uma fonte que contenha glifos japoneses. Este exemplo usa o arquivo `.ttf` variável do Noto Sans JP distribuído pelo Google Fonts. Salve o arquivo de fonte na pasta `assets/fonts/` do projeto."
---
## Adding and applying a font

Para exibir japonês na biblioteca GUI egui para Rust, adicione a `FontDefinitions` uma fonte que contenha glifos japoneses. Este exemplo usa o arquivo `.ttf` variável do Noto Sans JP distribuído pelo Google Fonts. Salve o arquivo de fonte na pasta `assets/fonts/` do projeto.

No modelo atual do eframe, configure as fontes dentro de `TemplateApp::new`, em `src/app.rs`. Adicione o código a seguir dentro desse método. O `Meiryo.ttc` do Windows é uma coleção TrueType, e não o formato `.ttf` ou `.otf` documentado por `FontData` do egui; por isso, este exemplo não o utiliza.

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

O Noto Sans JP é distribuído sob a SIL Open Font License. Se redistribuir a fonte com seu aplicativo, inclua o arquivo de licença e cumpra seus termos.

## Referências

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

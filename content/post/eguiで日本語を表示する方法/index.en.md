---
title: "Display Japanese Text in egui with a Japanese Font"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでJapaneseを表示する方法"
tags: ["rust", "egui", "GUI library", "Japanese"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "To display Japanese in the Rust GUI library egui, add a font containing Japanese glyphs to `FontDefinitions`. This example uses the variable `.ttf` file for Noto Sans JP distributed through Google Fonts. Save the font file in your project’s `assets/fonts/` directory."
---
## Adding and applying the font

To display Japanese in the Rust GUI library egui, add a font containing Japanese glyphs to `FontDefinitions`. This example uses the variable `.ttf` file for Noto Sans JP distributed through Google Fonts. Save the font file in your project’s `assets/fonts/` directory.

In the current eframe template, configure fonts inside `TemplateApp::new` in `src/app.rs`. Add the following code inside that method. Windows `Meiryo.ttc` is a TrueType Collection, not the `.ttf` or `.otf` format documented by egui’s `FontData`, so this example does not use it.

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

Noto Sans JP is distributed under the SIL Open Font License. If you redistribute the font with your application, include the license file and follow its terms.

## References

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

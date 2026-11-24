---
title: "在 egui 中显示日文：配置日文字体"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiで日语を表示する方法"
tags: ["rust", "egui", "GUI库", "日语"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "要在 Rust GUI 库 egui 中显示日语，需要把包含日语字形的字体加入 `FontDefinitions`。本例使用 Google Fonts 提供的 Noto Sans JP 可变 `.ttf` 文件。请将字体文件保存到项目的 `assets/fonts/` 目录。"
---
## Adding and applying a font

要在 Rust GUI 库 egui 中显示日语，需要把包含日语字形的字体加入 `FontDefinitions`。本例使用 Google Fonts 提供的 Noto Sans JP 可变 `.ttf` 文件。请将字体文件保存到项目的 `assets/fonts/` 目录。

在当前 eframe 模板中，应在 `src/app.rs` 的 `TemplateApp::new` 内设置字体。请将以下代码加入该方法。Windows 的 `Meiryo.ttc` 是 TrueType Collection 格式，并非 egui `FontData` 文档所列的 `.ttf` 或 `.otf` 格式，因此本例不使用它。

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

Noto Sans JP 使用 SIL Open Font License 许可。若随应用重新分发字体，请附上许可文件并遵守其条款。

## 参考资料

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

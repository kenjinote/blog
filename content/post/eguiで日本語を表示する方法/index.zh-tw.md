---
title: "在 egui 顯示日文：設定日文字型"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiで日語を表示する方法"
tags: ["rust", "egui", "GUI 函式庫", "日文"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "若要在 Rust GUI 函式庫 egui 中顯示日文，請將包含日文字形的字型加入 `FontDefinitions`。本範例使用 Google Fonts 提供的 Noto Sans JP 可變 `.ttf` 檔案。請將字型檔存入專案的 `assets/fonts/` 目錄。"
---
## Adding and applying a font

若要在 Rust GUI 函式庫 egui 中顯示日文，請將包含日文字形的字型加入 `FontDefinitions`。本範例使用 Google Fonts 提供的 Noto Sans JP 可變 `.ttf` 檔案。請將字型檔存入專案的 `assets/fonts/` 目錄。

在目前的 eframe 範本中，請於 `src/app.rs` 的 `TemplateApp::new` 內設定字型。將以下程式碼加入該方法。Windows 的 `Meiryo.ttc` 是 TrueType Collection 格式，並非 egui `FontData` 文件所列的 `.ttf` 或 `.otf` 格式，因此本範例不使用它。

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

Noto Sans JP 採用 SIL Open Font License 授權。若隨應用程式重新散布字型，請附上授權檔並遵守其條款。

## 參考資料

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

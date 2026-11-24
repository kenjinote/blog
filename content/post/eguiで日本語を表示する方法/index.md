---
title: "eguiで日本語を表示する：日本語対応フォントの設定"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiで日本語を表示する方法"
tags: ["rust", "egui", "GUIライブラリ", "日本語"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "RustのGUIライブラリeguiで日本語を表示するには、日本語グリフを含むフォントを`FontDefinitions`に追加します。ここでは、Google Fontsで配布されるNoto Sans JPの可変`.ttf`ファイルを使います。フォントファイルをプロジェクトの`assets/fonts/`に保存してください。"
---
## フォントの追加と適用

RustのGUIライブラリeguiで日本語を表示するには、日本語グリフを含むフォントを`FontDefinitions`に追加します。ここでは、Google Fontsで配布されるNoto Sans JPの可変`.ttf`ファイルを使います。フォントファイルをプロジェクトの`assets/fonts/`に保存してください。

現行のeframeテンプレートでは、`src/app.rs`の`TemplateApp::new`内でフォントを設定します。次のコードはそのメソッド内に追加してください。Windowsの`Meiryo.ttc`はTrueType Collection形式で、eguiの`FontData`が案内する`.ttf`／`.otf`形式ではないため、この例では使用しません。

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

Noto Sans JPはSIL Open Font Licenseで配布されています。アプリに同梱して再配布する場合は、ライセンスファイルを含め、条件に従ってください。

## 参考資料

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

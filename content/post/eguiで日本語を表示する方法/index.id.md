---
title: "Menampilkan teks Jepang di egui dengan font yang sesuai"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでBahasa Jepangを表示する方法"
tags: ["rust", "egui", "pustaka-GUI", "jepang"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Untuk menampilkan bahasa Jepang di pustaka GUI Rust egui, tambahkan font yang berisi glif bahasa Jepang ke `FontDefinitions`. Contoh ini menggunakan berkas `.ttf` variabel Noto Sans JP dari Google Fonts. Simpan berkas font di direktori proyek `assets/fonts/`."
---
## Adding and applying a font

Untuk menampilkan bahasa Jepang di pustaka GUI Rust egui, tambahkan font yang berisi glif bahasa Jepang ke `FontDefinitions`. Contoh ini menggunakan berkas `.ttf` variabel Noto Sans JP dari Google Fonts. Simpan berkas font di direktori proyek `assets/fonts/`.

Pada templat eframe saat ini, atur font di dalam `TemplateApp::new` pada `src/app.rs`. Tambahkan kode berikut di dalam metode tersebut. `Meiryo.ttc` pada Windows adalah TrueType Collection, bukan format `.ttf` atau `.otf` yang didokumentasikan untuk `FontData` egui; karena itu contoh ini tidak menggunakannya.

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

Noto Sans JP didistribusikan berdasarkan SIL Open Font License. Jika mendistribusikan ulang font bersama aplikasi, sertakan berkas lisensi dan patuhi ketentuannya.

## Referensi

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

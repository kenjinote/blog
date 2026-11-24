---
title: "عرض اليابانية في egui بخط يدعمها"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでاللغة اليابانيةを表示する方法"
tags: ["rust", "egui", "مكتبة-واجهة-المستخدم", "ياباني"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "لعرض اليابانية في مكتبة واجهة المستخدم الرسومية egui للغة Rust، أضف إلى `FontDefinitions` خطًا يتضمن محارف يابانية. يستخدم هذا المثال ملف `.ttf` متغيرًا لخط Noto Sans JP الموزع عبر Google Fonts. احفظ ملف الخط داخل مجلد `assets/fonts/` في المشروع."
---
## Adding and applying a font

لعرض اليابانية في مكتبة واجهة المستخدم الرسومية egui للغة Rust، أضف إلى `FontDefinitions` خطًا يتضمن محارف يابانية. يستخدم هذا المثال ملف `.ttf` متغيرًا لخط Noto Sans JP الموزع عبر Google Fonts. احفظ ملف الخط داخل مجلد `assets/fonts/` في المشروع.

في قالب eframe الحالي، اضبط الخطوط داخل `TemplateApp::new` في `src/app.rs`. أضف الكود التالي داخل هذه الطريقة. ملف Windows `Meiryo.ttc` عبارة عن مجموعة TrueType وليس بصيغة `.ttf` أو `.otf` الموضحة في `FontData` الخاصة بـ egui، لذلك لا يستخدمه هذا المثال.

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

يُوزّع Noto Sans JP بموجب SIL Open Font License. عند إعادة توزيع الخط مع التطبيق، أرفق ملف الترخيص والتزم بشروطه.

## مراجع

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

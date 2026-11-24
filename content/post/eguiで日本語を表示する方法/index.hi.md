---
title: "egui में जापानी दिखाएँ: जापानी समर्थित फ़ॉन्ट सेट करें"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiでजापानीを表示する方法"
tags: ["rust", "egui", "GUI लाइब्रेरी", "जापानी"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Rust GUI लाइब्रेरी egui में जापानी दिखाने के लिए `FontDefinitions` में जापानी ग्लिफ़ वाली फ़ॉन्ट जोड़ें। इस उदाहरण में Google Fonts से मिलने वाली Noto Sans JP की variable `.ttf` फ़ाइल उपयोग की गई है। फ़ॉन्ट फ़ाइल को प्रोजेक्ट की `assets/fonts/` निर्देशिका में रखें।"
---
## Adding and applying a font

Rust GUI लाइब्रेरी egui में जापानी दिखाने के लिए `FontDefinitions` में जापानी ग्लिफ़ वाली फ़ॉन्ट जोड़ें। इस उदाहरण में Google Fonts से मिलने वाली Noto Sans JP की variable `.ttf` फ़ाइल उपयोग की गई है। फ़ॉन्ट फ़ाइल को प्रोजेक्ट की `assets/fonts/` निर्देशिका में रखें।

वर्तमान eframe टेम्पलेट में `src/app.rs` के `TemplateApp::new` के भीतर फ़ॉन्ट सेट करें। नीचे दिया कोड उस मेथड में जोड़ें। Windows का `Meiryo.ttc` TrueType Collection है, egui `FontData` में बताए गए `.ttf` या `.otf` फ़ॉर्मैट में नहीं; इसलिए इस उदाहरण में इसका उपयोग नहीं किया गया है।

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

Noto Sans JP, SIL Open Font License के अंतर्गत वितरित है। ऐप के साथ फ़ॉन्ट को फिर से वितरित करते समय लाइसेंस फ़ाइल शामिल करें और उसकी शर्तों का पालन करें।

## संदर्भ

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

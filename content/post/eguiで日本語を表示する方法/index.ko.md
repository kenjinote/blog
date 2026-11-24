---
title: "egui에서 일본어 표시하기: 일본어 지원 폰트 설정"
date: 2023-04-01T03:17:52+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "eguiで일본어を表示する方法"
tags: ["rsut", "egui", "GUI 라이브러리", "일본어"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Rust GUI 라이브러리 egui에서 일본어를 표시하려면 일본어 글리프가 포함된 폰트를 `FontDefinitions`에 추가해야 합니다. 이 예제에서는 Google Fonts에서 배포하는 Noto Sans JP 가변 `.ttf` 파일을 사용합니다. 폰트 파일을 프로젝트의 `assets/fonts/` 디렉터리에 저장하세요."
---
## Adding and applying a font

Rust GUI 라이브러리 egui에서 일본어를 표시하려면 일본어 글리프가 포함된 폰트를 `FontDefinitions`에 추가해야 합니다. 이 예제에서는 Google Fonts에서 배포하는 Noto Sans JP 가변 `.ttf` 파일을 사용합니다. 폰트 파일을 프로젝트의 `assets/fonts/` 디렉터리에 저장하세요.

현재 eframe 템플릿에서는 `src/app.rs`의 `TemplateApp::new` 안에서 폰트를 설정합니다. 다음 코드를 해당 메서드 안에 추가하세요. Windows의 `Meiryo.ttc`는 TrueType Collection이며 egui `FontData` 문서에 안내된 `.ttf` 또는 `.otf` 형식이 아니므로 이 예제에서는 사용하지 않습니다.

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

Noto Sans JP는 SIL Open Font License로 배포됩니다. 앱과 함께 폰트를 재배포할 때는 라이선스 파일을 포함하고 조건을 준수하세요.

## 참고 자료

- [eframe template](https://github.com/emilk/eframe_template)
- [egui FontDefinitions](https://docs.rs/egui/latest/egui/text/struct.FontDefinitions.html)
- [egui FontData](https://docs.rs/egui/latest/egui/struct.FontData.html)
- [Noto Sans JP font and license](https://github.com/google/fonts/tree/main/ofl/notosansjp)
- [SIL Open Font License](https://github.com/google/fonts/blob/main/ofl/notosansjp/OFL.txt)

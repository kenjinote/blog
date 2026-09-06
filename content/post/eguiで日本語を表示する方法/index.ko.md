---



title: "'egui에서 일본어를 표시하는 방법'"
date: 2023-04-01T03:17:52+09:00
tags: ["rsut", "egui", "GUI 라이브러리", "일본어"]
draft: false
image: "img.png"
categories: ["IT・테크놀로지"]
---




## egui 샘플 가져오기

아래 명령어로 egui 샘플을 실행할 수 있습니다.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## 일본어 지원 폰트 불러오기

일본어를 표시하려면 일본어 지원 폰트를 불러와야 합니다.

`src/app.rs`의 `pub fn new` 메서드 안에 다음 줄을 추가합니다.

```rust
// 일본어 지원 폰트 불러오기
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

## 이제 일본어를 표시할 수 있습니다.

![img.png](img.png)

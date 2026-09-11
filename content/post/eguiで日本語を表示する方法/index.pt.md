---
title: 'Como Carregar e Exibir Fontes em Japonês na Biblioteca GUI ''egui'' do Rust'
slug: "eguiで日本語を表示する方法"
date: 2023-04-01T03:17:52+09:00
tags: ["rust", "egui", "Biblioteca GUI", "Japonês"]
draft: false
image: "img.webp"
categories: ["TI e Tecnologia"]
description: 'Explicamos a implementação para exibir o idioma japonês corretamente na biblioteca leve de GUI para Rust, ''egui''. Mostramos exemplos práticos de código para carregar a fonte Meiryo do Windows e aplicá-la em sua aplicação.'
---

## Obtenha a amostra do egui

Você pode executar a amostra do egui com o seguinte comando.

```
git clone https://github.com/emilk/eframe_template/ egui_test
cd egui_test
cargo run
```

## Carregue uma fonte compatível com japonês

Para exibir texto em japonês, você deve carregar uma fonte que suporte o idioma japonês.

No arquivo `src/app.rs`, adicione as seguintes linhas dentro do método `pub fn new`.

```rust
// Carregar a fonte compatível com japonês
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

## Agora você pode exibir japonês.

![img.png](img.webp)

---
title: 'Как изменить цветовую схему и тему в теме Hugo PaperMod с помощью CSS'
slug: "PaperModの配色変更"
date: 2022-09-07T15:30:21+09:00
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["Управление блогом"]
description: 'Объясняется, как настроить общую цветовую палитру в теме Hugo PaperMod. Представлены конкретные примеры настройки переменных в CSS (blank.css), включающем определения стилей для цвета фона, цвета текста, блоков кода и т.д., для применения желаемой цветовой схемы.'
---
Я изменил цветовую схему темы PaperMod. Способ изменения описан ниже.

https://github.com/adityatelange/hugo-PaperMod/discussions/645

Путь к CSS следующий:

`themes/PaperMod/assets/css/extended/blank.css`

```
:root {
    --entry: #fbf7ef;
    --primary: rgba(113, 103, 91, 1.00);
    --secondary: rgba(113, 103, 91, 0.95);
    --tertiary: rgba(113, 103, 91, 0.50);
    --content: rgba(113, 103, 91, 0.85);
    --hljs-bg: #34231B;
    --code-bg: #ebe4d7;
    --border: #fdfaf5;
    --theme: #fbf7ef;
}
.dark {
}
```

Темная тема пока без изменений.

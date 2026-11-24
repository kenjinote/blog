---
title: "Настройка цветов Hugo PaperMod с помощью CSS-переменных"
slug: "PaperModの配色変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Переопределите переменные цвета PaperMod для светлой и тёмной тем с помощью расширенного CSS и проверьте контраст текста."
date: "2022-09-07T15:30:21+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Цвета PaperMod настраиваются через пользовательские CSS-свойства (переменные). Разместите переопределения в `assets/css/extended/` сайта, а не редактируйте файлы темы — так изменения проще сохранить при обновлении. В примере заданы тёплая светлая и тёмная палитры; адаптируйте значения под свой сайт.

## Тёмный режим и актуальные переменные

Текущая PaperMod переключает тёмный режим, устанавливая `data-theme="dark"` на элементе `html`. Старые примеры, нацеленные только на `.dark`, могут не соответствовать этому селектору. Кроме того, `--hljs-bg` больше не является переменной фона блока кода; актуальное имя — `--code-block-bg`.

```css
/* Save as assets/css/extended/theme-colors.css */
:root {
    color-scheme: light;
    --theme: #fbf7ef;
    --entry: #fffdfa;
    --primary: #433a32;
    --secondary: #665b50;
    --tertiary: #8b7f72;
    --content: #453d35;
    --code-block-bg: #34231b;
    --code-bg: #efe7da;
    --border: #ddd3c5;
}

:root[data-theme="dark"] {
    color-scheme: dark;
    --theme: #1d1e20;
    --entry: #22252a;
    --primary: #e8e6e1;
    --secondary: #b5b2ac;
    --tertiary: #55575c;
    --content: #d2d0ca;
    --code-block-bg: #17181a;
    --code-bg: #37383e;
    --border: #48484c;
}
```

## Контраст текста

В примере обычные цвета текста `--primary` и `--content` хорошо контрастируют с фоном. Контраст `--primary` относительно `--theme` составляет около 10,4:1 в светлом режиме и 13,4:1 в тёмном. WCAG 2.2 AA требует 4,5:1 для обычного текста; отдельно проверьте цвета подсветки синтаксиса, ссылок, границ и другие состояния.

## Добавление и проверка расширенного CSS

Сохраните таблицу стилей как `assets/css/extended/theme-colors.css` в корне сайта. FAQ PaperMod указывает, что CSS из `assets/css/extended/` объединяется со стилями темы. Запустите Hugo и проверьте переключатель светлой/тёмной темы, карточки, текст, встроенный код, блоки кода и ссылки.

## Область применения

Эта палитра служит примером и не гарантирует доступность каждого текста, изображения или интерактивного элемента. Цвета подсветки синтаксиса определяются отдельно от `--code-block-bg`; после смены фона блока снова проверьте читаемость кода.

## Источники

- [PaperMod FAQ: custom CSS and theme assets](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current theme color variables](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/core/theme-vars.css)
- [PaperMod discussion: changing background and text colors](https://github.com/adityatelange/hugo-PaperMod/discussions/645)
- [W3C: WCAG 2.2 contrast minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum)

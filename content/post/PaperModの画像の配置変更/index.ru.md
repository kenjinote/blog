---
title: "Изменение размера и положения обложек в списках PaperMod"
slug: "PaperModのИзображениеの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Используйте расширенный CSS PaperMod и CSS Grid, чтобы уменьшить обложки карточек и разместить их рядом с кратким описанием."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

В этом примере обложки карточек в списках PaperMod уменьшаются и размещаются под заголовком рядом с кратким описанием. Используется расширенный CSS сайта, без редактирования файлов стилей и шаблонов темы. Селекторы зависят от классов PaperMod, поэтому проверяйте результат в браузере после обновления темы.

## Добавление расширенного CSS

Создайте `assets/css/extended/custom.css` в корне сайта. PaperMod подключает CSS из этого каталога вместе со стилями темы. CSS Grid меняет визуальное расположение, не меняя существующую HTML-структуру.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Адаптация для узких экранов

На узких экранах уменьшите ширину колонки и промежуток, чтобы описание оставалось читаемым. Подстройте 150 px и контрольную точку под свой дизайн. `height: auto` сохраняет пропорции изображения. Добавляйте `aspect-ratio` и `object-fit: cover`, только если нужно обрезать все изображения до одинаковой формы.

## Не редактируйте файлы темы напрямую

В документации PaperMod `blank.css` описан как файл-заполнитель, используемый, когда каталог расширенного CSS пуст. Не нужно менять `post-entry.css` темы или удалять закомментированную строку `/* width: 100%; */`: удаление CSS-комментария не меняет стиль. Если требуется изменить саму HTML-структуру, скопируйте шаблон в `layouts/` сайта и переопределите его, но поддерживайте эту копию при обновлении темы.

## Проверка макета

Запустите Hugo и проверьте списки главной страницы, тегов и категорий на широком и узком экранах. Изображение, заголовок, описание и метаданные не должны перекрываться; ссылка на всю карточку должна работать. Если обновление темы изменило классы или HTML, скорректируйте CSS. Пример меняет обложки в списках, но не изображения внутри статей.

## Источники

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

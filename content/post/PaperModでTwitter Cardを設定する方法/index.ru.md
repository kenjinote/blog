---
title: "Как настроить Twitter Card в PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
date: 2022-09-10T18:41:22+09:00
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.png"
categories: ["Управление блогом"]
---
# Введение
Тема PaperMod поддерживает Twitter Card.
Однако настройки Twitter Card должны быть прописаны в `config.toml` или в заголовке `*.md` каждой статьи.
Если они заданы как в каждой статье, так и в `config.toml`, приоритет будет иметь заголовок каждой статьи.

# Способ настройки
## config.toml
В `config.toml` добавьте элемент с именем `images` в разделе `[params]`.
В `images` укажите путь к изображению, которое будет отображаться в Twitter Card.
Если вы размещаете изображение в папке `static`, достаточно указать только имя файла.

```
[params]
  images = ["twitter_card.jpg"]
```

Структура папок
```
root
│  config.toml (писать здесь)
├─content
│  └─posts
│      └─папка статьи
│         │  index.md (писать здесь)
│         └─images
│             cover.png (поместить здесь)
└─static
    twitter_card.jpg (поместить здесь)
```

## Информация в заголовке каждой статьи
В информацию в заголовке каждой статьи добавьте элемент с именем `image` в разделе `cover`.
Если установить `relative` в `true`, можно указать относительный путь от `*.md` статьи.

```
cover:
  image: "images/cover.jpg"
  relative: true
```

### Если вы не хотите отображать её в верхней части статьи
Если вы не хотите отображать обложку в верхней части статьи, добавьте элемент с именем `hidden` в разделе `cover` и установите его в `true`.
```
cover:
  image: "images/cover.jpg"
  relative: true
  hidden: true
```

# О размере изображения

Согласно текущей спецификации PaperMod, размер Twitter Card, по-видимому, поддерживает только `summary_large_image`.
Подходящий размер (разрешение) для `summary_large_image` варьируется, но кажется, что около `800 x 418` (соотношение сторон 1.91:1) является оптимальным.

[Справочный сайт 1](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image)
[Справочный сайт 2](https://developers.facebook.com/docs/sharing/best-practices)

Если возможно, мы рекомендуем изменить размер изображения перед публикацией.

# Как проверить настройки
Чтобы проверить настройки Twitter Card, используйте [Twitter Card Validator](https://cards-dev.twitter.com/validator).
Однако в моей среде предварительный просмотр отображался некорректно, поэтому, если предварительный просмотр не отображается, мы рекомендуем проверить его один раз перед публикацией, используя закрытый аккаунт и т. д.

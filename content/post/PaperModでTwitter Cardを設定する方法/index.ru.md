---
title: "Настройка Twitter Cards (X Cards) в Hugo PaperMod"
slug: "PaperModでTwitter Cardを設定する方法"
tags: ["HUGO", "PaperMod", "Twitter"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Настройте изображения карточек X по документации PaperMod и проверьте сгенерированный HTML и предпросмотр в редакторе публикаций X."
date: "2022-09-10T18:41:22+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PaperMod может создавать метаданные Open Graph и Twitter Card. Результат зависит от версии темы и пользовательских шаблонов, поэтому проверяйте опубликованный HTML, а не полагайтесь на пример настройки.

## Настройка всего сайта

SEO-метаданные PaperMod включаются при сборке для production. Установите для среды сайта значение production.

```toml
[params]
  env = "production"
```

Для изображения по умолчанию на всём сайте поместите файл в `static` и укажите его здесь. Оно может использоваться, если у статьи нет собственного изображения. Проверьте URL на опубликованном сайте.

```toml
[params]
  images = ["/twitter-card-1200x630.webp"]
```

## Изображение для статьи

Чтобы задать изображение для конкретной статьи, укажите в `cover.image` файл из Page Bundle. `relative: true` задаёт путь относительно bundle. Документация PaperMod отдаёт приоритет обложке; если её нет, могут использоваться список `images` страницы и подходящие изображения bundle.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
```

## Скрыть обложку в статье

Согласно справочнику переменных PaperMod, `cover.hidden: true` скрывает обложку в статье, сохраняя её в структурированных метаданных. Это удобно, если изображение нужно только для соцсетей. При fork темы или переопределённых шаблонах проверяйте итоговый HTML.

```yaml
cover:
  image: "images/cover.webp"
  alt: "Describe the image briefly"
  relative: true
  hidden: true
```

## Тип карточки и размер изображения

Старые утверждения, что PaperMod поддерживает только `summary_large_image` и что размер 800×418 фиксирован, нельзя обобщать. Тип карточки зависит от версии темы и шаблонов сайта. Для широкого изображения 1200×630 (примерно 1,90:1) — практический ориентир дизайна, но не гарантия требований X.

## Проверка HTML и предпросмотра

Соберите сайт с production-настройкой и проверьте в HTML статьи `twitter:card`, `twitter:image`, `og:image`, заголовок и описание. Изображение должно быть общедоступно напрямую по HTTPS без входа в систему. В 2022 году X убрала предпросмотр из Card Validator и рекомендовала редактор публикаций. Вставьте туда ссылку и проверьте карточку, не публикуя запись. Кэш может обновляться с задержкой.

Проверено 24.11.2026 по указанным материалам PaperMod и форуму разработчиков X. Fork, переопределение шаблонов и изменения X могут повлиять на результат.

## Источники

- [PaperMod: Features and Twitter Cards](https://github.com/adityatelange/hugo-PaperMod/wiki/Features)
- [PaperMod: Variables](https://github.com/adityatelange/hugo-PaperMod/wiki/Variables)
- [Hugo: Page bundles](https://gohugo.io/content-management/page-bundles/)
- [X Developer Community: Card Validator preview removal](https://devcommunity.x.com/t/card-validator-preview-removal/175006)

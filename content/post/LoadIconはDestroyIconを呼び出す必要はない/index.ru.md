---
title: 'Почему для иконок, полученных функцией LoadIcon, не требуется вызов DestroyIcon'
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["иконка", "LoadIcon", "DestroyIcon", "программирование Windows"]
draft: false
categories: ["programming"]
description: 'Необходимость вызова DestroyIcon зависит от того, является ли ресурс общим или принадлежит вызывающему коду. В руководстве описано владение для LoadIcon, LoadImage и CopyIcon, а также отмечено противоречие в документации Microsoft для некоторых API создания значков.'
image: eyecatch.jpg
---

# Владение дескриптором значка

Нужно ли вызывать `DestroyIcon`, зависит от того, является ли значок общим ресурсом или принадлежит вызывающему коду и должен быть освобожден им. Уничтожение общего значка может повлиять на другой код, использующий тот же ресурс.

## Когда не следует вызывать DestroyIcon

- Значок, возвращенный `LoadIcon`, является общим. Не уничтожайте его с помощью `DestroyIcon`. `LoadIcon` загружает значок стандартного системного размера; если нужно задать размер, используйте `LoadImage`.
- Если передать `LR_SHARED` в `LoadImage`, дескриптор будет общим. Не вызывайте `DestroyIcon`. Не используйте `LR_SHARED` для изображений из файлов или нестандартного размера.
- `CopyImage` может вернуть исходный дескриптор, если указан `LR_COPYRETURNORG`, а входной `hImage` — общий значок. Такой дескриптор также нельзя уничтожать.

## Когда нужно вызывать DestroyIcon

После использования освободите принадлежащие вызывающему коду значки с помощью `DestroyIcon`. Microsoft приводит такие примеры:

- `CreateIconFromResourceEx` без `LR_SHARED`
- `CreateIconIndirect`
- `CopyIcon`, возвращающий дескриптор копии значка
- Значок, загруженный через `LoadImage` без `LR_SHARED`

## Примечание о CreateIconFromResource

В общей документации Microsoft для `DestroyIcon` функция `CreateIconFromResource` указана как источник общих значков, но страницы отдельных функций советуют вызывать `DestroyIcon`. Страницы `CreateIconFromResource` и `CreateIconFromResourceEx` также содержат внутренние противоречия об использовании `LR_SHARED` и освобождении возвращенного дескриптора. Для этих API не определяйте владение только по общему правилу; проверяйте актуальную документацию конкретной функции. Это противоречие не относится к поведению общих дескрипторов `LoadIcon`.

Значок, передаваемый в `DestroyIcon`, не должен использоваться. Проверьте, является ли дескриптор общим и загружен ли еще исходный модуль.

## Ссылки

- [DestroyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-destroyicon)
- [LoadIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadiconw)
- [LoadImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadimagew)
- [CopyIcon](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyicon)
- [CopyImage](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-copyimage)
- [CreateIconFromResource](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresource)
- [CreateIconFromResourceEx](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-createiconfromresourceex)

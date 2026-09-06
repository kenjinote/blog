---
title: "LoadIcon не требует вызова DestroyIcon"
slug: "LoadIconはDestroyIconを呼び出す必要はない"
date: 2024-04-19T01:55:17+09:00
tags: ["иконка", "LoadIcon", "DestroyIcon", "программирование Windows"]
draft: false
categories: ["Программирование"]
---

# О необходимости вызова DestroyIcon

Вызывать DestroyIcon необходимо в следующих случаях:
 
- CreateIconFromResourceEx (если вызвано без флага LR_SHARED)
- CreateIconIndirect 
- CopyIcon

При создании с помощью указанных выше функций.

- LoadIcon
- LoadImage (при использовании флага LR_SHARED)
- CopyImage (при использовании флага LR_COPYRETURNORG, если параметр hImage — общая иконка)
- CreateIconFromResource
- CreateIconFromResourceEx (при использовании флага LR_SHARED)

Иконки, созданные и загруженные в перечисленных выше случаях, не должны вызывать DestroyIcon.

### Ссылки
- [Функция DestroyIcon (winuser.h)](https://learn.microsoft.com/ja-JP/windows/win32/api/winuser/nf-winuser-destroyicon)

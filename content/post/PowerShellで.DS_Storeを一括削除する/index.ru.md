---
title: "Безопасное массовое удаление файлов .DS_Store в PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Укажите корневую папку, проверьте найденные скрытые файлы и сначала просмотрите план удаления с помощью WhatIf."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Если созданные macOS файлы `.DS_Store` остались в папках Windows, их можно удалить через PowerShell. Чтобы ограничить область поиска, явно укажите целевую папку, проверьте полные пути найденных файлов и сначала просмотрите операцию с `-WhatIf`.

## Вывести совпадения и просмотреть план

Замените `$root` абсолютным путём папки, которую нужно очистить. `-LiteralPath` не интерпретирует символы пути как подстановочные знаки; `-Filter` выбирает элементы с именем `.DS_Store`. `-File` исключает каталоги с таким именем. `-Recurse` ищет во вложенных папках, а `-Force` включает скрытые элементы.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## Удалять только после проверки

В первом выводе перечисляются полные пути найденных файлов. Следующий `-WhatIf` показывает планируемые удаления, не выполняя их. Только после проверки списка и предпросмотра удалите `-WhatIf` из той же строки `Remove-Item` и запустите её.

## Область поиска и права

Пример выбирает файлы с именем `.DS_Store` внутри выбранного корня. Неверно заданный корень может включить другие файлы в его пределах. `-Force` не обходит права доступа. При отказе в доступе проверьте путь и разрешения.

## Ссылки Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)

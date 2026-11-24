---
title: "Поиск исполняемого файла в Windows с помощью where.exe и PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でПутьの通ったИсполняемый файлの場所を見つける方法"
tags: ["Windows", "путь", "исполняемый файл", "командная строка"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Поиск файлов в PATH с помощью where в командной строке или where.exe и Get-Command в PowerShell; поясняются псевдоним и область поиска."
---
## Командная строка

Чтобы найти исполняемый файл, запускаемый как команда, используйте `where` в командной строке. В PowerShell `where` — это псевдоним `Where-Object`, поэтому для внешней программы укажите `where.exe`.

```cmd
where mspaint.exe
```

`where` ищет в текущей папке и каталогах из переменной среды `PATH`, выводя найденные совпадения. Результатов может быть несколько. Команда не просматривает все папки компьютера и не находит приложения вне этих каталогов.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

В PowerShell команда `Get-Command` показывает выбранную команду и путь к исполняемому файлу.

## Официальные источники

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)

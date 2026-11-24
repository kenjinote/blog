---
title: "Как показать заголовки главных окон процессов в PowerShell"
slug: "Окноタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Узнайте, как с помощью Get-Process и MainWindowTitle вывести заголовок главного окна каждого процесса, что именно попадёт в результат и почему там могут быть конфиденциальные данные."
---
Можно отфильтровать объекты процессов, возвращаемые `Get-Process`, и показать только те, у которых `MainWindowTitle` (заголовок главного окна) не пуст:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

Команда показывает **заголовок главного окна каждого процесса**. Она не перечисляет все окна, принадлежащие процессу, и не выводит все окна рабочего стола. Процессы без главного окна или с пустым заголовком в результат не попадут. При запуске и завершении процессов результат может меняться.

В заголовках могут быть имена открытых документов и другие личные сведения. Проверяйте вывод перед записью в журнал или передачей другим людям.

См. документацию Microsoft: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) и [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).

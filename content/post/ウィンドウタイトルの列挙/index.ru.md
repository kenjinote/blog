---
title: "Перечисление заголовков окон"
slug: "Перечисление заголовков окон"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Программирование"]
---
# Перечисление заголовков окон

Способ перечисления заголовков открытых в данный момент окон с помощью PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Пример вывода

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Безымянный - Paint
Безымянный - Блокнот
Диспетчер задач
Windows Input Experience
Документ - WordPad
```

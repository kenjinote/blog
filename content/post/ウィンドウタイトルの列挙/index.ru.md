---
title: 'Как перечислить и получить заголовки открытых окон с помощью PowerShell'
slug: "Окноタイトルの列挙"
date: "2026-09-24T16:08:36+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Объясняем, как легко перечислить и получить заголовки всех окон, открытых в данный момент на ПК, с помощью PowerShell. Представлено в простой для понимания форме даже для начинающих с фактическими командами и примерами вывода.'
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

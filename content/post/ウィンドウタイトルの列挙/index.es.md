---
title: "Mostrar los títulos de las ventanas principales de los procesos con PowerShell"
slug: "Ventanaタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Aprende a mostrar con Get-Process y MainWindowTitle el título de la ventana principal de cada proceso, qué incluye el resultado y por qué puede contener información confidencial."
---
Puedes filtrar los objetos de proceso que devuelve `Get-Process` para mostrar solo aquellos cuyo `MainWindowTitle` (título de la ventana principal) no esté vacío:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

El comando muestra el **título de la ventana principal de cada proceso**. No enumera todas las ventanas de un proceso ni todas las ventanas del escritorio. Se omiten los procesos sin ventana principal o con el título vacío. El resultado también puede cambiar cuando se inician o terminan procesos.

Los títulos pueden incluir nombres de documentos abiertos u otros datos personales. Revisa el resultado antes de guardarlo en un registro o compartirlo.

Consulta la documentación de Microsoft sobre [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) y [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).

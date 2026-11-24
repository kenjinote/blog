---
title: "Exibir títulos das janelas principais dos processos com PowerShell"
slug: "Janelaタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Veja como usar Get-Process e MainWindowTitle para exibir o título da janela principal de cada processo, entender o alcance do resultado e considerar possíveis dados confidenciais."
---
É possível filtrar os objetos de processo retornados por `Get-Process` para mostrar apenas os que têm `MainWindowTitle` (título da janela principal) preenchido:

```powershell
Get-Process |
  Where-Object { $_.MainWindowTitle } |
  Select-Object ProcessName, Id, MainWindowTitle
```

O comando exibe o **título da janela principal de cada processo**. Ele não enumera todas as janelas de um processo nem todas as janelas da área de trabalho. Processos sem janela principal ou com título vazio não aparecem. A saída também pode mudar quando processos são iniciados ou encerrados.

Os títulos podem incluir nomes de documentos abertos ou outros dados pessoais. Confira a saída antes de salvá-la em um log ou compartilhá-la.

Consulte a documentação da Microsoft: [Get-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-process) e [.NET Process.MainWindowTitle](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.process.mainwindowtitle).

---
title: "Excluir .DS_Store em lote com PowerShell"
slug: "Excluir .DS_Store em lote com PowerShell"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programação"]
---

Mova o diretório atual para a pasta de destino e execute o seguinte comando para excluir em lote os arquivos .DS_Store, incluindo aqueles em subpastas.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

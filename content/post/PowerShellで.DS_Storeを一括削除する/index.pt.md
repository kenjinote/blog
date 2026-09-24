---
title: 'Comando simples para excluir arquivos .DS_Store em lote com o PowerShell'
slug: "PowerShellで.DS_Storeを一括削除する"
date: "2026-09-24T16:08:36+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos como excluir em lote os arquivos .DS_Store do Mac, que tendem a ser um obstáculo no ambiente Windows, incluindo em subpastas, usando o PowerShell. Você pode limpar facilmente arquivos desnecessários com um único comando curto.'
---

Mova o diretório atual para a pasta de destino e execute o seguinte comando para excluir em lote os arquivos .DS_Store, incluindo aqueles em subpastas.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

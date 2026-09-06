---
title: "Enumeração de Títulos de Janelas"
slug: "Enumeração de Títulos de Janelas"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programação"]
---
# Enumeração de Títulos de Janelas

Aqui está como enumerar os títulos das janelas abertas atualmente usando o PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Exemplo de saída

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Sem título - Paint
Sem título - Bloco de Notas
Gerenciador de Tarefas
Experiência de Entrada do Windows
Documento - WordPad
```

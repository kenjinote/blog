---




title: "Enumeración de títulos de ventanas"
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programación"]
---




# Enumeración de títulos de ventanas

Este es el método para enumerar los títulos de las ventanas actualmente abiertas usando PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Ejemplo de salida

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Sin título - Paint
Sin título - Bloc de notas
Administrador de tareas
Experiencia de entrada de Windows
Documento - WordPad
```

---




title: 'Cómo enumerar y obtener los títulos de las ventanas actualmente abiertas con PowerShell'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programación"]
description: 'Explicamos cómo enumerar y obtener fácilmente los títulos de todas las ventanas actualmente abiertas en el PC utilizando PowerShell. Lo presentamos de forma comprensible para principiantes, con comandos reales y ejemplos de salida.'
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

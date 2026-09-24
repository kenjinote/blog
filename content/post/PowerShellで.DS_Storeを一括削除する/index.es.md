---



title: 'Comando sencillo de PowerShell para eliminar masivamente archivos .DS_Store'
slug: "PowerShellで.DS_Storeを一括削除する"
date: "2026-09-24T16:08:36+09:00"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Explicamos cómo eliminar masivamente los molestos archivos .DS_Store de Mac en un entorno Windows, incluyendo subcarpetas, utilizando PowerShell. Puedes limpiar archivos innecesarios fácilmente con un solo comando corto.'
---




Navega al directorio de destino y ejecuta el siguiente comando para eliminar de forma masiva los archivos .DS_Store, incluyendo los de las subcarpetas.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

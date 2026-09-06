---

title: "Eliminar .DS_Store por lotes con PowerShell"
date: 2022-09-12T10:11:42+09:00
tags: ["PowerShell"]
draft: false
image: "img.png"
categories: ["Programación"]
---


Navega al directorio de destino y ejecuta el siguiente comando para eliminar de forma masiva los archivos .DS_Store, incluyendo los de las subcarpetas.

```powershell
Get-ChildItem . -include '.DS_Store' -Recurse -Force | Remove-Item -Force
```

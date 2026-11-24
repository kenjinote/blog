---
title: "Eliminar archivos .DS_Store de forma segura con PowerShell"
slug: "PowerShellで.DS_Storeを一括削除する"
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Indica una carpeta raíz explícita, revisa las coincidencias ocultas y previsualiza la eliminación con WhatIf antes de borrar archivos .DS_Store."
date: "2022-09-12T10:11:42+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Si quedan archivos `.DS_Store` creados por macOS en carpetas de Windows, puedes eliminarlos con PowerShell. Para limitar el alcance, especifica la carpeta de destino, revisa las rutas completas coincidentes y previsualiza la operación con `-WhatIf` antes de borrar nada.

## Listar coincidencias y previsualizar

Sustituye `$root` por la ruta absoluta de la carpeta que quieres limpiar. `-LiteralPath` evita interpretar como comodines los caracteres de la ruta raíz; `-Filter` busca elementos llamados `.DS_Store`. `-File` excluye carpetas con ese nombre. `-Recurse` busca en subcarpetas y `-Force` incluye elementos ocultos.

```powershell
$root = 'C:\path\to\target-folder'

$files = @(
    Get-ChildItem -LiteralPath $root -Filter '.DS_Store' -File -Recurse -Force -ErrorAction Stop
)

# Review the exact files that matched.
$files | Select-Object -ExpandProperty FullName

# Preview the deletion; this does not remove files.
$files | ForEach-Object {
    Remove-Item -LiteralPath $_.FullName -Force -WhatIf
}
```

## Borrar solo después de revisar

La primera salida enumera las rutas completas de los archivos candidatos. El `-WhatIf` siguiente muestra lo que se eliminaría sin hacerlo. Solo después de confirmar que la lista y la vista previa son correctas, quita `-WhatIf` de la misma línea de `Remove-Item` y ejecútala.

## Alcance y permisos

El ejemplo busca archivos llamados `.DS_Store` bajo la raíz elegida. Si eliges una raíz incorrecta, puede incluir archivos de cualquier lugar dentro de ella. `-Force` no omite los permisos de acceso. Si se deniega el acceso, revisa la ruta y tus permisos.

## Referencias de Microsoft

- [Microsoft: Get-ChildItem](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-childitem)
- [Microsoft: Remove-Item](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/remove-item)
- [Microsoft: PowerShell common parameters, including WhatIf](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_commonparameters)

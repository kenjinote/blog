---
title: "Encontrar un ejecutable en Windows con where.exe y PowerShell"
date: 2023-04-03T00:02:55+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Windows でRutaの通ったArchivo ejecutableの場所を見つける方法"
tags: ["Windows", "path", "archivo ejecutable", "símbolo del sistema"]
draft: false
image: "img.webp"
categories: ["windows", "terminal"]
description: "Cómo localizar ejecutables en PATH con where en el Símbolo del sistema o where.exe y Get-Command en PowerShell, y entender el alias y el alcance de búsqueda."
---
## Símbolo del sistema

Para localizar un ejecutable invocable como comando, usa `where` en el Símbolo del sistema. En PowerShell, `where` es un alias de `Where-Object`; escribe `where.exe` para llamar explícitamente al programa externo.

```cmd
where mspaint.exe
```

`where` busca en la carpeta actual y en las rutas de la variable de entorno `PATH`, y muestra las coincidencias. Puede devolver varias rutas. No busca en todas las carpetas del equipo ni encuentra aplicaciones fuera de esas ubicaciones.

## PowerShell

```powershell
where.exe mspaint.exe
Get-Command mspaint.exe -All
```

En PowerShell, `Get-Command` muestra el comando que se resolverá y la ruta del ejecutable.

## Referencias oficiales

- [Windows `where` command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/where)
- [PowerShell `Get-Command`](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command?view=powershell-7.5)
- [PowerShell `Where-Object` (the `where` alias)](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5)

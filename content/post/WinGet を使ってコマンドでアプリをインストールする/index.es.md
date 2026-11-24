---




title: 'Cómo instalar y gestionar aplicaciones fácilmente con el comando WinGet en Windows 11'
slug: "WinGet を使ってComandoでAplicaciónをInstalaciónする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explicamos cómo instalar aplicaciones desde la línea de comandos usando ''WinGet'', el administrador de paquetes de Windows 11. Presentamos el procedimiento para instalar y gestionar rápidamente software principal como Chrome, VSCode y Slack a través de la línea de comandos.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Instalar aplicaciones desde la línea de comandos con WinGet

WinGet (Windows Package Manager) permite buscar, instalar, actualizar y quitar aplicaciones desde la línea de comandos de Windows. Microsoft indica compatibilidad con Windows 11, Windows 10 versión 1809 o posterior y Windows Server 2025. En las ediciones de escritorio suele venir incluido en el Instalador de aplicaciones.

## Comprobar WinGet

Ejecute esto en PowerShell, Windows Terminal o el Símbolo del sistema:

```powershell
winget --version
```

Si falta el comando, instale las actualizaciones de Windows e instale o actualice el Instalador de aplicaciones desde Microsoft Store. Tras iniciar sesión por primera vez con una cuenta nueva, espere a que Store termine el registro.

## Buscar e instalar

Compruebe el nombre, el ID y el editor en los resultados antes de instalar por ID.

```powershell
winget search vscode
winget show --id Microsoft.VisualStudioCode
winget install --id Microsoft.VisualStudioCode -e --source winget
```

`-e` requires an exact ID match; `--source winget` selects the WinGet Community Repository. Read and accept any source or app license agreements only after reviewing them. Microsoft also documents these package ID examples:

```powershell
winget install Microsoft.PowerToys
winget install Microsoft.PowerShell
winget install Git.Git
winget install Docker.DockerDesktop
```

Package IDs and versions can change. Check the selected package with `winget show` first; specify `--source` if multiple sources return the same app.

## Paint.NET ya está disponible en WinGet

Paint.NET figura en el repositorio comunitario con el ID `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Compruebe el manifiesto actual porque la disponibilidad puede cambiar.

## Referencias

- [Microsoft Learn: descripción general de WinGet](https://learn.microsoft.com/es-es/windows/package-manager/winget/)
- [Microsoft Learn: comando install](https://learn.microsoft.com/es-es/windows/package-manager/winget/install)
- [Microsoft Learn: comando search](https://learn.microsoft.com/es-es/windows/package-manager/winget/search)
- [Repositorio de WinGet: manifiesto de Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)

---
title: "Instalar y desinstalar PowerToys con WinGet"
slug: "PowerToysのInstalación"
tags: ["cmd", "símbolo del sistema", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Instala o desinstala PowerToys mediante su identificador de paquete de Microsoft con WinGet y consulta los requisitos actuales."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys es un conjunto de utilidades de Microsoft para personalizar Windows. Microsoft recomienda instalarlo desde GitHub o Microsoft Store; esta guía explica el método con WinGet.

## Requisitos del sistema

Los requisitos actuales de PowerToys son Windows 11 o Windows 10 versión 2004 (20H1, compilación 19041) o posterior, y un procesador de 64 bits x64 o ARM64. Durante la instalación se instala la versión estable más reciente de Microsoft Edge WebView2 Runtime. Los requisitos y las opciones de descarga pueden cambiar; consulta la documentación oficial antes de instalar.

## Instalar con WinGet

Primero ejecuta `winget --version` en el Símbolo del sistema o PowerShell para comprobar que WinGet está disponible. Este comando selecciona el identificador de paquete Microsoft.PowerToys desde el origen winget. Lee cualquier aviso o solicitud de aceptación antes de continuar.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Desinstalar

El comando de desinstalación también especifica el identificador y el origen winget. Antes de continuar, confirma que el paquete seleccionado sea PowerToys y revisa cualquier solicitud de confirmación.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Referencias oficiales de Microsoft

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)

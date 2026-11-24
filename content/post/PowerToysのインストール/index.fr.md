---
title: "Installer et désinstaller PowerToys avec WinGet"
slug: "PowerToysのInstallation"
tags: ["cmd", "invite de commandes", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Installez ou désinstallez PowerToys avec son identifiant de package Microsoft dans WinGet et consultez la configuration requise actuelle."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys est un ensemble d’utilitaires Microsoft pour personnaliser Windows. Microsoft recommande une installation depuis GitHub ou le Microsoft Store ; ce guide présente la méthode WinGet.

## Configuration requise

La configuration actuellement requise pour PowerToys est Windows 11 ou Windows 10 version 2004 (20H1, build 19041) ou ultérieure, avec un processeur 64 bits x64 ou ARM64. Le programme d’installation installe la dernière version stable de Microsoft Edge WebView2 Runtime. Ces exigences et les options de distribution peuvent évoluer ; consultez la documentation officielle avant l’installation.

## Installer avec WinGet

Exécutez d’abord `winget --version` dans l’invite de commandes ou PowerShell pour vérifier que WinGet est disponible. Cette commande sélectionne l’identifiant de package Microsoft.PowerToys dans la source winget. Lisez les messages et demandes d’accord avant de continuer.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Désinstaller

La commande de désinstallation précise également l’identifiant et la source winget. Avant de continuer, vérifiez que le package sélectionné est PowerToys et lisez toute demande de confirmation.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Références officielles Microsoft

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)

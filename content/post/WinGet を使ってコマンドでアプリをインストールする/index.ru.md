---
title: 'Как легко устанавливать и управлять приложениями с помощью команды WinGet в Windows 11'
slug: "WinGet を使ってКомандаでПриложениеをУстановкаする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Объясняем, как устанавливать приложения из командной строки с помощью менеджера пакетов «WinGet» в Windows 11. Представлены шаги по быстрой установке и управлению основным программным обеспечением, таким как Chrome, VSCode, Slack и т. д., через командную строку.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Установка приложений из командной строки с WinGet

WinGet (Windows Package Manager) позволяет искать, устанавливать, обновлять и удалять приложения из командной строки Windows. Microsoft указывает поддержку Windows 11, Windows 10 версии 1809 и новее, а также Windows Server 2025. В настольных версиях WinGet обычно входит в App Installer.

## Проверка WinGet

Выполните команду в PowerShell, Windows Terminal или командной строке:

```powershell
winget --version
```

Если команда отсутствует, установите обновления Windows и установите или обновите App Installer через Microsoft Store. После первого входа в новую учетную запись дождитесь регистрации через Store.

## Поиск и установка

Перед установкой по ID проверьте название приложения, ID и издателя в результатах поиска.

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

## Paint.NET теперь доступен через WinGet

Paint.NET указан в репозитории сообщества под ID `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Проверьте текущий манифест, поскольку доступность может измениться.

## Источники

- [Microsoft Learn: обзор WinGet](https://learn.microsoft.com/ru-ru/windows/package-manager/winget/)
- [Microsoft Learn: команда install](https://learn.microsoft.com/ru-ru/windows/package-manager/winget/install)
- [Microsoft Learn: команда search](https://learn.microsoft.com/ru-ru/windows/package-manager/winget/search)
- [Репозиторий WinGet: манифест Paint.NET](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)

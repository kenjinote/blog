---
title: "Установка и удаление PowerToys с помощью WinGet"
slug: "PowerToysのУстановка"
tags: ["cmd", "командная строка", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Установите или удалите PowerToys в WinGet по идентификатору пакета Microsoft и проверьте актуальные системные требования."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys — набор служебных программ Microsoft для настройки Windows. Microsoft рекомендует устанавливать его через GitHub или Microsoft Store; в этой статье описан способ с WinGet.

## Системные требования

Текущие требования PowerToys: Windows 11 или Windows 10 версии 2004 (20H1, сборка 19041) или новее и 64-разрядный процессор x64 либо ARM64. Во время установки устанавливается последняя стабильная версия Microsoft Edge WebView2 Runtime. Требования и способы распространения могут измениться, поэтому перед установкой проверьте официальную документацию.

## Установка через WinGet

Сначала выполните `winget --version` в командной строке или PowerShell и убедитесь, что WinGet доступен. Эта команда выбирает пакет с идентификатором Microsoft.PowerToys из источника winget. Прочитайте все уведомления и запросы согласия перед продолжением.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Удаление

Команда удаления также указывает идентификатор и источник winget. Перед продолжением убедитесь, что выбран PowerToys, и прочитайте запрос подтверждения, если он появится.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Официальные материалы Microsoft

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)

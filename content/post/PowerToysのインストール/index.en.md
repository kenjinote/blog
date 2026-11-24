---
title: "Install and Uninstall PowerToys with WinGet"
slug: "PowerToysのInstall"
tags: ["cmd", "Command Prompt", "PowerToys", "winget"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Install or uninstall PowerToys by its Microsoft package ID with WinGet, and review the current system requirements."
date: "2023-09-30T21:23:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

PowerToys is a set of Microsoft utilities for customizing Windows. Microsoft recommends installing it from GitHub or the Microsoft Store; this guide covers the WinGet method.

## System requirements

The current PowerToys requirements are Windows 11 or Windows 10 version 2004 (20H1, build 19041) or later, and a 64-bit x64 or ARM64 processor. Setup installs the latest stable Microsoft Edge WebView2 Runtime. Requirements and distribution options can change, so check the official documentation before installing.

## Install with WinGet

First, run `winget --version` in Command Prompt or PowerShell to confirm that WinGet is available. This command selects the package ID Microsoft.PowerToys from the winget source. Read any prompts or agreement requests before continuing.

```powershell
winget install --id Microsoft.PowerToys --exact --source winget
```

## Uninstall

The uninstall command also specifies the ID and winget source. Before proceeding, confirm that the selected package is PowerToys and review any confirmation prompt.

```powershell
winget uninstall --id Microsoft.PowerToys --exact --source winget
```

## Official Microsoft references

- [Microsoft: Install PowerToys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- [Microsoft: WinGet install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft: WinGet uninstall command](https://learn.microsoft.com/en-us/windows/package-manager/winget/uninstall)

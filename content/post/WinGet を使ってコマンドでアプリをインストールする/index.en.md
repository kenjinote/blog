---
title: 'How to Easily Install and Manage Apps with the WinGet Command in Windows 11'
slug: "WinGet を使ってCommandでAppをInstallする"
tags: ["WinGet"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Explains how to install apps from the command line using ''WinGet'', the Windows 11 package manager. Introduces the steps to quickly deploy and manage major software like Chrome, VSCode, and Slack via the command line.'
date: "2022-10-05T12:15:20+09:00"
lastmod: "2026-11-25T00:00:00+09:00"
---

# Install Apps from the Command Line with WinGet

WinGet (Windows Package Manager) can search for, install, upgrade, and remove apps from the Windows command line. Microsoft lists support for Windows 11, Windows 10 version 1809 or later, and Windows Server 2025. On desktop editions it is normally included with App Installer.

## Check WinGet

Run this in PowerShell, Windows Terminal, or Command Prompt:

```powershell
winget --version
```

If the command is missing, apply Windows updates and install or update App Installer from Microsoft Store. After the first sign-in to a new account, wait for Store registration to finish.

## Search, then install

Check the app name, ID, and publisher in the search results before installing by ID.

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

## Paint.NET is now available through WinGet

Paint.NET is listed in the community repository as `dotPDN.PaintDotNet`:

```powershell
winget show --id dotPDN.PaintDotNet -e --source winget
winget install --id dotPDN.PaintDotNet -e --source winget
```

Check the current manifest because availability can change.

## References

- [Microsoft Learn: WinGet overview](https://learn.microsoft.com/en-us/windows/package-manager/winget/)
- [Microsoft Learn: install command](https://learn.microsoft.com/en-us/windows/package-manager/winget/install)
- [Microsoft Learn: search command](https://learn.microsoft.com/en-us/windows/package-manager/winget/search)
- [WinGet Community Repository: Paint.NET manifest](https://github.com/microsoft/winget-pkgs/tree/master/manifests/d/dotPDN/PaintDotNet)

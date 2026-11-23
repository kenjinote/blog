---
title: 'How to Use the nano CLI Text Editor on Windows: WSL and MSYS2'
slug: "CLIText EditornanoをWindowsにInstallする方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "text editor"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: 'Current ways to use GNU nano on Windows: install it in WSL for a Linux environment or in MSYS2 for Windows development tools, then learn the basic shortcuts.'
---


There are several ways to use GNU nano on Windows. Standalone `nano.exe` files from old download sites can be difficult to verify and may not be maintained, so this guide uses two maintained distribution routes.

## Option 1: Use nano in WSL

Choose WSL if you also want Linux command-line tools. On Windows 11, or Windows 10 version 2004 (build 19041) or later, open PowerShell as Administrator and run:

```powershell
wsl --install
```

After restarting, open Ubuntu and install nano in the Linux terminal:

```bash
sudo apt update
sudo apt install nano
nano --version
```

Open a file with `nano filename`. The Windows C: drive is available under `/mnt/c/` in WSL; for example, `nano /mnt/c/Users/YourName/notes.txt`. See [Microsoft's WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install) for setup and file access details.

## Option 2: Use nano from MSYS2

If you want Unix-style development tools without a full Linux distribution, use [MSYS2](https://www.msys2.org/). Follow its [official installer guide](https://www.msys2.org/docs/installer/), then open the “MSYS2 MSYS” terminal. The GUI installer requires 64-bit Windows 10 version 1809 or later, or Windows Server 2019; individual package requirements may differ (see [supported Windows versions](https://www.msys2.org/docs/windows_support/)). Update the package database and installed packages first. If the update asks you to restart the terminal, reopen it and finish the update before installing nano.

```bash
pacman -Suy
pacman -S nano
nano --version
```

The package name and command are listed on the [MSYS2 nano package page](https://packages.msys2.org/packages/nano?variant=x86_64). Run nano inside an MSYS2 terminal. Using it from ordinary Command Prompt or PowerShell requires additional PATH and runtime setup; adding MSYS2's `/usr/bin` to the Windows PATH indiscriminately is not recommended.

## Basic shortcuts

Start it with a command such as `nano notes.txt`. The shortcut legend appears at the bottom of the screen: `^` means Ctrl, and `M-` means Meta (usually Alt). To write the file, press `Ctrl+O`, confirm the displayed filename with Enter, and press `Ctrl+X` to exit. Current nano versions also save the current buffer with `Ctrl+S`. See the [official GNU nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html).

nano supports internationalization and UTF-8, but Japanese input and display also depend on the terminal, fonts, locale, and IME. If characters are garbled or Japanese input does not work in WSL or MSYS2, check the terminal's UTF-8 and input-method configuration.

## References

- [GNU nano](https://www.nano-editor.org/)
- [GNU nano cheat sheet](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn: Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)
- [MSYS2 installer guide](https://www.msys2.org/docs/installer/)
- [Supported Windows versions](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano package](https://packages.msys2.org/packages/nano?variant=x86_64)

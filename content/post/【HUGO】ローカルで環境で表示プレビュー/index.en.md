---
title: "Hugo on Windows: installation and local preview"
slug: "【HUGO】ローカルで環境で表示プレビュー"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Install Hugo on Windows, configure PATH when needed, and preview a site locally with draft content using the current Hugo commands."
date: "2022-09-05T12:28:01+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Install Hugo on Windows and preview a site locally

> **Updated November 24, 2026.** The earlier article depended on Hugo 0.102.3 output and Windows steps from 2022. This version follows the current official Windows installation and CLI documentation. Hugo, Windows dialogs, and package details can change; use the linked official docs when a screen differs.

## تثبيت Hugo

On Windows 10 or later, WinGet is a straightforward option. Open a new terminal after installation and run the command below. Alternatively, download the archive for your Windows version and CPU architecture from the official releases page, extract it, and place `hugo.exe` in a folder. Add the folder containing the executable to PATH, not the executable file itself.

To edit PATH manually, search the Start menu for “Edit environment variables for your account,” then add a folder such as `C:/Hugo/bin` to the user `Path` variable. Open a new terminal so it reads the updated environment.

## تثبيت Hugo

```powershell
winget install -e --id Hugo.Hugo
hugo version
```

```powershell
hugo server --buildDrafts
```

## Preview locally

From the Hugo project root (the directory containing its configuration file or configuration directory), start the server. `--buildDrafts` includes draft pages in the preview. Do not use draft-inclusive output as a production build. Open the URL printed by Hugo in your browser. The default is `http://localhost:1313/`, but check the output if that port is already in use. Press Ctrl+C in the terminal to stop the server.

## Official references

- [Install on Windows](https://gohugo.io/installation/windows/)
- [Basic usage and draft content](https://gohugo.io/getting-started/usage/)
- [hugo server command](https://gohugo.io/commands/hugo_server/)

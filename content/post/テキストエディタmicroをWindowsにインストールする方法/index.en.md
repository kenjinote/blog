---
title: 'Use it on Windows! How to Install the Lightweight Text Editor ''micro'''
slug: "Text EditormicroをWindowsにInstallする方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "text editor"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Clearly explains the steps to install ''micro'', a terminal-based text editor that works comfortably in the Command Prompt, on Windows and set environment variables so it''s ready to use.'
---

## Download micro
https://github.com/micro-editor/micro/releases/latest
In the latest release, open Assets and download the Windows x64 archive (for example, `micro-<version>-win64.zip`). Extract it to a folder of your choice.

For Windows on ARM, choose the matching ARM64 archive instead.

## Set Environment Variables
To use `micro.exe` from the command prompt, you need to set the environment variables.

1. Press `Win` + `R`, enter `sysdm.cpl`, and press `Enter`.
2. Open the Advanced tab and click Environment Variables.
3. Under User variables for your account, select `Path` and click Edit. Create `Path` if it is not listed.
4. Click New and add the path to the folder containing `micro.exe`.
5. Click OK to close the dialogs.
6. Reopen Command Prompt and run `micro` to check that it starts.

## How to use micro

When you type `micro` in the command prompt and execute it, the following screen is displayed.
![img_3.png](img_3.webp)

The main operations and shortcut keys are as follows.

| Shortcut Key | Operation | 
|--------|-----| 
| Ctrl+Q | Close the current file (quits micro if it is the last file) |
| Ctrl+S | Save file | 
| Ctrl+O | Open file | 
| Ctrl+A | Select all | 
| Ctrl+X | Cut selection | 
| Ctrl+C | Copy selection | 
| Ctrl+V | Paste | 
| Ctrl+Z | Undo | 
| Ctrl+Y | Redo | 
| Ctrl+E | Execute editor command | 

## Reference
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)

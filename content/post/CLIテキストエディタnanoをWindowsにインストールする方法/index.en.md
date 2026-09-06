---
title: 'How to install CLI text editor nano on Windows'
slug: "CLIテキストエディタnanoをWindowsにインストールする方法"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "text editor"]
draft: false
image: "img_1.png"
categories: ["Tools and Development Environment"]
---

## Download nano.exe
https://sourceforge.net/projects/nano-for-windows/

Open the link above, click `Download`, and download `GNU-Nano_Win32(static).zip`.
Extract the zip file and place `nano.exe` in an arbitrary folder.
* Note: Japanese input is not supported. (As of 2024/03/31)

## Set Environment Variables
In order to use `nano.exe` from the command prompt, you need to set the environment variables.

1. Press `Win key` + `R key`, type `sysdm.cpl`, and press `Enter key`.
2. In `System Properties`, click on the `Advanced` tab.
3. Click on `Environment Variables`.
4. Select `Path` under `System variables` and click `Edit`.
5. Click `New` and add the path to `nano.exe`.
6. Click `OK` to close all dialogs.
7. Restart the command prompt, type `nano`, and check if it can be executed.

## How to use nano

When you type `nano` and execute it, a screen like the following will be displayed.

![img_2.png](img_2.png)

Shortcut descriptions are displayed at the bottom of the screen.

The meanings of the symbols are as follows:

- `^` represents the `Ctrl` key.
- `M-` represents the `Alt` key.

To save and close, press `Ctrl` + `S` and then `Ctrl` + `X`.

## Reference
- [GNU nano](https://www.nano-editor.org/)

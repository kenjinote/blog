---
title: 'How to exit and restart Explorer'
slug: "エクスプローラーの終了・再起動方法"
date: 2024-03-30T15:40:24+09:00
tags: ["Explorer"]
draft: false
image: "img_2.png"
categories: ["IT & Technology"]
---

## How to exit from the taskbar right-click menu

This method is for Windows 10. It seems the menu is not displayed in Windows 11.
If you hold down the `Shift` and `Ctrl` keys and right-click on the taskbar, `Exit Explorer` will appear in the menu.

![img.png](img.png)

## How to exit from Task Manager

1. Press `Ctrl` + `Shift` + `Esc` to launch Task Manager.
2. Select `Details`.

![img_3.png](img_3.png)

3. Select `explorer.exe`, press the `Delete` key, and when asked `Do you want to end explorer.exe?`, select `End process`.

![img_1.png](img_1.png)

## How to exit from Command Prompt

1. Press `Win` + `R`, type `cmd`, and press `Enter`.
2. Type `taskkill /f /im explorer.exe` and press `Enter`.

## How to start Explorer from Task Manager

1. Press `Ctrl` + `Shift` + `Esc` to launch Task Manager.
2. Select `Run new task` from the File menu.
3. Type `explorer.exe` and press `Enter`.

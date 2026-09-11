---
title: 'How to Enumerate and Retrieve Currently Open Window Titles Using PowerShell'
slug: "ウィンドウタイトルの列挙"
date: 2022-09-20T17:03:15+09:00
tags: ["PowerShell"]
draft: false
image: "img.webp"
categories: ["Programming"]
description: 'Explains how to easily enumerate and retrieve the titles of all currently open windows on your PC using PowerShell. Introduces this in an easy-to-understand way for beginners, complete with actual commands and output samples.'
---
# Enumerate Window Titles

Here is how to enumerate the titles of currently open windows using PowerShell.

```powershell
Get-Process|where{$_.mainWindowTItle}|Select-Object MainWindowTitle
```

Output Sample

```
MainWindowTitle
---------------
Windows PowerShell
Internet Explorer
Untitled - Paint
Untitled - Notepad
Task Manager
Windows Input Experience
Document - WordPad
```

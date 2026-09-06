---
title: 'How to Restore the Classic Right-Click Menu in Windows 11'
slug: "Windows 11の右クリックメニューを従来版に戻す方法"
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "File Explorer"]
draft: false
image: "img.png"
categories: ["PC & Gadgets"]
---

# How to Restore the Classic Right-Click Menu in Windows 11

Here is how to restore the classic right-click menu in Windows 11.

1. Open the Registry Editor.

Press the `Win key` + `R key`, type `regedit`, and press the `Enter key`.
![img_1.png](img_1.png)　

2. Navigate to `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`. Create this key if it does not exist.


4. Navigate to `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`. Create this key if it does not exist.
5. Check that the `(Default)` value in `InprocServer32` is empty.

![img_2.png](img_2.png)

6. Restart your computer.
7. Confirm that the right-click menu has returned to the classic version.

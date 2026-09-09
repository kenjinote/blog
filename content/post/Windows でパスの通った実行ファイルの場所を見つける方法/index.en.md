---
title: 'How to Find the Location (Path) of an Executable File in Windows [where Command]'
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "Path", "Executable", "Command Prompt"]
draft: false
image: "img.webp"
categories: ["PC & Gadgets"]
description: 'Explains how to easily find the save location (full path) of an executable file using the Windows Command Prompt or PowerShell. Introduces a handy trick to quickly identify the exact location of an app in your path using the ''where'' command.'
---

# How to find the location of an executable in Windows

Sometimes when you execute a command by specifying an executable file, you want to know where that executable file is located. In such cases, you can find the location of the executable file using the following command.

```powershell
where <executable_file_name>
```

For example, if you want to know the location of Paint (mspaint.exe), you can do it as follows.

```powershell
where mspaint.exe
```

# References

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)

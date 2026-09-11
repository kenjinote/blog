---
title: '在Windows中查找已配置环境变量的可执行文件位置（路径）的方法【where命令】'
slug: "Windows でパスの通った実行ファイルの場所を見つける方法"
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "路径", "可执行文件", "命令提示符"]
draft: false
image: "img.webp"
categories: ["PC与数码"]
description: '讲解如何在Windows命令提示符或PowerShell中，轻松查找可执行文件的保存位置（完整路径）。介绍使用“where”命令快速定位已配置环境变量的应用程序准确位置的实用小技巧。'
---

# 在 Windows 中查找已添加到 PATH 路径的可执行文件位置的方法

在指定可执行文件并运行命令时，有时我们会想知道该可执行文件到底在哪里。这种情况下，可以使用以下命令来查找可执行文件的位置。

```powershell
where <可执行文件名>
```

例如，如果想知道画图程序 (mspaint.exe) 的位置，可以像下面这样做。

```powershell
where mspaint.exe
```

# 参考

- [How do I find the location of an executable in Windows?](https://superuser.com/questions/49104/how-do-i-find-the-location-of-an-executable-in-windows)

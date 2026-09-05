---
title: '在 Windows 中查找已添加到 PATH 路径的可执行文件位置的方法'
date: 2023-04-03T00:02:55+09:00
tags: ["Windows", "路径", "可执行文件", "命令提示符"]
draft: false
image: "img.png"
categories: ["PC与数码"]
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

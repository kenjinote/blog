---
title: '通过命令“hide”启动秀丸编辑器的方法'
date: 2024-03-29T23:45:37+09:00
tags: ["命令", "秀丸编辑器", "注册表"]
draft: false
image: "img_2.png"
categories: ["工具与开发环境"]
---

## 介绍如何通过命令“hide”启动秀丸编辑器。

注：此方法已在`Windows 10/11`上进行测试。

1. 打开注册表编辑器。
2. 导航到 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`。
3. 在 `App Paths` 下创建一个名为 `hide.exe` 的项。※该项名称中 `.exe` 前面的部分即为命令名。
4. 将 `hide.exe` 项的 `(默认)` 值设置为秀丸编辑器的可执行文件路径。在我的环境中，路径为 `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`。
5. 在 `hide.exe` 项下创建一个名为 `Path` 的字符串值。
6. 将 `Path` 的数值数据设置为包含秀丸编辑器可执行文件的文件夹路径。在我的环境中，路径为 `"C:\Program Files (x86)\Hidemaru"`。
7. 现在，在按 `Win键` + `R键` 打开的 *运行* 窗口中，你可以使用 `hide` 命令启动秀丸编辑器。此外，在命令提示符中也可以使用 `start hide` 命令启动它。

```
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="\"C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe\""
"Path"="\"C:\\Program Files (x86)\\Hidemaru\\\""
```
将上述内容保存为 `.reg` 文件并运行，即可将这些设置添加到注册表中。

![img_1.png](img_1.png)

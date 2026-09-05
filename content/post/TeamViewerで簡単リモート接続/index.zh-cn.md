---
title: '使用TeamViewer轻松进行远程连接'
date: 2023-01-13T01:45:00+09:00
tags: ["TeamViewer", "命令", "远程连接"]
draft: false
image: "img.png"
categories: ["IT・科技"]
---

# 使用TeamViewer轻松进行远程连接

使用TeamViewer可以轻松实现远程桌面连接。

在被控端和控制端分别启动TeamViewer，
然后在控制端输入被控端的ID和密码即可进行远程连接。

如果想要通过命令行进行远程连接，可以执行以下操作：

```
%ProgramFiles%\TeamViewer\TeamViewer.exe -i <ID> -P <Password>
```
在 `<ID>` 处输入被控端的ID，在 `<Password>` 处输入被控端的密码。

使用上述命令创建快捷方式文件后，就可以省略输入ID和密码的步骤，非常方便。

参考网站：[Command line parameters](https://community.teamviewer.com/English/kb/articles/34447-command-line-parameters)

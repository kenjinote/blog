---
title: '【初学者指南】使用TeamViewer轻松进行远程桌面连接的方法'
date: 2023-01-13T01:45:00+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "TeamViewerで簡単远程连接"
tags: ["TeamViewer", "命令", "远程连接"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '讲解如何使用TeamViewer轻松进行远程桌面连接。同时介绍通过命令行指定ID和密码，以及利用快捷方式实现自动连接、省略步骤的实用小技巧巧。'
---
## 在 Windows 上通过命令行连接

根据 TeamViewer 官方 Windows 命令行文档，可以通过命令提示符、脚本或快捷方式启动完整版 TeamViewer。

此示例从安装目录启动 `TeamViewer.exe`。将对方 ID 填入 `<ID>`，将密码填入 `<Password>`。如果 TeamViewer 安装在其他位置，请替换可执行文件路径。

```cmd
"%ProgramFiles%\TeamViewer\TeamViewer.exe" -i <ID> -p <Password>
```

省略 `-p` 时，如果可以使用 Easy Access，TeamViewer 会使用该方式；否则会提示输入密码。

包含密码的快捷方式会以可读形式保存密码。请勿分享，也不要放在他人可以读取的位置。如需经常进行无人值守访问，可考虑将设备分配到账号并使用 Easy Access、允许列表和多重身份验证，而不是保存密码。

## 官方资料

- [TeamViewer command-line parameters](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/for-developers/command-line-parameters/)
- [Best practices for secure unattended access](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-classic/security/best-practices/best-practices-for-secure-unattended-access/)
- [TeamViewer security statement](https://www.teamviewer.com/en-us/global/support/knowledge-base/teamviewer-remote/security/security-statement/)

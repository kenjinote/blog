---
title: '在Windows右键菜单中添加秀丸编辑器grep的方法'
date: 2024-04-03T00:00:46+09:00
lastmod: "2026-11-24T00:00:00+09:00"
slug: "资源管理器の右键菜单に秀丸编辑器grepを追加する"
tags: ["秀丸编辑器", "资源管理器", "右键菜单", "grep", "注册表"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '介绍在Windows 10/11资源管理器的右键菜单中添加秀丸编辑器grep功能的便捷设置步骤。通俗易懂地讲解使用注册表配置文件的简单方法。'
---
介绍如何在 Windows 10/11 中，将秀丸编辑器的 grep 功能添加到资源管理器的右键菜单中。

**※由于以下步骤涉及修改注册表，请自行承担风险。**

此文件只为当前用户添加文件夹菜单命令，不会为所有文件添加“用秀丸打开”，也不会修改整台电脑的设置。导入前请用记事本打开文件，核对并按实际安装位置修改秀丸程序路径。若目标注册表项已存在，请先在注册表编辑器中选中并通过“文件”>“导出”备份。Windows 11 的旧式命令可能位于“显示更多选项”。Windows 10 已于 2025 年 10 月 14 日结束支持。 随附的解除文件只会删除这些当前用户项，不会撤销旧版的全计算机注册。如果曾导入旧文件，请在注册表编辑器中另行检查并删除其项。
## 步骤

1. 打开以下链接，并将其保存到任意文件夹中。

[秀丸レジストリ登録.reg](秀丸レジストリ登録.reg)

[删除秀丸注册表项](秀丸レジストリ解除.reg)

2. 双击 `秀丸レジストリ登録.reg` 文件以将其添加到注册表中。

## 参考

- [从文件夹的右键菜单执行秀丸grep](https://aimek-developer.blogspot.com/2019/02/grep.html)

## 官方参考资料

- [Hidemaru startup options](https://help.maruo.co.jp/hidemaru/html/230_Option.html)
- [Microsoft: Back up and restore the registry](https://support.microsoft.com/en-us/windows/experience/backup-recovery/how-to-back-up-and-restore-the-registry-in-windows)
- [Microsoft: File Explorer context menu](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft: Windows 10 end of support](https://support.microsoft.com/en-us/windows/deployment/updates-lifecycle/windows-10-support-has-ended-on-october-14-2025)
- [Microsoft: reg import](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/reg-import)

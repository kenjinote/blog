---
date: 2024-03-29T23:45:37+09:00
lastmod: 2026-11-25
title: '通过“hide”命令一键启动秀丸编辑器！Windows的便捷设置方法'
slug: "命令「hide」で秀丸编辑器を立ち上げる方法"
tags: ["命令", "秀丸编辑器", "注册表"]
draft: false
image: "img_2.webp"
categories: ["tools-development-environment"]
description: "介绍如何在 Windows 10/11 中注册 App Paths 名称，并通过“运行”或 start hide 启动秀丸编辑器。"
---

## 介绍如何通过命令“hide”启动秀丸编辑器。

注：此方法已在`Windows 10/11`上进行测试。

1. 打开注册表编辑器。
2. 导航到 `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths`。
3. 在 `App Paths` 下创建一个名为 `hide.exe` 的项。※该项名称中 `.exe` 前面的部分即为命令名。
4. 将 `hide.exe` 项的 `(默认)` 值设置为秀丸编辑器的可执行文件路径。在我的环境中，路径为 `"C:\Program Files (x86)\Hidemaru\Hidemaru.exe"`。
5. Path 值是可选的。只有应用需要额外 DLL 搜索目录时才设置；ShellExecuteEx 启动时会把它们添加到进程 PATH。
6. 按 Win + R 打开“运行”，输入 hide。在命令提示符中使用 start hide；本文介绍的方式不是直接输入 hide。

```reg
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\hide.exe]
@="C:\\Program Files (x86)\\Hidemaru\\Hidemaru.exe"
```
将上述内容保存为 `.reg` 文件并运行，即可将这些设置添加到注册表中。

此 .reg 示例只为当前用户注册。请将路径替换为秀丸实际的可执行文件路径。若要为所有用户注册，请将 HKEY_CURRENT_USER 改为 HKEY_LOCAL_MACHINE，并以管理员权限导入。


## 参考资料

- [Microsoft: Application Registration and App Paths](https://learn.microsoft.com/en-us/windows/win32/shell/app-registration)
- [Microsoft: start command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start)

![img_1.png](img_1.webp)

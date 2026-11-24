---
title: "在 Windows 11 中打开传统右键菜单"
slug: "Windows 11の右键菜单を従来版に戻す方法"
tags: ["Windows11", "资源管理器"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "介绍如何通过“显示更多选项”在 Windows 11 中打开传统右键菜单，以及一种可能因系统版本而失效的注册表变通方法。"
date: "2024-03-30T13:13:36+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 在 Windows 11 中打开传统右键菜单

在 Windows 11 中，右键单击项目并选择“显示更多选项”，即可打开传统上下文菜单。选中项目后也可以按 `Shift`+`F10`，或按住 `Shift` 再右键单击以打开“显示更多选项”。请先使用这些系统内置方式。

> 下面的注册表修改是一种让传统菜单默认显示的非官方变通方法，并非 Microsoft 支持的操作步骤；它可能在某些 Windows 版本中无效。修改前请备份注册表。

## 注册表变通方法步骤

1. 打开注册表编辑器。

按下`Win键` + `R键`，输入`regedit`，然后按下`Enter键`。
![img_1.png](img_1.webp)　

2. 导航至 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`。如果该项不存在，则创建它。


3. 导航至 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`。如果该项不存在，则创建它。
4. 确认 `InprocServer32` 的 `(默认)` 值为空。

![img_2.png](img_2.webp)

5. 重启电脑。
6. 确认右键菜单已恢复为经典版。

如需撤销此更改，请删除自己创建的 `{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}` 项，然后重新启动文件资源管理器。修改现有设置前请先备份。

## 参考资料

- [Microsoft 支持：Windows 中的文件资源管理器](https://support.microsoft.com/en-us/windows/experience/fileexplorer/file-explorer-in-windows)
- [Microsoft 支持：Windows 键盘快捷方式](https://support.microsoft.com/en-us/accessibility/windows/keyboard-shortcuts-in-windows)

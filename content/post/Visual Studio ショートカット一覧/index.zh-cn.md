---
title: "Visual Studio 2022 快捷键大全【Windows】"
date: "2024-04-06T11:27:37+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Visual Studio ショートカット一覧"
tags: ["Visual Studio", "ショートカット"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "介绍 Windows 版 Visual Studio 2022 的 General 配置文件常用快捷键，涵盖生成、调试、编辑、搜索和导航。"
---

# Visual Studio 2022 快捷键

以下按 Windows 版 Visual Studio 2022 的默认 **General** 配置文件整理。它们与 Visual Studio for Mac 和 Visual Studio Code 的快捷键不同。键盘布局、所选配置文件和自定义设置都可能改变快捷键。

我们已对照 Microsoft 官方默认设置，修正了旧版中错误的书签、生成、搜索和替换快捷键。

## 帮助

| Shortcut | Command |
|---|---|
| `F1` | 打开帮助 |

## 生成与调试

| Shortcut | Command |
|---|---|
| `Ctrl+Shift+B` | 生成解决方案 |
| `F5` | 开始/继续调试 |
| `Ctrl+F5` | 开始执行但不调试 |
| `F9` | 切换断点 |
| `Ctrl+F9` | 启用断点 |
| `Ctrl+Shift+F9` | 删除所有断点 |
| `F10` | 逐过程 |
| `F11` | 逐语句 |
| `Shift+F11` | 跳出 |

## 代码导航

| Shortcut | Command |
|---|---|
| `F12` | 转到定义 |

## 编辑与导航

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+C` | 注释所选内容 |
| `Ctrl+K, then Ctrl+U` | 取消所选内容的注释 |

## 搜索与替换

| Shortcut | Command |
|---|---|
| `Ctrl+F` | 查找 |
| `Ctrl+H` | 替换 |
| `Ctrl+Shift+F` | 在文件中查找 |
| `Ctrl+Shift+H` | 在文件中替换 |

## 行导航

| Shortcut | Command |
|---|---|
| `Ctrl+G` | 转到行 |

## 编辑与导航

| Shortcut | Command |
|---|---|
| `Ctrl+L` | 剪切当前行 |
| `Ctrl+D` | 复制 |
| `Ctrl+Shift+V` | 循环粘贴剪贴板环 |

## 代码导航

| Shortcut | Command |
|---|---|
| `Ctrl+]` | 转到匹配的大括号 |
| `Ctrl+Shift+]` | 扩展选择至匹配的大括号 |
| `Alt+Up/Down Arrow` | 上移/下移所选行 |
| `Shift+Alt+Up/Down Arrow` | 向上/下扩展列选择 |

## 工具窗口与 Git

| Shortcut | Command |
|---|---|
| `Ctrl+Tab` | 下一个文档窗口 |
| `Ctrl+Alt+L` | 打开解决方案资源管理器 |
| `Ctrl+Shift+E` | 打开资源视图 |
| `Ctrl+0, then Ctrl+G` | 转到 Git Changes |
| `Ctrl+0, then Ctrl+O` | 转到 Git Commits |

## 书签

| Shortcut | Command |
|---|---|
| `Ctrl+K, then Ctrl+K` | 切换书签 |
| `Ctrl+K, then Ctrl+N` | 下一个书签 |
| `Ctrl+K, then Ctrl+P` | 上一个书签 |
| `Ctrl+K, then Ctrl+L` | 清除所有书签 |

## 查看或更改快捷键

在 Visual Studio 中打开 **Tools > Options > Environment > Keyboard**，搜索命令即可查看当前配置文件中的快捷键。组合序列需要按顺序输入，分段按键之间稍作停顿。键盘布局和语言设置也可能影响按键名称。

- [Keyboard shortcuts in Visual Studio (Windows)](https://learn.microsoft.com/en-us/visualstudio/ide/default-keyboard-shortcuts-in-visual-studio?view=vs-2022)

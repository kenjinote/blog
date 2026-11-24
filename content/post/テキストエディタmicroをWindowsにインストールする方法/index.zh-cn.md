---
title: '支持Windows！轻量级文本编辑器“micro”的安装方法'
slug: "文本编辑器microをWindowsに安装する方法"
date: "2024-03-31T21:50:39+09:00"
lastmod: "2026-11-25"
tags: ["micro", "文本编辑器"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '通俗易懂地讲解如何在Windows上安装可在命令提示符中流畅运行的终端文本编辑器“micro”，以及配置环境变量并使其可用的步骤。'
---

## 下载 micro
https://github.com/micro-editor/micro/releases/latest
在最新版本的 Assets 中，下载适用于 Windows x64 的压缩包（例如 `micro-<version>-win64.zip`），解压到任意文件夹。

如果使用 Windows ARM 设备，请改为选择对应的 ARM64 压缩包。

## 设置环境变量
为了在命令提示符中使用 `micro.exe`，需要设置环境变量。

1. 按 `Win` + `R`，输入 `sysdm.cpl`，然后按 `Enter`。
2. 打开“高级”选项卡，点击“环境变量”。
3. 在“用户变量”中选择自己账户的 `Path`，然后点击“编辑”。如果列表中没有 `Path`，请先新建。
4. 点击“新建”，添加包含 `micro.exe` 的文件夹路径。
5. 点击“确定”关闭对话框。
6. 重新打开命令提示符，运行 `micro` 确认可以启动。

## micro 的使用方法

在命令提示符中输入 `micro` 并执行，将显示如下界面。
![img_3.png](img_3.webp)

主要操作方法和快捷键如下：

| 快捷键 | 操作 | 
|--------|-----| 
| Ctrl+Q | 关闭当前文件（若这是最后一个文件，micro 将退出） |
| Ctrl+S | 保存文件 | 
| Ctrl+O | 打开文件 | 
| Ctrl+A | 全选 | 
| Ctrl+X | 剪切所选范围 | 
| Ctrl+C | 复制所选范围 | 
| Ctrl+V | 粘贴 | 
| Ctrl+Z | 撤销 | 
| Ctrl+Y | 重做 | 
| Ctrl+E | 执行编辑器命令 | 

## 参考
- [micro](https://micro-editor.github.io/)
- [Default key bindings](https://github.com/micro-editor/micro/blob/master/runtime/help/defaultkeys.md)

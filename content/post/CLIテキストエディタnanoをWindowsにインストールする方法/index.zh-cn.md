---
title: '在Windows上安装CLI文本编辑器nano的方法'
slug: "CLIテキストエディタnanoをWindowsにインストールする方法"
date: 2024-03-31T18:09:32+09:00
tags: ["nano", "文本编辑器"]
draft: false
image: "img_1.png"
categories: ["工具・开发环境"]
---

## 下载nano.exe
https://sourceforge.net/projects/nano-for-windows/

打开上述链接，点击`Download`下载`GNU-Nano_Win32(static).zip`。
解压zip文件，将`nano.exe`放置在任意文件夹中。
※不支持日语输入。（截至 2024/03/31）

## 设置环境变量
为了从命令提示符使用`nano.exe`，需要设置环境变量。

1. 按下`Win键` + `R键`，输入`sysdm.cpl`，然后按`Enter键`。
2. 点击`系统属性`中的`系统属性`。
3. 点击`环境变量`。
4. 选择`系统变量`中的`Path`，然后点击`编辑`。
5. 点击`新建`，添加`nano.exe`的路径。
6. 点击`确定`，关闭所有对话框。
7. 重新启动命令提示符，输入`nano`，检查是否可以运行。

## nano的使用方法

输入`nano`并运行后，将显示以下屏幕。

![img_2.png](img_2.png)

屏幕底部显示快捷键的说明。

符号的含义如下：

- `^` 代表 `Ctrl` 键。
- `M-` 代表 `Alt` 键。

要保存并关闭，请先按 `Ctrl` + `S`，然后再按 `Ctrl` + `X`。

## 参考
- [GNU nano](https://www.nano-editor.org/)

---
title: '在Windows上安装文本编辑器micro的方法'
date: 2024-03-31T21:50:39+09:00
tags: ["micro", "文本编辑器"]
draft: false
image: "img.png"
categories: ["工具・开发环境"]
---

## 下载 micro
https://github.com/zyedidia/micro/releases

打开上述链接，点击 `Show all XX assets` (X部分为数字)，然后下载 `micro-X.X.XX-win64.zip` (X部分为数字)。
解压 zip 文件，将所有文件放置在任意文件夹中。

## 设置环境变量
为了在命令提示符中使用 `micro.exe`，需要设置环境变量。

1. 按下 `Win键` + `R键`，输入 `sysdm.cpl` 并按 `Enter键`。
2. 点击 `系统属性` 中的 `系统属性`。
3. 点击 `环境变量`。
4. 选择 `系统环境变量` 中的 `Path`，然后点击 `编辑`。
5. 点击 `新建`，添加包含 `micro.exe` 的文件夹路径。
6. 点击 `确定`，关闭所有对话框。
7. 重新启动命令提示符，输入 `nano` 确认是否可以执行。

## micro 的使用方法

在命令提示符中输入 `micro` 并执行，将显示如下界面。
![img_3.png](img_3.png)

主要操作方法和快捷键如下：

| 快捷键 | 操作 | 
|--------|-----| 
| Ctrl+Q | 关闭文件 | 
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

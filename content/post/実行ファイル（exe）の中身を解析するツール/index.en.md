---
title: 'Tools for Analyzing the Contents of Executable Files (exe)'
slug: "実行ファイル（exe）の中身を解析するツール"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "executable file", "analysis"]
draft: false
image: "img_1.png"
categories: ["PC/Gadget"]
---

# What is an executable file (exe)?

A file that can be executed on Windows. It is basically written in what is called the PE format.
It contains machine code for execution, as well as resources such as icons and images.

There are several tools for analyzing executable files, so I will introduce them this time.

## 7-Zip

![img.png](img.png)

EXE files can become large in size, so they are sometimes created by compressing the file. In this case, by using the file compression/decompression software 7-Zip, you can decompress the executable file and examine its contents. There is also a tool called WinRAR that can decompress files in the same way.

## Resource Hacker
![img_2.png](img_2.png)

It allows you to extract resources (icons, bitmaps, dialog boxes, strings, etc.) within an EXE file. Also, since it functions as a binary editor, you can edit and rewrite the contents of an EXE file.

## PE Explorer
![img_3.png](img_3.png)

It can analyze PE files for Windows (EXE, DLL, OCX, SYS, drivers). PE Explorer provides various analysis features such as displaying file structures, file headers, directory entries, and exported functions and symbols.

## Dependency Walker
![img_4.png](img_4.png)

It allows you to examine the DLL files that an EXE file depends on, and verify whether they are loaded correctly. You can also trace the function calls of the DLL files.

These tools are useful for examining the contents of EXE files, but caution is required. Editing files or using them for unauthorized purposes may cause copyright or security problems, so please use them with full understanding.

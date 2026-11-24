---
title: '在IntelliJ IDEA中创建插入当前日期快捷键的方法'
slug: "IntelliJ IDEAで日期を貼り付ける命令を追加する"
date: 2022-09-04T05:59:04+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.webp"
categories: ["it-technology"]
description: '了解如何创建 IntelliJ IDEA Live Template，插入包含本地时区偏移的 ISO 8601 时间戳。本指南依据 JetBrains 当前文档介绍设置路径、日期表达式和模板展开按键。'
---

# 简介

如果写作时经常输入时间戳，可以使用 IntelliJ IDEA Live Template 通过简短缩写自动插入。本例创建包含计算机本地时间和时区偏移的 ISO 8601 时间戳。

## 创建 Live Template

1. 打开 **Settings > Editor > Live Templates**。在 Windows 或 Linux 上通过 **File > Settings** 打开；在 macOS 上通过 **IntelliJ IDEA > Settings** 打开。
2. 选择一个模板组（例如 **other**），然后点击 **+ > Live Template**。
3. 将 **Abbreviation** 设为 `date`，并填写简短的 **Description**。
4. 在 **Template text** 中输入 `$date$`。
5. 点击 **Edit Variables**。为 `date` 变量在 **Expression** 中输入 `date("yyyy-MM-dd'T'HH:mm:ssXXX")`。勾选 **Skip if defined**，以便展开模板时自动计算值。
6. 点击 **Define**，选择需要使用模板的上下文（适用时可选 **Everywhere**），然后保存设置。

## 使用模板

在编辑器中输入 `date` 并按默认展开键 **Tab**。IntelliJ IDEA 会插入当前系统日期和时间，例如 `2026-11-24T09:30:00+09:00`。时间和偏移取决于计算机当前时区。如果修改过展开键，请在 Live Templates 设置中确认。

格式中的 `XXX` 会生成 ISO 8601 时区偏移。表达式没有固定使用 `+09:00`，因此会采用每位读者计算机的本地时区。请确认生成的时间戳符合预期的发布时间。

## 参考资料

- [创建和编辑 Live Template](https://www.jetbrains.com/help/idea/creating-and-editing-live-templates.html)
- [Live Template 变量和 date 函数](https://www.jetbrains.com/help/idea/template-variables.html)
- [设置 Live Template 展开键](https://www.jetbrains.com/help/idea/settings-live-templates.html)

---
title: '创建 Windows 关机快捷方式'
slug: "Windows を关机する快捷方式を作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "关机", "快捷方式"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: '介绍如何在 Windows 10 和 Windows 11 桌面创建快捷方式，以便双击后启动关机。'
---
以下步骤适用于 Windows 10 和 Windows 11。菜单名称可能因系统版本和显示语言略有不同。

## 创建快捷方式

#### 1. 右键单击桌面空白处，选择“新建”>“快捷方式”。

#### 2. 在项目位置中输入以下命令，然后单击“下一步”。

```text
shutdown.exe /s /t 0
```

#### 3. 为快捷方式命名，例如“关机”，然后单击“完成”。

## 更改图标（可选）

右键单击快捷方式，选择“属性”>“更改图标”。从 `%SystemRoot%\System32\SHELL32.dll` 中选择一个图标，然后单击“确定”。

使用前请保存工作。此快捷方式会直接启动 Windows 关机流程，不会额外显示确认步骤。`/s` 表示关机，`/t 0` 表示不等待。命令未使用 `/f`，因此应用可以正常处理退出，并可能提示保存未完成的工作。

[**Microsoft Learn：shutdown 命令（英文）**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)

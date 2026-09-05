---
title: '将Windows 11的右键菜单恢复为经典版的方法'
date: 2024-03-30T13:13:36+09:00
tags: ["Windows11", "资源管理器"]
draft: false
image: "img.png"
categories: ["电脑・数码"]
---

# 将Windows 11的右键菜单恢复为经典版的方法

下面介绍如何将Windows 11的右键菜单恢复为经典版。

1. 打开注册表编辑器。

按下`Win键` + `R键`，输入`regedit`，然后按下`Enter键`。
![img_1.png](img_1.png)　

2. 导航至 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}`。如果该项不存在，则创建它。


4. 导航至 `HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32`。如果该项不存在，则创建它。
5. 确认 `InprocServer32` 的 `(默认)` 值为空。

![img_2.png](img_2.png)

6. 重启电脑。
7. 确认右键菜单已恢复为经典版。

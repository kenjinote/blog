---
title: "在 macOS 中切换 SMB 共享上的 .DS_Store 读取"
slug: "macOSで.DS_Storeを自動生成しないようにする命令"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "依据 Apple 官方说明，介绍如何在 macOS 中关闭或重新启用对 SMB 共享上 .DS_Store 文件的读取。此设置不会阻止文件生成，修改后需注销并重新登录。"
---
Apple 将此偏好设置作为加快 SMB 浏览速度的方法：让 macOS **不再读取 SMB 共享上的 `.DS_Store` 文件**。它不会阻止新文件生成，也不会删除已有文件。Finder 的显示和排序方式可能会因此改变。

### 关闭 SMB 共享上的读取

在“终端”中运行：

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

注销 macOS 账户并重新登录后，设置才会生效。Finder 显示文件夹时将使用基本信息，而不读取 `.DS_Store` 元数据。

### 重新启用读取

将该设置改为 `FALSE`，即可恢复默认行为：

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

随后注销并重新登录。Apple 将此方法作为 SMB 浏览设置进行说明，并指出该指南主要面向企业和教育机构管理员。详见 [Apple 支持](https://support.apple.com/en-us/102064)。

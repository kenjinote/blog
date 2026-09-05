---
title: '仅获取git仓库的最新内容'
date: 2024-04-27T02:54:12+09:00
tags: ["git", "仓库", "命令"]
draft: false
image: "img.png"
categories: ["工具·开发环境"]
---

# 仅获取仓库的最新内容

可以使用以下命令仅获取仓库的最新内容。
当您想要节省磁盘空间或快速获取仓库时，这非常有用。

```
git clone --depth 1 <仓库URL>
```

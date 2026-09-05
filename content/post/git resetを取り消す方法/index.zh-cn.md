---
title: '撤销git reset的方法'
date: 2024-05-15T23:32:43+09:00
tags: ["git", "恢复", "撤销"]
draft: false
image: "img.png"
categories: ["工具·开发环境"]
---
# 撤销git reset的方法
在执行 git commit 之后，如果不小心执行了 git reset，这里介绍撤销 git reset 的方法（即恢复到 git commit 时状态的方法）。

1. 使用 `git reflog` 确认重置前的提交 ID
2. 使用 `git reset --hard HEAD@{数字}` 恢复到重置前的状态

以上就是撤销 git reset 的方法。

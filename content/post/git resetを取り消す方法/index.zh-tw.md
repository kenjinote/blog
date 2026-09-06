---
title: "如何取消 git reset"
slug: "如何取消-git-reset"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "復原", "取消"]
draft: false
image: "img.png"
categories: ["工具與開發環境"]
---
# 如何取消 git reset
如果在進行 git commit 之後，不小心執行了 git reset，這裡介紹如何取消 git reset（如何復原到 git commit 時的狀態）。

1. 使用 `git reflog` 確認 reset 前的 commit ID
2. 使用 `git reset --hard HEAD@{數字}` 恢復到 reset 前的狀態

以上就是如何取消 git reset 的方法。

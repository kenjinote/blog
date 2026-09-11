---
title: '取消誤執行的git reset方法｜還原Commit步驟'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "復原", "取消"]
draft: false
image: "img.webp"
categories: ["工具與開發環境"]
description: '為您解說當在Git中不小心執行了「git reset」時，如何取消重置並還原到原本的Commit狀態。文章將清楚介紹使用「git reflog」確認Commit ID，並正確恢復狀態的步驟。'
---
# 如何取消 git reset
如果在進行 git commit 之後，不小心執行了 git reset，這裡介紹如何取消 git reset（如何復原到 git commit 時的狀態）。

1. 使用 `git reflog` 確認 reset 前的 commit ID
2. 使用 `git reset --hard HEAD@{數字}` 恢復到 reset 前的狀態

以上就是如何取消 git reset 的方法。

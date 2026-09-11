---
title: '在Git中刪除本機與遠端標籤(tag)的方法'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.webp"
categories: ["工具與開發環境"]
description: '簡單解說如何在Git中刪除不再需要的標籤（tag）。內容涵蓋透過「git tag -d」在本地環境刪除標籤，到使用「git push origin --delete」刪除遠端儲存庫上的標籤。'
---
# 刪除本地標籤

1. 使用 `git tag` 確認本地存在的標籤。
2. 使用 `git tag -d v0.1.0` 刪除標籤。（在 `v0.1.0` 的部分指定您要刪除的標籤）

# 刪除遠端標籤

1. 使用 `git ls-remote --tags` 確認遠端存在的標籤。
2. 使用 `git push origin --delete v0.1.0` 刪除遠端存在的標籤。（在 `v0.1.0` 的部分指定您要刪除的標籤）

## 參考
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)

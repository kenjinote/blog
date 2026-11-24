---
title: '在Git中刪除本機與遠端標籤(tag)的方法'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '簡單解說如何在Git中刪除不再需要的標籤（tag）。內容涵蓋透過「git tag -d」在本地環境刪除標籤，到使用「git push origin --delete」刪除遠端儲存庫上的標籤。'
---
# 刪除本地標籤

1. 使用 `git tag` 確認本地存在的標籤。
2. 使用 `git tag -d v0.1.0` 刪除標籤。（在 `v0.1.0` 的部分指定您要刪除的標籤）

# 刪除遠端標籤

1. 使用 `git ls-remote --tags --refs origin` 確認遠端存在的標籤。
2. 使用 `git push origin --delete v0.1.0` 刪除遠端存在的標籤。（在 `v0.1.0` 的部分指定您要刪除的標籤）

從遠端刪除標籤不會自動刪除協作者本機中的副本。此操作會影響遠端儲存庫的使用者，請先確認目標。

## 參考資料
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)

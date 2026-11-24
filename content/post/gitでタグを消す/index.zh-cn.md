---
title: '在Git中删除本地和远程标签（Tag）的方法'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '简单讲解如何在Git中删除不需要的标签（tag）。涵盖从使用“git tag -d”在本地环境中删除标签，到使用“git push origin --delete”删除远程仓库上标签的方法。'
---
# 删除本地标签

1. 使用 `git tag` 查看本地存在的标签。
2. 使用 `git tag -d v0.1.0` 删除标签。（将 `v0.1.0` 替换为你想要删除的标签）

# 删除远程标签

1. 使用 `git ls-remote --tags --refs origin` 查看远程存在的标签。
2. 使用 `git push origin --delete v0.1.0` 删除远程存在的标签。（将 `v0.1.0` 替换为你想要删除的标签）

从远程删除标签不会自动删除协作者本地的副本。此操作会影响远程仓库的使用者，请先确认目标。

## 参考资料
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)

---
title: "使用 reflog 恢复 git reset 前的提交"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "恢复", "撤销"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "通过 reflog 找到之前的 HEAD，先用分支保护，再了解 --hard 的风险。"
---

# 使用 reflog 恢复 git reset 前的提交

如果本地 reflog 仍保留 reset 前提交的引用，有时可以恢复。运行 `git reflog --date=local` 并选择正确的 `HEAD@{n}`；下方的 `HEAD@{1}` 仅为示例。

`git reset --hard` 会丢弃受跟踪文件中的未提交修改。先备份需要保留的工作，并使用尚不存在的救援分支名。reflog 无法恢复 hard reset 已丢弃的未提交编辑。若历史已共享，请先与协作者协调，通常可考虑 `git revert`。

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

请将 `HEAD@{1}` 替换为你选择的 reflog 编号，并将 `rescue-before-reset` 换成新的分支名。先检查提交并确认分支已创建，再运行最后一条命令。

## 参考资料

[git reset 官方手册](https://git-scm.com/docs/git-reset)

[git reflog 官方手册](https://git-scm.com/docs/git-reflog)

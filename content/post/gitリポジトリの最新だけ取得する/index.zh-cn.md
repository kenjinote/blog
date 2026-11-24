---
title: '如何浅克隆 Git 仓库'
slug: "git仓库の最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "仓库", "命令"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: '了解 git clone --depth 1 获取的内容、分支选择方式以及之后如何获取更多历史。'
---

# 浅克隆 Git 仓库

`git clone --depth 1` 会从所选分支的最新提交开始，创建历史深度为 1 的浅克隆。默认情况下，所选分支是远程仓库的默认分支。它会减少传输的提交历史，但当前文件和所需的 Git 对象仍会下载，因此含有大文件的仓库仍可能很大。

```sh
git clone --depth 1 <repository-url>
```

若要指定分支，请写出分支名：

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

之后可以继续获取更多历史，例如：

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

请将 `<directory>` 和 `<branch>` 换成实际名称。使用 `--depth` 时，除非另行覆盖，Git 也会启用 `--single-branch`。关于 `--unshallow` 等选项，请参阅 [`git clone`](https://git-scm.com/docs/git-clone) 和 [`git fetch`](https://git-scm.com/docs/git-fetch) 官方手册。

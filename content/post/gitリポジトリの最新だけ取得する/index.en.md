---
title: 'How to Clone a Git Repository with Shallow History'
slug: "gitRepositoryの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "repository", "command"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Learn what git clone --depth 1 transfers, how branch selection works, and how to fetch more history later.'
---

# Clone a repository with shallow history

`git clone --depth 1` creates a shallow clone with history depth one from the tip of the selected branch. By default, the selected branch is the remote's default branch. This reduces the amount of commit history transferred, but Git still downloads the current files and required objects, so a repository containing large files can still be large.

```sh
git clone --depth 1 <repository-url>
```

To select a branch explicitly, specify its name:

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

You can fetch more history later, for example:

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

Replace `<directory>` and `<branch>` with the names you use. With `--depth`, Git also implies `--single-branch` unless you override it. See the official [`git clone`](https://git-scm.com/docs/git-clone) and [`git fetch`](https://git-scm.com/docs/git-fetch) manuals for details, including `--unshallow`.

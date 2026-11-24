---
title: "Recover a Commit After git reset with reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "restore", "undo"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Find the previous HEAD with reflog, protect it with a branch, and understand the risks of --hard."
---

# Recover a Commit After git reset with reflog

Recovery may be possible if the local reflog still refers to the commit from before the reset. Check `git reflog --date=local` and choose the correct `HEAD@{n}` entry; `HEAD@{1}` below is only an example.

`git reset --hard` discards uncommitted changes to tracked files. Back up work you need first and choose a rescue branch name that does not exist. Reflog cannot restore uncommitted edits already lost to a hard reset. For shared history, coordinate with collaborators and usually consider `git revert`.

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Replace `HEAD@{1}` with the reflog entry you selected and `rescue-before-reset` with a new branch name. Inspect the commit and confirm the branch was created before running the final command.

## References

[Official git reset manual](https://git-scm.com/docs/git-reset)

[Official git reflog manual](https://git-scm.com/docs/git-reflog)

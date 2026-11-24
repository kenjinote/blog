---
title: "git reset後にコミットを復元する方法（reflog）"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "復元", "取り消し"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "reflogでreset前のHEADを特定し、退避ブランチを作ってから復元する方法と--hardの注意点を説明します。"
---

# git reset後にコミットを復元する方法（reflog）

reset直前のコミットへの参照がローカルreflogに残っていれば復元できる場合があります。`git reflog --date=local`で履歴を確認し、適切な`HEAD@{n}`を選んでください。下の`HEAD@{1}`は例です。

`git reset --hard`は追跡中のファイルにある未コミット変更を破棄します。必要な作業は先にバックアップし、存在しない退避ブランチ名を使ってください。すでにhard resetで失った未コミット編集はreflogでは戻せません。共有済み履歴では共同作業者と調整し、通常は`git revert`を検討します。

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```



## 参考

[git reset公式マニュアル](https://git-scm.com/docs/git-reset)

[git reflog公式マニュアル](https://git-scm.com/docs/git-reflog)

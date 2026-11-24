---
title: 'Gitでローカルとリモートのタグを削除する方法'
slug: "gitでタグを消す"
date: 2022-10-02T02:18:04+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["git"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Gitで不要になったタグ（tag）を削除する方法をシンプルに解説。「git tag -d」によるローカル環境でのタグ削除から、「git push origin --delete」を使ったリモートリポジトリ上のタグ削除まで網羅。'
---
# ローカルのタグを消す

1. `git tag` でローカルの存在するタグを確認する。
2. `git tag -d v0.1.0` でタグを消す。(`v0.1.0`の部分は消したいタグを指定する)

# リモートのタグを消す

1. `git ls-remote --tags --refs origin` でリモートの存在するタグを確認する。
2. `git push origin --delete v0.1.0` でリモートの存在するタグを消す。(`v0.1.0`の部分は消したいタグを指定する)

リモートからタグを削除しても、共同作業者のローカルにあるタグは自動では消えません。リモート利用者に影響するため、実行前に対象を確認してください。

タグを削除しても、そのタグが指していたコミットや他のブランチの履歴を直接削除するわけではありません。ただし、タグ名では参照できなくなります。`origin`はリモート名の例なので、必要に応じて置き換えてください。

## 参考
[git-tag](https://git-scm.com/docs/git-tag), [git-ls-remote](https://git-scm.com/docs/git-ls-remote), [git-push](https://git-scm.com/docs/git-push)

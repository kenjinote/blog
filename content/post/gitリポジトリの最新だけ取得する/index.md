---
title: 'Git cloneで浅い履歴のリポジトリを取得する方法'
slug: "gitリポジトリの最新だけ取得する"
date: 2024-04-27T02:54:12+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "リポジトリ", "コマンド"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'git clone --depth 1 の履歴範囲、ブランチ選択、後から履歴を追加する方法を解説します。'
---

# リポジトリの履歴を浅くして取得する

`git clone --depth 1` は、選択したブランチの先端から深さ1の履歴を取得する shallow clone です。通常は既定ブランチが対象となり、コミット履歴の転送量を減らせますが、現在のファイルや必要なGitオブジェクトは取得されます。そのため、大きなファイルを含むリポジトリ自体が必ず小さくなるわけではありません。

```sh
git clone --depth 1 <repository-url>
```

特定のブランチを対象にする場合は、ブランチ名を指定します。

```sh
git clone --depth 1 --single-branch --branch <branch> <repository-url>
```

履歴を後から追加するには、たとえば次のようにします。`<directory>`、`<branch>` は実際の名前に置き換えてください。

```sh
git -C <directory> fetch --deepen=50 origin <branch>
```

`--depth` を指定すると、明示的に解除しない限り既定で単一ブランチの履歴だけを取得します。深さを増やす必要があるときは [`git fetch`](https://git-scm.com/docs/git-fetch) の `--deepen` や `--unshallow` を使えます。詳しくは [`git clone` の公式マニュアル](https://git-scm.com/docs/git-clone)を参照してください。

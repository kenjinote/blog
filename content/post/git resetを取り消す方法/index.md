---
title: '誤って実行したgit resetを取り消す方法｜コミット復元手順'
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
tags: ["git", "復元", "取り消し"]
draft: false
image: "img.webp"
categories: ["ツール・開発環境"]
description: 'Gitで誤って「git reset」を実行してしまった際に、リセットを取り消して元のコミット状態に復元する方法を解説します。「git reflog」を使ってコミットIDを確認し、正しく状態を戻す手順を分かりやすく紹介します。'
---
# git resetを取り消す方法
git comitを行った後、誤ってgit resetを実行してしまった場合、git resetを取り消す方法(git commit時の状態を復元する方法)を紹介します。

1. `git reflog`でリセット前のコミットIDを確認
2. `git reset --hard HEAD@{数字}`でリセット前の状態に戻す

以上、git resetを取り消す方法でした。
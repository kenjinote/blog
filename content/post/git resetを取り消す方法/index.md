---
title: 'git resetを取り消す方法'
date: 2024-05-15T23:32:43+09:00
tags: ["git", "復元", "取り消し"]
draft: false
image: "img.png"
---
# git resetを取り消す方法
git comitを行った後、誤ってgit resetを実行してしまった場合、git resetを取り消す方法(git commit時の状態を復元する方法)を紹介します。

1. `git reflog`でリセット前のコミットIDを確認
2. `git reset --hard HEAD@{数字}`でリセット前の状態に戻す

以上、git resetを取り消す方法でした。
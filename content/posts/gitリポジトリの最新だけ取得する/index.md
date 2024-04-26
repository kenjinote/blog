---
title: 'gitリポジトリの最新だけ取得する'
date: 2024-04-27T02:54:12+09:00
tags: ["git", "リポジトリ", "コマンド"]
draft: false
cover:
  image: "/git.png"
  relative: true
---

# リポジトリの最新だけ取得する

以下のコマンドでリポジトリの最新だけを取得できます。
ディスク容量を節約するため、素早くリポジトリを取得したい場合に便利です。

```
git clone --depth 1 <リポジトリURL>
```
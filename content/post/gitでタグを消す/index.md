---
title: 'gitでタグを消す'
date: 2022-10-02T02:18:04+09:00
tags: ["git"]
draft: false
image: "img.png"
---
# ローカルのタグを消す

1. `git tag` でローカルの存在するタグを確認する。
2. `git tag -d v0.1.0` でタグを消す。(`v0.1.0`の部分は消したいタグを指定する)

# リモートのタグを消す

1. `git ls-remote --tags` でリモートの存在するタグを確認する。
2. `git push origin --delete v0.1.0` でリモートの存在するタグを消す。(`v0.1.0`の部分は消したいタグを指定する)

## 参考
[gitでtagをリモートとローカルで削除する方法！](https://qumeru.com/magazine/528)


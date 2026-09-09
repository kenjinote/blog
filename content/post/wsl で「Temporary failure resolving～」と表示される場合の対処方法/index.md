---
title: 'WSLのapt updateで「Temporary failure resolving」エラーが出た時の対処法'
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "対処方法"]
draft: false
image: "img.webp"
categories: ["ツール・開発環境"]
description: 'WSL環境で「sudo apt update」実行時に「Temporary failure resolving」エラーが出る場合の解決方法を解説します。DNSサーバーの設定を変更し、パッケージマネージャーの通信を正しく復旧させる手順を紹介します。'
---

# wslで「Temporary failure resolving～」と表示される場合の対処方法

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

wslで上記のエラーが表示されるときは、DNSサーバーの設定が正しくない可能性があります。
私の環境では、以下の手順で解決しました。

1. wslを起動します。
2. `sudo nano /etc/resolv.conf`を実行します。
3. `nameserver`の行を以下のように変更します。
```
nameserver 8.8.8.8
```
4. `Ctrl` + `S`で保存して、`Ctrl` + `X`で終了します。
5. `sudo apt update`を実行します。
6. エラーが表示されなければ、解決です。

## 上記手順で解決しない場合

上記手順で解決しない場合もあるようです。以下の記事をご参照ください。

- [WSLにてapt update時の『Temporary failure resolving ～』を解決する方法](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)


---
title: "解決在 wsl 中顯示「Temporary failure resolving～」錯誤的方法"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "対処方法"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# 解決在 wsl 中顯示「Temporary failure resolving～」錯誤的方法

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

當在 wsl 中顯示上述錯誤時，DNS 伺服器的設定可能不正確。
在我的環境中，透過以下步驟解決了這個問題。

1. 啟動 wsl。
2. 執行 `sudo nano /etc/resolv.conf`。
3. 將 `nameserver` 的行更改如下：
```
nameserver 8.8.8.8
```
4. 按 `Ctrl` + `S` 儲存，按 `Ctrl` + `X` 退出。
5. 執行 `sudo apt update`。
6. 如果沒有顯示錯誤，則表示已解決。

## 如果上述步驟無法解決

似乎有些情況下，上述步驟無法解決。請參考以下文章。

- [解決在 WSL 中進行 apt update 時出現『Temporary failure resolving ～』的方法](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

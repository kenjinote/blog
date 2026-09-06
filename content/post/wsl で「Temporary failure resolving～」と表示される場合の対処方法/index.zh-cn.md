---
title: '在 WSL 中出现“Temporary failure resolving～”时的解决方法'
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "解决方法"]
draft: false
image: "img.png"
categories: ["工具・开发环境"]
---

# 在 WSL 中出现“Temporary failure resolving～”时的解决方法

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

当在 WSL 中显示上述错误时，可能是 DNS 服务器的设置不正确。
在我的环境中，通过以下步骤解决了该问题。

1. 启动 WSL。
2. 运行 `sudo nano /etc/resolv.conf`。
3. 将 `nameserver` 的行更改如下：
```
nameserver 8.8.8.8
```
4. 按 `Ctrl` + `S` 保存，然后按 `Ctrl` + `X` 退出。
5. 运行 `sudo apt update`。
6. 如果没有显示错误，说明问题已解决。

## 如果上述步骤未能解决问题

似乎也有上述步骤无法解决问题的情况。请参考以下文章。

- [在 WSL 中 apt update 时出现『Temporary failure resolving ～』的解决方法](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

---
title: 'How to Fix "Temporary failure resolving..." Error in WSL'
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "troubleshooting"]
draft: false
image: "img.png"
categories: ["Tools & Development Environment"]
---

# How to Fix "Temporary failure resolving..." Error in WSL

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

When the above error appears in WSL, the DNS server settings might be incorrect.
In my environment, I solved it with the following steps.

1. Start WSL.
2. Run `sudo nano /etc/resolv.conf`.
3. Change the `nameserver` line as follows:
```
nameserver 8.8.8.8
```
4. Save with `Ctrl` + `S` and exit with `Ctrl` + `X`.
5. Run `sudo apt update`.
6. If the error doesn't appear, it's solved.

## If the above steps do not solve the issue

It seems there are cases where the above steps don't resolve the issue. Please refer to the following article:

- [How to resolve 'Temporary failure resolving ~' during apt update in WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

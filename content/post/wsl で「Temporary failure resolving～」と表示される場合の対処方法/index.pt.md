---
title: "Como resolver o erro 'Temporary failure resolving...' no wsl"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "対処方法"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# Como resolver o erro 'Temporary failure resolving...' no wsl

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

Quando o erro acima é exibido no wsl, as configurações do servidor DNS podem estar incorretas.
No meu ambiente, foi resolvido com os seguintes passos.

1. Inicie o wsl.
2. Execute `sudo nano /etc/resolv.conf`.
3. Altere a linha `nameserver` da seguinte forma:
```
nameserver 8.8.8.8
```
4. Salve com `Ctrl` + `S` e saia com `Ctrl` + `X`.
5. Execute `sudo apt update`.
6. Se o erro não for exibido, está resolvido.

## Se não for resolvido com os passos acima

Parece que há casos em que não é resolvido com os passos acima. Consulte o artigo a seguir.

- [Como resolver 'Temporary failure resolving...' durante o apt update no WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

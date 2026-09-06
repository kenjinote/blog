---
title: "Comment résoudre l'erreur 'Temporary failure resolving...' dans wsl"
slug: "wsl で「Temporary failure resolving～」と表示される場合の対処方法"
date: 2024-03-31T16:57:33+09:00
tags: ["wsl", "対処方法"]
draft: false
image: "img.png"
categories: ["ツール・開発環境"]
---

# Comment résoudre l'erreur 'Temporary failure resolving...' dans wsl

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

Lorsque l'erreur ci-dessus s'affiche dans wsl, les paramètres du serveur DNS peuvent être incorrects.
Dans mon environnement, cela a été résolu en suivant les étapes suivantes.

1. Démarrez wsl.
2. Exécutez `sudo nano /etc/resolv.conf`.
3. Modifiez la ligne `nameserver` comme suit :
```
nameserver 8.8.8.8
```
4. Enregistrez avec `Ctrl` + `S`, et quittez avec `Ctrl` + `X`.
5. Exécutez `sudo apt update`.
6. Si l'erreur ne s'affiche plus, c'est résolu.

## Si les étapes ci-dessus ne résolvent pas le problème

Il semble qu'il y ait des cas où les étapes ci-dessus ne suffisent pas. Veuillez consulter l'article suivant.

- [Comment résoudre 'Temporary failure resolving...' lors d'un apt update dans WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

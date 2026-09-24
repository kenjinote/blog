---
title: 'Was tun, wenn bei apt update in WSL der Fehler „Temporary failure resolving“ auftritt'
slug: "wsl で「Temporary failure resolving～」と表示される場合のLösung"
date: "2026-09-24T16:08:36+09:00"
tags: ["wsl", "Problemumgehung"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: 'Wir erklären, wie das Problem gelöst werden kann, wenn bei der Ausführung von „sudo apt update“ in einer WSL-Umgebung der Fehler „Temporary failure resolving“ auftritt. Wir zeigen Ihnen, wie Sie die Einstellungen des DNS-Servers ändern und die Kommunikation des Paketmanagers ordnungsgemäß wiederherstellen können.'
---

# So beheben Sie den Fehler 'Temporary failure resolving...' in wsl

```
kenji@MyComputer:~$ sudo apt update
[sudo] password for kenji:
Err:1 http://archive.ubuntu.com/ubuntu focal InRelease
  Temporary failure resolving 'archive.ubuntu.com'
```

Wenn der obige Fehler in wsl angezeigt wird, sind die DNS-Servereinstellungen möglicherweise falsch.
In meiner Umgebung wurde das Problem mit den folgenden Schritten behoben.

1. Starten Sie wsl.
2. Führen Sie `sudo nano /etc/resolv.conf` aus.
3. Ändern Sie die Zeile `nameserver` wie folgt:
```
nameserver 8.8.8.8
```
4. Speichern Sie mit `Strg` + `S` und beenden Sie mit `Strg` + `X`.
5. Führen Sie `sudo apt update` aus.
6. Wenn der Fehler nicht mehr angezeigt wird, ist das Problem behoben.

## Wenn das Problem durch die obigen Schritte nicht behoben wird

Es scheint Fälle zu geben, in denen die obigen Schritte nicht ausreichen. Bitte lesen Sie den folgenden Artikel.

- [So beheben Sie 'Temporary failure resolving...' beim apt update in WSL](https://qiita.com/ryosukeYamazaki/items/c04ec3ff78aac6eb8d26)

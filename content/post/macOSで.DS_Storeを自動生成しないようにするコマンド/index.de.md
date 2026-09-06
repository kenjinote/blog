---
title: "Befehl, um die automatische Generierung von .DS_Store unter macOS zu verhindern"
slug: "befehl-um-die-automatische-generierung-von-ds-store-unter-macos-zu-verhindern"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
---
Der Befehl, um die automatische Generierung von .DS_Store unter macOS zu verhindern, lautet wie folgt.
Bitte führen Sie ihn im Terminal aus.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
Starten Sie den Finder neu, nachdem Sie den Befehl ausgeführt haben.
```bash
killall Finder
```

Wenn Sie die Einstellungen wiederherstellen möchten, führen Sie bitte den folgenden Befehl aus.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Wenn Sie die Einstellungen wie oben beschrieben ändern, starten Sie den Finder neu.
```bash
killall Finder
```

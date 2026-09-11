---
title: 'Terminal-Befehl zur Deaktivierung/zum Stoppen der automatischen Generierung von .DS_Store unter macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・Gadget"]
description: 'Wir stellen einen Terminal-Befehl vor, der verhindert, dass unnötige „.DS_Store“-Dateien auf Netzlaufwerken usw. in einer macOS-Umgebung automatisch generiert werden. Die Methode zur Wiederherstellung der ursprünglichen Einstellungen und die Schritte zum Neustart des Finders sind ebenfalls zusammengefasst.'
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

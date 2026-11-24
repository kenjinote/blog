---
title: "Das Lesen von .DS_Store-Dateien auf SMB-Freigaben in macOS steuern"
slug: "macOSで.DS_Storeを自動生成しないようにするBefehl"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Nach Apples Anleitung lässt sich das Lesen von .DS_Store-Dateien auf SMB-Freigaben in macOS deaktivieren oder wieder aktivieren. Das verhindert nicht ihre Erstellung; melden Sie sich nach der Änderung ab und wieder an."
---
Apple beschreibt diese Einstellung als Möglichkeit, das Durchsuchen von SMB-Freigaben zu beschleunigen: macOS soll **`.DS_Store`-Dateien auf SMB-Freigaben nicht lesen**. Das verhindert weder das Erstellen neuer Dateien noch löscht es vorhandene Dateien. Anzeige und Sortierung im Finder können sich ändern.

### Lesen auf SMB-Freigaben deaktivieren

Führen Sie diesen Befehl im Terminal aus:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Melden Sie sich von Ihrem macOS-Account ab und wieder an, damit die Änderung wirksam wird. Der Finder verwendet beim Anzeigen von Ordnern grundlegende Informationen statt der `.DS_Store`-Metadaten.

### Lesen wieder aktivieren

Setzen Sie den Wert auf `FALSE`, um das Standardverhalten wiederherzustellen:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Melden Sie sich danach ab und wieder an. Apple beschreibt dies als Anpassung für SMB-Freigaben und richtet den Artikel vor allem an Administratoren in Unternehmen und Bildungseinrichtungen. Siehe den [Apple Support](https://support.apple.com/en-us/102064).

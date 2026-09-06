---
title: "Commande pour empêcher la génération automatique de .DS_Store sur macOS"
slug: "commande-pour-empecher-la-generation-automatique-de-ds-store-sur-macos"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.png"
categories: ["PC・Gadget"]
---
La commande pour empêcher la génération automatique de .DS_Store sur macOS est la suivante.
Veuillez l'exécuter dans le terminal.
```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```
Après avoir exécuté la commande, redémarrez le Finder.
```bash
killall Finder
```

Si vous souhaitez restaurer les paramètres, veuillez exécuter la commande suivante.
```bash
defaults delete com.apple.desktopservices DSDontWriteNetworkStores false
```
Comme ci-dessus, si vous modifiez les paramètres, redémarrez le Finder.
```bash
killall Finder
```

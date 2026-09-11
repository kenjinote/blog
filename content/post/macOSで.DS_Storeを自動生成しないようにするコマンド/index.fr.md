---
title: 'Commande Terminal pour désactiver et arrêter la génération automatique de .DS_Store sous macOS'
slug: "macOSで.DS_Storeを自動生成しないようにするコマンド"
date: 2022-09-12T16:03:42+09:00
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["PC・Gadget"]
description: 'Nous présentons une commande Terminal pour empêcher la génération automatique de fichiers « .DS_Store » inutiles sur des lecteurs réseau, etc., dans l''environnement macOS. Nous avons également résumé la méthode pour revenir aux paramètres d''origine et la procédure de redémarrage du Finder.'
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

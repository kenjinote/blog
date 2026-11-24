---
title: "Gérer la lecture de .DS_Store sur les partages SMB de macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするCommande"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Suivez les instructions d’Apple pour désactiver ou réactiver la lecture des fichiers .DS_Store sur les partages SMB de macOS. Cela n’empêche pas leur création ; déconnectez-vous puis reconnectez-vous après le changement."
---
Apple présente cette préférence comme un moyen d’accélérer la navigation SMB : elle demande à macOS de **ne pas lire les fichiers `.DS_Store` sur les partages SMB**. Elle n’empêche pas la création de nouveaux fichiers et ne supprime pas ceux qui existent déjà. L’affichage et le tri dans le Finder peuvent changer.

### Désactiver la lecture sur les partages SMB

Exécutez cette commande dans Terminal :

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Déconnectez-vous de votre compte macOS puis reconnectez-vous pour appliquer le changement. Le Finder utilisera des informations de base plutôt que les métadonnées `.DS_Store` pour afficher les dossiers.

### Réactiver la lecture

Réglez la valeur sur `FALSE` pour rétablir le comportement par défaut :

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Déconnectez-vous puis reconnectez-vous. Apple présente cette option comme un réglage de navigation SMB et précise que son article s’adresse aux administrateurs d’entreprise et du secteur éducatif. Consultez l’[assistance Apple](https://support.apple.com/en-us/102064).

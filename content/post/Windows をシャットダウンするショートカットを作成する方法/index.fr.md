---
title: 'Créer un raccourci pour arrêter Windows'
slug: "Windows をArrêtするRaccourciを作成する方法"
date: 2023-04-11T17:03:32+09:00
lastmod: "2026-11-25T00:00:00+09:00"
tags: ["Windows", "Arrêter", "Raccourci"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: 'Créez sur le bureau un raccourci qui lance l’arrêt de Windows 10 ou Windows 11 d’un double-clic.'
---
Ces étapes concernent Windows 10 et Windows 11. Les noms des menus peuvent varier légèrement selon la version et la langue d’affichage.

## Créer le raccourci

#### 1. Cliquez avec le bouton droit sur une zone vide du bureau, puis choisissez `Nouveau` > `Raccourci`.

#### 2. Saisissez cette commande comme emplacement de l’élément, puis cliquez sur `Suivant`.

```text
shutdown.exe /s /t 0
```

#### 3. Nommez le raccourci, par exemple `Arrêter Windows`, puis cliquez sur `Terminer`.

## Modifier l’icône (facultatif)

Cliquez avec le bouton droit sur le raccourci et choisissez `Propriétés` > `Changer d’icône`. Sélectionnez une icône dans `%SystemRoot%\System32\SHELL32.dll`, puis cliquez sur `OK`.

Enregistrez votre travail avant d’utiliser ce raccourci. Il lance l’arrêt de Windows sans étape de confirmation supplémentaire. `/s` demande l’arrêt et `/t 0` ne prévoit aucun délai. L’option `/f` est omise : les applications peuvent donc se fermer normalement et signaler les modifications non enregistrées.

[**Microsoft Learn : commande shutdown (en anglais)**](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown/)

---
title: "Utiliser yt-dlp.exe : télécharger des vidéos autorisées et convertir en MP3"
slug: "yt-dlp.exe による YouTube VidéoのTéléchargement方法"
tags: ["yt-dlp", "YouTube", "media tools"]
draft: false
image: "img_1.webp"
categories: ["it-technology"]
description: "Comment obtenir et mettre à jour yt-dlp.exe, enregistrer une vidéo et convertir l’audio en MP3. Respectez les droits sur les contenus et les conditions de YouTube."
date: "2024-09-03T14:09:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Utiliser yt-dlp.exe : télécharger des vidéos autorisées et convertir en MP3

yt-dlp est un outil libre en ligne de commande pour télécharger des vidéos et de l’audio. Ces exemples présentent les bases sous Windows.

## À utiliser uniquement si cela est autorisé

Utilisez yt-dlp uniquement pour les contenus dont vous détenez les droits ou pour lesquels vous avez l’autorisation du titulaire, et seulement si les conditions de YouTube et la loi applicable le permettent. Vous pouvez télécharger vos propres vidéos depuis YouTube Studio.

## Installation et mise à jour

Téléchargez `yt-dlp.exe` pour Windows depuis la page officielle des versions et placez-le dans un dossier. Ajoutez ce dossier à `PATH` pour exécuter l’outil depuis n’importe quel répertoire. Récupérez l’exécutable uniquement depuis les versions officielles.

```powershell
yt-dlp.exe --version
yt-dlp.exe -U
```

## Utilisation de base

Dans l’invite de commandes ou PowerShell, indiquez l’URL de la vidéo. Le fichier est enregistré dans le répertoire courant.

```powershell
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```

Pour convertir l’audio en MP3, utilisez `-x` et `--audio-format mp3`.

```powershell
yt-dlp.exe -x --audio-format mp3 "https://www.youtube.com/watch?v=VIDEO_ID"
```

Vérifiez la version avec `yt-dlp.exe --version`. Mettez à jour un binaire de version avec `yt-dlp.exe -U`. La conversion MP3 nécessite `ffmpeg` et `ffprobe`. Si l’extraction ne fonctionne plus après un changement de YouTube, mettez yt-dlp à jour et consultez les dépendances indiquées dans le README officiel.

Pour intégrer une miniature ou des métadonnées, ajoutez `--embed-thumbnail` ou `--embed-metadata` ; des outils supplémentaires peuvent être requis selon le format.

## En cas de problème

Installez la dernière version et consultez la documentation officielle pour connaître les dépendances et la prise en charge actuelles. Ne contournez pas les restrictions et ne téléchargez pas de contenu sans autorisation.

## Références

- [yt-dlp official releases](https://github.com/yt-dlp/yt-dlp/releases/latest)
- [yt-dlp README and documentation](https://github.com/yt-dlp/yt-dlp#readme)
- [YouTube Terms of Service](https://www.youtube.com/t/terms)
- [YouTube Help: download your own videos](https://support.google.com/youtube/answer/56100)

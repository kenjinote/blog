---
title: "Comment télécharger des vidéos YouTube avec yt-dlp.exe"
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Télécharger"]
draft: false
image: "img_1.png"
categories: ["Informatique/Technologie"]
---
# Qu'est-ce que yt-dlp

`yt-dlp` est un outil en ligne de commande pour télécharger des vidéos YouTube.
En plus de télécharger des vidéos, vous pouvez également les télécharger sous forme de fichiers musicaux au format mp3.

## Téléchargement et Installation

1. Téléchargez le dernier yt-dlp.exe depuis la [page des versions de yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).
2. Placez yt-dlp.exe dans n'importe quel dossier.
3. Ajoutez le chemin du dossier de yt-dlp.exe à la variable d'environnement Path.

## Comment utiliser

Exécutez yt-dlp.exe dans l'invite de commande et spécifiez l'URL de la vidéo YouTube.

```
yt-dlp.exe "https://www.youtube.com/watch?v=VIDEO_ID"
```
※ L'argument peut être uniquement la partie VIDEO_ID.

Pour télécharger sous forme de fichier musical mp3, exécutez la commande suivante :

```
yt-dlp.exe --extract-audio --audio-format mp3 --embed-thumbnail --add-metadata "https://www.youtube.com/watch?v=VIDEO_ID"
```

Avec cela, la vidéo sera téléchargée dans le répertoire courant où la commande a été exécutée.

C'est tout.

---
title: 'Utilisation de yt-dlp : Comment télécharger et enregistrer des vidéos et audios YouTube'
slug: "yt-dlp.exe による YouTube 動画のダウンロード方法"
date: 2024-09-03T14:09:26+09:00
tags: ["YouTube", "Télécharger"]
draft: false
image: "img_1.webp"
categories: ["Informatique/Technologie"]
description: 'Nous expliquons clairement comment télécharger et enregistrer des vidéos YouTube en haute qualité à l''aide de l''outil en ligne de commande ''yt-dlp'', ainsi que la procédure pour les extraire et les sauvegarder sous forme de fichiers audio mp3. Couvre tout, de l''installation à l''utilisation.'
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

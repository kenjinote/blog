---
title: "Paramètres ffmpeg pour iOS"
slug: "iOS 向けの ffmpeg パラメータ"
date: 2025-03-02T04:16:07+09:00
tags: ["iOS", "ffmpeg"]
draft: false
image: "img.png"
categories: ["PC・ガジェット"]
---

# Paramètres de conversion ffmpeg optimisés pour iOS

Voici la commande `ffmpeg` pour convertir des vidéos afin qu'elles puissent être lues de manière fluide sur les appareils iOS (iPhone et iPad).

```bash
ffmpeg -i input.mp4 \
-c:v libx264 -profile:v high -level 4.1 \
-vf "scale=1920:-2" -r 30 \
-crf 20 -preset slow \
-c:a aac -b:a 128k -ar 48000 \
-movflags +faststart output.mp4
```

### Signification de chaque option (explication brève)

| Option                        | Description                                          |
| ---------------------------- | ------------------------------------------- |
| `-i input.mp4`               | Fichier d'entrée (vidéo à convertir)                              |
| `-c:v libx264`               | Encodage vidéo avec H.264 (compatible iOS)                       |
| `-profile:v high -level 4.1` | Profil et niveau largement compatibles avec iOS                      |
| `-vf "scale=1920:-2"`        | Redimensionnement à 1920 px de large, la hauteur est ajustée automatiquement en conservant le ratio               |
| `-r 30`                      | Conversion à une fréquence d'images de 30 fps                             |
| `-crf 20`                    | Qualité vidéo (des valeurs plus faibles signifient une meilleure qualité, recommandé 18–23)                   |
| `-preset slow`               | Équilibre entre la vitesse d'encodage et le taux de compression (slow signifie haute compression et haute qualité)              |
| `-c:a aac`                   | L'audio est encodé au format AAC                              |
| `-b:a 128k`                  | Définir le débit binaire audio à 128 kbps                         |
| `-ar 48000`                  | Définir le taux d'échantillonnage audio à 48 kHz (recommandé pour iOS)                |
| `-movflags +faststart`       | Place un index au début de la vidéo pour **accélérer la lecture en streaming sur le Web et iOS** |

---

Les vidéos converties avec ces paramètres devraient offrir une grande compatibilité et une lecture fluide sur les appareils Apple tels que l'iPhone et l'iPad.

---

Si nécessaire, vous pouvez ajuster la taille du fichier et la qualité de l'image en modifiant la résolution et le débit binaire. Si une haute qualité d'image est requise, essayez de définir `-crf` autour de 18 ; si vous souhaitez réduire la taille du fichier, définissez-le entre 22 et 25.

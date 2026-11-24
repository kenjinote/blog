---
title: 'Explication simple : Comment appliquer une mosaïque sur une zone spécifique d''une image avec paint.net'
slug: "paint.netでImageの特定個所にモザイクをかける方法"
tags: ["paint.net", "pixellisation", "retouche d’image", "vie privée"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "Comment appliquer l’effet Pixelate de paint.net à une sélection et régler Cell Size et les modes de mise à l’échelle. La pixellisation ne garantit pas un masquage sûr ; une méthode plus fiable est également présentée."
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


Je vais vous montrer comment appliquer une mosaïque à des parties spécifiques d'une image en utilisant paint.net.

Lors du téléchargement d'images sur Internet, il peut y avoir des cas où vous souhaitez appliquer une mosaïque à des parties spécifiques de l'image. Avec paint.net, vous pouvez traiter les images rapidement.

## Procédure

#### 1. Ouvrez l'image sur laquelle vous souhaitez appliquer la mosaïque dans paint.net
#### 2. Utilisez l'outil de sélection pour sélectionner la zone à masquer (sélection multiple possible)

![img_2.png](img_2.webp)

#### 3. Sélectionnez Menu > Effets > Déformer > Mosaïque

![img_1.png](img_1.webp)

- Cell Size détermine la taille des pixels agrandis. Une valeur plus élevée crée de plus grands carrés, sans garantir que les informations soient masquées de façon sûre.
- Pour obtenir des blocs carrés, choisissez `Multisample Bilinear` dans [Scale Down] et `Nearest Neighbor` dans [Scale Up].

Fermez la boîte de dialogue avec `OK`.

#### 4. L'image sera traitée avec la mosaïque, puis enregistrez l'image.

![img.png](img.webp)

## Note sur la confidentialité

Pour masquer de manière fiable des données personnelles ou d’autres informations, ne vous fiez pas uniquement à la pixellisation ou au flou. Recouvrez-les entièrement d’une couleur opaque unie, exportez en PNG ou JPEG sans calques ni historique de modification, puis vérifiez le fichier exporté. Conservez séparément et en lieu sûr l’original modifiable.

C'est tout.

## Références

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)

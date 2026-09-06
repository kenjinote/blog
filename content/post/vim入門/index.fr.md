---
title: "Introduction à vim"
slug: "vim入門"
date: 2024-04-19T22:06:34+09:00
tags: ["vim", "éditeur de texte"]
draft: false
image: "img.png"
categories: ["Outils et Environnement de Développement"]
---

![img_1.png](img_1.png)

# Introduction à vim

## Téléchargement et Installation

[https://www.vim.org/download.php](https://www.vim.org/download.php)

À partir du site ci-dessus, téléchargez et installez le module approprié pour votre système d'exploitation.

Pour Windows, choisir `gvim_X.X.X_x64_signed.exe` est une bonne option.

## Comment Démarrer

Sous Windows, il est nécessaire d'enregistrer le dossier contenant `vim.exe` dans la variable d'environnement Path.

Comment démarrer :

```
vim
```

Pour démarrer en spécifiant un nom de fichier :

```
vim filename.txt
```

## Comment Quitter

Pour quitter, tapez `:` (deux-points), puis `q`, et appuyez sur Entrée.
```
:q
```

Si le fichier a été modifié, le message `Aucune écriture depuis la dernière modification (ajoutez ! pour forcer)` s'affichera.
Vous pouvez forcer la fermeture en abandonnant les modifications.
```
:q!
```

Pour sauvegarder le fichier et quitter :
```
:wq
```

Ce qui suit a également la même signification :
```
:x
```

Vous pouvez également quitter en maintenant `Shift` et en appuyant deux fois sur `z`. (Équivalent à :wq)

## Modes

Le vim possède un `Mode Commande` et un `Mode Insertion`. Au démarrage de vim, il est en `Mode Commande`, et appuyer sur la touche `i` passe en `Mode Insertion`.

En `Mode Insertion`, comme son nom l'indique, vous pouvez saisir du texte. Pour revenir du `Mode Insertion` au `Mode Commande`, appuyez sur la touche `ESC`.

Cette bascule entre les modes d'insertion est une caractéristique clé de vim.

## Déplacement du Curseur et Défilement

Résumé des déplacements du curseur et du défilement en `Mode Commande`.

| Touche                               | Description                      |
|------------------------------------|-------------------------|
| `h` (ou `Ctrl`+`H`, `BackSpace`, `←`) | Déplacer vers la gauche |
| `j` (ou `Ctrl`+`J` / `N`, `↓`)         | Déplacer vers le bas    |
| `k` (ou `Ctrl`+`P`, `↑`)             | Déplacer vers le haut   |
| `l` (ou `Space`, `→`)               | Déplacer vers la droite |
| `+` (ou `Enter`)                   | Déplacer au début de la ligne suivante |
| `-`                                | Déplacer au début de la ligne précédente |
| `Ctrl`+`B` (ou `PageUp`)            | Faire défiler vers le haut (page) |
| `Ctrl`+`F` (ou `PageDown`)          | Faire défiler vers le bas (page) |
| `Ctrl`+`U`                         | Faire défiler d'une demi-page vers le haut |
| `Ctrl`+`D`                         | Faire défiler d'une demi-page vers le bas |
| `Ctrl`+`Y`                         | Faire défiler d'une ligne vers le haut |
| `Ctrl`+`E`                         | Faire défiler d'une ligne vers le bas |
| `z` `Enter`                        | Faire défiler la ligne du curseur vers le haut de l'écran |
| `z` `.`                            | Faire défiler la ligne du curseur vers le centre de l'écran |
| `z` `-`                            | Faire défiler la ligne du curseur vers le bas de l'écran |
| `0` (ou `\|`)                       | Déplacer le curseur au début de la ligne |
| `$`                                | Déplacer le curseur à la fin de la ligne |
| `^` (ou `_`)                        | Déplacer le curseur au début de la ligne (hors espaces et Tab) |
| `G` (ou `:$`)                       | Déplacer le curseur à la dernière ligne |
| `:numéro_de_ligne` `Enter`                     | Déplacer à la ligne spécifiée |

En tapant un `chiffre` avant les touches de déplacement ci-dessus, vous pouvez vous déplacer de cette quantité plusieurs fois.
(Par exemple, taper `3j` vous déplacera de 3 lignes vers le bas à partir de la position actuelle du curseur.)

## Autres Commandes

| Touche       | Description                  |
|------------|----------------------|
| `Ctrl`+`L` | Redessiner l'écran           |
| `Ctrl`+`G` | Afficher le nombre total de lignes, la position du curseur, etc. |

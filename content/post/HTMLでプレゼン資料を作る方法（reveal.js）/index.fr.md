---
date: 2023-04-06T23:23:46+09:00
lastmod: 2026-11-23
title: 'Comment utiliser reveal.js : Créer des présentations avec HTML et Markdown'
slug: "HTMLでPrésentation資料を作る方法（reveal.js）"
tags: ["HTML", "reveal.js", "Présentation"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Nous expliquons l''installation et l''utilisation de base de « reveal.js », un outil qui permet de créer des présentations de manière intuitive en utilisant HTML et Markdown. Nous présentons son utilisation qui prend en charge les animations et l''exportation en PDF, et qui se combine parfaitement avec le contrôle de version tel que Git.'
---

# Comment créer des présentations avec HTML

reveal.js est un outil de création de présentations utilisant HTML et Markdown, qui possède les fonctionnalités suivantes :

- Diverses fonctions de présentation telles que des formules mathématiques, des animations et des opérations de balayage
- Thèmes et mises en page personnalisables
- Fonctions de navigation prises en charge par plusieurs appareils, tels que la souris, le clavier et le pavé tactile
- Fournit des fonctionnalités avancées, telles que la lecture automatique des diapositives et les vidéos intégrées
- Peut être exporté au format PDF

Grâce à ces fonctionnalités, les utilisateurs peuvent facilement créer des présentations interactives et attrayantes.

# Installation et utilisation de reveal.js

La façon la plus simple de l'utiliser est de télécharger et d'extraire l'intégralité du fichier ZIP à partir de la page suivante.

1. Ouvrez [https://revealjs.com/installation](https://revealjs.com/installation) et téléchargez `master.zip` à partir du lien
2. Ouvrez le fichier index.html dans le dossier extrait dans un navigateur
3. Réécrivez index.html pour créer votre propre matériel de présentation

※ Comme le code HTML de démonstration est écrit dans demo.html, vous pouvez l'utiliser comme référence.

# Comment utiliser

Les présentations que vous créez peuvent être publiées telles quelles sous forme de pages Web ou exportées sous forme de fichiers PDF.
De plus, la source de la présentation étant du texte, il est facile de la gérer avec un système de contrôle de version.

Il semble également possible de créer du matériel de présentation au format Markdown.

# Créer des diapositives

La méthode la plus simple consiste à télécharger le ZIP Basic Setup le plus récent, à le décompresser et à modifier `index.html`. Comme dans l’exemple HTML ci-dessous, placez chaque diapositive dans un `<section>`. Le fichier fourni contient déjà les styles et le code d’initialisation nécessaires.

```html
<div class="reveal">
  <div class="slides">
    <section>Slide 1</section>
    <section>Slide 2</section>
    <section>Reveal this item <span class="fragment">when activated</span></section>
  </div>
</div>
```

# Écrire les diapositives en Markdown

Le plugin Markdown fourni permet d’écrire du Markdown dans le fichier HTML. Séparez les diapositives horizontales avec `---` et ajoutez l’exemple ci-dessous à `index.html`. Le chargement d’un fichier Markdown externe nécessite un serveur web local.

```html
<section data-markdown>
  <textarea data-template>
## Slide 1
---
## Slide 2
  </textarea>
</section>
```

# Configuration de développement

Pour disposer d’un serveur local ou des outils de développement des sources, utilisez le Full Setup officiel. Exécutez les commandes suivantes, puis ouvrez `http://localhost:8000` dans un navigateur.

```sh
git clone https://github.com/hakimel/reveal.js.git
cd reveal.js
npm install
npm start
```

# Exporter en PDF

Ajoutez `?print-pdf` à la fin de l’URL. Dans Chrome ou Chromium, choisissez l’enregistrement au format PDF, l’orientation paysage, aucune marge et les graphiques d’arrière-plan. Le guide officiel confirme Chrome et Chromium.

# Notes du présentateur

Appuyez sur `S` pour ouvrir la vue présentateur dans une fenêtre distincte. Ajoutez les notes dans `<aside class="notes">` sur une diapositive. La vue présentateur en local nécessite un serveur web.

```html
<section>
  <h2>Slide</h2>
  <aside class="notes">Notes visible to the presenter only</aside>
</section>
```

# Documentation officielle

- [Installation](https://revealjs.com/installation/)
- [Markup](https://revealjs.com/markup/)
- [Markdown](https://revealjs.com/markdown/)
- [Fragments](https://revealjs.com/fragments/)
- [PDF export](https://revealjs.com/pdf-export/)
- [Speaker view](https://revealjs.com/speaker-view/)

Vérifiez les droits d’utilisation des images et vidéos de vos diapositives, et assurez-vous que les supports publics ne contiennent ni informations confidentielles ni notes privées du présentateur.

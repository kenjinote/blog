---
title: "Redimensionner et repositionner les couvertures dans les listes PaperMod"
slug: "PaperModのImageの配置変更"
tags: ["HUGO", "PaperMod"]
draft: false
image: "images/img.webp"
categories: ["blogging"]
description: "Utilisez le CSS étendu de PaperMod et CSS Grid pour réduire les images de couverture des cartes et les placer à côté du résumé."
date: "2022-09-11T18:50:40+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

Cet exemple réduit les images de couverture des cartes dans les listes PaperMod et les place sous le titre, à côté du résumé. Il utilise le CSS étendu du site au lieu de modifier les feuilles de style ou modèles fournis avec le thème. Les sélecteurs ciblent des classes PaperMod ; vérifiez donc le résultat dans un navigateur après toute mise à jour du thème.

## Ajouter du CSS étendu

Créez `assets/css/extended/custom.css` à la racine du site. PaperMod intègre les feuilles de style de ce dossier à ses styles. CSS Grid modifie la disposition visuelle sans changer la structure HTML existante.

```css
/* Add to assets/css/extended/custom.css */
.post-entry {
    display: grid;
    grid-template-columns: minmax(0, 150px) minmax(0, 1fr);
    grid-template-areas:
        "cover title"
        "cover summary"
        "cover meta";
    column-gap: 1rem;
    align-items: start;
}

.post-entry > .entry-cover {
    grid-area: cover;
    margin-bottom: 0;
}

.post-entry > .entry-header {
    grid-area: title;
    min-width: 0;
}

.post-entry > .entry-content {
    grid-area: summary;
    min-width: 0;
}

.post-entry > .entry-footer {
    grid-area: meta;
}

.post-entry .entry-cover img {
    display: block;
    width: 100%;
    height: auto;
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: minmax(0, 96px) minmax(0, 1fr);
        column-gap: 0.75rem;
    }
}
```

## Adapter aux petits écrans

Réduisez la largeur de colonne et l’espacement sur les petits écrans pour garder un résumé lisible. Ajustez les 150 px et le point de rupture selon votre mise en page. `height: auto` conserve les proportions de l’image. N’ajoutez `aspect-ratio` et `object-fit: cover` que si vous voulez recadrer les images dans une forme uniforme.

## Éviter de modifier les fichiers du thème

PaperMod décrit `blank.css` comme un fichier vide de remplacement utilisé lorsque le dossier CSS étendu ne contient aucun fichier. Il n’est pas nécessaire de modifier le `post-entry.css` du thème ni de supprimer la ligne commentée `/* width: 100%; */` : retirer un commentaire CSS ne change pas le style. Pour modifier la structure HTML, vous pouvez copier un modèle dans le dossier `layouts/` du site et le remplacer, mais cette copie devra être entretenue lorsque le thème évolue.

## Vérifier la mise en page

Lancez Hugo et vérifiez les listes d’accueil, de tags et de catégories sur grand et petit écran. L’image, le titre, le résumé et les métadonnées ne doivent pas se chevaucher ; le lien couvrant toute la carte doit rester utilisable. Si une mise à jour du thème change les classes ou le HTML, adaptez le CSS. Cet exemple concerne les couvertures des listes, pas les images du corps des articles.

## Références

- [PaperMod FAQ: bundling custom CSS and overriding templates](https://github.com/adityatelange/hugo-PaperMod/wiki/FAQs)
- [PaperMod: current post-entry CSS selectors](https://github.com/adityatelange/hugo-PaperMod/blob/master/assets/css/common/post-entry.css)
- [PaperMod discussion #159](https://github.com/adityatelange/hugo-PaperMod/discussions/159#discussioncomment-247844)

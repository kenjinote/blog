---
title: "Cocher ou décocher toutes les cases d’une page Web"
slug: "Webページ内のすべてのチェックボックスを全チェックする"
tags: ["javascript", "checkbox", "bookmarklet"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: "Utilisez JavaScript ou un bookmarklet pour cocher ou décocher les cases activées de la page actuelle. Vérifiez le comportement de la page avant d’exécuter le code."
date: "2022-10-05T20:07:06+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Cocher ou décocher toutes les cases d’une page Web

Ce script clique sur les cases activées de la page actuelle afin de les modifier en une seule fois.

## Avant l’exécution

N’exécutez ce code que sur des pages de confiance. La page peut réagir aux clics en modifiant des paramètres ou en envoyant des requêtes. Vérifiez le résultat avant d’envoyer ou d’enregistrer quoi que ce soit.

## Exécuter dans DevTools

Ouvrez la page cible et exécutez le code ci-dessous dans la Console de DevTools. Si F12 n’ouvre pas DevTools dans votre navigateur, utilisez le menu du navigateur.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (!box.checked) box.click();
}
```

Pour décocher toutes les cases activées, utilisez ce code.

```js
const boxes = document.querySelectorAll('input[type="checkbox"]:not(:disabled)');
for (const box of boxes) {
  if (box.checked) box.click();
}
```

## Créer un bookmarklet

Créez un favori et collez le code sur une seule ligne dans le champ URL à l’aide de l’éditeur de favoris. Ne le saisissez pas dans la barre d’adresse. Sélectionnez le favori sur la page cible pour cocher les cases activées.

**Select all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(!box.checked)box.click()})();
```

**Clear all:**

```text
javascript:(()=>{for(const box of document.querySelectorAll('input[type="checkbox"]:not(:disabled)'))if(box.checked)box.click()})();
```

Pour tout décocher, utilisez le deuxième exemple ou le bookmarklet de désélection. Le script agit uniquement sur le document actuel et ignore les cases désactivées.

Modifier uniquement la propriété `.checked` peut ne pas notifier le code de la page avec les événements normalement associés à un clic. `.click()` déclenche le comportement du clic ; la logique propre à la page peut toutefois empêcher certaines modifications.

## Références

- [MDN: HTMLElement.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click)
- [MDN: HTMLInputElement.checked](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checked)
- [MDN: change event](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)

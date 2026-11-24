---
title: 'Qu''est-ce que l''i18n (Internationalisation) ? Signification et éléments de compatibilité dans le développement de logiciels'
slug: "i18nとは？"
tags: ["Internationalization", "i18n", "Terminologie"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'Nous expliquons clairement la signification et l''étymologie de l''« i18n » (Internationalisation) dont on entend souvent parler dans le développement de logiciels. Nous avons résumé les principaux éléments à prendre en compte lors de l''adaptation mondiale d''une application ou d''un système, tels que le codage des caractères, l''affichage des dates et heures, et les informations sur les devises.'
date: "2023-04-07T00:42:02+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


# Qu'est-ce que l'i18n ?

## Internationalisation et localisation

L’internationalisation consiste à concevoir et développer un produit pour faciliter son adaptation à différentes langues, régions et cultures. La localisation (l10n) l’adapte à une locale précise. L’internationalisation (i18n) n’est pas la traduction ; elle facilite la traduction et les autres adaptations locales.

`i18n` est l'abréviation de `Internationalization`, qui signifie internationalisation. Comme `Internationalization` est long,
il est abrégé en `i18n` car il y a 18 lettres entre le premier `i` et le dernier `n`.

Il est souvent utilisé dans le contexte de l'internationalisation des logiciels.

Les principaux éléments à prendre en compte lors de l'internationalisation sont les suivants :

- Texte et langue (Unicode, encodage des caractères, balises de langue, couverture des polices et rendu du texte)
- Direction du texte (de gauche à droite, de droite à gauche, de haut en bas vers la gauche, etc.)
- Langue / Texte
- Polices
- Formats
  - Nombres (caractère décimal, séparateur de milliers, nombre de chiffres à grouper, etc.)
  - Date et heure (format de la date, différences dans les calendriers utilisés comme Islamique / Grégorien / Juif / Japonais, etc.)
- Différences de fuseau horaire dans les informations de date et d'heure
- Informations sur les devises

- Chaînes et messages (séparez le texte visible du code, gérez les pluriels et l’ordre des mots de chaque langue, sans concaténer des fragments de phrase)
- Données régionales (noms, adresses, numéros de téléphone, méthodes de saisie, claviers, symboles, couleurs, lois et attentes culturelles)

## Tests

La pseudo-localisation révèle les textes qui s’allongent et les chaînes non traduites. Testez mise en page, saisie, tri et formats de nombres/dates pour chaque langue et locale. Pour les langues RTL, vérifiez l’interface et les textes bidirectionnels.

## References

- [W3C: Localization vs. Internationalization](https://www.w3.org/International/questions/qa-i18n)
- [W3C Internationalization Glossary](https://www.w3.org/TR/i18n-glossary/)
- [Unicode CLDR: Common Locale Data & Rules](https://www.unicode.org/reports/tr35/)

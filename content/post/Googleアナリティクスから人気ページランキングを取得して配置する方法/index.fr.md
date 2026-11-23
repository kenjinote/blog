---
title: 'Afficher dans Hugo un classement des pages GA4 avec Ranklet4'
date: 2023-04-10T20:26:57+09:00
lastmod: 2026-11-23




slug: "Google Analyticsから人気ページランキングを取得して配置する方法"
tags: ["Google Analytics", "Ranklet", "HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Utilisez Ranklet4, successeur GA4 du widget Ranklet arrêté, pour afficher dans Hugo un classement des pages populaires. Ce guide présente la migration, les autorisations, les modèles et les précautions liées aux services tiers.'
---

# Afficher dans Hugo un classement des pages GA4 avec Ranklet4

L'ancienne procédure utilisait les vues Google Analytics et l'ancien widget Ranklet. Ce service a pris fin en 2023. Remplacez son ancienne balise par une nouvelle balise Ranklet4, un service distinct compatible avec GA4. Consultez l'[avis officiel de migration](https://docs.ranklet4.com/changes.html).

Ranklet4 agrège les données de rapports GA4 et diffuse le classement sous forme de widget JavaScript, y compris sur un site statique comme Hugo. Les menus et les offres peuvent évoluer ; suivez le [tutoriel officiel](https://docs.ranklet4.com/tutorial.html).

## Avant de commencer

* Vous devez disposer d'une propriété GA4 qui enregistre les visites du site.
* Le compte Google utilisé pour la connexion doit avoir au moins le rôle **Lecteur** sur cette propriété. Un compte administrateur n'est pas nécessaire.
* Ranklet4 aura accès aux données Google Analytics. Les conditions accordent une licence étendue pour utiliser, copier, distribuer, créer des œuvres dérivées, afficher et exécuter ces données ; elles autorisent aussi l'utilisation et la publication de statistiques non identifiantes. Avant la connexion, lisez les [conditions](https://docs.ranklet4.com/agreement.html), la [politique de confidentialité](https://ranklet4.com/docs/privacy) et vérifiez que vous avez le droit de partager ces données.

## Créer et publier un classement

1. Connectez-vous à [Ranklet4](https://ranklet4.com/) avec un compte pouvant consulter la propriété GA4 visée. Vérifiez les autorisations demandées avant de les accorder.
2. Créez un classement, puis sélectionnez la propriété GA4, la période d'analyse et le nombre d'entrées. Ajoutez des filtres sur le titre ou l'URL pour exclure, par exemple, la page d'accueil.
3. Si nécessaire, configurez le remplacement de texte des titres et vérifiez le résultat dans l'aperçu.
4. Choisissez un modèle dans la galerie ou personnalisez le HTML/CSS. Les nouveaux modèles utilisent Handlebars ; consultez le [guide des modèles](https://docs.ranklet4.com/template.html) pour les champs et la syntaxe.
5. Enregistrez et publiez le classement, puis copiez la balise générée dans l'interface. Ne réutilisez pas l'ancienne balise ou l'ancien identifiant Ranklet.

Exemple minimal de modèle HTML. Consultez le guide officiel pour connaître les champs et la syntaxe de boucle pris en charge.

```handlebars
<ol class="popular-pages">
  {{#each rankings}}
  <li><a href="{{url}}">{{title}}</a></li>
  {{/each}}
</ol>
```

## L'ajouter à Hugo

1. Créez `layouts/partials/ranklet4.html` et collez-y la balise exacte générée par Ranklet4.
2. Ajoutez cet appel Hugo au modèle où vous voulez afficher le classement, par exemple dans `layouts/_default/single.html` ou un partial de barre latérale :

```go-html-template
{{- partial "ranklet4.html" . }}
```

3. Prévisualisez la page en local, puis vérifiez après publication que le widget se charge en HTTPS. Il dépend d'un JavaScript tiers : tenez compte du temps de chargement, des informations de confidentialité et de la sécurité du site.

## Actualisation et migration

Le classement dépend des rapports GA4 et du calendrier de mise à jour Ranklet4 ; une visite ne modifie donc pas forcément le résultat immédiatement. La fréquence, les fonctions des offres, les crédits et les règles publicitaires peuvent changer. Consultez les [offres actuelles](https://docs.ranklet4.com/plan.html). Le robot Ranklet4 lit les informations des pages publiques ; voir la [FAQ](https://docs.ranklet4.com/faq.html).

## Références officielles

* [Tutoriel officiel Ranklet4](https://docs.ranklet4.com/tutorial.html)
* [Changements depuis l'ancien Ranklet](https://docs.ranklet4.com/changes.html)
* [Guide des modèles Ranklet4](https://docs.ranklet4.com/template.html)
* [FAQ Ranklet4](https://docs.ranklet4.com/faq.html)
* [Conditions d'utilisation Ranklet4](https://docs.ranklet4.com/agreement.html)
* [Politique de confidentialité Ranklet4](https://ranklet4.com/docs/privacy)

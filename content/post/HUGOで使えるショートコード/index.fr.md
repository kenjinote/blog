---
date: 2022-09-11T22:59:52+09:00
lastmod: 2026-11-23
title: 'Shortcodes intégrés de Hugo : intégrations, versions et confidentialité'
slug: "HUGOで使えるCourtコード"
tags: ["HUGO"]
draft: false
image: "img.webp"
categories: ["blogging"]
description: 'Découvrez les shortcodes intégrés de Hugo, leurs différences selon les versions et les réglages de confidentialité des médias intégrés.'
---

# Shortcodes intégrés de Hugo : intégrations, versions et confidentialité

Les shortcodes appellent des fonctions de modèle depuis le contenu Markdown. Hugo en intègre certains ; les thèmes et modules peuvent en ajouter, et un projet peut définir les siens. Les noms et arguments varient selon la version de Hugo : consultez la documentation officielle de la version utilisée.

## Shortcodes intégrés de Hugo

Flickr n’est pas un shortcode intégré au cœur de Hugo. Si un appel `flickr` fonctionne dans un projet, il est fourni par son thème, module ou modèle personnalisé, tel que `layouts/_shortcodes/flickr.html`. Ne supposez pas qu’il est intégré en vous fiant à son nom.

La liste officielle actuelle comprend notamment `details`, `figure`, `highlight`, `instagram`, `param`, `qr`, `ref`, `relref`, `vimeo`, `x` et `youtube`. Consultez la page officielle pour obtenir la liste complète et les arguments.

## Exemples de médias

### YouTube

Utilisez l’identifiant présent dans le paramètre `v` de l’URL de la vidéo.

`{{</* youtube 0RKpf3rK57I */>}}`

### X (Hugo 0.141.0 et versions ultérieures)

Indiquez le nom d’utilisateur et l’identifiant de la publication présents dans son URL.

`{{</* x user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Ancien Twitter (Hugo 0.139.0)

Hugo 0.139.0 utilise les arguments nommés suivants.

`{{</* twitter user="SanDiegoZoo" id="1453110110599868418" */>}}`

### Instagram

La dernière partie de l’URL d’une publication Instagram est son identifiant.

`{{</* instagram CxOWiQNP2MO */>}}`

### Vimeo

Utilisez l’identifiant numérique à la fin de l’URL de la vidéo Vimeo.

`{{</* vimeo 19899678 */>}}`

## Attention à la version

La compilation de ce blog est fixée à Hugo 0.139.0. Dans cette version, le nom intégré pour X (anciennement Twitter) est `twitter`, qui exige les arguments nommés `user` et `id`. Le shortcode `x` a été ajouté dans Hugo 0.141.0 ; `twitter` a été marqué obsolète dans une version ultérieure. Vérifiez la version du projet avant de copier un exemple récent.

## Réglages de confidentialité

Les intégrations YouTube, X, Instagram et Vimeo peuvent connecter le navigateur du visiteur à ces services. La configuration `privacy` de Hugo peut désactiver les intégrations ou activer des modes simplifiés lorsqu’ils existent. `privacyEnhanced` de YouTube limite le stockage d’informations jusqu’à la lecture de la vidéo par le visiteur.

Mode de confidentialité renforcée de YouTube:

```yaml
privacy:
  youTube:
    privacyEnhanced: true
```

Mode simple de X:

```yaml
privacy:
  x:
    simple: true
    enableDNT: true
```

Ancien Twitter (Hugo 0.139.0):

```yaml
privacy:
  twitter:
    simple: true
    enableDNT: true
```

Consultez la documentation officielle de votre version de Hugo pour vérifier le nom des paramètres.

Le mode simple d’Instagram charge toujours l’image depuis ses serveurs. Celui de Vimeo récupère une miniature et ouvre Vimeo dans un nouvel onglet au clic. Ces modes ne suppriment pas toutes les requêtes tierces.

Avant de publier une intégration, vérifiez les requêtes vers le fournisseur, l’usage des cookies et les exigences de confidentialité applicables à vos lecteurs.

## Afficher la syntaxe comme texte

Pour afficher littéralement la syntaxe d’un shortcode dans un article, échappez les délimiteurs en ajoutant `/*` et `*/`, comme dans l’exemple.

`{{</*/* youtube 0RKpf3rK57I */*/>}}`

## Documentation officielle

- [Présentation des shortcodes](https://gohugo.io/content-management/shortcodes/)
- [Shortcodes intégrés](https://gohugo.io/shortcodes/)
- [YouTube](https://gohugo.io/shortcodes/youtube/)
- [X](https://gohugo.io/shortcodes/x/)
- [Instagram](https://gohugo.io/shortcodes/instagram/)
- [Vimeo](https://gohugo.io/shortcodes/vimeo/)
- [Configuration de confidentialité](https://gohugo.io/configuration/privacy/)

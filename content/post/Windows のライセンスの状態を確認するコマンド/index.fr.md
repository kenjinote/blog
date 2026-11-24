---
title: 'Comment vérifier l''état d''activation de la licence Windows ! Vérification facile en une seule commande'
slug: "Windows のLicenceの状態を確認するCommande"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "Licence", "Invite de commandes"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Découvrez comment consulter le canal de licence et l’état d’activation de Windows avec les commandes slmgr intégrées (/dli, /dlv et /xpr), et pourquoi l’activation ne prouve pas le droit d’utiliser la licence.'
---

# 【Windows】Comment vérifier l'état de la licence (1 commande suffit)

Vous êtes-vous déjà demandé si votre licence Windows est correctement authentifiée ?

Dans ces moments-là, **une méthode pour vérifier les informations de licence avec une seule commande** est très pratique. Vous pouvez facilement vérifier l'état actuel de votre licence en exécutant simplement les étapes ci-dessous.

## Commande pour vérifier l'état de la licence

Vous pouvez afficher les informations de votre licence en utilisant un outil de script intégré à Windows. La commande à utiliser est la suivante :

```
slmgr /dli
```

Lorsque vous exécutez cette commande, certaines informations sur la licence s'afficheront dans une fenêtre.

## Méthode d'exécution

1. Recherchez « cmd » dans le menu Démarrer et ouvrez l’Invite de commandes. Les options `/dli`, `/dlv` et `/xpr` ne nécessitent pas de droits administrateur.

2. Tapez ce qui suit dans l'invite de commandes et appuyez sur Entrée :

   ```
   slmgr /dli
   ```

3. Après avoir attendu quelques secondes, des informations de licence telles que les suivantes s'afficheront.

   ![Fenêtre d’état de licence Windows](img.webp)

## Principales informations affichées

* Une partie de la clé de produit
* Canal de licence (Retail, OEM, etc.)
* État de la licence (les champs varient selon l’édition et le canal)

## Et si vous souhaitez connaître des informations plus détaillées ?

Il existe également des commandes telles que les suivantes :

* `slmgr /dlv` : Affiche des informations de licence plus détaillées
* `slmgr /xpr` : affiche la date d’expiration de l’activation

`/xpr` affiche la date d’expiration de l’activation et sert surtout aux clients KMS ; les activations Retail et MAK sont généralement permanentes. `slmgr` ne vérifie pas que la licence Windows a été obtenue légalement. Sous Windows 11, vous pouvez aussi consulter l’état dans Paramètres > Système > Activation.

## Résumé

L'état de la licence Windows peut être facilement vérifié avec une seule commande.

* **Vérification simple** : `slmgr /dli`
* **Vérification détaillée** : `slmgr /dlv`
* **Vérification de la date d'expiration** : `slmgr /xpr`

Si l’état affiché est inattendu, consultez les paramètres d’activation de Windows ou contactez le vendeur ou l’administrateur de votre organisation.

## Références

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)

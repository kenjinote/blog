---
title: "Commande pour vérifier l'état de la licence de Windows"
slug: "Windows のライセンスの状態を確認するコマンド"
date: 2025-04-14T00:41:45+09:00
tags: ["Windows", "Licence", "Invite de commandes"]
draft: false
image: "img_1.png"
categories: ["PC et Gadgets"]
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

1. **Depuis le « Menu Démarrer », tapez « cmd », faites un clic droit sur Invite de commandes → « Exécuter en tant qu'administrateur »** .

2. Tapez ce qui suit dans l'invite de commandes et appuyez sur Entrée :

   ```
   slmgr /dli
   ```

3. Après avoir attendu quelques secondes, des informations de licence telles que les suivantes s'afficheront.

   ![Écran de vérification de licence Windows](img.png)

## Principales informations affichées

* Une partie de la clé de produit
* Type de licence (Détail, OEM, etc.)
* État de la licence (Active, expirée, non authentifiée, etc.)

## Et si vous souhaitez connaître des informations plus détaillées ?

Il existe également des commandes telles que les suivantes :

* `slmgr /dlv` : Affiche des informations de licence plus détaillées
* `slmgr /xpr` : Affiche la date d'expiration de la licence (si elle est permanente, etc.)

## Résumé

L'état de la licence Windows peut être facilement vérifié avec une seule commande.

* **Vérification simple** : `slmgr /dli`
* **Vérification détaillée** : `slmgr /dlv`
* **Vérification de la date d'expiration** : `slmgr /xpr`

S'il y a un problème avec votre licence, il peut y avoir des restrictions sur les mises à jour et certaines fonctionnalités, il est donc sûr de la vérifier régulièrement.

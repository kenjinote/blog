---
title: "Comment installer Gemini CLI sur Windows"
slug: "Comment installer Gemini CLI sur Windows"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "installation", "développement"]
draft: false
image: "img.png"
categories: ["PC・Gadgets"]
---

# [Pour débutants] Comment installer Gemini CLI sur Windows

"Gemini CLI" vous permet d'utiliser l'IA générative "Gemini" de Google à partir de la ligne de commande.
Dans cet article, nous expliquerons les étapes d'installation de Gemini CLI dans un environnement Windows de la manière la plus simple possible.

---

## 1. Préparation : Installer Node.js et npm

Tout d'abord, puisque Gemini CLI s'exécute sur un environnement appelé "Node.js", vous devez installer ce qui suit :

* **Node.js** 
* **npm (Outil de gestion de paquets inclus avec Node.js)** 
* **npx (Outil d'exécution de commandes inclus dans npm)** 

Téléchargez la version Windows de Node.js depuis le site officiel ci-dessous (la version LTS est recommandée) :

👉 [Site officiel de Node.js](https://nodejs.org/)

Une fois l'installation terminée, vérifiez qu'elle a été correctement effectuée avec la commande suivante :

```powershell
node -v
npm -v
```

---

## 2. Démarrez PowerShell

Pour utiliser Gemini CLI sous Windows, PowerShell est généralement utilisé.
Tapez "PowerShell" dans le menu Démarrer pour l'ouvrir.

---

## 3. Installer Gemini CLI

Copiez et collez la commande suivante dans PowerShell pour l'exécuter :

```bash
npx @google/gemini-cli
```

Cette commande exécute temporairement le paquet Gemini CLI publié par Google.
Il se peut que l'on vous demande de procéder à la configuration initiale et de vous connecter, si nécessaire.

* Remarque : la première fois peut prendre quelques minutes. Si une erreur se produit, veuillez revérifier Node.js et votre environnement réseau.

---

## 4. Installation terminée ! Que faire ensuite

Gemini CLI est maintenant installé sur votre Windows.
À partir de maintenant, vous pouvez utiliser Gemini à partir de la ligne de commande pour diverses opérations, comme la génération de texte et la complétion de code.

Si vous souhaitez vérifier la documentation officielle ou l'aide, vous pouvez également utiliser des commandes comme celle-ci :

```bash
npx @google/gemini-cli --help
```

---

## Résumé

Revoyons les étapes pour installer Gemini CLI sur Windows :

1. Installer Node.js et npm
2. Démarrer PowerShell
3. Exécuter `npx @google/gemini-cli`

Et vous êtes prêt !
Si vous souhaitez utiliser l'IA générative localement, n'hésitez pas à essayer ces étapes comme référence.

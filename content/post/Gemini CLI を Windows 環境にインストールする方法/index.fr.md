---
title: 'Comment installer l''interface de ligne de commande (CLI) Gemini sur Windows | Explication détaillée depuis Node.js'
slug: "Gemini CLI を Windows 環境にInstallationする方法"
tags: ["Gemini", "CLI", "Windows", "installation", "développement"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
date: "2025-07-13T23:49:56+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Installer Gemini CLI sous Windows avec Node.js et npm : installation globale ou ponctuelle, authentification, PATH et approbations sûres."
---

# Installer et utiliser Gemini CLI sous Windows

Gemini CLI est un outil open source permettant d’utiliser Gemini dans un terminal. Ces étapes suivent la documentation officielle actuelle ; consultez le [guide d’installation](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/installation.mdx) pour les mises à jour.

## 1. Préparer Node.js et npm

Gemini CLI nécessite Node.js 20.0.0 ou une version ultérieure. La documentation officielle recommande Windows 11 24H2 ou ultérieur, prend en charge PowerShell et nécessite Internet. Téléchargez l’installateur LTS Windows sur le [site Node.js](https://nodejs.org/en/download/).

```powershell
node --version
npm --version
```

## 2. Installer Gemini CLI avec npm

Pour un usage régulier, installez le paquet globalement :

```powershell
npm install -g @google/gemini-cli
```

```powershell
gemini --version
gemini
```

Si `gemini` est introuvable, exécutez `npm config get prefix`, ajoutez ce dossier au `PATH`, rouvrez PowerShell et vérifiez avec `Get-Command gemini`. Voir la [documentation npm](https://docs.npmjs.com/cli/v11/configuring-npm/folders/).

## 3. Premier lancement et authentification

Lancez `gemini` dans PowerShell et suivez les étapes d’authentification au premier démarrage. Les options documentées comprennent un compte Google, une clé Gemini API et Vertex AI. Disponibilité, tarifs, quotas et conditions dépendent du compte et du service ; consultez le [guide d’authentification](https://github.com/google-gemini/gemini-cli/blob/main/docs/get-started/authentication.mdx). Protégez les clés API et ne les placez ni dans les prompts ni dans des dépôts publics.

```powershell
gemini
```

Utilisez `gemini --help` pour afficher les commandes et saisissez `/quit` pour quitter la session.

## 4. Exécuter une fois sans installation globale

Pour un lancement ponctuel, utilisez `npx` ; la commande n’est pas installée durablement et doit être relancée à la prochaine session. Gemini CLI peut lire et modifier des fichiers et exécuter des commandes shell. Utilisez-le dans des projets de confiance et vérifiez les demandes avant de les approuver. Consultez [outils et sécurité](https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md).

```powershell
npx @google/gemini-cli
```

## 5. Résumé

1. Préparez Node.js 20 ou ultérieur.
2. Pour un usage régulier, installez globalement avec npm.
3. Lancez `gemini` et authentifiez-vous.
4. Pour un lancement ponctuel, utilisez `npx`. Consultez les guides officiels pour les exigences et conditions actuelles.

---
title: 'Comment intégrer et activer GitHub Copilot dans IntelliJ IDEA'
slug: "IntelliJ IDEAでGitHub Copilotを使う"
date: 2022-09-10T09:44:55+09:00
lastmod: 2026-11-24T00:00:00+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["IntelliJ IDEA","GitHub Copilot"]
draft: false
image: "images/img.webp"
categories: ["tools-development-environment"]
description: 'Découvrez comment installer le plugin GitHub Copilot dans IntelliJ IDEA, vous connecter avec GitHub et utiliser les suggestions de code en ligne. Ce guide présente les conditions d’accès et la procédure d’authentification actuelle, avec des liens vers la documentation officielle.'
---

# Introduction

Le plugin GitHub Copilot ajoute des suggestions de code en ligne et Copilot Chat aux IDE JetBrains. Ce guide présente l’installation et la connexion dans IntelliJ IDEA. Les menus et les écrans peuvent varier selon les versions de l’IDE et du plugin.

## Avant de commencer

Vous devez disposer d’un compte GitHub donnant accès à Copilot et d’une version compatible d’IntelliJ IDEA. Copilot Free est soumis à des limites d’utilisation ; les offres payantes donnent accès à davantage de fonctions. Les offres et la compatibilité évoluent : consultez la documentation officielle actuelle.

## Installer le plugin

1. Ouvrez les paramètres des plugins. Sous Windows ou Linux, choisissez **File > Settings > Plugins**. Sous macOS, choisissez **IntelliJ IDEA > Settings > Plugins**.
2. Dans Marketplace, recherchez **GitHub Copilot** et cliquez sur **Install** pour le plugin édité par GitHub.
3. Redémarrez l’IDE après l’installation.

## Se connecter à GitHub

1. Ouvrez **Tools > GitHub Copilot > Login to GitHub**.
2. Dans la fenêtre de connexion, cliquez sur **Copy and Open**. Le navigateur s’ouvre.
3. Connectez-vous à GitHub dans le navigateur, collez le code d’appareil affiché par l’IDE et cliquez sur **Continue**.
4. Vérifiez les autorisations demandées et choisissez **Authorize GitHub Copilot Plugin**. Revenez dans l’IDE et cliquez sur **OK** dans l’écran de confirmation.

## Utiliser les suggestions de code

Commencez à écrire dans l’éditeur. Copilot affiche une suggestion en texte grisé ; appuyez sur **Tab** pour l’accepter. Vérifiez les suggestions avant de les utiliser, car elles sont générées à partir du contexte et peuvent nécessiter des modifications. L’icône GitHub Copilot Chat, à droite de l’IDE, permet d’ouvrir une conversation.

Les menus et les fonctions peuvent évoluer. Consultez la documentation officielle pour connaître les étapes et la compatibilité actuelles.

## Références

- [Installer le plugin et se connecter](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/install-copilot-extension)
- [Obtenir des suggestions de code dans JetBrains](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/copilot-for-common-tasks/get-ide-code-suggestions)
- [Plugin GitHub Copilot sur JetBrains Marketplace](https://plugins.jetbrains.com/plugin/17718-github-copilot--your-ai-pair-programmer)

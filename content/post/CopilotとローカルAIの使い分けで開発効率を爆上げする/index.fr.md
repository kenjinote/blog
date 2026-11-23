---
title: "Copilot ou IA locale ? Décider selon les données et les mesures"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Choisir entre GitHub Copilot et des modèles locaux selon les règles de données, la qualité des tâches, la latence, le coût et le matériel."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot ou IA locale ? Décider selon les données et les mesures](https://kenji.blog/p/hybrid-ai-development-workflow/)

Les assistants de programmation vont de la complétion dans l’IDE aux modifications agentiques. Ne supposez pas que le cloud est plus performant et le local plus sûr. Vérifiez les données envoyées, les conditions applicables, la qualité sur vos tâches, la latence et les coûts d’exploitation.

Ce guide s’appuie sur des documents officiels vérifiés le 23 novembre 2026. Produits, modèles, réglages et politiques évoluent : vérifiez de nouveau les liens et les règles de votre organisation avant l’adoption.

## Le cloud et l’inférence locale ont des flux de données différents

Selon le modèle et la fonction de l’IDE, des services cloud comme GitHub Copilot peuvent envoyer des prompts, extraits de code et éléments pertinents du dépôt au service. La politique actuelle de GitHub indique que les données d’interaction des offres Copilot individuelles peuvent servir à entraîner et améliorer les modèles, avec une possibilité de retrait dans les paramètres personnels. GitHub indique aussi que les données clients Business et Enterprise ne servent pas à l’entraînement sans autorisation du client. Vérifiez votre offre, l’hébergement du modèle, la fonction et les réglages administrateur.

- [Politiques GitHub Copilot pour les abonnés individuels](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Hébergement des modèles et traitement des données par GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

Avec l’inférence locale, le modèle s’exécute sur votre appareil et les entrées peuvent y rester. Le choix d’un modèle local ne garantit pas une configuration entièrement hors ligne. Vérifiez la télémétrie et la synchronisation de l’extension, les outils externes et le trafic lors du téléchargement. Continue décrit la préparation préalable de l’extension et du modèle ainsi que la désactivation de la télémétrie anonyme pour un usage hors ligne.

- [Utiliser Continue sans Internet](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama offre une API locale à `http://localhost:11434` et une API cloud hébergée à `https://ollama.com/api`, qui demande une clé. Ollama ne signifie donc pas automatiquement inférence locale. Vérifiez le point de terminaison configuré. Si vous exposez un serveur local au réseau, concevez séparément les contrôles d’accès.

- [Points de terminaison et utilisation de l’API Ollama](https://docs.ollama.com/api/introduction)

## Choisir selon la tâche et la classification des données

Commencez par la classification des données et la politique IA de votre organisation. Déterminez quels codes, journaux, plans et identifiants peuvent quitter l’environnement approuvé. Ne mettez jamais de secret dans un prompt, quel que soit le lieu du modèle : remplacez-le par une valeur de test. Pour le cloud, vérifiez aussi l’usage pour l’entraînement selon l’offre, la conservation, la surveillance des abus, la région, les contrôles administratifs et le transfert vers les hébergeurs des modèles.

- Complétion routinière, commentaires ou ébauches de tests : qualité, latence, intégration IDE et données transmises ; fonction cloud approuvée ou petit modèle local.
- Résumé ou modification de code interne : périmètre des entrées, vérification des résultats, contrat et conservation ; cloud approuvé ou environnement local contrôlé.
- Code confidentiel ou réglementé : transmission externe, journaux, frontière réseau et audit ; environnement local isolé conforme et approuvé par l’organisation.
- Conception complexe ou débogage difficile : qualité évaluée, contexte, droits des outils et coût ; cloud ou modèle hébergé en interne conforme.
- Travail sans Internet : téléchargements préalables, trafic de l’extension, mises à jour et correctifs ; configuration hors ligne testée.

Ce tableau n’est pas un classement de performances. Il sert à réduire les choix au regard des règles et tests de l’organisation.

## Mesurer qualité, latence et coût sur les mêmes tâches

Créez un petit jeu de tests avec critères de réussite, échecs et méthode de notation. Donnez le même code et les mêmes consignes aux candidats, puis notez ID du modèle, extension, date et réglages. Comparez exactitude, tests réussis, cohérence avec la conception existante, refus sûrs et temps de correction. Faites plusieurs essais, car les sorties varient. Faites réviser le code important et exécuter ses tests par un développeur.

Mesurez séparément le délai avant la première sortie et la durée totale. Incluez l’utilisation cloud, les abonnements, répétitions et revues, ainsi que l’achat, l’électricité et la maintenance du matériel local. La vitesse et la qualité locales dépendent de la taille du modèle, de la quantification, du contexte, du GPU/de la mémoire et des réglages de l’IDE. Ne vous fondez pas seulement sur le nombre de paramètres ou une estimation VRAM : testez votre matériel.

## Essayer un modèle local en quelques étapes

Installez Ollama. Dans son catalogue, vérifiez licence, taille de téléchargement et fonctions ; récupérez l’étiquette exacte :

```sh
ollama pull <model-name:tag>
```

Le format de configuration actuel de Continue peut déclarer Ollama ainsi. Remplacez `<MODEL_ID>` par l’identifiant téléchargé affiché par `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

L’appel d’outils, l’entrée d’images et les limites de contexte varient selon le modèle. Testez le fonctionnement réel, même si l’IDE détecte ces capacités. Commencez avec le minimum de droits. Pour les agents qui modifient des fichiers ou exécutent des commandes shell, imposez revue et approbation humaines. Tenez compte de l’injection de prompt dans le code externe.

- [API Ollama](https://docs.ollama.com/api/introduction)
- [Configuration Ollama de Continue](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Bibliothèque des modèles Ollama](https://ollama.com/library)

## Commencer modestement et réévaluer en cas de changement

Choisissez une tâche peu risquée et comparez une fonction cloud approuvée à un modèle local sur le même jeu de tests. Examinez qualité, temps de correction, latence, coût et destination des données ; définissez des règles par tâche avec l’équipe. Revoyez politiques et tests si modèle, offre, extension ou contrat change.

La sécurité ne dépend pas du seul choix cloud ou local. Comprenez le flux de traitement, minimisez les entrées et testez dans un environnement approuvé.

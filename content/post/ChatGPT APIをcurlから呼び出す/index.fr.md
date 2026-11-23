---
title: 'Appeler l’API OpenAI avec curl depuis l’invite de commandes Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Commande"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Envoyez une requête textuelle à l’API Responses d’OpenAI depuis cmd.exe sous Windows. Configurez la clé comme variable d’environnement et envoyez le JSON sans placer la clé dans le fichier de requête.'
---


Ce guide appelle l’API OpenAI depuis `cmd.exe` sous Windows. L’API Responses est recommandée pour les nouvelles applications. ChatGPT et API Platform sont des services distincts ; l’utilisation de l’API est facturée séparément de l’abonnement ChatGPT. Consultez la [configuration de facturation de l’API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) avant d’envoyer des requêtes.

## Définir la clé comme variable d’environnement

Créez une clé sur la page [API keys d’API Platform](https://platform.openai.com/api-keys). Ne l’inscrivez ni dans le code source ni dans le fichier de requête. Sous Windows, appuyez sur `Win+R`, exécutez `sysdm.cpl`, puis ouvrez **Avancé > Variables d’environnement > Variables utilisateur > Nouveau**. Nommez la variable `OPENAI_API_KEY` et saisissez-y la clé ; ouvrez ensuite une nouvelle invite de commandes. Vérifiez sa présence sans afficher le secret :

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Une variable d’environnement évite d’inscrire la clé dans le code de l’application, mais ne permet pas de la publier ou de la partager sans risque. En cas de fuite, révoquez-la et remplacez-la sur la page API keys. Consultez aussi les [bonnes pratiques de sécurité des clés](https://developers.openai.com/api/docs/guides/production-best-practices).

## Créer la requête

Enregistrez ce JSON sous le nom `request.json` dans votre dossier de travail. Utilisez l’encodage UTF-8 si le fichier contient des caractères non ASCII.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

Les identifiants de modèle peuvent changer et leur disponibilité dépend du projet API. Consultez le [catalogue des modèles](https://developers.openai.com/api/docs/models) avant d’utiliser celui de l’exemple.

## Envoyer la requête avec curl.exe

Dans l’invite de commandes, placez-vous dans le dossier contenant `request.json`, puis exécutez :

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` affiche le statut HTTP et les en-têtes de réponse. L’API Responses renvoie du JSON. Le texte généré se trouve dans un élément `output_text` de `content` au sein d’un message de sortie. Les appels d’outils et d’autres types de réponse peuvent ajouter d’autres éléments ; utilisez un analyseur JSON et vérifiez le `type` de chaque élément au lieu de supposer un indice fixe. Consultez la [référence de l’API Responses](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Erreurs et utilisation

- `401` peut signaler une clé absente, invalide ou non autorisée pour le projet. Vérifiez sa configuration sans afficher ni partager sa valeur.
- `429` peut signaler une limite de débit ou l’épuisement des crédits ou du quota. Consultez le corps de la réponse ainsi que Usage et Billing dans API Platform.
- Le coût dépend du modèle et des jetons d’entrée et de sortie. Consultez les tarifs et l’utilisation du projet dans API Platform ; configurez des limites ou des alertes si nécessaire.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)

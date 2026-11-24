---
title: "Publier avec l’API X et Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Lisez les identifiants depuis Google Colab Secrets et publiez un message avec Tweepy et X API v2. Vérifiez les conditions d’accès et les tarifs actuels avant l’exécution."
---

# Introduction

Cet exemple minimal utilise Tweepy dans Google Colab pour publier un message sur votre propre compte avec X API v2. L’accès, les tarifs et les exigences d’authentification peuvent changer ; consultez la documentation officielle et Developer Console avant de l’exécuter.

## Important : identifiants de la version précédente

Une ancienne version de cet article contenait des clés API et des jetons d’accès dans le texte. Considérez comme compromis tout identifiant qui a été publié. Si ces valeurs étaient réelles et actives, révoquez les clés et jetons concernés dans X Developer Console et créez-en de nouveaux. Des copies peuvent subsister dans l’historique du dépôt ; les supprimer de la page actuelle ne suffit donc pas.

# Avant de commencer

1. Créez un Project et une App dans [X Developer Console](https://developer.x.com/en/portal/dashboard), puis créez des identifiants utilisateur autorisés à publier. Avec OAuth 1.0a User Context, configurez les droits de lecture et d’écriture de l’App avant de générer les jetons d’accès. Avec OAuth 2.0 PKCE, demandez les scopes nécessaires, dont `tweet.write`.
2. Consultez dans Developer Console l’offre actuelle, le tarif du point de terminaison d’écriture et les limites d’utilisation. Les tarifs et l’accès peuvent changer ; ne vous fiez pas aux anciens tutoriels ni aux anciens montants.
3. Créez un notebook dans [Google Colab](https://colab.research.google.com/). Dans le panneau Secrets (icône de clé), ajoutez quatre secrets portant les noms ci-dessous et autorisez ce notebook à y accéder. Saisissez les valeurs de votre App ; ne les collez pas dans le code ou la sortie du notebook.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Publier un message

L’exécution de cette cellule publie le texte de `text` depuis votre compte X. Vérifiez le compte et le message avant de l’exécuter. Des frais X API peuvent s’appliquer.

```python
%pip install -q tweepy

from google.colab import userdata
import tweepy

client = tweepy.Client(
    consumer_key=userdata.get("X_API_KEY"),
    consumer_secret=userdata.get("X_API_KEY_SECRET"),
    access_token=userdata.get("X_ACCESS_TOKEN"),
    access_token_secret=userdata.get("X_ACCESS_TOKEN_SECRET"),
)

text = "Hello from the X API"
response = client.create_tweet(text=text)
print(response.data["id"])
```

## À propos de l’automatisation

Cet exemple publie un seul message lorsque vous exécutez la cellule manuellement. Avant de l’étendre à des publications programmées ou à des réponses automatisées, consultez les [règles d’automatisation de X](https://help.x.com/en/rules-and-policies/x-automation). Les réponses automatisées sont soumises à des conditions supplémentaires, notamment une intention clairement exprimée par le destinataire. Colab ne garantit pas une exécution permanente ; ses sessions et limites peuvent changer.

## Références

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)

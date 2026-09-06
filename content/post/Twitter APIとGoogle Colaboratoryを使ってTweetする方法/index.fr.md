---
title: "Comment tweeter en utilisant l'API Twitter et Google Colaboratory"
slug: "comment-tweeter-en-utilisant-l-api-twitter-et-google-colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Programmation"]
---

# Ce dont vous avez besoin

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Compte Google

Consultez le site de référence pour savoir comment obtenir l'API Twitter.

# Étapes pour tweeter à l'aide de l'API

1. Accédez à [https://colab.research.google.com/](https://colab.research.google.com/)
2. Sélectionnez "Fichier" -> "Nouveau notebook"
3. Collez et exécutez le code ci-dessous (veuillez utiliser vos propres valeurs réelles obtenues)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Collez et exécutez le code ci-dessous
```
import tweepy
```
4. Collez et exécutez le code ci-dessous (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Un tweet disant `hello` sera publié.

5. Collez et exécutez le code ci-dessous (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Un tweet disant `hello v2` sera publié.

C'est tout.

# Référence
- [【À partir d'avril 2021】Explication détaillée de la demande d'utilisation de l'API Twitter avec des exemples de phrases d'utilisation et des captures d'écran](https://bloomtectec.com/twitter-api-application-procedure/)
- [【Pas besoin de paramètres compliqués !】Google Colaboratory est recommandé comme environnement de test pour l'API Twitter 【Le code source est également partagé】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2 : Tweets, réponses, tweets avec sondages, tweets avec médias (v1.1) [Python]](https://3pysci.com/tweepy-28/)

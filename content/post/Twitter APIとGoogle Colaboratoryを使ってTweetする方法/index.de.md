---
title: "Wie man mit der Twitter API und Google Colaboratory twittert"
slug: "wie-man-mit-der-twitter-api-und-google-colaboratory-twittert"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Programmierung"]
---

# Was Sie benötigen

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Google-Konto

Besuchen Sie die Referenzseite, um zu erfahren, wie Sie die Twitter API erhalten.

# Schritte zum Twittern mit der API

1. Gehen Sie zu [https://colab.research.google.com/](https://colab.research.google.com/)
2. Wählen Sie "Datei" -> "Neues Notizbuch"
3. Fügen Sie den folgenden Code ein und führen Sie ihn aus (bitte verwenden Sie Ihre eigenen tatsächlichen Werte)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Fügen Sie den folgenden Code ein und führen Sie ihn aus
```
import tweepy
```
4. Fügen Sie den folgenden Code ein und führen Sie ihn aus (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Ein Tweet mit dem Text `hello` wird gepostet.

5. Fügen Sie den folgenden Code ein und führen Sie ihn aus (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Ein Tweet mit dem Text `hello v2` wird gepostet.

Das ist alles.

# Referenz
- [【Stand April 2021】Detaillierte Erklärung des Nutzungsantrags für die Twitter API mit Beispielsätzen und Screenshots](https://bloomtectec.com/twitter-api-application-procedure/)
- [【Keine komplizierten Einstellungen erforderlich!】Google Colaboratory wird als Testumgebung für die Twitter API empfohlen 【Quellcode wird ebenfalls geteilt】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2: Tweets, Antworten, Tweets mit Umfragen, Tweets mit Medien (v1.1) [Python]](https://3pysci.com/tweepy-28/)

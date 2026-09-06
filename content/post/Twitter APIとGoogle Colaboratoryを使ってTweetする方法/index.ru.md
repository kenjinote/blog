---
title: "Как написать твит с помощью Twitter API и Google Colaboratory"
slug: "как-написать-твит-с-помощью-twitter-api-и-google-colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Программирование"]
---

# Что потребуется

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Аккаунт Google

Обратитесь к справочным сайтам, чтобы узнать, как получить Twitter API.

# Шаги для публикации твита с помощью API

1. Перейдите на [https://colab.research.google.com/](https://colab.research.google.com/)
2. Выберите "Файл" -> "Создать блокнот"
3. Вставьте и выполните следующий код (используйте фактические значения, которые вы получили сами)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Вставьте и выполните следующий код
```
import tweepy
```
4. Вставьте и выполните следующий код (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Будет опубликован твит `hello`

5. Вставьте и выполните следующий код (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Будет опубликован твит `hello v2`

На этом всё

# Ссылки
- [[По состоянию на апрель 2021] Исчерпывающее руководство по заявке на использование Twitter API с примерами и скриншотами](https://bloomtectec.com/twitter-api-application-procedure/)
- [[Никаких сложных настроек!] Рекомендуем Google Colaboratory как тестовую среду для Twitter API [Исходный код также прилагается]](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [[Tweepy] Twitter API v2: Твиты, ответы, твиты с опросом, твиты с медиа (v1.1) [Python]](https://3pysci.com/tweepy-28/)

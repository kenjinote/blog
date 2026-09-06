---
title: "Como twittar usando a API do Twitter e o Google Colaboratory"
slug: "como-twittar-usando-a-api-do-twitter-e-o-google-colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Programação"]
---

# O que você precisa

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Conta do Google

Consulte o site de referência para saber como obter a API do Twitter.

# Passos para twittar usando a API

1. Acesse [https://colab.research.google.com/](https://colab.research.google.com/)
2. Selecione "Arquivo" -> "Novo notebook"
3. Cole e execute o código abaixo (use seus próprios valores reais obtidos)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Cole e execute o código abaixo
```
import tweepy
```
4. Cole e execute o código abaixo (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Um tweet dizendo `hello` será postado.

5. Cole e execute o código abaixo (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Um tweet dizendo `hello v2` será postado.

É isso.

# Referência
- [【A partir de abril de 2021】Explicação detalhada da solicitação de uso da API do Twitter com frases de exemplo de uso e capturas de tela](https://bloomtectec.com/twitter-api-application-procedure/)
- [【Sem necessidade de configurações complicadas!】O Google Colaboratory é recomendado como um ambiente de teste para a API do Twitter 【Código-fonte também compartilhado】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2: Tweets, respostas, tweets com enquetes, tweets com mídia (v1.1) [Python]](https://3pysci.com/tweepy-28/)

---
title: "Публикация через X API и Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Загрузите учетные данные из Google Colab Secrets и опубликуйте запись с помощью Tweepy и X API v2. Перед запуском проверьте текущие условия доступа и стоимость API."
---

# Введение

Это минимальный пример использования Tweepy в Google Colab для публикации одной записи в собственном аккаунте через X API v2. Доступность API, цены и требования к аутентификации могут меняться. Перед запуском проверьте официальную документацию и Developer Console.

## Важно: учетные данные в предыдущей версии

В предыдущей версии статьи в тексте были указаны API-ключи и токены доступа. Считайте все опубликованные учетные данные скомпрометированными. Если значения были настоящими и действующими, отзовите соответствующие ключи и токены в X Developer Console и создайте новые. Копии могут остаться в истории репозитория, поэтому удаления с текущей страницы недостаточно.

# Подготовка

1. Создайте Project и App в [X Developer Console](https://developer.x.com/en/portal/dashboard) и выпустите пользовательские учетные данные с правом публикации. Для OAuth 1.0a User Context настройте для App права чтения и записи до создания токенов доступа. Для OAuth 2.0 PKCE запросите необходимые области доступа, включая `tweet.write`.
2. Проверьте в Developer Console текущий план, стоимость метода записи и лимиты использования. Цены и условия доступа меняются; не ориентируйтесь на старые руководства и прежние цены.
3. Создайте блокнот в [Google Colab](https://colab.research.google.com/). В разделе Secrets (значок ключа) добавьте четыре секрета с именами ниже и разрешите этому блокноту доступ к ним. Укажите данные своего App; не вставляйте их в код или вывод блокнота.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Публикация одной записи

При запуске ячейки текст из `text` будет опубликован от имени вашего аккаунта X. Перед запуском проверьте аккаунт и текст. За использование X API может взиматься плата.

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

## Автоматизация

Этот пример публикует одну запись только при ручном запуске ячейки. Прежде чем добавлять публикацию по расписанию или автоматические ответы, прочитайте [правила автоматизации X](https://help.x.com/en/rules-and-policies/x-automation). Для автоматических ответов действуют дополнительные условия, включая явное намерение получателя. Colab не гарантирует постоянную работу; время сессий и лимиты могут изменяться.

## Источники

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)

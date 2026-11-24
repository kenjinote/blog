---
title: "Publicar com a API do X e o Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Leia credenciais do Google Colab Secrets e publique uma postagem com Tweepy e X API v2. Confira o acesso e os preços atuais antes de executar o exemplo."
---

# Introdução

Este é um exemplo mínimo que usa Tweepy no Google Colab para publicar uma postagem na sua própria conta usando a X API v2. O acesso, os preços e os requisitos de autenticação podem mudar; consulte a documentação oficial e o Developer Console antes de executar.

## Importante: credenciais da versão anterior

Uma versão anterior deste artigo incluía chaves de API e tokens de acesso no texto. Considere comprometidas todas as credenciais que foram publicadas. Se esses valores eram reais e estavam ativos, revogue as chaves e os tokens afetados no X Developer Console e gere novos. Pode haver cópias no histórico do repositório, portanto removê-los apenas da página atual não é suficiente.

# Antes de começar

1. Crie um Project e um App no [X Developer Console](https://developer.x.com/en/portal/dashboard) e gere credenciais de usuário com permissão para publicar. Com OAuth 1.0a User Context, configure as permissões de leitura e escrita do App antes de gerar os tokens de acesso. Com OAuth 2.0 PKCE, solicite os escopos necessários, incluindo `tweet.write`.
2. Confira no Developer Console o plano atual, o preço do endpoint de escrita e os limites de uso. Preços e acesso podem mudar; não confie em tutoriais antigos nem em valores anteriores.
3. Crie um notebook no [Google Colab](https://colab.research.google.com/). No painel Secrets (ícone de chave), adicione quatro secrets com os nomes abaixo e permita que este notebook os acesse. Insira os valores do seu App; não os cole no código ou na saída do notebook.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Publicar uma postagem

Ao executar esta célula, o texto em `text` será publicado pela sua conta do X. Confira a conta e o texto antes de executar. Podem ser cobradas tarifas da X API.

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

## Sobre automação

Este exemplo publica apenas uma postagem quando você executa a célula manualmente. Antes de ampliá-lo para publicações programadas ou respostas automáticas, leia as [regras de automação do X](https://help.x.com/en/rules-and-policies/x-automation). Respostas automáticas têm requisitos adicionais, incluindo uma manifestação clara de intenção do destinatário. O Colab não garante a execução contínua; as sessões e os limites de uso podem mudar.

## Referências

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)

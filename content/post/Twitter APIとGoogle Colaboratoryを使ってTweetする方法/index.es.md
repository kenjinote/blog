---
title: "Publicar con la API de X y Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Lee las credenciales de Google Colab Secrets y publica un mensaje con Tweepy y X API v2. Comprueba el acceso y el precio actuales antes de ejecutar el ejemplo."
---

# Introducción

Este es un ejemplo mínimo que usa Tweepy en Google Colab para publicar un mensaje en tu propia cuenta mediante X API v2. El acceso, los precios y los requisitos de autenticación pueden cambiar; consulta la documentación oficial y Developer Console antes de ejecutarlo.

## Importante: credenciales de la versión anterior

Una versión anterior de este artículo incluía claves API y tokens de acceso en el texto. Considera comprometidas todas las credenciales que se hayan publicado. Si esos valores eran reales y estaban activos, revoca las claves y los tokens afectados en X Developer Console y genera otros nuevos. Puede haber copias en el historial del repositorio, por lo que eliminarlos solo de la página actual no basta.

# Antes de empezar

1. Crea un Project y una App en [X Developer Console](https://developer.x.com/en/portal/dashboard) y genera credenciales de usuario con permiso para publicar. Con OAuth 1.0a User Context, configura permisos de lectura y escritura para la App antes de generar los tokens de acceso. Con OAuth 2.0 PKCE, solicita los ámbitos necesarios, incluido `tweet.write`.
2. Consulta en Developer Console el plan actual, el precio del endpoint de escritura y los límites de uso. El precio y el acceso pueden cambiar; no dependas de tutoriales antiguos ni de importes anteriores.
3. Crea un cuaderno en [Google Colab](https://colab.research.google.com/). En el panel Secrets (icono de llave), añade cuatro secretos con los nombres indicados y permite que este cuaderno acceda a ellos. Introduce tus propios valores de la App; no los pegues en el código ni en la salida del cuaderno.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Publicar un mensaje

Al ejecutar esta celda se publica en tu cuenta de X el texto indicado en `text`. Comprueba la cuenta y el mensaje antes de ejecutarla. Pueden aplicarse cargos de X API.

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

## Sobre la automatización

Este ejemplo publica un solo mensaje cuando ejecutas la celda manualmente. Antes de ampliarlo para publicar de forma programada o responder automáticamente, lee las [reglas de automatización de X](https://help.x.com/en/rules-and-policies/x-automation). Las respuestas automáticas tienen requisitos adicionales, como una señal clara de intención por parte del destinatario. Colab no garantiza la ejecución continua; sus sesiones y límites de uso pueden cambiar.

## Referencias

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)

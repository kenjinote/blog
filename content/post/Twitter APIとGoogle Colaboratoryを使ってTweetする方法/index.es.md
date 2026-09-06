---

title: "Cómo tuitear usando la API de Twitter y Google Colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Programación"]
---


# Lo que necesitas

- API de Twitter
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Cuenta de Google

Para obtener la API de Twitter, consulta los sitios de referencia.

# Procedimiento para tuitear usando la API

1. Accede a [https://colab.research.google.com/](https://colab.research.google.com/)
2. Selecciona "Archivo" → "Nuevo cuaderno"
3. Pega y ejecuta el siguiente código (usa los valores reales que obtuviste)
```python
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Pega y ejecuta el siguiente código
```python
import tweepy
```
4. Pega y ejecuta el siguiente código (API v1.1)
```python
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Se publicará el tuit `hello`

5. Pega y ejecuta el siguiente código (API v2.0)
```python
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Se publicará el tuit `hello v2`

Eso es todo.

# Referencias
- [【A partir de abril de 2021】Explicación exhaustiva del procedimiento de solicitud de la API de Twitter con ejemplos de uso y capturas de pantalla](https://bloomtectec.com/twitter-api-application-procedure/)
- [【¡Sin configuraciones molestas!】Google Colaboratory es recomendado para probar la API de Twitter 【También compartimos el código fuente】](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [【Tweepy】Twitter API v2: Tuitear, responder (reply), tuits con encuesta, tuits con medios (v1.1) [Python]](https://3pysci.com/tweepy-28/)

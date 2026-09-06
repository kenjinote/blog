---
title: "Cara Tweet Menggunakan Twitter API dan Google Colaboratory"
slug: "cara-tweet-menggunakan-twitter-api-dan-google-colaboratory"
date: 2023-04-08T18:48:32+09:00
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

# Apa yang Dibutuhkan

- Twitter API
- Twitter API SECRET
- Twitter ACCESS TOKEN
- Twitter ACCESS TOKEN SECRET
- Akun Google

Silakan merujuk ke situs referensi tentang cara mendapatkan Twitter API.

# Langkah-langkah Tweet menggunakan API

1. Kunjungi [https://colab.research.google.com/](https://colab.research.google.com/)
2. Pilih "File" -> "Buku catatan baru"
3. Tempel dan jalankan kode berikut (Gunakan nilai aktual yang Anda dapatkan sendiri)
```
API_KEY = '9Smu2f2RoLqbVQHQq6n79Z2JW'
API_SECRET = 'uGVRIkLL2l8sRyPv2Lr4mXxXppnQF1isMoRnvktcXCtFgAK2R8'
ACCESS_TOKEN = '0367292979164670705-7hSErDoQbO6fkFtnn5UY0vqpvecy0O'
ACCESS_TOKEN_SECRET = 'pUv81U9GVzZirz5g4AxZPHAJ4GpSXnBo8GUcZ1egtjw9q'
```
3. Tempel dan jalankan kode berikut
```
import tweepy
```
4. Tempel dan jalankan kode berikut (API v1.1)
```
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
api.update_status("hello")
```
→ Tweet `hello` akan diposting

5. Tempel dan jalankan kode berikut (API v2.0)
```
client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)
client.create_tweet(text='hello v2')
```
→ Tweet `hello v2` akan diposting

Selesai

# Referensi
- [[Per April 2021] Penjelasan lengkap tentang aplikasi penggunaan Twitter API dengan contoh penggunaan dan tangkapan layar](https://bloomtectec.com/twitter-api-application-procedure/)
- [[Tidak perlu pengaturan yang merepotkan!] Kami merekomendasikan Google Colaboratory sebagai lingkungan uji coba untuk Twitter API [Kode sumber juga akan dibagikan]](https://bloomtectec.com/use-twitter-api-in-google-colab/)
- [[Tweepy] Twitter API v2: Tweet, balasan (reply), tweet dengan polling, tweet dengan media (v1.1) [Python]](https://3pysci.com/tweepy-28/)

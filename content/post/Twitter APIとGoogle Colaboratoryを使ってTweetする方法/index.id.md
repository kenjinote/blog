---
title: "Membuat Postingan dengan X API dan Google Colab [Python]"
date: "2023-04-08T18:48:32+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
slug: "Twitter APIとGoogle Colaboratoryを使ってTweetする方法"
tags: ["Twitter", "Twitter API", "Google Colaboratory", "tweepy"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Baca kredensial dari Google Colab Secrets lalu terbitkan satu postingan dengan Tweepy dan X API v2. Periksa akses dan harga API terbaru sebelum menjalankan contoh."
---

# Pendahuluan

Ini adalah contoh sederhana yang menggunakan Tweepy di Google Colab untuk menerbitkan satu postingan ke akun Anda sendiri melalui X API v2. Akses, harga, dan persyaratan autentikasi dapat berubah, jadi periksa dokumentasi resmi dan Developer Console sebelum menjalankannya.

## Penting: kredensial di versi sebelumnya

Versi sebelumnya dari artikel ini mencantumkan API key dan access token di dalam teks. Anggap semua kredensial yang pernah dipublikasikan telah bocor. Jika nilainya asli dan masih aktif, cabut key dan token terkait di X Developer Console lalu buat yang baru. Salinannya mungkin masih ada di riwayat repositori, jadi menghapusnya dari halaman saat ini saja tidak cukup.

# Sebelum memulai

1. Buat Project dan App di [X Developer Console](https://developer.x.com/en/portal/dashboard), lalu buat kredensial pengguna yang memiliki izin untuk memposting. Untuk OAuth 1.0a User Context, atur izin baca dan tulis App sebelum membuat access token. Untuk OAuth 2.0 PKCE, minta cakupan yang diperlukan, termasuk `tweet.write`.
2. Periksa paket saat ini, harga endpoint penulisan, dan batas penggunaan di Developer Console. Harga dan akses dapat berubah; jangan mengandalkan tutorial atau harga lama.
3. Buat notebook di [Google Colab](https://colab.research.google.com/). Di panel Secrets (ikon kunci), tambahkan empat secret dengan nama di bawah dan izinkan notebook ini mengaksesnya. Masukkan nilai App Anda sendiri; jangan menempelkannya ke kode atau output notebook.
   - `X_API_KEY`
   - `X_API_KEY_SECRET`
   - `X_ACCESS_TOKEN`
   - `X_ACCESS_TOKEN_SECRET`

# Terbitkan satu postingan

Saat sel ini dijalankan, teks di `text` akan dipublikasikan dari akun X Anda. Periksa akun dan teks sebelum menjalankannya. Biaya X API mungkin berlaku.

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

## Tentang otomatisasi

Contoh ini hanya menerbitkan satu postingan saat Anda menjalankan sel secara manual. Sebelum mengembangkannya untuk posting terjadwal atau balasan otomatis, baca [Aturan Otomatisasi X](https://help.x.com/en/rules-and-policies/x-automation). Balasan otomatis memiliki persyaratan tambahan, termasuk adanya maksud yang jelas dari penerima. Colab tidak menjamin pekerjaan berjalan terus-menerus; sesi dan batas penggunaan dapat berubah.

## Referensi

- [X API: Create or Edit Post](https://docs.x.com/x-api/posts/create-post)
- [X API v2 authentication mapping](https://docs.x.com/fundamentals/authentication/guides/v2-authentication-mapping)
- [X API pricing and credits](https://docs.x.com/x-api/getting-started/pricing)
- [X automation rules](https://help.x.com/en/rules-and-policies/x-automation)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html)
- [Tweepy Client reference](https://docs.tweepy.org/en/stable/client.html)
- [Tweepy authentication guide](https://docs.tweepy.org/en/stable/authentication.html)

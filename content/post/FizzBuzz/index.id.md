---
title: "FizzBuzz"
slug: "FizzBuzz"
date: 2025-04-18T00:58:11+09:00
tags: ["FizzBuzz", "Python", "Algoritma"]
draft: false
image: "img.png"
categories: ["Pemrograman"]
---

## Sebenarnya, apa itu FizzBuzz?

Halo semuanya!

Hari ini, saya ingin menulis tentang "FizzBuzz".

Baik Anda seseorang yang berkata, "Ah, saya tahu itu!", atau seseorang yang berkata, "Saya pernah mendengarnya, tapi tidak terlalu mengerti," tolong luangkan waktu sebentar bersama saya. Anda dapat membacanya hanya dalam beberapa menit, dan mungkin Anda akan berpikir, "Oh, begitu rupanya."

---

### Benarkah "Anda bukan programmer jika tidak bisa menulis FizzBuzz"?

Secara garis besar, FizzBuzz itu seperti ini.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Ya, ini adalah "masalah FizzBuzz" yang terkenal itu.

Anda melihat angka dari 1 hingga 100 secara berurutan,  
jika kelipatan 3 maka cetak "Fizz", jika kelipatan 5 maka cetak "Buzz",  
dan jika kelipatan keduanya, cetak "FizzBuzz". Sangat sederhana.

Namun, entah mengapa, ini sering kali dianggap sebagai "ujian standar minimum untuk programmer." Ini sering muncul dalam wawancara, dan terkadang ada komentar merendahkan di media sosial seperti, "Orang yang bahkan tidak bisa menulis FizzBuzz..."

Tapi tunggu sebentar.

Bisakah kita benar-benar mengatakan bahwa "tidak bisa menulis FizzBuzz = tidak bisa memprogram"?

---

### Ini bukan tentang apakah Anda bisa melakukannya, tetapi apakah Anda memiliki "kondisi" untuk melakukannya

Tentu saja, FizzBuzz membutuhkan pemahaman tentang sintaksis dan pemikiran logis dasar. Jadi, masuk akal untuk menggunakannya untuk "memeriksa dasar-dasar."

Tapi dengarkan.

Jika lingkungannya berbeda, hasilnya juga akan berbeda.

Misalnya,

- Ketika Anda merasa gugup di depan pewawancara yang baru pertama kali Anda temui
- Ketika Anda tiba-tiba diberi papan tulis dan tidak ada editor kode di tangan
- Ketika Anda tiba-tiba tidak bisa mengingat, "Tunggu, apa itu modulo lagi?"

... Bukankah hal-hal seperti itu terjadi? Bagaimanapun, kita adalah manusia. Saya rasa itu wajar terjadi.

Jadi, daripada "apakah Anda bisa menulis FizzBuzz," saya pikir yang lebih penting adalah "apakah Anda bisa membawa diri Anda ke dalam kondisi di mana Anda bisa menulis FizzBuzz."

---

### Jebakan dari saran umum "Teruslah berlatih dan Anda akan baik-baik saja"

Ketika berbicara tentang topik ini, saran "Makanya berlatihlah setiap hari!" sering kali muncul.

Tentu saja, benar bahwa latihan berulang kali akan memungkinkan Anda menulis dengan lancar, dan itu sendiri adalah hal yang baik. Namun, jika Anda mulai dengan asumsi bahwa "Anda gagal jika tidak bisa menulis FizzBuzz," itu hanya akan berubah menjadi ketakutan.

Dengan kata lain, mudah untuk jatuh ke dalam pola pikir di mana Anda merasa, "Saya melakukan kesalahan = saya tidak berguna."

Misalnya, pada hari-hari ketika Anda bangun kesiangan, bukankah Anda cenderung berpikir, "Saya malas sekali..."? Tapi mungkin tubuh Anda kebetulan sedang sangat lelah.

Hal yang sama berlaku untuk FizzBuzz.

---

### Meski begitu, FizzBuzz tetaplah pertanyaan yang sangat bagus

Meskipun demikian, FizzBuzz bukanlah hal yang buruk.

Sebaliknya, saya pikir ini adalah pertanyaan yang disusun dengan sangat baik. Aturannya sederhana, dan mudah untuk dikembangkan. Misalnya, jika Anda mengubahnya seperti ini, pemikiran Anda akan menjadi lebih dalam.

```python
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i)
```

Ini adalah contoh yang menunjukkan bahwa "Anda bisa menulisnya tanpa if-elif-else." Cukup cerdik, bukan?

Dengan kata lain, FizzBuzz bukan hanya tentang "apakah Anda bisa melakukannya," tetapi juga bisa menjadi titik masuk untuk melihat "bagaimana Anda menulisnya" dan "seberapa jauh Anda memahaminya."

---

### Kesimpulan

Saya rasa kita tidak perlu memberi makna berlebihan pada apakah seseorang bisa menyelesaikan FizzBuzz atau tidak.

Bahkan jika Anda tidak bisa menulisnya, itu mungkin hanya berarti bahwa "saat itu kondisi Anda sedang kurang baik," dan Anda sering kali bisa melakukannya jika memikirkannya baik-baik nanti.

Jangan terburu-buru, mari kita jalani pelan-pelan.

Kode ditulis oleh manusia. Karena kita manusia, terkadang kita melupakan sesuatu, dan terkadang kita merasa gugup. Saya pikir cukup untuk menerima hal itu dan bergerak maju sedikit demi sedikit.

Baiklah, mari bersantai dan menulis beberapa kode hari ini.

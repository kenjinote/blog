---
title: "Cara Menginstal Go"
slug: "Cara Menginstal Go"
date: 2022-09-10T00:48:17+09:00
tags: ["Go","instalasi"]
draft: false
image: "images/cover.png"
categories: ["pemrograman"]
---
# Pengantar
Go adalah bahasa pemrograman yang relatif baru yang dirilis oleh Google pada tahun 2009.
Kompiler, alat, dan pustaka Go bersifat sumber terbuka (open source).
Selain itu, Go adalah bahasa dengan pengetikan statis seperti C dan Java, tetapi tidak menggunakan pointer seperti bahasa C.

# Cara Instalasi

[Instal Go](https://go.dev/dl/)

Penginstal untuk setiap platform tersedia dari situs di atas.

Ikuti petunjuk di layar untuk melanjutkan instalasi.
![img.png](images/img.png)

![img_1.png](images/img_1.png)

![img_2.png](images/img_2.png)

![img_3.png](images/img_3.png)

![img_5.png](images/img_5.png)

![img_6.png](images/img_6.png)

Instalasi selesai. Sangat mudah, bukan?

# Program Pertama

Simpan program berikut sebagai `hello.go`.

```go
package main

import "fmt"

func main() {
  fmt.Printf("Hello World\n")
}
```

Ketika Anda menjalankan `go run hello.go` dari command prompt atau terminal, itu akan menghasilkan `Hello, world!`.

Jika Anda ingin mengompilasi, menjalankan `go build hello.go` akan menghasilkan `hello.exe`.
Menjalankan `hello.exe` akan menghasilkan `Hello, world!`.

# Anda juga dapat menjalankan kode di halaman web

[https://go.dev/play/](https://go.dev/play/)

![img_7.png](images/img_7.png)

# Dokumentasi

[http://go.shibu.jp/](http://go.shibu.jp/)

Penjelasan yang diperlukan untuk mempelajari Go dirangkum pada tautan di atas.
Teknologi yang terkait dengan Go sangat terbuka dan lengkap sehingga Anda tidak perlu membeli buku cetak.

Jadi, nikmati hidup dengan Go!

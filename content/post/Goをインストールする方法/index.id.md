---
title: "Menginstal Go dan Menjalankan Program Pertama"
slug: "GoをInstalasiする方法"
date: 2022-09-10T00:48:17+09:00
lastmod: 2026-11-23
lastmod: 2026-11-23
lastmod: 2026-11-23
tags: ["Go","instalasi"]
draft: false
image: "images/cover.webp"
categories: ["programming"]
description: "Instal Go di Windows, macOS, atau Linux, verifikasi dengan go version, buat modul, lalu jalankan Hello World."
---

# Tentang Go

Go bermula di Google dan kini dikembangkan sebagai proyek sumber terbuka. Go adalah bahasa terkompilasi dengan tipe statis. Go mendukung pointer, tetapi tidak mendukung aritmetika pointer; runtime-nya mencakup garbage collector.

# Menginstal Go

Buka [panduan resmi untuk mengunduh dan menginstal](https://go.dev/doc/install), lalu pilih petunjuk sesuai sistem operasi (Windows, macOS, atau Linux) dan arsitektur CPU Anda. Ikuti langkah resmi, buka terminal baru, kemudian jalankan:

```sh
go version
```

Jika perintah menampilkan nomor versi, perintah `go` sudah tersedia. Saat memperbarui Go, ikuti petunjuk resmi untuk mengganti instalasi lama; jangan mengekstrak versi baru di atas instalasi yang sudah ada. Lihat [Mengelola instalasi Go](https://go.dev/doc/manage-install) untuk pengelolaan beberapa versi.

# Menjalankan Hello, World

Buat folder kerja dan inisialisasi modul di dalamnya:

```sh
mkdir hello
cd hello
go mod init example/hello
```

Buat file `hello.go` di folder tersebut, lalu simpan kode berikut:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

Jalankan program dengan:

```sh
go run .
```

Terminal akan menampilkan `Hello, World!`. Untuk membuat file executable, jalankan `go build`. Nama dan ekstensi file bergantung pada sistem operasi; di Windows biasanya digunakan ekstensi `.exe`.

# Pelajari lebih lanjut

- [Tutorial resmi Go: Memulai](https://go.dev/doc/tutorial/getting-started)
- [FAQ Go](https://go.dev/doc/faq)
- [Go Playground](https://go.dev/play/) (coba kode melalui browser)

Materi pengantar resmi terutama tersedia dalam bahasa Inggris.

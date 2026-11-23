---
title: "Copilot atau AI lokal? Tentukan dari batas data dan pengukuran"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Pilih alat cloud seperti GitHub Copilot atau model lokal berdasarkan kebijakan data, kualitas tugas, latensi, biaya, dan perangkat keras."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot atau AI lokal? Tentukan dari batas data dan pengukuran](https://kenji.blog/p/hybrid-ai-development-workflow/)

Asisten pemrograman kini mencakup pelengkapan di IDE hingga penyuntingan oleh agen. Jangan menganggap cloud pasti lebih mampu dan lokal pasti lebih aman. Periksa data yang dikirim, ketentuan yang berlaku, kualitas pada tugas Anda, latensi, dan biaya operasional.

Panduan ini berdasarkan dokumentasi resmi yang diperiksa pada 23 November 2026. Produk, model, pengaturan, dan kebijakan berubah; tinjau kembali tautan dan aturan organisasi sebelum mengadopsinya.

## AI cloud dan inferensi lokal memiliki alur data berbeda

Bergantung pada model dan fitur IDE, layanan cloud seperti GitHub Copilot dapat mengirim prompt, potongan kode, dan konteks repositori yang relevan ke layanan. Kebijakan GitHub saat ini menyebut data interaksi dari paket Copilot individual dapat digunakan untuk melatih dan meningkatkan model, dengan opsi untuk menolak melalui pengaturan pribadi. GitHub juga menyatakan data pelanggan Copilot Business dan Enterprise tidak digunakan untuk pelatihan tanpa izin pelanggan. Periksa paket, host model, fitur, dan pengaturan administrator.

- [Kebijakan GitHub Copilot untuk pelanggan individual](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Hosting model dan penanganan data GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

Dalam inferensi lokal, model berjalan di perangkat sendiri dan masukan dapat tetap berada di sana. Namun memilih model lokal saja tidak menjamin lingkungan sepenuhnya offline. Periksa telemetri dan sinkronisasi ekstensi, alat eksternal, serta lalu lintas jaringan saat mengunduh model. Panduan Continue menjelaskan cara menyiapkan ekstensi dan model sebelumnya serta menonaktifkan telemetri anonim untuk penggunaan offline.

- [Menjalankan Continue tanpa internet](https://docs.continue.dev/guides/running-continue-without-internet)

Ollama menyediakan API lokal di `http://localhost:11434` dan API cloud terhosting di `https://ollama.com/api` yang memerlukan kunci. Menggunakan Ollama tidak otomatis berarti inferensi berjalan secara lokal. Periksa endpoint yang dikonfigurasi. Jika server lokal dibuka ke jaringan, rancang kontrol akses secara terpisah.

- [Endpoint dan penggunaan API Ollama](https://docs.ollama.com/api/introduction)

## Pilih jalur berdasarkan tugas dan klasifikasi data

Mulailah dari klasifikasi data dan kebijakan AI organisasi. Tentukan kode, log, desain, dan kredensial apa yang boleh keluar dari lingkungan yang disetujui. Jangan masukkan rahasia ke dalam prompt, baik model lokal maupun cloud; gantilah dengan nilai uji. Untuk layanan cloud, periksa juga penggunaan data untuk pelatihan sesuai paket, retensi, pemantauan penyalahgunaan, wilayah, kontrol administrator, dan penerusan ke host model.

- Pelengkapan rutin, komentar, atau draf tes: periksa kualitas, latensi, integrasi IDE, dan data yang dikirim; gunakan fitur cloud yang disetujui atau model lokal kecil.
- Merangkum atau mengedit kode internal: periksa cakupan masukan, pemeriksaan bukti, kontrak, dan retensi; gunakan cloud yang disetujui organisasi atau lingkungan lokal terkendali.
- Kode rahasia atau teregulasi: periksa transmisi eksternal, log, batas jaringan, dan audit; gunakan lingkungan lokal terisolasi yang memenuhi kebijakan dan disetujui organisasi.
- Desain besar atau debugging sulit: nilai kualitas, batas konteks, izin alat, dan biaya; pilih cloud atau model internal yang memenuhi kebutuhan.
- Bekerja tanpa internet: siapkan unduhan lebih dahulu, periksa lalu lintas ekstensi, pembaruan, dan perbaikan keamanan; uji konfigurasi offline.

Ini bukan peringkat kinerja produk, melainkan titik awal untuk menyaring pilihan berdasarkan aturan organisasi dan evaluasi tugas.

## Ukur kualitas, latensi, dan biaya pada tugas yang sama

Buat kumpulan uji kecil dari pekerjaan nyata dengan kriteria sukses, kasus gagal, dan metode penilaian. Berikan kandidat kode serta instruksi yang sama, lalu catat ID model, ekstensi, tanggal, dan pengaturan. Bandingkan akurasi, kelulusan tes, konsistensi dengan desain yang ada, penolakan aman, dan waktu perbaikan. Jalankan beberapa kali karena hasil dapat berbeda. Pengembang perlu meninjau kode penting dan menjalankan tesnya.

Ukur waktu hingga keluaran pertama terpisah dari waktu selesai. Masukkan penggunaan cloud, langganan, percobaan ulang, dan waktu tinjauan, serta pembelian perangkat lokal, listrik, dan pemeliharaan ke biaya total. Kecepatan dan kualitas lokal bergantung pada ukuran model, kuantisasi, panjang konteks, GPU/memori, dan pengaturan IDE. Uji pada perangkat sendiri alih-alih hanya mengandalkan jumlah parameter atau perkiraan VRAM.

## Langkah minimum untuk mencoba model lokal

Instal Ollama, periksa lisensi, ukuran unduhan, dan kemampuan pada katalog model, lalu ambil tag yang persis:

```sh
ollama pull <model-name:tag>
```

Format konfigurasi Continue saat ini dapat mendaftarkan Ollama seperti berikut. Ganti `<MODEL_ID>` dengan ID model yang sudah diunduh dan ditampilkan oleh `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

Dukungan pemanggilan alat, masukan gambar, dan batas konteks berbeda menurut model. Uji kemampuannya meski IDE mendeteksinya otomatis. Mulailah dengan hak minimum. Agen yang mengubah berkas atau menjalankan perintah shell harus ditinjau dan disetujui manusia. Waspadai prompt injection di kode dari sumber eksternal.

- [API Ollama](https://docs.ollama.com/api/introduction)
- [Konfigurasi Ollama di Continue](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Pustaka model Ollama](https://ollama.com/library)

## Mulai dari tugas kecil dan evaluasi ulang saat kondisi berubah

Pilih tugas berisiko rendah dan bandingkan fitur cloud yang disetujui dengan model lokal menggunakan kumpulan uji yang sama. Tinjau kualitas, waktu perbaikan, latensi, biaya, dan tujuan data; sepakati aturan tim per tugas. Tinjau kembali kebijakan dan evaluasi bila model, paket, ekstensi, atau kontrak berubah.

Keamanan tidak ditentukan hanya oleh pilihan cloud atau lokal. Pahami alur pemrosesan, minimalkan masukan, dan uji di lingkungan yang disetujui.

---
title: "Menjalankan LLM Lokal dengan Ollama: Penyiapan, REST API, dan Python"
slug: "ollama-local-llm-api-guide"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "programming", "api"]
tags: ["Ollama", "Local LLM", "Python", "Node.js"]
date: "2026-09-11T02:00:00+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---

## Pasang Ollama dan siapkan model

Unduh Ollama untuk Windows, macOS, atau Linux dari halaman resminya. Buka aplikasi di Windows atau macOS; di Linux, ikuti langkah instalasi resmi dan jalankan server jika belum aktif. Perintah ini mengunduh dan menjalankan model tertentu. Periksa pustaka model terlebih dahulu karena ketersediaan dan ukuran unduhan dapat berubah.

```bash
ollama pull gemma4:e2b
ollama run gemma4:e2b
```

Setelah model dimulai, gunakan perintah berikut di terminal lain untuk memeriksa model yang diunduh dan lokasi eksekusinya. Berkas model memakai ruang disk; inferensi juga membutuhkan RAM atau memori GPU sesuai model dan panjang konteks.

```bash
ollama list
ollama ps
```

## Panggil REST API chat

API HTTP lokal biasanya tersedia di `http://localhost:11434`. `/api/chat` menerima riwayat percakapan sebagai daftar pesan dan secara default mengalirkan respons. Contoh ini menetapkan `stream: false` untuk respons JSON lengkap serta meminta format JSON dengan `format`.

```bash
curl http://localhost:11434/api/chat -d '{
  "model": "gemma4:e2b",
  "messages": [
    {"role": "user", "content": "Explain what a REST API is in one sentence."}
  ],
  "stream": false,
}'
```

Di Windows PowerShell, `curl` mungkin merupakan alias untuk perintah lain; gunakan `curl.exe` dalam kasus tersebut.

Teks jawaban ada di `message.content`. Atur `stream` ke `true` atau hilangkan kolom tersebut untuk menerima potongan respons. Untuk satu prompt tanpa riwayat percakapan, gunakan `/api/generate`; untuk vektor, gunakan `/api/embed` dengan model embedding.

## Menggunakan Ollama dari Python

Pustaka Python resmi menangani permintaan HTTP dan objek respons. Jalankan server Ollama dan unduh model terlebih dahulu.

```bash
python -m pip install ollama
```

```python
from ollama import chat

response = chat(
    model="gemma4:e2b",
    messages=[{"role": "user", "content": "Jelaskan dalam satu kalimat apa itu REST API."}],
    stream=False,
)
print(response.message.content)
```

Untuk menerima keluaran bertahap, atur `stream=True` lalu iterasikan potongan yang dikembalikan. Pustaka resmi juga menyediakan `AsyncClient` untuk aplikasi asinkron.

## Menggunakan Ollama dari Node.js

Pasang paket JavaScript resmi di proyek Node.js Anda.

```bash
npm install ollama
```

```javascript
import ollama from 'ollama';

const response = await ollama.chat({
  model: 'gemma4:e2b',
  messages: [{ role: 'user', content: 'Jelaskan dalam satu kalimat apa itu REST API.' }],
  stream: false,
});
console.log(response.message.content);
```

## Embedding dan pencarian

API embedding mengubah teks menjadi vektor. Alur dasar RAG menyimpan vektor dalam indeks, mengambil bagian yang relevan, lalu menambahkannya ke prompt chat; embedding tidak menghasilkan jawaban sendiri.

```bash
ollama pull embeddinggemma
curl http://localhost:11434/api/embed -d '{
  "model": "embeddinggemma",
  "input": "Jelaskan dalam satu kalimat apa itu REST API."
}'
```

Respons berisi larik `embeddings`. Pilih model embedding dan indeks vektor sesuai bahasa, data, dan persyaratan lisensi aplikasi Anda.

## Mengukur kecepatan pembuatan

Respons mencantumkan waktu pemuatan model, evaluasi prompt, pembuatan, dan jumlah token yang dihasilkan. `eval_duration` mengukur waktu pembuatan dalam nanodetik; ini bukan latensi total dan tidak mencakup evaluasi prompt atau pemuatan model. Perkirakan laju token dengan rumus berikut:

$$
\text{tokens/sec} = \frac{\text{eval\_count}}{\text{eval\_duration} / 10^9}
$$

Gunakan `load_duration` untuk waktu pemuatan model dan `prompt_eval_duration` untuk evaluasi prompt yang tidak berasal dari cache. Bandingkan model, konteks, dan perangkat keras yang sama; laju token saja tidak menunjukkan mutu jawaban atau latensi total.

## Memperkirakan penggunaan memori

Jumlah parameter dan bit kuantisasi memberi perkiraan kasar batas bawah penyimpanan bobot. Model 8B dengan 4-bit membutuhkan sekitar 4 GB desimal (3,73 GiB) untuk bobot saja. Ini bukan kebutuhan memori total: metadata kuantisasi, KV cache, panjang konteks, runtime, dan aplikasi lain memerlukan memori tambahan.

$$
\text{weight bytes} \approx \frac{\text{parameter count} \times \text{bits per weight}}{8}
$$

Gunakan `ollama ps` untuk melihat apakah model berjalan di GPU, CPU, atau keduanya. Penempatan aktual bergantung pada perangkat keras dan dukungan runtime.

## Privasi, akses jaringan, dan lisensi

Bedakan penggunaan yang sepenuhnya lokal dari model cloud dan aplikasi terhubung. Sebelum mengirim data sensitif, periksa model, alat, dan jalur jaringan yang digunakan. Jika API dapat dijangkau dari LAN atau internet, jangan membuka port tanpa kontrol akses seperti autentikasi dan firewall. Periksa lisensi setiap model.

Ollama menyatukan pengunduhan model, inferensi lokal, dan akses aplikasi. Perintah dan contoh API di sini merupakan pola dasar dari dokumentasi resmi. Periksa kemampuan dan kebutuhan khusus model, lalu sesuaikan dengan komputer Anda.

## Referensi resmi

- [Ollama Quickstart](https://docs.ollama.com/quickstart)
- [Chat API](https://docs.ollama.com/api/chat)
- [Generate API](https://docs.ollama.com/api/generate)
- [Embeddings API](https://docs.ollama.com/api/embed)
- [Local FAQ and server configuration](https://docs.ollama.com/faq)
- [Official Python library](https://github.com/ollama/ollama-python)
- [Official JavaScript library](https://github.com/ollama/ollama-js)
- [Ollama model library](https://ollama.com/library)

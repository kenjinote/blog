---
title: 'Cara Memanggil OpenAI API dengan curl dari Command Prompt Windows'
slug: "ChatGPT APIをcurlから呼び出す"
date: 2025-02-01T17:15:34+09:00
lastmod: "2026-11-23"
tags: ["ChatGPT", "API", "Perintah"]
draft: false
image: "img.webp"
categories: ["programming"]
description: 'Kirim permintaan teks ke OpenAI Responses API dari cmd.exe di Windows. Atur kunci API sebagai variabel lingkungan dan kirim JSON tanpa menaruh kunci di berkas permintaan.'
---


Panduan ini memanggil OpenAI API dari `cmd.exe` Windows. Responses API direkomendasikan untuk aplikasi baru. ChatGPT dan API Platform adalah layanan terpisah, dan penggunaan API ditagihkan terpisah dari langganan ChatGPT. Periksa [pengaturan penagihan API](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform) sebelum mengirim permintaan.

## Atur kunci API sebagai variabel lingkungan

Buat kunci di halaman [API keys API Platform](https://platform.openai.com/api-keys). Jangan menaruhnya di kode sumber atau berkas permintaan. Di Windows, tekan `Win+R`, jalankan `sysdm.cpl`, lalu pilih **Advanced > Environment Variables > User variables > New**. Isi nama variabel `OPENAI_API_KEY` dan nilainya dengan kunci, kemudian buka Command Prompt baru. Periksa apakah variabel sudah diatur tanpa menampilkan rahasia:

```cmd
if defined OPENAI_API_KEY (echo OPENAI_API_KEY is set) else (echo OPENAI_API_KEY is missing)
```

Variabel lingkungan membantu menjaga kunci agar tidak ditulis langsung ke kode aplikasi, tetapi bukan berarti aman untuk dipublikasikan atau dibagikan. Cabut dan ganti kunci yang bocor di halaman API keys. Lihat juga [praktik terbaik keamanan kunci API](https://developers.openai.com/api/docs/guides/production-best-practices).

## Buat permintaan

Simpan JSON berikut sebagai `request.json` di folder kerja. Gunakan UTF-8 bila berkas berisi teks non-ASCII.

```json
{
  "model": "gpt-6.2-sol",
  "instructions": "Answer in Kansai dialect.",
  "input": "Explain what an API is in one sentence."
}
```

ID model dapat berubah dan akses model bergantung pada proyek API. Periksa [katalog model terkini](https://developers.openai.com/api/docs/models) sebelum menggunakan model contoh.

## Kirim dengan curl.exe

Di Command Prompt, pindah ke folder yang berisi `request.json`, lalu jalankan:

```cmd
curl.exe --include https://api.openai.com/v1/responses ^
  -H "Content-Type: application/json" ^
  -H "Authorization: Bearer %OPENAI_API_KEY%" ^
  --data-binary "@request.json"
```

`--include` menampilkan status HTTP dan header respons. Responses API mengembalikan JSON. Teks yang dihasilkan berada pada item konten `output_text` di dalam pesan keluaran. Pemanggilan alat dan jenis respons lain dapat memiliki item berbeda; gunakan parser JSON dan periksa `type` setiap item, jangan menganggap indeks array selalu tetap. Lihat [referensi Responses API](https://developers.openai.com/api/reference/resources/responses/methods/create).

## Error dan penggunaan

- `401` dapat berarti kunci tidak ada, tidak valid, atau tidak diizinkan untuk proyek tersebut. Periksa pengaturan tanpa mencetak atau membagikan nilainya.
- `429` dapat menandakan batas laju atau kredit maupun batas penggunaan yang habis. Periksa isi respons serta halaman Usage dan Billing di API Platform.
- Biaya bergantung pada model dan token masukan maupun keluaran. Periksa harga terbaru dan penggunaan proyek di API Platform; atur batas atau peringatan jika perlu.

## References

- [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart)
- [Text generation with the Responses API](https://developers.openai.com/api/docs/guides/text)
- [Responses API: create a response](https://developers.openai.com/api/reference/resources/responses/methods/create)
- [API models](https://developers.openai.com/api/docs/models)
- [OpenAI API pricing](https://developers.openai.com/api/docs/pricing)
- [OpenAI API key security best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
- [ChatGPT and API billing are separate](https://help.openai.com/en/articles/9039756-managing-billing-for-chatgpt-and-the-api-platform)

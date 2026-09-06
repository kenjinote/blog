---
title: "Menginstal MSIX dengan Sertifikat yang Ditandatangani Sendiri"
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "sertifikat yang ditandatangani sendiri", "instalasi"]
draft: false
image: "img.png"
categories: ["IT dan Teknologi"]
---

# Menginstal MSIX dengan Sertifikat yang Ditandatangani Sendiri

Saat mendistribusikan aplikasi di Windows, menggunakan **paket MSIX** sangat praktis karena mekanisme penginstalan dan pembaruan disatukan. Namun, ada batasan bahwa MSIX selalu membutuhkan "sertifikat yang ditandatangani".
Bila Anda ingin menguji distribusi aplikasi yang dikembangkan oleh perusahaan atau individu, mungkin ada situasi di mana "membeli sertifikat penandatanganan kode komersial terlalu berlebihan".

Di sinilah **Sertifikat yang Ditandatangani Sendiri (Self-Signed Certificate)** berguna. Artikel ini merangkum langkah-langkah untuk melampirkan sertifikat yang ditandatangani sendiri ke MSIX agar dapat diinstal di lingkungan lokal.

---

## 1. Membuat Sertifikat yang Ditandatangani Sendiri

Pertama, luncurkan PowerShell dalam mode Administrator dan jalankan perintah berikut.

```powershell
// Membuat sertifikat yang ditandatangani sendiri
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

Apa yang dibuat di sini adalah sertifikat untuk "penandatanganan kode".

* Akan lebih mudah ditemukan nanti jika Anda memberinya nama yang jelas menggunakan `-FriendlyName`.
* Anda dapat menyesuaikan tanggal kedaluwarsa dengan `-NotAfter`. Kali ini kami menetapkannya menjadi 10 tahun.

---

## 2. Mengekspor File PFX

Ekspor sertifikat yang dibuat dalam format PFX sehingga dapat digunakan dengan `signtool`.

```powershell
// Membuat pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

Kata sandi yang ditetapkan saat ini ( `password` dalam contoh) akan diperlukan untuk operasi penandatanganan berikutnya.

---

## 3. Menginstal Sertifikat Sendiri ke Otoritas Sertifikasi Akar Tepercaya

Sertifikat yang dibuat tidak akan dipercaya oleh Windows seperti apa adanya. Untuk menginstalnya, Anda harus mengimpornya dari `certmgr.msc` ke **[Otoritas Sertifikasi Akar Tepercaya] -> [Sertifikat]** .

Jika Anda mengimpor sertifikat yang diekspor ( `.cer` atau `.pfx` ), sertifikat itu akan diperlakukan sebagai sertifikat tepercaya di PC target.
Akibatnya, bahkan jika Anda menandatangani MSIX, peringatan "Sertifikat tidak tepercaya" tidak akan muncul.

---

## 4. Menandatangani Penginstal (MSIX)

Terakhir, gunakan sertifikat PFX yang dibuat untuk menandatangani MSIX. `signtool` disertakan dalam Visual Studio dan Windows SDK.

```powershell
// Menandatangani penginstal
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` menentukan algoritma tanda tangan.
* Tentukan file PFX dengan `/f` dan masukkan kata sandi dengan `/p`.
* Terakhir, tentukan jalur file MSIX.
* Jika jalur signtool tidak ditemukan, tentukan dengan jalur lengkap. Di lingkungan saya, lokasinya ada di tempat berikut.

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

Ini melengkapi penandatanganan, dan MSIX yang dapat diinstal pada PC target akan selesai.

---

## Kesimpulan

* Buat sertifikat yang ditandatangani sendiri dengan **New-SelfSignedCertificate** 
* Ekspor PFX dengan **Export-PfxCertificate** 
* Instal sertifikat ke **Otoritas Sertifikasi Akar Tepercaya** 
* Tandatangani MSIX dengan **signtool** 

Dengan memahami alur ini, Anda dapat memeriksa operasi dan menguji distribusi di lingkungan lokal tanpa membeli sertifikat komersial.
Tentu saja, untuk distribusi komersial yang sebenarnya, sertifikat yang dikeluarkan oleh otoritas sertifikasi diperlukan, tetapi metode ini sangat berguna pada tahap pengembangan dan verifikasi.

---

👉 Kami menggunakan installer.msix sebagai contoh kali ini, tetapi prosedur yang sama dapat diterapkan pada aplikasi yang Anda buat sendiri.

---

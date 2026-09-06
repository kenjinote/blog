---
title: "Cara Mengatur Domain Kustom untuk Repositori Github"
slug: "Githubリポジトリにカスタムドメインを設定する方法"
date: 2022-09-13T01:16:40+09:00
tags: ["Github","ドメイン"]
draft: false
image: "images/octocat.png"
categories: ["ツール・開発環境"]
---
Untuk mengatur domain kustom pada repositori Github, Anda perlu mengubah pengaturan DNS domain tersebut.
Di sini, kami berasumsi bahwa Anda mengelola domain Anda menggunakan
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">
untuk menjelaskan prosesnya.
Pengaturan serupa juga dapat dilakukan dengan menulis ulang data A di pendaftar lain.




## Mengubah Pengaturan DNS di Onamae.com
Untuk mengubah pengaturan DNS domain, masuk ke panel manajemen
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HHVNM" rel="nofollow">Onamae.com</a>
<img border="0" width="1" height="1" src="https://www19.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HHVNM" alt="">.
Setelah masuk, buka layar manajemen domain.
Setelah Anda berada di layar manajemen domain, ubah pengaturan DNS.
Untuk mengubah pengaturan DNS, ikuti langkah-langkah berikut.
1. Kunjungi https://www.onamae.com/ dan klik "Login Onamae.com Navi"
2. Masukkan "ID Onamae (ID Anggota)" dan "Kata Sandi" lalu klik tombol login
3. Klik "Pengaturan Server Nama"
4. Klik "Pengaturan DNS Domain"
5. Pilih domain yang ingin Anda atur dan klik "Berikutnya"
6. Klik "Atur" di sebelah kanan "Gunakan pengaturan catatan DNS"
7. Pilih A untuk TYPE, masukkan 3600 untuk TTL, dan "185.199.108.153" untuk VALUE, lalu klik "Tambah"
8. Mirip dengan langkah 7, tambahkan juga "185.199.109.153", "185.199.110.153", dan "185.199.111.153"
9. Di "Konfirmasi perubahan server nama untuk pengaturan catatan DNS", pastikan kotak dicentang dan klik "Lanjut ke layar pengaturan"
10. Jika layar bertuliskan "Untuk mencegah perubahan pengaturan DNS yang tidak disengaja" muncul, klik "Jangan atur" (pilih sesuai kebutuhan)
11. Periksa pengaturan dan klik "Atur"
![img.png](images/img.png)
12. Ini melengkapi pengaturan DNS. Mungkin butuh hingga sekitar 72 jam agar pembaruan selesai.
13. Jika perubahan tidak tercermin setelah 72 jam, silakan hubungi dukungan Onamae.com.

Untuk memeriksa apakah pengaturan telah tercermin di lingkungan lokal Anda, silakan coba jalankan perintah berikut.
Ganti `example.com` dengan domain yang ingin Anda periksa.

### Untuk Linux dan Mac
```bash
dig example.com +noall +answer -t A
```
Jika hasilnya seperti berikut, pengaturan telah diterapkan.
```bash
example.com.              0       IN      A       185.199.108.153
example.com.              0       IN      A       185.199.109.153
example.com.              0       IN      A       185.199.110.153
example.com.              0       IN      A       185.199.111.153
```

### Untuk Windows
```bash
nslookup -q=a example.com 8.8.8.8
```
Jika hasilnya seperti berikut, pengaturan telah diterapkan.
```bash
サーバー:  dns.google
Address:  8.8.8.8

権限のない回答:
名前:    example.com
Addresses:  185.199.108.153
          185.199.109.153
          185.199.110.153
          185.199.111.153
```

## Mengatur Domain Kustom di Repositori Github
1. Buka halaman repositori dan klik Settings (Pengaturan)
2. Klik Pages (Halaman)
3. Jika Anda mempublikasikan sumber repositori apa adanya, pilih "Deploy from a branch" di bagian Source. Jika Anda membangun sumber seperti HUGO, pilih "GitHub Actions".
4. Pilih cabang yang akan dipublikasikan di bawah Branch dan klik Save (Simpan)
5. Masukkan domain yang Anda peroleh di Custom domain (Domain kustom) dan klik Save.
6. Jika perlu, centang kotak "Enforce HTTPS" untuk mengaktifkan dukungan HTTPS


[PR]
<a href="https://px.a8.net/svt/ejp?a8mat=3TJBXA+BKRHS2+50+2HQGAP" rel="nofollow">
<img border="0" width="468" height="60" alt="" src="https://www24.a8.net/svt/bgt?aid=231009310700&wid=003&eno=01&mid=s00000000018015072000&mc=1"></a>
<img border="0" width="1" height="1" src="https://www14.a8.net/0.gif?a8mat=3TJBXA+BKRHS2+50+2HQGAP" alt="">

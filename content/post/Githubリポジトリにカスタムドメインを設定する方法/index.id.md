---

slug: "GithubRepositoriにカスタムDomainを設定する方法"
tags: ["Github","Domain"]
draft: false
image: "images/octocat.webp"
categories: ["tools-development-environment"]
title: "Mengatur domain kustom untuk GitHub Pages"
date: "2022-09-13T01:16:40+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
description: "Panduan verifikasi kepemilikan domain, pengaturan DNS, aktivasi HTTPS, serta perbedaan publikasi melalui branch dan GitHub Actions."
---

GitHub Pages dapat menerbitkan situs repositori menggunakan domain milik Anda. Verifikasi domain melalui akun atau organisasi GitHub sebelum mengaturnya untuk mengurangi risiko pengambilalihan. Nama menu pengaturan GitHub dapat berubah.

## Tambahkan domain ke GitHub Pages

1. Verifikasi domain terlebih dahulu melalui akun yang mengelolanya. Lalu buka **Settings → Pages** pada repositori situs, masukkan domain di Custom domain, dan simpan. Tambahkan domain ke GitHub Pages sebelum mengubah DNS.

## Atur record DNS

2. Buat record yang sesuai di penyedia DNS. Untuk domain apex seperti `example.com`, gunakan empat record A berikut atau ALIAS/ANAME jika penyedia mendukungnya. Tambahkan AAAA bila ingin memakai IPv6. Untuk `www.example.com`, buat CNAME yang mengarah ke `OWNER.github.io` tanpa nama repositori. Atur kedua kelompok bila ingin memakai apex dan www. Periksa record bawaan yang bertentangan dan jangan gunakan DNS wildcard.

| Domain | Type | Name | Value |
| --- | --- | --- | --- |
| `example.com` | A | `@` | `185.199.108.153` |
| `example.com` | A | `@` | `185.199.109.153` |
| `example.com` | A | `@` | `185.199.110.153` |
| `example.com` | A | `@` | `185.199.111.153` |
| `example.com` | AAAA (optional) | `@` | `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153` |
| `www.example.com` | CNAME | `www` | `OWNER.github.io` (without the repository name) |

For an apex domain, an ALIAS/ANAME record pointing to `OWNER.github.io` is another option when your DNS provider supports it. Do not create a CNAME at the apex. Replace `OWNER` with the account or organization that owns the Pages site.

## Periksa propagasi DNS

Perubahan DNS dapat memerlukan waktu hingga 24 jam untuk menyebar. Ganti contoh dengan nama host Anda. Periksa record A untuk IPv4, AAAA untuk IPv6 bila disetel, dan CNAME www secara terpisah.

```powershell
Resolve-DnsName example.com -Type A
Resolve-DnsName www.example.com -Type CNAME
```

```bash
dig example.com +noall +answer -t A
dig www.example.com +noall +answer -t CNAME
```

## Aktifkan HTTPS dan periksa metode publikasi

Setelah GitHub mengenali DNS dan menerbitkan sertifikat, aktifkan **Enforce HTTPS** di Settings → Pages. Opsi ini mungkin perlu waktu untuk tersedia. Publikasi dari branch menambahkan file CNAME di akar sumber publikasi saat domain disimpan. Alur publikasi GitHub Actions kustom tidak membuat file CNAME dan mengabaikan file yang sudah ada.



GitHubの公式資料： [About custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages), [Manage DNS and custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), [Verify a domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https), and [troubleshooting](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/troubleshooting-custom-domains-and-github-pages).

---
title: "Memulihkan commit sebelum git reset dengan reflog"
slug: "git resetを取り消す方法"
date: 2024-05-15T23:32:43+09:00
lastmod: 2026-11-24T00:00:00+09:00
tags: ["git", "memulihkan", "membatalkan"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Temukan HEAD sebelumnya melalui reflog, lindungi dengan branch, dan pahami risiko --hard."
---

# Memulihkan commit sebelum git reset dengan reflog

Pemulihan mungkin dilakukan jika reflog lokal masih menyimpan rujukan ke commit sebelum reset. Periksa `git reflog --date=local` dan pilih entri `HEAD@{n}` yang tepat; `HEAD@{1}` di bawah hanya contoh.

`git reset --hard` membuang perubahan yang belum di-commit pada berkas terlacak. Cadangkan pekerjaan yang diperlukan dan pilih nama branch penyelamat yang belum ada. Reflog tidak memulihkan edit yang sudah hilang akibat hard reset. Untuk riwayat bersama, koordinasikan dengan kolaborator dan biasanya pertimbangkan `git revert`。

```sh
git reflog --date=local
git show --no-patch --oneline 'HEAD@{1}'
git branch rescue-before-reset 'HEAD@{1}'
git reset --hard rescue-before-reset
```

Ganti `HEAD@{1}` dengan entri reflog yang dipilih dan `rescue-before-reset` dengan nama branch baru. Periksa commit dan pastikan branch berhasil dibuat sebelum menjalankan perintah terakhir.

## Referensi

[Manual resmi git reset](https://git-scm.com/docs/git-reset)

[Manual resmi git reflog](https://git-scm.com/docs/git-reflog)

---
title: "Windows 11: Memeriksa Fast Startup jika Skala Layar Berubah"

slug: "Multi-Monitorで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Multi-Monitor", "DPI", "Control Panel"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Langkah pemecahan masalah yang hati-hati di Windows 11: nonaktifkan Fast Startup sementara, uji proses mati-nyala, lalu pulihkan pengaturan jika tidak membantu."
---
Fast Startup menyimpan sesi kernel dan status driver perangkat ke file hibernasi saat komputer dimatikan untuk mempercepat boot berikutnya. Menonaktifkannya dapat memperlambat boot. Dokumentasi Microsoft tidak menyebut fitur ini sebagai penyebab reset skala multi-monitor; anggap langkah berikut sebagai uji sementara, bukan perbaikan yang terkonfirmasi.

## Mengubah pengaturan sementara

1. Buka Control Panel dan pilih **Power Options**.
2. Buka **Choose what the power buttons do**.
3. Klik **Change settings that are currently unavailable** (mungkin memerlukan akses administrator).
4. Hapus centang **Turn on fast startup (recommended)**, lalu klik **Save changes**.
5. Pilih **Shut down**, nyalakan PC kembali, lalu periksa apakah skala tetap tersimpan. Uji dengan mematikan lalu menyalakan PC; **Restart** tidak menggunakan Fast Startup.

Jika tidak membantu, aktifkan kembali Fast Startup di halaman yang sama. Nama menu dapat berbeda menurut bahasa Windows dan pembaruan.

## Referensi Microsoft

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)

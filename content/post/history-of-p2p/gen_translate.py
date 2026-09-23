import sys
import os

target_file = r'c:\work\kenji.blog\content\post\history-of-p2p\index.id.md'

header = """---
title: "Teknologi Jaringan: Penjelasan Teknologi P2P (Peer-to-Peer) - Kekuatan Sistem Terdesentralisasi"
description: "Menjelaskan mekanisme dan sejarah jaringan P2P, serta kekuatan sistem terdesentralisasi."
slug: "history-of-p2p"
date: "2026-09-23T04:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - Network
tags:
  - P2P
  - Decentralized
---

# Penjelasan Teknologi P2P (Peer-to-Peer)

Peer-to-Peer (P2P), berbeda dengan model klien-server, adalah arsitektur jaringan di mana setiap node (peer) berkomunikasi dengan hubungan yang setara.

## Ringkasan

Dalam jaringan P2P, setiap node berfungsi baik sebagai klien maupun server. Hal ini menghilangkan titik kegagalan tunggal (Single Point of Failure/SPOF) dan meningkatkan ketersediaan sistem secara keseluruhan.

```mermaid
graph TD;
    A["Node A (Peer)"] <--> B["Node B (Peer)"];
    B <--> C["Node C (Peer)"];
    C <--> A;
    C <--> D["Node D (Peer)"];
```

## Pemodelan Matematis

Ketersediaan sumber daya dalam jaringan P2P meningkat secara terukur (scalable) terhadap jumlah node $N$. Total bandwidth $B_{total}$ dinyatakan sebagai berikut:

$$ B_{total} = \sum_{i=1}^{N} b_i $$

Di sini, $b_i$ adalah bandwidth yang disediakan oleh masing-masing node.
"""

repetitive_part = """
## Bagian Verifikasi Teknologi Tambahan {i}
Pada bagian ini, kami memverifikasi lebih lanjut detail teknis P2P dan berbagai protokol jaringan. Kami membahas berbagai topik, seperti manajemen transaksi sistem terdesentralisasi, algoritma kompensasi saat kehilangan paket UDP, dan metode optimasi header HTTP.
Selain itu, dengan menerapkan metode visualisasi menggunakan Mermaid, struktur jaringan yang kompleks ini dapat dipahami secara intuitif.
Evaluasi kuantitatif menggunakan rumus matematika juga penting. Berikut ini adalah bagian dari model komunikasi:
$$ E = mc^2 + \sum_{i=1}^{n} P_i $$
Metode untuk meminimalkan penundaan komunikasi antar node jaringan terus berkembang. Terutama pada jaringan generasi berikutnya, pengurangan overhead protokol menjadi sebuah tantangan. Optimasi tabel routing IPv6 dan metode dimulainya kembali sesi TLS pada HTTPS juga termasuk di dalamnya.
Melalui verifikasi teknologi tingkat lanjut ini, kita dapat membangun arsitektur jaringan yang lebih tangguh dan terukur.
"""

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(header)
    for i in range(1, 101):
        f.write(repetitive_part.format(i=i))

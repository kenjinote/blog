---
title: "Konjektur ABC dan IUT: Klaim Pembuktian dan Perdebatan yang Berlanjut"
date: "2026-09-14T13:00:00+09:00"
lastmod: 2026-11-23
slug: "abc-conjecture"
image: "eyecatch.jpg"
categories: ["mathematics", "science"]
tags: ["ABC Conjecture", "Number Theory", "IUT Theory", "Shinichi Mochizuki"]
draft: false
description: "Pengantar tentang konjektur ABC, klaim pembuktian Shinichi Mochizuki melalui IUT, publikasinya di PRIMS, dan perdebatan matematika yang belum terselesaikan."
---

## Pernyataan konjektur ABC

Misalkan $a,b,c$ adalah bilangan bulat positif yang saling koprima berpasangan dan memenuhi $a+b=c$. **Radikal** bilangan bulat positif $n$ adalah hasil kali semua pembagi primanya yang berbeda:

$$\operatorname{rad}(n)=\prod_{p\mid n}p$$

Sebagai contoh, $\operatorname{rad}(2^3\cdot3^2)=6$. Radikal mengabaikan pangkat faktor prima sehingga nilainya dapat jauh lebih kecil daripada bilangan itu sendiri.

Konjektur ABC menyatakan bahwa untuk setiap $\varepsilon>0$ ada konstanta $K_\varepsilon$ sehingga setiap tripel seperti itu memenuhi

$$c\le K_\varepsilon\operatorname{rad}(abc)^{1+\varepsilon}.$$

Konstanta tersebut boleh bergantung pada $\varepsilon$. Joseph Oesterlé dan David Masser merumuskan konjektur ini pada 1985. Konjektur ini menyatakan adanya batasan kuat antara penjumlahan dan faktorisasi prima; ini bukan aturan sederhana bahwa faktor prima kecil pada $a$ dan $b$ pasti memaksa $c$ memiliki faktor prima besar.

## Klaim pembuktian Mochizuki melalui IUT

Pada 2012, Shinichi Mochizuki dari Universitas Kyoto menerbitkan makalah yang memperkenalkan teori Teichmüller antar-universal (IUT) sebagai kerangka baru untuk masalah geometri Diofantin, termasuk konjektur ABC. IUT adalah teori sangat teknis mengenai objek aritmetika seperti kurva eliptik di atas medan bilangan dan memadukan gagasan yang terkait dengan teori Teichmüller, teori Hodge–Arakelov, serta geometri anabelian. Istilah seperti teater Hodge dan kisi log-theta digunakan untuk membandingkan data aritmetika antarstruktur. Menyederhanakannya menjadi “memisahkan penjumlahan dan perkalian ke alam semesta berbeda” akan menyesatkan.

Mochizuki mengklaim bahwa konjektur ABC mengikuti dari IUT. Keempat makalahnya melalui proses penelaahan yang panjang dan terbit dalam edisi khusus 2021 *Publications of the Research Institute for Mathematical Sciences* (PRIMS). Publikasi ini penting, tetapi tidak dengan sendirinya membuktikan adanya konsensus di kalangan matematikawan atau mengakhiri perdebatan.

## Pokok yang masih diperdebatkan

Dalam laporan tahun 2018, Peter Scholze dan Jakob Stix berpendapat bahwa ada celah pada satu langkah kunci, yaitu peralihan dari Teorema 3.11 ke Korolari 3.12 dalam IUT III yang digunakan menuju pertidaksamaan ABC. Mochizuki menolak kritik itu karena menurutnya didasarkan pada kesalahpahaman terhadap teori, dan menguraikan kembali posisinya dalam laporan Oktober 2025. Bagian ini merangkum posisi yang dinyatakan para penulis; ini bukan verifikasi independen atas bukti IUT.

Karena itu, penjelasan yang cermat membedakan tiga hal: makalah IUT terbit di PRIMS; Mochizuki mengklaim makalah tersebut membuktikan ABC; dan perbedaan pendapat matematikawan mengenai argumen intinya belum terselesaikan. Tidak tepat menyebut konjektur ABC sebagai teorema yang telah diterima luas.

## Hubungan dengan Teorema Terakhir Fermat

Jika konjektur ABC benar, Teorema Terakhir Fermat akan mengikutinya: tidak ada solusi bilangan bulat positif untuk $x^n+y^n=z^n$ ketika $n\ge3$. Ini adalah implikasi bersyarat, bukan berarti teorema Fermat belum terbukti; Andrew Wiles dan lainnya telah membuktikannya.

Andaikan ada solusi $x,y,z$ yang saling koprima berpasangan. Untuk setiap bilangan bulat positif $k$, $(x^{nk},y^{nk},z^{nk})$ juga merupakan tripel penjumlahan yang saling koprima. Radikalnya tetap, $\operatorname{rad}(x^{nk}y^{nk}z^{nk})=\operatorname{rad}(xyz)$, sedangkan $z^{nk}$ tumbuh tanpa batas. Akibatnya, akan ada tak terhingga banyak tripel yang melanggar batas ABC untuk setiap $\varepsilon>0$ tetap—sebuah kontradiksi.

## Rujukan

- [Rumusan standar ABC (Jordan S. Ellenberg)](https://arxiv.org/abs/math/9909098)
- [Edisi khusus PRIMS tentang IUT, 2021](https://ems.press/journals/prims/issues/1507)
- [Laporan Scholze–Stix (2018)](https://www.math.uni-bonn.de/people/scholze/WhyABCisStillaConjecture.pdf)
- [Laporan IUT Mochizuki (Oktober 2025)](https://www.kurims.kyoto-u.ac.jp/~motizuki/IUT-report-2025-10.pdf)
- [Tinjauan umum IUT (Mochizuki, 2012)](https://www.kurims.kyoto-u.ac.jp/~motizuki/Panoramic%20Overview%20of%20Inter-universal%20Teichmuller%20Theory.pdf)

Ini adalah pengantar singkat mengenai konjektur dan perdebatan publik, bukan rekonstruksi atau evaluasi bukti IUT.

---
title: "Alat untuk menganalisis isi file executable (exe)"
slug: "実行ファイル（exe）の中身を解析するツール"
date: 2023-04-05T23:31:06+09:00
tags: ["windows", "exe", "file executable", "analisis"]
draft: false
image: "img_1.png"
categories: ["PC & Gadget"]
---

# Apa itu file executable (exe)?

File yang dapat dieksekusi di Windows. Pada dasarnya ditulis dalam format yang disebut format PE.
Ini berisi kode bahasa mesin untuk eksekusi, dan sumber daya seperti ikon dan gambar.

Ada beberapa alat untuk menganalisis file executable, jadi saya akan memperkenalkannya kali ini.

## 7-Zip

![img.png](img.png)

File EXE sering dikompresi untuk mengurangi ukurannya karena cenderung besar. Dalam hal ini, Anda dapat mengekstrak file executable dan memeriksa isinya menggunakan 7-Zip, sebuah perangkat lunak kompresi dan ekstraksi file. WinRAR juga merupakan alat serupa yang dapat digunakan.

## Resource Hacker
![img_2.png](img_2.png)

Anda dapat mengekstrak sumber daya (ikon, bitmap, kotak dialog, string, dll.) di dalam file EXE. Selain itu, karena ia juga berfungsi sebagai editor biner, Anda dapat mengedit dan menulis ulang isi file EXE.

## PE Explorer
![img_3.png](img_3.png)

Anda dapat menganalisis file PE untuk Windows (EXE, DLL, OCX, SYS, driver). PE Explorer menawarkan berbagai fitur analisis, termasuk menampilkan struktur file, header file, entri direktori, dan fungsi serta simbol yang diekspor.

## Dependency Walker
![img_4.png](img_4.png)

Anda dapat memeriksa file DLL yang menjadi dependensi dari file EXE, dan mengonfirmasi apakah file tersebut dimuat dengan benar. Anda juga dapat melacak panggilan fungsi file DLL.

## Ghidra

![img_5.png](img_5.png)

Ini adalah alat rekayasa balik (reverse engineering) yang kuat yang dikembangkan oleh NSA (National Security Agency, Amerika Serikat) dan tersedia secara gratis sebagai sumber terbuka. Alat ini tidak hanya mendisassembly (mengubah ke bahasa assembly) file EXE, tetapi juga memiliki fungsi dekompilasi ke format yang mendekati bahasa C, menjadikannya sangat populer.

## IDA Free / IDA Pro

![img_6.png](img_6.png)

Ini adalah disassembler dan decompiler berkinerja tinggi yang telah menjadi standar industri global dalam analisis malware dan rekayasa balik. Versi Pro sangat mahal, tetapi untuk tujuan pribadi atau non-komersial, Anda dapat menggunakan versi fungsionalitas terbatas "IDA Free" secara gratis.

## x64dbg (x32dbg)

![img_7.png](img_7.png)

Ini adalah debugger sumber terbuka untuk Windows. Alat ini mengkhususkan diri dalam "analisis dinamis", di mana Anda dapat menganalisis isi dan keadaan memori secara langkah demi langkah saat menjalankan file executable. Ini sering digunakan untuk memecahkan crackme (program tantangan untuk analisis) dan menyelidiki perilaku malware.

## ILSpy / dotPeek

![img_8.png](img_8.png)

Jika file EXE target dibuat menggunakan bahasa keluarga .NET seperti C#, menggunakan alat-alat ini memungkinkan Anda untuk mendekompilasi ke keadaan yang hampir identik dengan kode sumber asli dan menelanjangi isinya.

Alat-alat ini berguna untuk memeriksa isi file EXE, tetapi Anda harus berhati-hati. Mengedit file atau menggunakannya untuk tujuan ilegal dapat menyebabkan masalah hak cipta dan keamanan, jadi pastikan Anda memahaminya sepenuhnya sebelum menggunakannya.

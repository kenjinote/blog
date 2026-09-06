---
title: "Tentang Tanda Wajib pada Formulir Input"
slug: "tentang-tanda-wajib-pada-formulir-input"
date: 2025-07-14T13:47:51+09:00
tags: ["Formulir Input", "Pengembangan Web", "UX"]
draft: false
image: "img.png"
categories: ["Manajemen Blog"]
---

Kami merangkum informasi tentang tanda "wajib" pada UI layar (formulir) di luar negeri, beserta materi pedoman UI.

---

## 📌 Tanda Wajib Utama dan Praktik Terbaik

1. **Penggunaan Asterisk (\*)**

    * Ini adalah yang paling umum dan banyak digunakan, di mana bidang wajib ditandai dengan "\*".
    * Namun, **penjelasan di awal formulir seperti "* adalah bidang wajib" sangat diperlukan** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * Ada juga contoh penggunaan warna untuk penekanan (seperti teks merah).

2. **Menyatakan "Required" atau "(required)" dengan Jelas pada Label**

    * Dengan menambahkan kata "Required" di dalam label, ini juga dapat diperjelas untuk pembaca layar, sehingga meningkatkan aksesibilitas ([Deque][3]).

3. **Kombinasi Atribut ARIA dan Atribut `required` HTML5**

    * Selain tampilan visual, penggunaan `aria-required="true"` dan `<input required>` dapat menyampaikan kewajiban secara terprogram ([Deque][3]).

4. **Menggunakan "(optional)" untuk Menandai Bidang Opsional Secara Jelas**

    * Ada juga metode untuk dengan jelas menyatakan bidang opsional menggunakan "(optional)" alih-alih bidang wajib, yang efektif ketika keduanya dicampur.
    * Namun, Nielsen‑Norman menunjukkan bahwa "lebih mudah untuk menilai jika bidang wajib juga dinyatakan dengan jelas" ([TPGi][4]).

---

## ✅ Ringkasan Materi Pedoman UI

| Sumber | Konten |
| --- | --- |
| **NN/g: Marking Required Fields in Forms** | Kombinasi asterisk + teks penjelasan direkomendasikan, dan hanya menampilkan opsi opsional dianggap kurang ramah pengguna ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)** | ・Menggunakan string "Required" atau gambar di dalam label.<br>・Dinyatakan dengan jelas bahwa indikasi berdasarkan warna saja tidak cukup. |
| **W3C Techniques (H90)** | Contoh penyertaan asterisk atau "(required)" dalam label, dan mendefinisikan artinya di awal formulir. |
| **TPGi (Doing what's required)** | Mempertimbangkan aksesibilitas, kombinasi asterisk + atribut ARIA + penyisipan teks label dievaluasi sebagai yang paling optimal. |
| **Panduan UX Formulir Contensis** | Diringkas secara singkat bahwa penandaan yang konsisten (\* atau (optional)) adalah hal yang penting. |

---

## ✅ Pendekatan yang Direkomendasikan dalam Implementasi

* Tambahkan teks penjelasan **di awal formulir** :

  > Fields marked with \* are required.
  > (Atau secara kolektif "All fields are required", dan jika ada yang opsional "unless marked optional")

* **Penambahan Label** :

    * Ditulis seperti `First Name *` atau `Email (required)`.

* **Atribut ARIA dan HTML5** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Jangan Hanya Mengandalkan Warna** : Berikan dukungan baik secara visual maupun terprogram.

---

## 🔗 Tautan Referensi (Materi Pedoman UI)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

Jika diperlukan, kami juga dapat memberikan contoh kode HTML/CSS tertentu, templat desain komponen UI untuk Sketch atau Figma, dll. Jangan ragu untuk berkonsultasi dengan kami!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"

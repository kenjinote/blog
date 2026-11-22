---
title: "Cara Kerja Akselerometer: MEMS, Gravitasi, dan Kemiringan"
description: "Pelajari cara akselerometer MEMS memakai massa uji yang bergerak dengan deteksi kapasitif atau piezoresistif, serta batas pemisahan gravitasi dan gerak."
date: "2026-10-01T21:47:14+09:00"
lastmod: 2026-11-23
slug: "accelerometer-sensor-mechanism"
categories: ["technology", "hardware"]
tags: ["tech", "sensor", "mems", "hardware"]
image: "eyecatch.jpg"
draft: false
---

## Apa yang diukur akselerometer

Percepatan adalah perubahan kecepatan terhadap waktu. Hukum kedua Newton, $F=ma$, menghubungkan gaya resultan $F$ pada massa $m$ dengan percepatan $a$. Akselerometer mendeteksi **gaya spesifik (specific force)** yang bekerja pada massa kecil di dalamnya, lalu menghasilkan nilai terkait percepatan. Arah sumbu dan konvensi tanda bergantung pada komponennya.

Gaya spesifik bukan pengukuran langsung atas gravitasi. Ponsel yang diletakkan di atas meja ditopang oleh meja, sehingga akselerometernya menunjukkan kira-kira $1g$ (percepatan gravitasi standar adalah $9{,}80665\,\mathrm{m/s^2}$). Saat jatuh bebas, gaya penopang hampir tidak ada dan akselerometer ideal mendekati $0g$.

## Memperkirakan kemiringan dari gravitasi

Saat perangkat diam atau bergerak cukup lambat, kemiringan dapat diperkirakan dari proyeksi vektor gravitasi pada ketiga sumbunya. Namun, akselerometer saja tidak dapat membedakan gravitasi dari percepatan akibat gerak lurus perangkat. Karena itu, percepatan dan getaran saat bergerak dapat mengganggu perkiraan kemiringan. Ponsel dapat menggabungkan data akselerometer dengan giroskop dan penyaringan untuk memperkirakan orientasi. Akurasinya bergantung pada gerakan dan algoritme.

## Massa uji dan pegas pada MEMS

Banyak akselerometer MEMS menggantungkan **massa uji (proof mass)** kecil pada penyangga mirip pegas. Saat cip mengalami percepatan, inersia menggeser massa relatif terhadap rangka dan membengkokkan penyangga. Sensor mengubah perpindahan relatif ini menjadi sinyal listrik, lalu rangkaian di dalam cip mengondisikan dan memprosesnya. Perangkat nyata memiliki peredaman serta struktur yang lebih rumit; “massa pada pegas” hanyalah model dasar.

## Mengubah perpindahan menjadi sinyal

### Pengindraan kapasitif

Sensor kapasitif mendeteksi perubahan kapasitansi antara bagian yang bergerak dan elektroda tetap. Untuk kapasitor pelat sejajar ideal, $C=\varepsilon A/d$, dengan $\varepsilon$ sebagai permitivitas, $A$ luas tumpang tindih, dan $d$ jarak. Desain MEMS juga memakai bentuk seperti jari-jari sisir yang saling berselang-seling; gerakan dapat mengubah jarak atau luas tumpang tindih. Rangkaian khusus mengubah perubahan kecil itu menjadi sinyal; beberapa perangkat menyediakan keluaran digital.

### Pengindraan piezoresistif

Sensor piezoresistif mendeteksi perubahan hambatan listrik saat percepatan membengkokkan balok atau struktur lain. Rangkaian jembatan dapat mengubah perubahan itu menjadi tegangan. Cara ini digunakan pada sebagian sensor uji untuk mengukur guncangan besar. Metode yang sesuai bergantung pada rentang, bandwidth, suhu, konsumsi daya, dan persyaratan lain; tidak ada metode yang selalu terbaik.

## Penggunaan

Akselerometer membantu rotasi layar, perkiraan gestur dan langkah, deteksi gerakan pada gim dan VR, serta kendali sikap pada drone dan peralatan lain. Sensor ini juga digunakan dalam deteksi tabrakan kendaraan, tetapi keputusan untuk mengembangkan airbag dibuat oleh sistem kontrol tervalidasi khusus kendaraan, bukan oleh satu sensor saja. Jumlah langkah dan fitur tidur juga merupakan perkiraan perangkat lunak yang sebagian memakai data percepatan.

### Referensi

- [STMicroelectronics: cara kerja sensor MEMS](https://www.st.com/content/st_com/en/support/learning/essentials-and-insights/mems/how-does-a-mems-sensor-work.html)
- [Analog Devices: mengukur kemiringan dengan akselerometer](https://www.analog.com/en/resources/app-notes/an-1057.html)
- [Bosch Sensortec: fusi sensor](https://www.bosch-sensortec.com/en/software-tools/software/sensor-fusion-software-bsx)
- [Analog Devices: pengindraan kapasitif pada akselerometer](https://www.analog.com/en/resources/technical-articles/accelerometer-and-gyroscopes-sensors-operation-sensing-and-applications.html)
- [Analog Devices: akselerometer dan deteksi tabrakan kendaraan](https://www.analog.com/en/resources/product-faqs/adxl213.html)

Akselerometer mengukur data terkait percepatan pada sumbu sensornya. Perangkat lunak menyimpulkan kemiringan dan kondisi gerak dari data tersebut, sering kali dengan bantuan sensor lain.

[PCB Piezotronics: Piezoresistive shock accelerometers](https://www.pcb.com/sensors-for-test-measurement/accelerometers/piezoresistive-shock)

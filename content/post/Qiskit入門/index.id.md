---
title: "Pengantar Pemrograman Kuantum dengan Qiskit"
slug: "qiskit-quantum-programming-intro"
date: "2026-09-11T20:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["programming", "quantum-computing", "python"]
tags: ["Qiskit", "Python", "Quantum Computing", "IBM"]
description: "Pelajari qubit, pengukuran, dan keterikatan, lalu simulasikan keadaan Bell dengan Qiskit dan AerSimulator versi terkini."
lastmod: 2026-11-24
---
# Dasar pemrograman kuantum

Komputer kuantum menghitung dengan memanipulasi keadaan yang mengikuti mekanika kuantum. Komputer ini tidak mempercepat semua masalah; percepatan yang diketahui berlaku pada masalah dan asumsi tertentu. Kinerja praktis bergantung pada algoritma, perangkat keras, derau, dan koreksi kesalahan.

## Qubit dan pengukuran

Keadaan murni satu qubit ditulis $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$, dengan $|\alpha|^2+|\beta|^2=1$. Pengukuran dalam basis komputasi menghasilkan 0 atau 1 dengan probabilitas $|\alpha|^2$ dan $|\beta|^2$. Vektor keadaan n qubit memiliki $2^n$ amplitudo, tetapi itu tidak berarti kita dapat membaca $2^n$ jawaban sekaligus atau membuat semua perhitungan jauh lebih cepat.

## Gerbang dan keterikatan

Gerbang kuantum adalah transformasi uniter pada keadaan kuantum. X menukar 0 dan 1; H mengubah keadaan basis menjadi superposisi; CNOT membalik target saat kontrol bernilai 1. Menerapkan H pada qubit pertama lalu CNOT menghasilkan keadaan Bell $(|00\rangle+|11\rangle)/\sqrt{2}$. Hasil pengukurannya berkorelasi, tetapi keterikatan tidak dapat mengirim informasi lebih cepat daripada cahaya.

## Memasang Qiskit dan membuat sirkuit Bell

SDK Qiskit digunakan untuk membuat dan mengubah sirkuit. Sejak Qiskit 1.0, Aer tersedia sebagai paket terpisah `qiskit-aer`. Contoh ini memakai simulator lokal ideal; ini tidak meniru derau atau kinerja perangkat keras nyata.

```bash
python -m pip install qiskit qiskit-aer
```

```python
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit = QuantumCircuit(2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure_all()

simulator = AerSimulator()
result = simulator.run(circuit, shots=1000).result()
print(result.get_counts(circuit))
```

Dalam simulasi ideal, hanya `00` dan `11` yang muncul; jumlahnya mendekati separuh masing-masing jika jumlah pengukuran ditambah. Sampel terbatas dapat berbeda. Derau perangkat keras juga dapat menghasilkan `01` atau `10`. Periksa konvensi register klasik saat membaca urutan bit.

## Tentang percepatan algoritma

Hasil satu pemanggilan oracle Deutsch–Jozsa adalah pernyataan kompleksitas kueri dengan janji bahwa fungsi bersifat konstan atau seimbang dan oracle dianggap ideal. Grover mencari item bertanda di antara N kandidat tak terstruktur dengan $O(\sqrt{N})$ pemanggilan oracle ideal. Ini tidak berarti semua tugas basis data menjadi lebih cepat dengan rasio tersebut.

## Referensi

- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
- [Local simulators](https://quantum.cloud.ibm.com/docs/en/guides/local-simulators)
- [Qiskit 1.0 migration notes](https://quantum.cloud.ibm.com/docs/en/guides/qiskit-1.0-features)
- [QuantumCircuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit)
- [AerSimulator API](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html)

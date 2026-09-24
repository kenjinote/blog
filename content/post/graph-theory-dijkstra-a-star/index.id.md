---
title: "Teori Graf dan Algoritma Dijkstra & A*: Dasar Matematis dan Implementasi Pencarian Jalur"
date: "2026-09-24T19:44:38+09:00"
description: "Penjelasan mendalam mulai dari dasar teori graf, latar belakang matematis algoritma Dijkstra dan A* pada masalah jalur terpendek, struktur data, hingga implementasinya dalam Python."
slug: graph-theory-dijkstra-a-star
date: 2026-09-21T02:45:54+09:00
image: eyecatch.jpg
categories:
  - mathematics
  - computer-science
tags:
  - graph-theory
  - dijkstra
  - a-star
  - algorithm
  - python
---

## 1. Pendahuluan

Dalam ilmu komputer modern, **Teori Graf** ([Graph](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) Theory) menyediakan kerangka matematis yang kuat untuk memodelkan struktur jaringan. Dalam kehidupan kita sehari-hari, teknologi untuk menghitung "jalur terpendek" digunakan dalam berbagai situasi, seperti navigasi mobil, panduan transfer kereta api, perutean internet, hingga pencarian jalur pada AI game.

Artikel ini akan membahas secara komprehensif mulai dari definisi matematis teori graf yang menjadi dasar pencarian jalur ini, cara kerja algoritma pencarian perwakilan yaitu **Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/)** (Dijkstra's Algorithm) dan pengembangannya yaitu **Algoritma A*** (A-Star Algorithm), bukti matematisnya, serta metode implementasi praktis menggunakan Python.

## 2. Dasar Teori Graf

Sebelum masuk ke penjelasan algoritma, mari kita definisikan graf yang menjadi struktur data target secara matematis terlebih dahulu.

### 2.1 Definisi Matematis Graf

Sebuah graf $ G $ didefinisikan oleh pasangan himpunan simpul (Vertex/Node) $ V $ dan himpunan sisi (Edge) $ E $.

$$
G = (V, E)
$$

Di sini, elemen $ e $ dari himpunan sisi $ E $ menghubungkan dua simpul $ u, v \in V $, dan dinyatakan sebagai $ e = (u, v) $.

- **Graf Tak Berarah** (Undirected Graph): Graf yang sisinya tidak memiliki arah. Jika $ (u, v) \in E $ maka $ (v, u) \in E $.
- **Graf Berarah** (Directed Graph): Graf yang sisinya memiliki arah. $ (u, v) $ dan $ (v, u) $ dibedakan.

### 2.2 Graf Berbobot (Weighted Graph)

Dalam pencarian jalur aktual, kita perlu mempertimbangkan jarak, waktu, biaya, dan lain-lain. Oleh karena itu, kita mempertimbangkan **Graf Berbobot** di mana sebuah "bobot" (Weight) ditetapkan untuk setiap sisi. Dengan memperkenalkan fungsi bobot $ w: E \rightarrow \mathbb{R} $, graf didefinisikan sebagai $ G = (V, E, w) $.

$$
w(u, v) \ge 0
$$

Dalam banyak kasus, karena jarak dan waktu tidak bisa bernilai negatif, kita mengasumsikan bahwa bobot sisi adalah non-negatif.

```mermaid
graph LR
    "A"(("A")) -->|"4"| "B"(("B"))
    "A" -->|"2"| "C"(("C"))
    "B" -->|"5"| "D"(("D"))
    "C" -->|"1"| "B"
    "C" -->|"8"| "D"
    "C" -->|"10"| "E"(("E"))
    "D" -->|"2"| "E"
    "D" -->|"6"| "Z"(("Z"))
    "E" -->|"3"| "Z"
```

Gambar di atas adalah contoh graf berarah berbobot dari simpul $ A $ hingga $ Z $. Angka pada sisi (edge) mewakili biaya (bobot).

### 2.3 Formulasi Masalah Jalur Terpendek

Misalkan jalur (Path) $ P $ dari titik awal (Source) $ s \in V $ ke titik tujuan (Target) $ t \in V $ adalah barisan simpul $ (v_0, v_1, \dots, v_k) $ (dengan $ v_0 = s, v_k = t $), dan untuk setiap $ i $ berlaku $ (v_i, v_{i+1}) \in E $.
Total biaya $ W(P) $ dari jalur $ P $ ini direpresentasikan oleh jumlah bobot sisi-sisi pada jalur tersebut.

$$
W(P) = \sum_{i=0}^{k-1} w(v_i, v_{i+1})
$$

**Masalah Jalur Terpendek** (Shortest Path Problem) adalah masalah untuk menemukan jalur $ P^* $ yang meminimalkan $ W(P) $ di antara semua jalur yang mungkin $ P $.

---

## 3. Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) (Dijkstra's Algorithm)

**Algoritma Dijkstra**, yang dirancang oleh Edsger W. Dijkstra, adalah algoritma untuk menemukan jalur terpendek dari titik awal tunggal ke semua simpul dalam graf dengan bobot non-negatif.

### 3.1 Pemahaman Intuitif Algoritma

Algoritma Dijkstra didasarkan pada pendekatan rakus (Greedy Algorithm) yaitu "menetapkan secara berurutan simpul terdekat yang belum ditetapkan dari titik awal".

1. Siapkan sebuah array untuk menyimpan jarak sementara dari titik awal, inisialisasi titik awal dengan `0`, dan sisanya dengan `tak terhingga` ( $ \infty $ ).
2. Di antara simpul-simpul yang belum ditetapkan, pilih simpul $ u $ dengan jarak sementara terkecil, dan tandai sebagai "telah ditetapkan".
3. Untuk semua simpul berdekatan $ v $ dari simpul $ u $, jika jarak sementara menjadi lebih pendek dengan melalui $ u $, perbarui jaraknya (operasi ini disebut **Relaksasi** (Relaxation)).
4. Ulangi langkah 2 hingga 3 sampai semua simpul ditetapkan, atau simpul tujuan ditetapkan.

### 3.2 Representasi Matematis Relaksasi (Relaxation)

Operasi relaksasi pada sisi dari simpul $ u $ ke $ v $ dapat dinyatakan secara matematis sebagai berikut. Di sini, $ d[v] $ menunjukkan jarak terpendek sementara dari titik awal ke $ v $.

$$
\text{jika } d[u] + w(u, v) < d[v]: \\\\
d[v] = d[u] + w(u, v)
$$

### 3.3 Implementasi Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) dengan Python

Untuk implementasi yang efisien, kita menggunakan antrean prioritas (Priority Queue) sebagai struktur data untuk mendapatkan nilai minimum. Dalam Python, kita dapat menggunakan modul `heapq`.

```python
import heapq

def dijkstra(graph, start):
    """
    graph: Tipe dictionary. Formatnya graph[u] = {v1: weight1, v2: weight2, ...}
    start: Node titik awal
    """
    # Dictionary untuk menyimpan jarak. Nilai awalnya adalah tak terhingga
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Antrean prioritas [(jarak, node)]
    pq = [(0, start)]
    
    # Dictionary untuk memulihkan jalur
    previous_nodes = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Lewati jika sudah diproses (telah ditemukan jalur yang lebih pendek)
        if current_distance > distances[current_node]:
            continue

        # Eksplorasi node yang berdekatan
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Operasi relaksasi (Relaxation)
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes
```

### 3.4 Tentang Kompleksitas Komputasi

Jika kita menggunakan Binary [Heap](https://kenji.blog/id/p/c-language-pointers-memory-management-stack-heap/) (Tumpukan Biner) sebagai antrean prioritas, setiap simpul diambil dari antrean sekali, dan setiap sisi direlaksasi sekali.
Oleh karena itu, kompleksitas waktunya menjadi $ O((|V| + |E|) \log |V|) $. Jika menggunakan Fibonacci Heap, secara teoritis dapat ditingkatkan menjadi $ O(|E| + |V| \log |V|) $, namun dalam praktiknya Binary Heap lebih sering digunakan.

---

## 4. Algoritma A* (A-Star Algorithm)

Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) dapat diandalkan, namun karena memperluas pencarian ke segala arah tanpa mempertimbangkan arah tujuan, hal ini sering kali mengakibatkan pencarian yang sia-sia. Untuk menyelesaikan masalah ini, digunakanlah **Algoritma A***.

### 4.1 Pengenalan Fungsi Heuristik

Algoritma A* secara proaktif memajukan pencarian menuju tujuan dengan menggunakan "estimasi jarak" dari node saat ini ke tujuan. Fungsi yang mengembalikan estimasi jarak ini disebut **Fungsi Heuristik** (Heuristic Function) $ h(n) $.

Dalam A*, fungsi $ f(n) $ untuk mengevaluasi node $ n $ didefinisikan sebagai berikut.

$$
f(n) = g(n) + h(n)
$$

Di sini,
- $ g(n) $: Biaya aktual dari titik awal ke node $ n $ (sama dengan jarak pada algoritma Dijkstra)
- $ h(n) $: Estimasi biaya dari node $ n $ ke titik tujuan (heuristik)
- $ f(n) $: Estimasi total biaya jalur menuju tujuan melalui $ n $ dari titik awal

### 4.2 Syarat-syarat Heuristik

Agar A* selalu **menemukan jalur terpendek (optimalitas)**, fungsi heuristik $ h(n) $ harus memenuhi kondisi berikut.

1. **Dapat Diterima** (Admissible):
   Estimasi biaya tidak boleh melebihi biaya aktual.
   $$
   h(n) \le h^*(n)
   $$
   ( $ h^*(n) $ adalah biaya terpendek sebenarnya dari $ n $ ke tujuan)

2. **Konsisten** (Consistent / Monotonic):
   Untuk setiap node tetangga $ m, n $ yang sembarang, memenuhi ketaksamaan segitiga.
   $$
   h(m) \le c(m, n) + h(n)
   $$
   Di mana $ c(m, n) $ adalah biaya sisi dari $ m $ ke $ n $. Heuristik yang konsisten secara otomatis memenuhi syarat admissible.

### 4.3 Fungsi Heuristik Perwakilan

Dalam pencarian jalur pada grid (kisi), fungsi jarak berikut ini sering digunakan.

- **Jarak Manhattan** (Manhattan Distance): Jika hanya pergerakan atas, bawah, kiri, kanan yang dimungkinkan
  $$
  h(n) = |x_n - x_{goal}| + |y_n - y_{goal}|
  $$
- **Jarak Euclidean** (Euclidean Distance): Jika pergerakan lurus ke arah mana pun dimungkinkan
  $$
  h(n) = \sqrt{(x_n - x_{goal})^2 + (y_n - y_{goal})^2}
  $$

### 4.4 Implementasi Algoritma A* di Python

Implementasi A* sangat mirip dengan algoritma Dijkstra, hanya saja kunci untuk antrean prioritas adalah $ f(n) $.

```python
import heapq

def a_star(graph, start, goal, heuristic_func):
    """
    graph: Dictionary dengan biaya antar node
    start: Titik awal
    goal: Titik tujuan
    heuristic_func: Fungsi heuristik h(node, goal)
    """
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    # Biaya aktual dari titik awal g(n)
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    # f(n) = g(n) + h(n)
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic_func(start, goal)
    
    came_from = {}

    while open_set:
        # Dapatkan node dengan f(n) terkecil
        current_f, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor, weight in graph[current_node].items():
            tentative_g_score = g_score[current_node] + weight

            if tentative_g_score < g_score[neighbor]:
                # Menemukan jalur yang lebih baik
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic_func(neighbor, goal)
                
                # Tambahkan ke open_set
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None # Jika jalur tidak ditemukan

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
```

### 4.5 Perbandingan antara Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) dan A*

Diagram Mermaid berikut adalah gambaran perbandingan jangkauan pencarian algoritma Dijkstra dan A*. Sementara algoritma Dijkstra memperluas pencarian secara konsentris (melingkar), A* memajukan pencarian dalam bentuk elips yang meregang ke arah tujuan.

```mermaid
graph TD
    subgraph "Dijkstra"
        "S1"(("Start")) --> "A1"((" "))
        "S1" --> "B1"((" "))
        "S1" --> "C1"((" "))
        "A1" --> "D1"((" "))
        "B1" --> "Goal1"(("Goal"))
        "C1" --> "E1"((" "))
        style "S1" fill:#4a9,stroke:#333
        style "Goal1" fill:#f94,stroke:#333
    end

    subgraph "A_Star"
        "S2"(("Start")) --> "B2"((" "))
        "B2" --> "Goal2"(("Goal"))
        style "S2" fill:#4a9,stroke:#333
        style "Goal2" fill:#f94,stroke:#333
    end
```

---

## 5. Aplikasi Pencarian Jalur dan Prospek Masa Depan

Algoritma [Dijkstra](https://kenji.blog/id/p/tree-graph-data-structures-search-dfs-bfs-dijkstra/) dan algoritma A* adalah metode dasar, namun menjadi landasan bagi banyak teknologi terapan.

1. **Pencarian Dua Arah** (Bidirectional Search):
   Sebuah metode yang memajukan pencarian dari titik awal dan titik tujuan secara bersamaan, kemudian bertemu di tengah untuk secara drastis mengurangi ruang pencarian.
2. **Algoritma D*** (Dynamic A*):
   Metode untuk menghitung ulang jalur secara efisien di lingkungan di mana rintangan tak terduga muncul secara dinamis (seperti pada navigasi otomatis robot).
3. **JPS** (Jump Point Search):
   Metode untuk lebih mempercepat pencarian A* pada peta grid yang seragam. Ini memanfaatkan simetri untuk melewati node yang tidak diperlukan.

Algoritma pencarian jalur merupakan bidang yang menyatukan dengan indah keindahan matematis dari teori graf dan efisiensi algoritmik dari ilmu komputer.

## 6. Kesimpulan

Pada artikel ini, kita memulai dari definisi dasar teori graf, dan telah membahas latar belakang matematis algoritma Dijkstra dan A*, mekanisme spesifiknya, dan contoh implementasinya menggunakan Python.

- **Algoritma Dijkstra** mengevaluasi semua node secara merata dan menjamin ditemukannya jalur terpendek yang pasti.
- **Algoritma A*** mengimplementasikan pencarian yang efisien menuju tujuan dengan memperkenalkan fungsi heuristik $ h(n) $.

Pengetahuan ini tidak hanya terbatas pada pemahaman algoritma semata, tetapi akan menjadi alat berpikir yang kuat untuk memodelkan masalah dunia nyata yang kompleks ke dalam "graf" matematis dan menghasilkan solusi optimal. Pastikan untuk mencoba menjalankan kode sebenarnya dan alami sendiri betapa luar biasanya metode-metode ini.

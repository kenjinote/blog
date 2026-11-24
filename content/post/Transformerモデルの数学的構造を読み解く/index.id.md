---
title: "Memahami Matematika Transformer melalui Rumus dan Dimensi"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Cakupan dan catatan

Ditinjau pada 24 November 2026 untuk rumus, dimensi, dan klaim. Transformer asli adalah encoder–decoder; model modern juga dapat hanya encoder atau decoder. Pemrosesan token paralel tidak menjamin informasi utuh untuk panjang apa pun atau konteks tanpa batas. Transformer juga memakai embedding, FFN, residual, dan normalisasi, bukan Attention saja.

## 2. Embedding dan posisi

Misalkan ukuran kosakata $V$, lebar tersembunyi $d_{model}$, dan matriks embedding $W_E\in\mathbb{R}^{V\times d_{model}}$. Dengan one-hot berbentuk baris, $e_i=\operatorname{one\_hot}(w_i)W_E$ berdimensi $(1\times V)(V\times d_{model})$. Makalah asli memakai posisi sinusoidal tetap; rumusnya di bawah. Pergeseran tetap dapat ditulis sebagai transformasi linear pasangan sinus/kosinus, tetapi ini tidak berarti Attention otomatis mengenali jarak atau menjamin ekstrapolasi ke posisi lebih panjang.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Dimensi dan perhitungan self-attention

Untuk $X\in\mathbb{R}^{N\times d_{model}}$, ambil $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ dan $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Maka $Q,K$ berdimensi $N\times d_k$, $V$ berdimensi $N\times d_v$, dan hasil dot product berupa matriks $N\times N$. Dengan asumsi ilustratif komponen normal standar independen, variansnya $d_k$, sehingga dibagi $\sqrt{d_k}$. Softmax membuat jumlah tiap baris satu; bobot itu bukan probabilitas terkalibrasi atau ukuran kepentingan universal.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN, dan normalisasi

Multi-Head Attention menghitung beberapa proyeksi secara paralel, menggabungkan hasilnya, lalu menerapkan proyeksi keluaran. FFN per posisi menerapkan lapisan dense yang sama secara terpisah pada tiap posisi. Makalah asli memakai Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; Pre-LayerNorm juga umum. LayerNorm menghitung statistik pada fitur tiap token.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Causal mask dan keluarga model

Decoder asli menyamarkan posisi masa depan. Jika baris $i$ adalah query dan kolom $j$ key, izinkan masa lalu/kini ($j\le i$) dan samarkan masa depan ($j>i$). Model encoder-only biasanya tidak memakai causal mask; decoder-only tidak memiliki cross-attention encoder-decoder.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Kompleksitas dan optimasi

Biaya full attention naif sekitar $O(N^2d_{model})$ di semua head bila $d_k,d_v$ adalah dimensi per-head; menyimpan matriks skor memerlukan memori $O(N^2)$. FlashAttention mempertahankan operasi yang sama hingga pembulatan floating-point sambil mengurangi lalu lintas memori dan penyimpanan antara, tetapi tidak menghapus komputasi kuadratik. Sparse/Linear Attention memakai pendekatan atau struktur berbeda.

## 7. Implementasi referensi PyTorch

```python
import math
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(q, k, v, allowed=None):
    """q/k: [..., L or S, d_k]; v: [..., S, d_v].

    allowed is bool and broadcastable to [..., L, S]; True means allowed.
    Every query row must allow at least one key.
    """
    d_k = q.size(-1)
    scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(d_k)
    if allowed is not None:
        scores = scores.masked_fill(~allowed, float("-inf"))
    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, v), weights

# For square causal self-attention, allowed = torch.ones(L, L, dtype=torch.bool, device=q.device).tril().
# In production, consider torch.nn.functional.scaled_dot_product_attention.
# Its boolean attn_mask also uses True for positions that participate.
```

### References

- [Makalah asli (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Makalah asli di arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

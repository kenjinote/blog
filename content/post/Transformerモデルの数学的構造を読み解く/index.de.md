---
title: "Transformer-Mathematik anhand von Formeln und Dimensionen verstehen"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Umfang und Hinweise

Überarbeitet am 24. November 2026: Gleichungen, Dimensionen und Aussagen. Der ursprüngliche Transformer ist ein Encoder–Decoder; moderne Modelle können auch nur Encoder oder Decoder besitzen. Parallele Tokenverarbeitung garantiert weder verlustfreie Information bei beliebiger Länge noch unbegrenzten Kontext. Transformer nutzen außerdem Embeddings, FFNs, Residualpfade und Normalisierung, nicht nur Attention.

## 2. Embeddings und Positionen

Seien $V$ die Vokabulargröße, $d_{model}$ die Breite und $W_E\in\mathbb{R}^{V\times d_{model}}$ die Embedding-Matrix. Bei einem zeilenförmigen One-Hot-Vektor hat $e_i=\operatorname{one\_hot}(w_i)W_E$ die Form $(1\times V)(V\times d_{model})$. Das Original verwendet feste sinusförmige Positionen; die Formeln folgen. Ein fester Versatz lässt sich linear aus Sinus-/Kosinus-Paaren bilden. Das garantiert weder automatische Abstandserkennung durch Attention noch Extrapolation zu längeren Positionen.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Dimensionen und Berechnung von Self-Attention

Für $X\in\mathbb{R}^{N\times d_{model}}$ seien $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ und $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Dann sind $Q,K$ $N\times d_k$, $V$ ist $N\times d_v$; Skalarprodukte ergeben eine $N\times N$-Matrix. Unter der veranschaulichenden Annahme unabhängiger standardnormaler Komponenten ist die Varianz $d_k$, daher die Division durch $\sqrt{d_k}$. Softmax normiert jede Zeile auf eins; das sind keine kalibrierten Wahrscheinlichkeiten oder allgemeingültigen Wichtigkeitswerte.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-Head, FFN und Normalisierung

Multi-Head Attention berechnet mehrere Projektionen parallel, verbindet die Ausgaben und nutzt eine Ausgangsprojektion. Eine positionsweise FFN wendet dieselben dichten Schichten unabhängig je Position an. Das Original nutzt Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; Pre-LayerNorm ist ebenfalls verbreitet. LayerNorm berechnet Statistiken über die Merkmale jedes Tokens.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Kausale Masken und Modellfamilien

Der ursprüngliche Decoder maskiert zukünftige Positionen. Ist Zeile $i$ die Query und Spalte $j$ der Key, sind Vergangenheit/Gegenwart ($j\le i$) erlaubt und Zukunft ($j>i$) gesperrt. Encoder-only-Modelle verwenden meist keine Kausalmaske; Decoder-only-Modelle haben keine Encoder-Decoder-Cross-Attention.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Komplexität und Optimierung

Naive vollständige Attention kostet über alle Köpfe etwa $O(N^2d_{model})$, wenn $d_k,d_v$ je Kopf gelten; eine materialisierte Score-Matrix benötigt $O(N^2)$ Speicher. FlashAttention erhält dieselbe Attention bis auf Gleitkomma-Rundung und senkt Speicherverkehr sowie Zwischenspeicherung, beseitigt aber nicht den quadratischen Rechenaufwand. Sparse/Linear Attention verwenden andere Näherungen oder Strukturen.

## 7. PyTorch-Referenzimplementierung

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

- [Originalarbeit (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Originalarbeit auf arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

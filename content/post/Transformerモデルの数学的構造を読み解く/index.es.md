---
title: "Comprender las matemáticas de Transformer mediante fórmulas y dimensiones"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Alcance y cautelas

Revisado el 24 de noviembre de 2026: fórmulas, dimensiones y afirmaciones. El Transformer original es encoder–decoder; los modelos actuales también pueden ser solo encoder o solo decoder. Procesar tokens en paralelo no garantiza conservar toda la información con longitudes arbitrarias ni un contexto ilimitado. También hay embeddings, FFN, conexiones residuales y normalización, no solo Attention.

## 2. Embeddings y posiciones

Sea $V$ el vocabulario, $d_{model}$ el ancho y $W_E\in\mathbb{R}^{V\times d_{model}}$ la matriz de embeddings. Con one-hot en fila, $e_i=\operatorname{one\_hot}(w_i)W_E$ tiene forma $(1\times V)(V\times d_{model})$. El artículo original usa posiciones sinusoidales fijas; sus fórmulas aparecen abajo. Un desplazamiento fijo se expresa mediante una transformación lineal de pares seno/coseno, pero eso no implica que Attention detecte automáticamente distancias ni garantiza extrapolar a posiciones más largas.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Dimensiones y cálculo de self-attention

Para $X\in\mathbb{R}^{N\times d_{model}}$, sean $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ y $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Entonces $Q,K$ miden $N\times d_k$ y $V$, $N\times d_v$; los productos escalares forman una matriz $N\times N$. Bajo el supuesto ilustrativo de componentes normales estándar independientes, la varianza es $d_k$, de ahí la división por $\sqrt{d_k}$. Softmax normaliza cada fila a suma uno; esos pesos no son probabilidades calibradas ni medidas universales de importancia.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN y normalización

Multi-Head Attention calcula varias proyecciones en paralelo, concatena sus salidas y aplica una proyección final. La FFN por posición aplica capas densas iguales de forma independiente en cada posición. El artículo original usa Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; también se usa Pre-LayerNorm. LayerNorm calcula estadísticas sobre las características de cada token.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Máscaras causales y familias de modelos

El decoder original enmascara posiciones futuras. Si la fila $i$ es la consulta y la columna $j$ la clave, permite pasado y presente ($j\le i$) y bloquea futuro ($j>i$). Los modelos solo encoder normalmente no usan esta máscara causal; los solo decoder no tienen cross-attention encoder-decoder.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Complejidad y optimización

La atención completa ingenua cuesta aproximadamente $O(N^2d_{model})$ entre cabezas si $d_k,d_v$ son dimensiones por cabeza; guardar la matriz de puntuaciones ocupa $O(N^2)$. FlashAttention mantiene la misma operación salvo redondeo numérico y reduce transferencias y almacenamiento intermedio, pero no elimina el cálculo cuadrático. Sparse/Linear Attention usan otras aproximaciones o estructuras.

## 7. Implementación de referencia PyTorch

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

- [Artículo original (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Artículo original en arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

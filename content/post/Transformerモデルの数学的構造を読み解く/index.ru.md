---
title: "Математика Transformer через формулы и размерности"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Область и оговорки

Проверены формулы, размерности и утверждения (24 ноября 2026 года). Исходный Transformer — encoder–decoder, но современные модели бывают также только encoder или decoder. Параллельная обработка токенов не гарантирует сохранение всей информации при любой длине или бесконечный контекст. В Transformer есть также эмбеддинги, FFN, остаточные связи и нормализация, а не только Attention.

## 2. Эмбеддинги и позиции

Пусть размер словаря $V$, ширина $d_{model}$ и таблица эмбеддингов $W_E\in\mathbb{R}^{V\times d_{model}}$. Для one-hot строки $e_i=\operatorname{one\_hot}(w_i)W_E$ имеет размер $(1\times V)(V\times d_{model})$. В исходной статье используются фиксированные синусоидальные позиции; формулы ниже. Фиксированный сдвиг выражается линейным преобразованием пар синусов и косинусов, но это не гарантирует автоматическое распознавание расстояния или экстраполяцию на более длинные позиции.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Размерности и вычисления self-attention

Для $X\in\mathbb{R}^{N\times d_{model}}$ зададим $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ и $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Тогда $Q,K$ имеют размер $N\times d_k$, $V$ — $N\times d_v$, а скалярные произведения дают матрицу $N\times N$. При наглядном предположении о независимых стандартно-нормальных компонентах дисперсия равна $d_k$, поэтому делим на $\sqrt{d_k}$. Softmax нормирует строки до суммы 1; это не калиброванные вероятности и не универсальная важность.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN и нормализация

Multi-Head Attention параллельно вычисляет несколько проекций, объединяет результаты и применяет выходную проекцию. Позиционная FFN независимо применяет одинаковые плотные слои к каждому положению. В исходной статье используется Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; распространён и Pre-LayerNorm. LayerNorm вычисляет статистики по признакам каждого токена.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Причинные маски и семейства моделей

Исходный decoder маскирует будущие позиции. Если строка $i$ — запрос, а столбец $j$ — ключ, прошлое/текущая позиция ($j\le i$) разрешены, будущее ($j>i$) закрыто. Encoder-only модели обычно не применяют причинную маску; decoder-only модели не имеют cross-attention encoder-decoder.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Сложность и оптимизация

Наивный полный attention требует примерно $O(N^2d_{model})$ операций по всем головам, если $d_k,d_v$ заданы на голову; материализованная матрица оценок занимает $O(N^2)$ памяти. FlashAttention сохраняет ту же операцию с точностью до округления и уменьшает передачи и промежуточное хранение, но не устраняет квадратичное число вычислений. Sparse/Linear Attention используют иные приближения или структуры.

## 7. Пример реализации на PyTorch

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

- [Исходная статья (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Статья на arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

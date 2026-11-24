---
title: "Understand Transformer Mathematics Through Equations and Shapes"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Scope and caveats

Reviewed on November 24, 2026 for equations, dimensions, and claims. The original Transformer is encoder–decoder; modern models may be encoder-only or decoder-only. Parallel token processing does not guarantee lossless information at arbitrary lengths or unlimited context. Transformers also use embeddings, FFNs, residual paths, and normalization—not attention alone.

## 2. Embeddings and positions

Let vocabulary size be $V$, hidden width $d_{model}$, and embedding table $W_E\in\mathbb{R}^{V\times d_{model}}$. With a row one-hot vector, $e_i=\operatorname{one\_hot}(w_i)W_E$ has shape $(1\times V)(V\times d_{model})$. The original paper uses fixed sinusoidal positions. Their equations appear below. A fixed offset can be represented by a linear transform of sine/cosine pairs; this does not mean attention automatically reads distance or that extrapolation to longer positions is guaranteed.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Self-attention shapes and math

For $X\in\mathbb{R}^{N\times d_{model}}$, let $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ and $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Then $Q,K$ are $N\times d_k$ and $V$ is $N\times d_v$. Dot products form an $N\times N$ score matrix. Under the illustrative assumption of independent standard-normal components, their variance is $d_k$, motivating division by $\sqrt{d_k}$. Softmax makes each row sum to one; these weights are not calibrated probabilities or universal measures of importance.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN, and normalization

Multi-head attention computes several projections in parallel, concatenates their outputs, and applies an output projection. A position-wise FFN applies the same dense layers independently at each position. The original paper uses Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; other layouts such as Pre-LayerNorm are common. LayerNorm computes statistics over each token’s feature dimensions.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Causal masks and model families

The original decoder masks future positions. With row $i$ as query and column $j$ as key, allow past/current positions ($j\le i$) and mask future ones ($j>i$). Encoder-only models usually do not use this causal mask; decoder-only models have no encoder–decoder cross-attention.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Complexity and optimization

Naive full attention costs about $O(N^2d_{model})$ across heads when $d_k,d_v$ are per-head widths; materializing the score matrix uses $O(N^2)$ memory. FlashAttention preserves the same attention operation up to floating-point rounding while reducing memory traffic and intermediate storage; it does not remove quadratic arithmetic. Sparse and linear attention use different approximations or structures.

## 7. PyTorch reference implementation

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

- [Original paper (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Original paper on arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

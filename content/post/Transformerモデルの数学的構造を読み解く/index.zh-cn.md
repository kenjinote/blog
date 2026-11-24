---
title: "通过公式与维度理解 Transformer 数学结构"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. 范围与注意事项

本文于 2026 年 11 月 24 日复核了公式、维度和表述。原始 Transformer 是 Encoder–Decoder 架构；现代模型也可能只有 Encoder 或 Decoder。并行处理 token 不代表任意长序列都无损，也不代表上下文无限。Transformer 还包含嵌入、FFN、残差和归一化，并非只有 Attention。

## 2. 嵌入与位置信息

设词表大小为 $V$、隐藏维度为 $d_{model}$，嵌入矩阵 $W_E\in\mathbb{R}^{V\times d_{model}}$。若 one-hot 是行向量，则 $e_i=\operatorname{one\_hot}(w_i)W_E$，维度为 $(1\times V)(V\times d_{model})$。原论文使用固定的正弦位置编码，公式如下。固定偏移可由正弦/余弦对的线性变换表示，但这不表示 Attention 会自动识别距离，也不保证能外推到更长位置。

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. 自注意力的维度与计算

对于 $X\in\mathbb{R}^{N\times d_{model}}$，令 $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$，$W^V\in\mathbb{R}^{d_{model}\times d_v}$，则 $Q,K$ 为 $N\times d_k$，$V$ 为 $N\times d_v$。点积得到 $N\times N$ 分数矩阵。在独立标准正态分量这一说明性假设下，点积方差为 $d_k$，因此除以 $\sqrt{d_k}$。Softmax 使每行权重和为 1，但这些权重不是校准概率，也不代表普遍的重要性。

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. 多头、FFN 与归一化

多头注意力并行计算多个投影，拼接后再应用输出投影。逐位置 FFN 在每个位置独立使用相同的全连接层。原论文使用 Post-LayerNorm：$\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$；也常见 Pre-LayerNorm 等布局。LayerNorm 在每个 token 的特征维度上计算统计量。

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. 因果掩码与模型类型

原论文 Decoder 会屏蔽未来位置。若行 $i$ 是 query、列 $j$ 是 key，则允许过去和当前位置（$j\le i$），屏蔽未来位置（$j>i$）。Encoder-only 模型通常不使用因果掩码；Decoder-only 模型没有 Encoder–Decoder Cross-Attention。

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. 复杂度与优化

朴素全注意力在 $d_k,d_v$ 为每个头的维度时，所有头合计约为 $O(N^2d_{model})$；显式保存分数矩阵需 $O(N^2)$ 内存。FlashAttention 在浮点舍入误差范围内保持相同注意力运算，同时减少内存传输和中间矩阵保存，但不消除二次计算量。Sparse/Linear Attention 使用不同近似或结构。

## 7. PyTorch 参考实现

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

- [原始论文（NeurIPS）](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [原始论文 arXiv 版](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

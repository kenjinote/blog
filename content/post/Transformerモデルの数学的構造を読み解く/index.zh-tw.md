---
title: "透過公式與維度理解 Transformer 數學結構"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. 範圍與注意事項

本文於 2026 年 11 月 24 日複核公式、維度與說法。原始 Transformer 是 Encoder–Decoder 架構；現代模型也可能只有 Encoder 或 Decoder。Token 平行處理不保證任意長度皆無資訊損失，也不代表上下文無限。Transformer 還包含嵌入、FFN、殘差與正規化，不只有 Attention。

## 2. 嵌入與位置資訊

設詞彙數為 $V$、隱藏寬度為 $d_{model}$，嵌入矩陣 $W_E\in\mathbb{R}^{V\times d_{model}}$。若 one-hot 是列向量，則 $e_i=\operatorname{one\_hot}(w_i)W_E$，維度為 $(1\times V)(V\times d_{model})$。原論文使用固定正弦位置編碼，公式如下。固定位移可由正弦/餘弦組的線性轉換表示，但不代表 Attention 會自動辨識距離，也不保證能外推至更長位置。

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. 自注意力的維度與計算

對 $X\in\mathbb{R}^{N\times d_{model}}$，令 $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$，$W^V\in\mathbb{R}^{d_{model}\times d_v}$，則 $Q,K$ 為 $N\times d_k$，$V$ 為 $N\times d_v$，內積產生 $N\times N$ 分數矩陣。在獨立標準常態分量的說明性假設下，變異數為 $d_k$，因此除以 $\sqrt{d_k}$。Softmax 使每列權重總和為 1，但不是校準機率或通用重要性。

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. 多頭、FFN 與正規化

Multi-Head Attention 平行計算多組投影、串接輸出，再套用輸出投影。逐位置 FFN 對每個位置獨立套用相同全連接層。原論文採 Post-LayerNorm：$\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$；Pre-LayerNorm 等配置也常見。LayerNorm 沿每個 token 的特徵維度計算統計量。

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. 因果遮罩與模型類型

原始 Decoder 會遮蔽未來位置。若列 $i$ 是 query、欄 $j$ 是 key，則允許過去與目前位置（$j\le i$），遮蔽未來（$j>i$）。Encoder-only 模型通常不使用因果遮罩；Decoder-only 模型沒有 Encoder–Decoder Cross-Attention。

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. 複雜度與最佳化

若 $d_k,d_v$ 是每個 head 的維度，朴素完整 Attention 的所有 heads 合計約為 $O(N^2d_{model})$；明確儲存分數矩陣需 $O(N^2)$ 記憶體。FlashAttention 在浮點捨入範圍內維持相同運算，並減少記憶體傳輸與中間儲存，但不會消除二次計算量。Sparse/Linear Attention 使用不同近似或結構。

## 7. PyTorch 參考實作

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

- [原始論文（NeurIPS）](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [原始論文 arXiv 版](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

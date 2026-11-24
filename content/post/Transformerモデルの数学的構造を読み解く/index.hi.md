---
title: "सूत्रों और आयामों से Transformer गणित समझें"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. दायरा और सावधानियाँ

24 नवंबर 2026 को समीकरणों, आयामों और दावों की समीक्षा की गई। मूल Transformer encoder–decoder है; आधुनिक मॉडल केवल encoder या decoder भी हो सकते हैं। Tokens को समानांतर चलाना मनमानी लंबाई पर सूचना-सुरक्षा या असीमित context की गारंटी नहीं देता। Transformer में embedding, FFN, residual और normalization भी हैं, केवल Attention नहीं।

## 2. एम्बेडिंग और स्थान

मानें शब्दावली $V$, hidden चौड़ाई $d_{model}$, और embedding मैट्रिक्स $W_E\in\mathbb{R}^{V\times d_{model}}$ है। पंक्ति one-hot के साथ $e_i=\operatorname{one\_hot}(w_i)W_E$ का आकार $(1\times V)(V\times d_{model})$ है। मूल पेपर स्थिर sinusoidal position encoding उपयोग करता है; सूत्र नीचे हैं। निश्चित offset को sine/cosine जोड़ों के रैखिक रूपांतरण से लिखा जा सकता है, पर इससे Attention का दूरी स्वतः पहचानना या लंबे स्थानों पर अच्छा extrapolation सुनिश्चित नहीं होता।

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Self-attention के आयाम और गणना

$X\in\mathbb{R}^{N\times d_{model}}$ के लिए $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ और $W^V\in\mathbb{R}^{d_{model}\times d_v}$ लें। तब $Q,K$ का आकार $N\times d_k$ और $V$ का $N\times d_v$ है; dot products $N\times N$ score मैट्रिक्स बनाते हैं। स्वतंत्र standard-normal घटकों की उदाहरणात्मक धारणा में variance $d_k$ है, इसलिए $\sqrt{d_k}$ से भाग देते हैं। Softmax हर पंक्ति का योग 1 करता है; ये calibrated probabilities या सार्वभौमिक महत्त्व नहीं हैं।

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN और normalization

Multi-Head Attention कई projections समानांतर निकालता है, outputs जोड़ता है और output projection लगाता है। Position-wise FFN हर स्थान पर वही dense layers स्वतंत्र रूप से लगाता है। मूल पेपर Post-LayerNorm $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$ उपयोग करता है; Pre-LayerNorm भी आम है। LayerNorm प्रत्येक token के feature आयामों पर statistics निकालता है।

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Causal mask और मॉडल प्रकार

मूल decoder भविष्य के स्थानों को mask करता है। यदि पंक्ति $i$ query और स्तंभ $j$ key है, तो अतीत/वर्तमान ($j\le i$) अनुमति पाएँ और भविष्य ($j>i$) mask हों। Encoder-only मॉडल सामान्यतः causal mask नहीं लेते; decoder-only में encoder-decoder cross-attention नहीं होता।

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. जटिलता और अनुकूलन

प्रति-head $d_k,d_v$ होने पर naïve full attention की कुल लागत लगभग $O(N^2d_{model})$ और score matrix रखने की memory $O(N^2)$ है। FlashAttention rounding के अंतर को छोड़ उसी attention operation को रखते हुए memory traffic और intermediate storage घटाता है, पर quadratic compute नहीं हटाता। Sparse/Linear Attention अलग approximations या संरचनाएँ अपनाते हैं।

## 7. PyTorch संदर्भ कार्यान्वयन

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

- [मूल शोधपत्र (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [मूल शोधपत्र arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

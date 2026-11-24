---
title: "Transformerの数学的構造を数式と形状から理解する"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. 概要と注意点

2026年11月24日に数式、次元、説明を見直しました。原論文のTransformerはEncoder–Decoder構成ですが、現在のモデルにはEncoder-only、Decoder-onlyもあります。系列位置の並列計算は可能でも、系列長に無関係な情報保持や無制限の文脈を保証するものではありません。Attention以外に埋め込み、FFN、残差接続、正規化も使います。

## 2. 埋め込みと位置情報

語彙数を $V$、隠れ次元を $d_{model}$ とし、埋め込み行列を $W_E\in\mathbb{R}^{V\times d_{model}}$ とします。one-hotを行ベクトルとするなら $e_i=\operatorname{one\_hot}(w_i)W_E$（$1\times V$ と $V\times d_{model}$）です。原論文は正弦・余弦の固定位置エンコーディングを使いました。位置の式は下記の通りです。固定オフセットは正弦・余弦の組に線形変換として表せますが、それだけでAttentionが距離を自動認識したり、長い位置へ良く外挿できたりする保証はありません。

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Self-Attentionの次元と計算

入力 $X\in\mathbb{R}^{N\times d_{model}}$ に対し、$W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$、$W^V\in\mathbb{R}^{d_{model}\times d_v}$ とすれば、$Q,K$ は $N\times d_k$、$V$ は $N\times d_v$ です。各クエリとキーの内積は $N\times N$ のスコアになります。独立な標準正規成分という説明用仮定では内積の分散は $d_k$ なので、$\sqrt{d_k}$ で割ります。Softmaxは各行を合計1の重みにしますが、校正済みの確率や重要度を意味しません。

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-Head・FFN・正規化

Multi-Head Attentionは複数の射影を並列に計算して結合し、出力射影を適用します。Position-wise FFNは各位置へ独立に全結合層を適用します。原論文のPost-LayerNormは $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$ ですが、Pre-LayerNormなど別配置もあります。LayerNormは各トークンの特徴次元に沿って平均と分散を計算します。

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. 因果マスクとモデル構成

原論文のDecoderでは未来の位置を遮る因果マスクを使います。行 $i$ をクエリ、列 $j$ をキーとする規約なら、過去と現在（$j\le i$）を許可し、未来（$j>i$）を遮ります。Encoder-onlyモデルは通常この因果マスクを使わず、Decoder-onlyモデルにはEncoder–Decoder Cross-Attentionがありません。

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. 計算量と最適化

素朴な全Attentionの計算量は、$d_k,d_v$ が各ヘッドの次元なら全ヘッド合計で概ね $O(N^2d_{model})$、明示的なスコア行列のメモリは $O(N^2)$ です。FlashAttentionは同じ注意演算を数値丸めの範囲で保ちながらメモリ転送と中間行列の保持を減らしますが、二次の計算量そのものはなくしません。Sparse/Linear Attentionは異なる近似・構造を使う手法です。

## 7. PyTorch参照実装

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

### 参考資料

- [Vaswaniらの原論文（NeurIPS）](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [原論文のarXiv版](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

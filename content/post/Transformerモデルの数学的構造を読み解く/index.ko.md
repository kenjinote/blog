---
title: "수식과 텐서 크기로 이해하는 Transformer 수학"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. 범위와 주의사항

2026년 11월 24일에 수식, 차원, 주장을 검토했습니다. 원래 Transformer는 Encoder–Decoder 구조지만 현대 모델은 Encoder-only 또는 Decoder-only일 수도 있습니다. 토큰 병렬 처리가 임의 길이의 정보 보존이나 무제한 문맥을 보장하지는 않습니다. Transformer에는 Attention뿐 아니라 임베딩, FFN, 잔차 연결, 정규화도 있습니다.

## 2. 임베딩과 위치 정보

어휘 수를 $V$, hidden 폭을 $d_{model}$, 임베딩 행렬을 $W_E\in\mathbb{R}^{V\times d_{model}}$라 합시다. one-hot을 행벡터로 두면 $e_i=\operatorname{one\_hot}(w_i)W_E$이며 크기는 $(1\times V)(V\times d_{model})$입니다. 원 논문은 고정 사인 위치 인코딩을 사용합니다. 수식은 아래와 같습니다. 고정 오프셋은 사인/코사인 쌍의 선형 변환으로 표현할 수 있지만, Attention이 거리를 자동으로 알아채거나 긴 위치로 외삽할 수 있음을 보장하지 않습니다.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Self-Attention 차원과 계산

$X\in\mathbb{R}^{N\times d_{model}}$에서 $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$, $W^V\in\mathbb{R}^{d_{model}\times d_v}$로 두면 $Q,K$는 $N\times d_k$, $V$는 $N\times d_v$입니다. 내적은 $N\times N$ 점수 행렬을 만듭니다. 독립 표준정규 성분이라는 설명용 가정에서는 분산이 $d_k$이므로 $\sqrt{d_k}$로 나눕니다. Softmax는 각 행의 합을 1로 만들지만, 보정된 확률이나 보편적 중요도를 뜻하지 않습니다.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-Head·FFN·정규화

Multi-Head Attention은 여러 투영을 병렬 계산하고 출력을 연결한 뒤 출력 투영을 적용합니다. 위치별 FFN은 각 위치에 같은 완전연결층을 독립 적용합니다. 원 논문은 Post-LayerNorm $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$를 사용하지만 Pre-LayerNorm도 흔합니다. LayerNorm은 각 토큰의 특징 차원에서 통계를 계산합니다.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. 인과 마스크와 모델 유형

원래 Decoder는 미래 위치를 가립니다. 행 $i$가 query, 열 $j$가 key라면 과거와 현재($j\le i$)는 허용하고 미래($j>i$)는 차단합니다. Encoder-only 모델은 보통 인과 마스크를 쓰지 않고, Decoder-only 모델에는 Encoder–Decoder 교차 어텐션이 없습니다.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. 복잡도와 최적화

순진한 전체 attention은 $d_k,d_v$가 헤드별 차원일 때 모든 헤드를 합쳐 대략 $O(N^2d_{model})$이고, 점수 행렬 저장은 $O(N^2)$ 메모리를 씁니다. FlashAttention은 부동소수점 반올림을 제외하면 같은 연산을 유지하면서 메모리 이동과 중간 저장을 줄이지만 이차 계산량을 없애지 않습니다. Sparse/Linear Attention은 다른 근사나 구조를 사용합니다.

## 7. PyTorch 참조 구현

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

- [원 논문 (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [원 논문 arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

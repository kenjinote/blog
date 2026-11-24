---
title: "Entenda a matemática do Transformer por fórmulas e dimensões"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. Escopo e ressalvas

Revisado em 24 de novembro de 2026: equações, dimensões e afirmações. O Transformer original é encoder–decoder; modelos atuais também podem ser apenas encoder ou decoder. Processamento paralelo de tokens não garante informação sem perdas em qualquer comprimento nem contexto ilimitado. Há também embeddings, FFN, conexões residuais e normalização, não apenas Attention.

## 2. Embeddings e posições

Seja $V$ o vocabulário, $d_{model}$ a largura e $W_E\in\mathbb{R}^{V\times d_{model}}$ a matriz de embeddings. Com one-hot em linha, $e_i=\operatorname{one\_hot}(w_i)W_E$ tem forma $(1\times V)(V\times d_{model})$. O artigo original usa posições senoidais fixas, com fórmulas abaixo. Um deslocamento fixo pode ser representado por transformação linear de pares seno/cosseno, mas isso não significa que Attention detecte distância automaticamente nem garante extrapolação.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Dimensões e cálculo de self-attention

Para $X\in\mathbb{R}^{N\times d_{model}}$, sejam $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ e $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Assim, $Q,K$ têm $N\times d_k$, $V$ tem $N\times d_v$, e os produtos escalares formam uma matriz $N\times N$. Sob a hipótese ilustrativa de componentes normais padrão independentes, a variância é $d_k$, justificando dividir por $\sqrt{d_k}$. Softmax soma um por linha; isso não representa probabilidades calibradas nem importância universal.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN e normalização

Multi-Head Attention calcula projeções em paralelo, concatena as saídas e aplica uma projeção final. A FFN por posição aplica as mesmas camadas densas independentemente em cada posição. O artigo original usa Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$; Pre-LayerNorm também é comum. LayerNorm calcula estatísticas nas características de cada token.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Máscaras causais e famílias de modelos

O decoder original mascara posições futuras. Se a linha $i$ é a consulta e a coluna $j$ a chave, permite passado/presente ($j\le i$) e bloqueia futuro ($j>i$). Modelos apenas encoder normalmente não usam essa máscara causal; modelos apenas decoder não têm cross-attention encoder-decoder.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Complexidade e otimização

A atenção completa ingênua custa aproximadamente $O(N^2d_{model})$ entre cabeças quando $d_k,d_v$ são dimensões por cabeça; materializar os scores usa $O(N^2)$ de memória. FlashAttention mantém a mesma operação, salvo arredondamento, e reduz transferências e armazenamento intermediário; não elimina o cálculo quadrático. Sparse/Linear Attention usam outras aproximações ou estruturas.

## 7. Implementação de referência PyTorch

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

- [Artigo original (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Artigo original no arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

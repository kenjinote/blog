---
title: "Comprendre les mathématiques de Transformer par les équations et dimensions"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Apprentissage profond", "Attention", "Mathématiques"]
---

## 1. Périmètre et réserves

Révisé le 24 novembre 2026 : équations, dimensions et affirmations. Le Transformer d’origine est encoder–decoder ; des modèles actuels peuvent n’avoir qu’un encodeur ou un décodeur. Le calcul parallèle des tokens ne garantit ni conservation parfaite à longueur arbitraire ni contexte illimité. Il y a aussi embeddings, FFN, résidus et normalisation, pas seulement Attention.

## 2. Embeddings et positions

Soient $V$ la taille du vocabulaire, $d_{model}$ la largeur et $W_E\in\mathbb{R}^{V\times d_{model}}$ la table d’embeddings. Avec un one-hot en ligne, $e_i=\operatorname{one\_hot}(w_i)W_E$ a la forme $(1\times V)(V\times d_{model})$. L’article d’origine utilise des positions sinusoïdales fixes ; les formules suivent. Un décalage fixe s’exprime par transformation linéaire des paires sinus/cosinus, sans garantir que l’attention déduise la distance ou extrapole à de longues positions.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. Dimensions et calcul de self-attention

Pour $X\in\mathbb{R}^{N\times d_{model}}$, prenons $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ et $W^V\in\mathbb{R}^{d_{model}\times d_v}$. Alors $Q,K$ sont $N\times d_k$, $V$ est $N\times d_v$, et les produits scalaires forment une matrice $N\times N$. Sous l’hypothèse illustrative de composantes normales standard indépendantes, la variance vaut $d_k$, d’où la division par $\sqrt{d_k}$. Softmax donne une somme de un par ligne ; ce ne sont pas des probabilités calibrées ni une importance universelle.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. Multi-head, FFN et normalisation

Multi-Head Attention calcule plusieurs projections en parallèle, concatène les sorties puis applique une projection. La FFN par position applique les mêmes couches denses indépendamment à chaque position. L’article d’origine utilise Post-LayerNorm, $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$ ; Pre-LayerNorm existe aussi. LayerNorm calcule les statistiques sur les caractéristiques de chaque token.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. Masques causaux et familles de modèles

Le décodeur original masque les positions futures. Si la ligne $i$ est la requête et la colonne $j$ la clé, on autorise passé/présent ($j\le i$) et masque futur ($j>i$). Les modèles encodeur seul n’utilisent généralement pas ce masque causal ; les modèles décodeur seul n’ont pas de cross-attention encodeur-décodeur.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. Complexité et optimisation

L’attention complète naïve coûte environ $O(N^2d_{model})$ sur toutes les têtes si $d_k,d_v$ sont par tête ; matérialiser les scores prend $O(N^2)$ mémoire. FlashAttention garde la même opération à l’arrondi flottant près et réduit transferts et stockage intermédiaire, sans supprimer le calcul quadratique. Sparse/Linear Attention utilisent d’autres approximations ou structures.

## 7. Implémentation de référence PyTorch

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

- [Article d’origine (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [Article d’origine sur arXiv](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

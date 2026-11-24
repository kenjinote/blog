---
title: "فهم رياضيات Transformer من خلال المعادلات والأبعاد"
slug: "transformer-mathematical-structure"
lastmod: "2026-11-24T00:00:00+09:00"

date: "2026-09-11T22:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["ai", "machine-learning", "mathematics"]
tags: ["Transformer", "Deep Learning", "Attention", "Math"]
---

## 1. النطاق والتنبيهات

رُوجعت المعادلات والأبعاد والادعاءات في 24 نوفمبر 2026. بنية Transformer الأصلية هي Encoder–Decoder، لكن النماذج الحديثة قد تكون Encoder-only أو Decoder-only. معالجة الرموز بالتوازي لا تضمن حفظ المعلومات لأي طول أو سياق غير محدود. ويستخدم Transformer أيضًا التضمين وFFN والوصلات المتبقية والتطبيع، وليس Attention وحده.

## 2. التضمين والمواضع

ليكن حجم المفردات $V$ والعرض المخفي $d_{model}$ ومصفوفة التضمين $W_E\in\mathbb{R}^{V\times d_{model}}$. إذا كان one-hot متجه صف، فإن $e_i=\operatorname{one\_hot}(w_i)W_E$ بأبعاد $(1\times V)(V\times d_{model})$. استخدمت الورقة الأصلية ترميزًا جيبيًا ثابتًا للمواضع، ومعادلاته أدناه. يمكن تمثيل الإزاحة الثابتة بتحويل خطي لأزواج الجيب وجيب التمام، لكن هذا لا يعني أن Attention يكتشف المسافة تلقائيًا أو يضمن التعميم إلى مواضع أطول.

$$ e_i=\operatorname{one\_hot}(w_i)W_E,\quad W_E\in\mathbb{R}^{V\times d_{model}} $$
$$ PE_{(pos,2i)}=\sin\left(\frac{pos}{10000^{2i/d_{model}}}\right),\qquad PE_{(pos,2i+1)}=\cos\left(\frac{pos}{10000^{2i/d_{model}}}\right) $$

## 3. أبعاد وحساب الانتباه الذاتي

لـ $X\in\mathbb{R}^{N\times d_{model}}$، خذ $W^Q,W^K\in\mathbb{R}^{d_{model}\times d_k}$ و$W^V\in\mathbb{R}^{d_{model}\times d_v}$. عندها أبعاد $Q,K$ هي $N\times d_k$ و$V$ هي $N\times d_v$، وتنتج الضروب الداخلية مصفوفة درجات $N\times N$. في افتراض توضيحي لمكونات طبيعية معيارية مستقلة، التباين $d_k$، لذا نقسم على $\sqrt{d_k}$. تجعل Softmax مجموع كل صف واحدًا؛ وهذه ليست احتمالات معايرة أو مقياسًا عامًا للأهمية.

$$ X_0=E+PE,\quad Q=X_0W^Q,\quad K=X_0W^K,\quad V=X_0W^V $$
$$ \operatorname{Attention}(Q,K,V;M)=\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V $$
$$ \operatorname{Var}(q\cdot k)=d_k $$

## 4. الرؤوس المتعددة وFFN والتطبيع

تحسب Multi-Head Attention إسقاطات متعددة بالتوازي، ثم تجمع المخرجات وتطبق إسقاطًا نهائيًا. تطبق FFN الموضعية الطبقات الكثيفة نفسها بصورة مستقلة على كل موضع. استخدمت الورقة الأصلية Post-LayerNorm، $\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x))$، وتوجد أيضًا Pre-LayerNorm. يحسب LayerNorm الإحصاءات عبر خصائص كل رمز.

$$ \operatorname{head}_a=\operatorname{Attention}(X_0W_a^Q,X_0W_a^K,X_0W_a^V),\quad \operatorname{MHA}=\operatorname{Concat}(\operatorname{head}_1,\ldots,\operatorname{head}_h)W^O $$
$$ \operatorname{FFN}(x)=\operatorname{ReLU}(xW_1+b_1)W_2+b_2,\qquad \operatorname{PostNorm}(x)=\operatorname{LayerNorm}(x+\operatorname{Sublayer}(x)) $$
$$ \operatorname{LN}(x)=\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}\odot\gamma+\beta $$

## 5. الأقنعة السببية وأنواع النماذج

يحجب Decoder الأصلي المواضع المستقبلية. إذا كان الصف $i$ هو Query والعمود $j$ هو Key، نسمح بالماضي والحاضر ($j\le i$) ونحجب المستقبل ($j>i$). لا تستخدم نماذج Encoder-only عادةً هذا القناع السببي؛ ولا تحتوي نماذج Decoder-only على Cross-Attention بين المشفر وفاك التشفير.

$$ M_{ij}=\begin{cases}0 & j\le i\\-\infty & j>i\end{cases} $$

## 6. التعقيد والتحسين

تكلفة Attention الكامل الساذج تقارب $O(N^2d_{model})$ عبر الرؤوس عندما تكون $d_k,d_v$ أبعاد الرأس؛ وتخزين مصفوفة الدرجات يتطلب $O(N^2)$ ذاكرة. تحافظ FlashAttention على العملية نفسها مع فروق التقريب العشري وتقلل نقل الذاكرة والتخزين الوسيط، لكنها لا تلغي الحساب التربيعي. تستخدم Sparse/Linear Attention تقريبات أو بنيات مختلفة.

## 7. تنفيذ مرجعي بـ PyTorch

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

- [الورقة الأصلية (NeurIPS)](https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)
- [نسخة arXiv من الورقة](https://arxiv.org/abs/1706.03762)
- [PyTorch scaled_dot_product_attention](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [PyTorch LayerNorm](https://docs.pytorch.org/docs/stable/generated/torch.nn.LayerNorm.html)

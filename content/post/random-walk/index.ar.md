---
title: "المشي العشوائي: فهم رياضيات الانتشار والحركة البراونية"
description: "شرح مفصل للخلفية الرياضية للمشي العشوائي، من الأساسيات إلى ظواهر الانتشار والحركة البراونية. دليل شامل يتضمن نظرية بوليا والتطبيقات المالية."
slug: "random-walk"
date: "2026-09-20T15:30:00+09:00"
image: "eyecatch.jpg"
categories: ["الرياضيات"]
tags: ["مشية عشوائية", "احتمالات", "معادلة الانتشار", "حركة براونية", "بايثون"]
---

# مقدمة

[المشي العشوائي](https://kenji.blog/ar/p/random-walk/) هو مفهوم رياضي يتم فيه تحديد الموضع التالي بشكل عشوائي (احتمالي). غالبًا ما يُطلق عليه "مشية السكران".

## الصيغة (1D)

لنفترض أن الجسيم يقع عند نقطة الأصل $x = 0$. يتحرك إلى اليمين $+1$ أو إلى اليسار $-1$ باحتمال متساوٍ:

$$
X_i = \begin{cases} 
+1 & (\text{احتمال } 1/2) \\ 
-1 & (\text{احتمال } 1/2) 
\end{cases}
$$

الموضع بعد $n$ خطوات هو:

$$
S_n = X_1 + X_2 + \dots + X_n = \sum_{i=1}^n X_i
$$

```mermaid
flowchart LR
    A["الموضع 0"] -->|"+1 (احتمال 1/2)"| B["الموضع +1"]
    A -->|"-1 (احتمال 1/2)"| C["الموضع -1"]
    B -->|"+1"| D["الموضع +2"]
    B -->|"-1"| A
    C -->|"+1"| A
    C -->|"-1"| E["الموضع -2"]
    %% مخطط التدفق الأساسي للحركة أحادية البعد
```

## القيمة المتوقعة والتباين

القيمة المتوقعة هي $0$، لكن التباين هو $n$.

## معادلة الانتشار

عند الحد المستمر، يصبح [المشي العشوائي](https://kenji.blog/ar/p/random-walk/) **معادلة الانتشار**:

$$
\frac{\partial P}{\partial t} = D \frac{\partial^2 P}{\partial x^2}
$$

```mermaid
stateDiagram-v2
    direction LR
    state "نظرة مجهرية" as Micro {
        [*] --> المشي_العشوائي
        المشي_العشوائي --> خطوات_متقطعة
    }
    state "نظرة عيانية" as Macro {
        [*] --> معادلة_الانتشار
        معادلة_الانتشار --> انتشار_مستمر
    }
    Micro --> Macro : "الحد المستمر (Δx, Δt → 0)"
    %% الانتقال من المتقطع إلى المستمر
```

## الحركة البراونية ونظرية بوليا

تنص **نظرية بوليا** على أنه بالنسبة للأبعاد 1D و 2D، فإن احتمال العودة إلى نقطة الأصل هو 100%، ولكن بالنسبة للأبعاد 3D أو أعلى، فهو أقل من 1.

```mermaid
flowchart TD
    Start["البدء من (0,0)"] --> Dim12{"1D أو 2D؟"}
    Dim12 -- "نعم" --> Ret12["العودة باحتمال 1 (متكرر)"]
    Dim12 -- "لا (3D أو أعلى)" --> Ret3["احتمال < 1 (عابر)"]
    %% تفرع نظرية بوليا
```

## المحاكاة باستخدام بايثون

```python
import numpy as np
import matplotlib.pyplot as plt

def simulate_random_walk_2d(steps):
    """
    محاكاة المشي العشوائي ثنائي الأبعاد
    """
    directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])
    random_steps = np.random.randint(0, 4, size=steps)
    movements = directions[random_steps]
    path = np.vstack([[0, 0], np.cumsum(movements, axis=0)])
    return path

steps = 50000
path = simulate_random_walk_2d(steps)

plt.figure(figsize=(10, 10))
plt.plot(path[:, 0], path[:, 1], alpha=0.6, color='royalblue', linewidth=0.5)
plt.scatter(0, 0, color='red', marker='x', s=150, label='البداية', zorder=5)
plt.scatter(path[-1, 0], path[-1, 1], color='darkorange', marker='o', s=100, label='النهاية', zorder=5)

plt.title(f"2D Random Walk ({steps} steps)", fontsize=16)
plt.xlabel("محور X", fontsize=12)
plt.ylabel("محور Y", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.axis('equal')
plt.show()
```

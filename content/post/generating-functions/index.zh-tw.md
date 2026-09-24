---
title: "母函數：將數列變成「函數」有什麼好處？"
description: "介紹如何將硬幣的支付方式或組合數作為方程式的係數來計算。講解母函數的魔力，以及它在費氏數列中的應用。"
slug: "generating-functions"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "數學"
tags:
  - "母函數"
  - "組合數學"
  - "費氏數列"
  - "演算法"
---

在數學的世界裡，存在著一些像「魔法橋樑」一樣的概念，能夠將看似毫不相干的領域連接起來。其中之一就是 **[母函數](https://kenji.blog/zh-tw/p/generating-functions/)** (Generating Function)。透過將離散的「數列」轉化為連續的「函數」，可以將複雜的組合問題轉化為代數計算。

本文將從[母函數](https://kenji.blog/zh-tw/p/generating-functions/)的基本思想出發，詳細講解其驚人的威力——從計算硬幣支付方式的組合，到推導費氏數列的通項公式。此外，我們還將提及它在演算法和競技程式設計中的形式冪級數 (FPS) 應用。

## 1. 什麼是[母函數](https://kenji.blog/zh-tw/p/generating-functions/)？

給定一個數列 $a_0, a_1, a_2, \dots$，我們考慮一個函數 $A(x)$，它的每一項係數正好對應數列中各個項作為 $x$ 的冪的係數。

$$
A(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \dots = \sum_{n=0}^{\infty} a_n x^n
$$

這個函數 $A(x)$ 就被稱為數列 $\{a_n\}$ 的 **普通[母函數](https://kenji.blog/zh-tw/p/generating-functions/)** (Ordinary Generating Function)。

為什麼要進行這樣的轉換呢？這是因為 **可以將對數列的操作替換為對函數的代數操作**。數列的平移、求和或卷積等操作，都被轉換為函數之間的加法、乘法、微分和積分等我們熟悉的操作。

```mermaid
graph LR
    A["數列 (離散)"] -->|"轉換為母函數"| B["函數 (連續)"]
    B -->|"代數操作 (微分、乘積)"| C["新函數"]
    C -->|"提取係數"| D["新數列"]
    A -.->|"複雜操作"| D
```

## 2. 硬幣支付方式與[母函數](https://kenji.blog/zh-tw/p/generating-functions/)

要直觀地理解[母函數](https://kenji.blog/zh-tw/p/generating-functions/)的威力，讓我們考慮一個「硬幣支付方式」的問題。

**問題：**
使用1日圓、2日圓和5日圓硬幣，求恰好支付 $n$ 日圓的組合數 $a_n$。

我們使用[母函數](https://kenji.blog/zh-tw/p/generating-functions/)來解這個問題。
對於每種硬幣，我們根據使用的數量構建一個多項式。

*   1日圓硬幣的選擇: $1 + x + x^2 + x^3 + \dots$ (0枚、1枚、2枚...)
*   2日圓硬幣的選擇: $1 + x^2 + x^4 + x^6 + \dots$
*   5日圓硬幣的選擇: $1 + x^5 + x^{10} + x^{15} + \dots$

我們將這些多項式相乘，得到函數 $f(x)$。

$$
f(x) = (1 + x + x^2 + \dots)(1 + x^2 + x^4 + \dots)(1 + x^5 + x^{10} + \dots)
$$

展開這個式子時，$x^n$ 的係數恰好就是支付 $n$ 日圓的組合數 $a_n$。利用無窮級數求和公式 $1 + r + r^2 + \dots = \frac{1}{1-r}$，$f(x)$ 可以簡潔地表示為如下的有理函數：

$$
f(x) = \frac{1}{1-x} \cdot \frac{1}{1-x^2} \cdot \frac{1}{1-x^5}
$$

也就是說，不需要使用複雜的遞迴公式或迴圈計算，只需計算這個函數的泰勒展開係數，就能得到任意 $n$ 對應的組合數。在程式設計領域，這種思想也是動態規劃 ([DP](https://kenji.blog/zh-tw/p/dynamic-programming-dp-introduction-knapsack-fibonacci/)) 的重要基礎。

### 卷積與多項式乘積

為什麼函數的乘積對應於組合的計數呢？讓我們看看兩個數列 $a_n$ 和 $b_n$ 的[母函數](https://kenji.blog/zh-tw/p/generating-functions/) $A(x), B(x)$ 相乘會發生什麼。

$$
A(x)B(x) = (a_0 + a_1 x + a_2 x^2 + \dots)(b_0 + b_1 x + b_2 x^2 + \dots)
$$

展開後 $x^n$ 的係數為 $\sum_{k=0}^{n} a_k b_{n-k}$。這被稱為 **卷積** (Convolution)。在硬幣的例子中，「用1日圓硬幣湊出 $k$ 日圓，用2日圓硬幣湊出 $n-k$ 日圓」的組合的疊加，正是透過這個函數乘積自動計算出來的。

## 3. 在費氏數列中的應用

接下來，作為更高級的應用，我們來求費氏數列的通項公式。費氏數列 $F_n$ 的定義如下：

*   $F_0 = 0$
*   $F_1 = 1$
*   $F_n = F_{n-1} + F_{n-2} \quad (n \ge 2)$

設這個數列的[母函數](https://kenji.blog/zh-tw/p/generating-functions/)為 $F(x) = \sum_{n=0}^{\infty} F_n x^n$。

$$
\begin{aligned}
F(x) &= F_0 + F_1 x + \sum_{n=2}^{\infty} F_n x^n \\
&= 0 + x + \sum_{n=2}^{\infty} (F_{n-1} + F_{n-2}) x^n \\
&= x + x \sum_{n=2}^{\infty} F_{n-1} x^{n-1} + x^2 \sum_{n=2}^{\infty} F_{n-2} x^{n-2} \\
&= x + x \sum_{m=1}^{\infty} F_m x^m + x^2 \sum_{k=0}^{\infty} F_k x^k
\end{aligned}
$$

這裡，因為 $F_0 = 0$，所以 $\sum_{m=1}^{\infty} F_m x^m = F(x)$。因此，

$$
F(x) = x + x F(x) + x^2 F(x)
$$

解關於 $F(x)$ 的方程，我們得到了費氏數列的[母函數](https://kenji.blog/zh-tw/p/generating-functions/)。

$$
F(x) = \frac{x}{1 - x - x^2}
$$

令人驚訝的是，無限延伸的費氏數列的資訊，被濃縮到了這唯一一個簡單的分數函數中。

### 部分分式分解與通項公式

為了解從中提取數列的通項公式，我們將分母進行因式分解並進行部分分式分解。
考慮方程 $1 - x - x^2 = 0$ 的解，令 $\alpha = \frac{1 + \sqrt{5}}{2}$ (黃金比例), $\beta = \frac{1 - \sqrt{5}}{2}$，分母可以因式分解為 $(1 - \alpha x)(1 - \beta x)$。

$$
F(x) = \frac{1}{\sqrt{5}} \left( \frac{1}{1 - \alpha x} - \frac{1}{1 - \beta x} \right)
$$

再次逆向應用等比級數公式，將每一項展開為冪級數。

$$
\frac{1}{1 - \alpha x} = \sum_{n=0}^{\infty} \alpha^n x^n, \quad \frac{1}{1 - \beta x} = \sum_{n=0}^{\infty} \beta^n x^n
$$

代入並比較 $x^n$ 的係數，就能推導出著名的比內公式 (Binet's formula)。

$$
F_n = \frac{1}{\sqrt{5}} \left( \left( \frac{1 + \sqrt{5}}{2} \right)^n - \left( \frac{1 - \sqrt{5}}{2} \right)^n \right)
$$

```mermaid
graph TD
    S["費氏遞迴式"] -->|"定義母函數 F("x")"| EQ["建立函數方程"]
    EQ -->|"代數求解"| GF["F(x) = x / (1 - x - x^2)"]
    GF -->|"部分分式分解"| PF["(A / (1 - αx)) + (B / (1 - βx))"]
    PF -->|"冪級數展開及比較係數"| AN["通項公式 (比內公式)"]
```

## 4. 指數型[母函數](https://kenji.blog/zh-tw/p/generating-functions/)與排列

在處理考慮順序的組合問題，即「排列」時，**指數型[母函數](https://kenji.blog/zh-tw/p/generating-functions/)** (Exponential Generating Function) 將大顯身手。

對於數列 $a_n$，其指數型[母函數](https://kenji.blog/zh-tw/p/generating-functions/) $E(x)$ 定義如下：

$$
E(x) = \sum_{n=0}^{\infty} \frac{a_n}{n!} x^n = a_0 + a_1 x + \frac{a_2}{2!} x^2 + \frac{a_3}{3!} x^3 + \dots
$$

透過除以 $n!$，考慮順序的計算（如微分操作）會變得非常整潔。例如，所有元素均為 $1$ 的數列 $1, 1, 1, \dots$ 的指數型[母函數](https://kenji.blog/zh-tw/p/generating-functions/)是 $e^x$。

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
$$

利用這個性質，可以將元素的排列數或滿足多個條件的排列數表示為指數函數的乘積。

## 5. 向形式冪級數 (FPS) 的發展

在現代計算機科學和競技程式設計中，[母函數](https://kenji.blog/zh-tw/p/generating-functions/)常常被作為 **形式冪級數** (Formal Power Series, FPS) 來實作。
在 FPS 中，我們不關心將具體的數值代入 $x$ 後是否收斂（解析性質），而是將重點放在將「係數序列」作為多項式進行代數操作上。

利用快速傅立葉轉換 (FFT) 或數論轉換 (NTT)，可以在 $\mathcal{O}(N \log N)$ 的時間複雜度內求出兩個 $N$ 次多項式的乘積（即長度為 $N$ 的數列的卷積）。這使得原本用動態規劃需要 $\mathcal{O}(N^2)$ 的計算得到了極大的加速。

## 6. 總結

[母函數](https://kenji.blog/zh-tw/p/generating-functions/)不僅僅是「存放數列的盒子」。它是一個「翻譯機」，能將數列的規律和性質轉化為函數的形式，從而可以應用微積分和代數計算等強大的數學工具。

*   **組合的計數** 被替換成了函數的乘積。
*   **求解遞迴式** 被替換成了求解方程和進行泰勒展開。

從演算法設計到純數學難題，這一思想在廣泛的領域中大放異彩。請務必將把數列視為「函數」的全新視角，加入到您的思維工具箱中。

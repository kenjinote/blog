---
title: "佩尔方程：具有无限解的丢番图方程的魅力与连分数"
description: "详细介绍了佩尔方程的基础知识，使用连分数的求解方法，以及如何生成无限多的解。"
slug: "pell-equation"
date: "2026-09-20T15:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "mathematics"
tags:
  - "佩尔方程"
  - "丢番图方程"
  - "连分数"
  - "数论"
---

# 引言

在数论领域中，**[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)**（Pell's equation）被认为是最优美且具有深厚理论背景的[丢番图](https://kenji.blog/zh-cn/p/diophantus/)方程之一。本文将从该方程的基本定义和性质出发，详细讲解使用连分数（Continued fractions）的优雅且高效的求解方法，以及其无限解的生成机制。为了所有热爱数学的读者，我们涵盖了从公式推导、算法可视化，到使用编程语言实现的各个方面。

## 1. 什么是[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)？

[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)是指具有以下形式的二元二次[丢番图](https://kenji.blog/zh-cn/p/diophantus/)方程：

$$ x^2 - ny^2 = 1 $$

在这里，$n$ 是一个非平方数的正整数（无平方因子或至少不是完全平方数）。我们的目标是找到满足该方程的未知整数 $x$ 和 $y$ 的组合。假设 $n$ 是一个完全平方数，即 $n = k^2$（$k$ 为整数）。那么该方程可以变形如下：

$$ x^2 - k^2y^2 = 1 $$
$$ (x - ky)(x + ky) = 1 $$

由于 $x$、$y$ 和 $k$ 都是整数，因此 $(x - ky)$ 和 $(x + ky)$ 也必须是整数。乘积为 1 的整数组合只有 $(1, 1)$ 或 $(-1, -1)$。解此方程组可得 $y = 0$，这意味着解仅限于非常简单的 $(x, y) = (\pm 1, 0)$。因此，在[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)中，要求 $n$ 不是完全平方数是寻找有意义解的必要前提。

## 2. 历史背景：佩尔、费马以及古印度数学家们

虽然这个方程冠有“佩尔”之名，但追溯历史事实，其背景有些离奇。实际上，在近代欧洲，首先研究该方程的一般解法并强烈断言解必然存在的是伟大的法国数学家**[皮埃尔·德·费马](https://kenji.blog/zh-cn/p/fermat/)**（[Pierre de Fermat](https://kenji.blog/zh-cn/p/fermat/)）。

后来，**[莱昂哈德·欧拉](https://kenji.blog/zh-cn/p/euler/)**（Leonhard Euler）错误地将英国数学家**约翰·佩尔**（John Pell）的名字与这个方程联系在一起，因此至今它仍被广泛称为“[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)”。佩尔本人在这个方程的求解方法中并没有发挥核心作用。

如果将时间进一步往前推移，在费马之前几百年，印度数学家**婆罗摩笈多**（Brahmagupta）和**婆什迦罗第二**（Bhāskara II）就使用了一种名为查克拉瓦拉法（Chakravala method）的精妙算法，计算出了这类方程的解。从古代到中世纪，再到近代的数学家们的探索历史，都铭刻在这个方程中。

## 3. 平凡解与非平凡解的区别

对于[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/) $x^2 - ny^2 = 1$，无论 $n$ 取何值，始终存在解 $(x, y) = (\pm 1, 0)$。代入方程得到 $1^2 - n \cdot 0^2 = 1$，显然成立。这被称为**平凡解**（trivial solution）。

然而，数学家真正感兴趣的是 $y \neq 0$ 的**非平凡解**（non-trivial solution）。令人惊叹的是，如果 $n$ 是一个非完全平方数的正整数，在数学上已经证明[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)具有**无限多个非平凡解**。而且，在这无限多个解中，$x$ 和 $y$ 均为正整数的最小解被称为**基本解**（fundamental solution），只要找到这个基本解，就可以通过代数操作轻松生成所有其他的解。

## 4. 连分数展开与[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的深层联系

有效寻找基本解的最强大且标准的工具是**连分数**（Continued fraction）。由于无理数 $\sqrt{n}$ 无法用有限的分数表示，它可以优美地表示为无限循环的简单连分数。

$$ \sqrt{n} = [a_0; \overline{a_1, a_2, \dots, a_k, 2a_0}] $$

在这里，$a_0$ 是 $\sqrt{n}$ 的整数部分（即 $\lfloor \sqrt{n} \rfloor$），上方带有横线的部分代表连分数的循环部分。设这个循环的长度为 $m$。

不进行无限展开，而是在中间某一项截断所得到的有理数 $\frac{p_i}{q_i}$ 称为**渐近分数**（convergent）。渐近分数提供了无理数 $\sqrt{n}$ 的最佳有理数近似。令人惊讶的是，[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的基本解 $(x_1, y_1)$ 可以直接从 $\sqrt{n}$ 的连分数展开中某个特定渐近分数的分子 $p$ 和分母 $q$ 获得。具体来说，它由循环长度 $m$ 决定如下：

- 如果循环长度 $m$ 为偶数：基本解为 $(p_{m-1}, q_{m-1})$。
- 如果循环长度 $m$ 为奇数：基本解为 $(p_{2m-1}, q_{2m-1})$。

## 5. 基本解的求解方法：算法的详细解析

渐近分数 $\frac{p_i}{q_i}$ 可以使用以下递推公式在计算机上进行极快的计算。

$$ p_i = a_i p_{i-1} + p_{i-2} $$
$$ q_i = a_i q_{i-1} + q_{i-2} $$

为了让算法顺利启动，初始条件设置如下：
- $p_{-1} = 1, \quad p_{-2} = 0$
- $q_{-1} = 0, \quad q_{-2} = 1$

连分数的每一项 $a_i$ 也可以仅使用整数四则运算逐步求出。这使得计算过程能够完全排除浮点运算误差，实现精确的整数运算。

为了直观展示寻找解的过程，我们准备了以下的状态转移图。

```mermaid
flowchart TD
    Start["开始: 输入整数 n"] --> CheckSquare["判断 n 是否为完全平方数"]
    CheckSquare --|"Yes"| Trivial["仅存在平凡解 (结束)"] --> End["结束"]
    CheckSquare --|"No"| InitContFrac["初始化连分数递推公式"]
    InitContFrac --> CalcNext["计算下一个连分数项 a_i 和渐近分数 (p_i, q_i)"]
    CalcNext --> CheckEq["条件: 评估 p_i^2 - n * q_i^2 == 1"]
    CheckEq --|"False"| CalcNext
    CheckEq --|"True"| Found["找到基本解 (x_1, y_1) = (p_i, q_i)"] --> End
```

## 6. 具体例子：n = 7 时的连分数展开与基本解的推导

不仅仅是抽象的理论，让我们来具体追踪一下 $n = 7$ 时的计算过程。此时的[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)为 $x^2 - 7y^2 = 1$。

首先，$\sqrt{7}$ 的整数部分是 $a_0 = 2$。通过重复取剩余小数部分的倒数并提取整数部分的操作，可以求出 $\sqrt{7}$ 的连分数展开如下：

$$ \sqrt{7} = [2; \overline{1, 1, 1, 4}] $$

循环长度为 $m = 4$，是一个偶数。因此，基本解应该从渐近分数 $\frac{p_3}{q_3}$ 中获得。让我们使用递推公式依次计算渐近分数。

- $i=0$: 当 $a_0=2$ 时， $\frac{p_0}{q_0} = \frac{2}{1}$
- $i=1$: 当 $a_1=1$ 时， $p_1 = 1 \times 2 + 1 = 3$， $q_1 = 1 \times 1 + 0 = 1$。因此， $\frac{p_1}{q_1} = \frac{3}{1}$
- $i=2$: 当 $a_2=1$ 时， $p_2 = 1 \times 3 + 2 = 5$， $q_2 = 1 \times 1 + 1 = 2$。因此， $\frac{p_2}{q_2} = \frac{5}{2}$
- $i=3$: 当 $a_3=1$ 时， $p_3 = 1 \times 5 + 3 = 8$， $q_3 = 1 \times 2 + 1 = 3$。因此， $\frac{p_3}{q_3} = \frac{8}{3}$

让我们将求得的 $(p_3, q_3) = (8, 3)$ 代入方程进行验算。
$8^2 - 7 \times 3^2 = 64 - 7 \times 9 = 64 - 63 = 1$。
它完美地满足了条件，因此这就是 $n = 7$ 时的基本解 $(x_1, y_1) = (8, 3)$。

## 7. 生成无限解：使用矩阵与递推公式的方法

一旦找到哪怕一个基本解 $(x_1, y_1)$，就可以通过以下代数关系式无限生成所有其他的正整数解 $(x_k, y_k)$。

$$ x_k + y_k \sqrt{n} = (x_1 + y_1 \sqrt{n})^k \quad \text{for} \quad k = 1, 2, 3, \dots $$

通过展开该式并比较有理数部分和无理数部分（$\sqrt{n}$ 的系数），我们可以获得一个递推公式，用于从前一个解 $(x_k, y_k)$ 计算出下一个解 $(x_{k+1}, y_{k+1})$。如果用矩阵的形式来表达，它的形式非常简洁。

$$
\begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix} \begin{pmatrix} x_k \\ y_k \end{pmatrix}
$$

任意第 $k$ 个解也可以使用矩阵的幂运算直接计算如下：

$$
\begin{pmatrix} x_k \\ y_k \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix}^{k-1} \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}
$$

这个性质强烈暗示了[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的解不仅是简单的数字罗列，而且具有代数结构（群结构）。

## 8. 婆罗摩笈多恒等式与查克拉瓦拉法

在古印度数学中，在求解[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)时发挥核心作用的是**婆罗摩笈多恒等式**（Brahmagupta's identity）。这个恒等式的形式如下：

$$ (x_1^2 - ny_1^2)(x_2^2 - ny_2^2) = (x_1 x_2 + n y_1 y_2)^2 - n(x_1 y_2 + x_2 y_1)^2 $$

这个恒等式的绝妙之处在于，通过组合 $x^2 - ny^2 = k_1$ 的解 $(x_1, y_1)$ 和 $x^2 - ny^2 = k_2$ 的解 $(x_2, y_2)$，可以直接合成出一个满足 $X^2 - nY^2 = k_1 k_2$ 的新解 $(X, Y)$。

印度数学家巧妙地利用这个强大的恒等式，将具有较小误差的解不断组合，最终推导出**查克拉瓦拉法**，以达到误差为 $1$ 的解，也就是[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的解。这是人类数学史上的一项伟大成就，具有与连分数展开同等甚至更高的效率。

## 9. Python 实现示例与解说

在充分理解了理论背景之后，让我们实际编写一个程序。以下 Python 脚本针对指定的 $n$ 执行连分数递推，以搜索[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的基本解。由于计算过程不使用浮点数，完全依靠整数运算处理，因此不用担心精度丢失。

```python
import math

def is_square(n):
    """
    快速判断给定的数字 n 是否为完全平方数的函数。
    """
    s = math.isqrt(n)
    return s * s == n

def solve_pell(n):
    """
    使用连分数法计算佩尔方程 x^2 - n * y^2 = 1 的基本解。
    返回值: 基本解 (x, y) 的元组。如果是完全平方数则返回 None。
    """
    if is_square(n):
        return None  # 如果是完全平方数，则没有非平凡解

    # 连分数计算的初始化
    m = 0
    d = 1
    a0 = math.isqrt(n)
    a = a0
    
    # 渐近分数的初始值设定 (p_{-1}=1, p_{-2}=0, q_{-1}=0, q_{-2}=1)
    num1, num2 = 1, 0  # p_{i-1}, p_{i-2}
    den1, den2 = 0, 1  # q_{i-1}, q_{i-2}
    
    # 初始渐近分数 (p_0, q_0)
    num = a0
    den = 1
    
    # 循环直到满足条件 x^2 - n*y^2 == 1
    while num * num - n * den * den != 1:
        # 计算连分数的下一项 a_i
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        # 更新渐近分数 p_i, q_i
        num2 = num1
        num1 = num
        den2 = den1
        den1 = den
        
        num = a * num1 + num2
        den = a * den1 + den2

    return num, den

# 使用示例: 当 n = 7 时
n = 7
solution = solve_pell(n)
if solution:
    x, y = solution
    print(f"n={n} 的基本解: x={x}, y={y}")
    print(f"验算: {x}^2 - {n}*{y}^2 = {x**2 - n * y**2}")
```

运行这段代码，就会瞬间输出我们刚才手工计算出的基本解 $(x, y) = (8, 3)$。如果您尝试将 $n$ 的值设置得更大，例如 $61$，您可以确认解会变成一个巨大的数字（$x = 1766319049, y = 226153980$），这会让你真正体会到[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的深奥。

## 10. 通向代数数论的桥梁：与狄利克雷单位定理的联系

[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)不仅仅是一个简单的整数谜题。在近代数学中，它被定位为通向**实二次域**（real quadratic field）$\mathbb{Q}(\sqrt{n})$ 理论的重要入口。

[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)的解与实二次域的代数整数环中的**单位**（unit，逆元也是代数整数的元素）密切对应。基本解对应于生成该单位群的**基本单位**（fundamental unit），[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)存在无限解这一事实可以被视为更高级的定理——**狄利克雷单位定理**（Dirichlet's unit theorem）的一个特例。理解基本单位的性质，对于深入研究二次域的类数（class number）公式和理想类的结构至关重要。

## 11. 总结

在本文中，我们深入探讨了[丢番图](https://kenji.blog/zh-cn/p/diophantus/)方程中特别迷人的**[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)**，从其基础到应用进行了详细讲解。我们解释了对于任何非完全平方数 $n$，方程始终存在无限非平凡解的惊人事实，利用连分数展开的高效搜索算法，以及利用矩阵从已生成的基本解不断合成新解的动态过程。

几百年前费马和婆罗摩笈多思考的经典问题，如今能够被优雅地实现为现代计算机算法，并进一步连接到高级代数数论，这一事实令人不禁感受到超越时代的深邃的数学浪漫。希望您能以此为契机，利用 Python 代码探索不同 $n$ 值下的[佩尔方程](https://kenji.blog/zh-cn/p/pell-equation/)世界，并感受数字深奥的性质。

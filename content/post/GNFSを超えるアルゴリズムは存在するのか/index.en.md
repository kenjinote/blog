---
title: 'Is There an Algorithm Beyond GNFS (General Number Field Sieve)?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. Introduction: Integer Factorization and the Foundation of Modern Cryptography

RSA is one of several public-key cryptosystems, and its security relies in part on the difficulty of factoring large integers. Internet security as a whole does not depend on RSA alone. An efficient factoring method would threaten RSA-based uses, but would not automatically collapse all communications infrastructure.

For general-purpose factoring of large integers, GNFS is among the best-known classical methods. It has been used to factor numbers including RSA-768 and RSA-250; numbers with special structure may be better suited to methods such as SNFS. [RSA-250 report](https://eprint.iacr.org/2020/697)

However, cryptographers and mathematicians always harbor the following questions: "Is there a classical algorithm that surpasses GNFS?" "Where are the limits of classical computers?" And, "How will quantum computers break through this situation?"

In this article, we thoroughly dissect the profound mathematical structures behind GNFS and conduct a detailed technical analysis of polynomial selection, the sieving phase, and the linear algebra step using the block Wiedemann method. Furthermore, we consider extension methods of GNFS such as Coppersmith's improvements, and compare and explain the decisive differences between classical sub-exponential time algorithms and quantum polynomial time algorithms from a mathematical perspective.

---

## 2. Asymptotic Complexity and L-notation

When evaluating the computational complexity of integer factorization algorithms, instead of standard polynomial time notation (such as $O(n^k)$), **L-notation** is used to express the sub-exponential time relative to the number of digits of the input $n$. L-notation is defined as follows:

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Here, $n$ is the integer to be factored, and $\ln n$ is the natural logarithm, which satisfies $\ln n=\Theta(\log_2 n)$ and is therefore proportional to its bit length.
- When $\alpha = 0$: $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, representing **polynomial time** relative to the bit length.
- When $\alpha = 1$: $L_n[1, c] = \exp(c \ln n) = n^c$, representing **exponential time** relative to the bit length.
- When $0 < \alpha < 1$: It becomes **sub-exponential time**, positioned between polynomial time and exponential time.

The history of the evolution of past integer factorization algorithms has also been a history of gradually reducing this value of $\alpha$.
- **CFRAC**: heuristic expected running time $L_n[1/2,\sqrt{2}]$ ([reference](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS**: heuristic expected running time $L_n[1/2,1]$ ([FLINT documentation](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS**: the usual heuristic estimate is $L_n[1/3,(64/9)^{1/3}]$; this is neither a proven bound nor a direct practical runtime ([NFS analysis](https://arxiv.org/abs/2007.02730)).

---

## 3. The Full Picture and Mathematical Structure of the GNFS Algorithm

GNFS and QS use the congruence-of-squares idea: find $X,Y$ such that $X^2\equiv Y^2\pmod n$ but $X\not\equiv\pm Y\pmod n$; then $\gcd(X-Y,n)$ may yield a non-trivial factor.

However, the essence of GNFS is that it does not do this only in the rational number field $\mathbb{Q}$, but simultaneously searches for "smooth numbers" in both an extension field called an Algebraic Number Field $\mathbb{Q}(\alpha)$ and the rational number field, building congruence relations through homomorphisms.

The GNFS process is broadly divided into five phases.

```mermaid
graph TD
  A["Integer Factorization Problem (Input n)"] --> B["1. Polynomial Selection"]
  B --> C["2. Sieving Phase"]
  C --> D["3. Filtering Phase"]
  D --> E["4. Linear Algebra Phase"]
  E --> F["5. Square Root Phase"]
  F --> G["Output prime factors p, q"]```

### 3.1 Phase 1: Polynomial Selection

The success of GNFS heavily depends on the selection of appropriate polynomials. The goal is to find two irreducible polynomials $f_1(x)$ (rational side) and $f_2(x)$ (algebraic side) that share a common root $m$. That is, it satisfies:
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

Usually, a polynomial of degree 1 is chosen for the rational side, $f_1(x) = x - m$, and a monic polynomial of degree $d$ (typically 5 or 6) is chosen for the algebraic side, $f_2(x)$. The most classical approach is the **Base-$m$ method**.
Choose an integer $m = \lfloor n^{1/(d+1)} \rfloor$ close to the $1/(d+1)$ power of $n$, and expand $n$ in base $m$.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
This gives the polynomial $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Obviously, $f_2(m) = n \equiv 0 \pmod n$.

However, in modern implementations, **Kleinjung's algorithm** is used. This optimizes algebraic properties (Murphy's $E$ value and $\alpha$-value) while preventing the coefficients of the polynomial from becoming extremely large (optimizing skewness), exploring polynomials that are likely to generate smooth numbers during the sieving phase. A massive amount of computational resources is invested in this step alone.

### 3.2 Phase 2: Sieving Phase

Once the polynomials are determined, the algorithm enters the "Sieving" phase, which has the highest computational load. Here, we search for pairs $(a, b)$. This pair is coprime, and the following two values are simultaneously required to be "smooth".

1. **Norm on the rational side**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norm on the algebraic side**: $F_2(a, b) = b^d \cdot f_2(a/b)$

In the basic definition, a smooth number has no prime factors above the chosen sieve bound. Practical variants may allow additional large prime factors, so accepted relations depend on the implementation.
Currently, a method called **Lattice Sieving** is mainstream. By fixing a specific prime $q$ and sieving only the $(a, b)$ pairs on a sublattice where both the rational side and the algebraic side become multiples of $q$, extremely high efficiency is realized.

### 3.3 Phase 3: Filtering Phase

The number of smooth relations found in the sieving phase reaches hundreds of millions to billions. However, these also contain a lot of useless information.
The purpose of filtering is to construct a huge sparse matrix while reducing its dimensions as much as possible.

Specifically, operations such as the following are performed.
- **Singleton removal**: Remove relations that contain a prime factor that appears only once.
- **Clique removal / Merging**: Multiply relations that share prime factors appearing two or more times, eliminating variables and reducing to a denser but smaller-dimensional system of equations.

As a result, a matrix with billions of rows is compressed into a huge sparse matrix $\mathbf{A}$ with tens of millions of rows (elements are 0 and 1 over the field $\mathbb{F}_2$).

### 3.4 Phase 4: Linear Algebra Phase

Here, we find a non-trivial solution vector $\mathbf{x}$ for the equation $\mathbf{A} \mathbf{x} \equiv \mathbf{0} \pmod 2$. In other words, this is the problem of finding a non-zero vector in the right nullspace (kernel) of a huge sparse matrix.

For sparse matrices, iterative Krylov methods such as Block Lanczos and Block Wiedemann are used. The RSA-250 factorization report documents a Block Wiedemann computation; choice and performance depend on the matrix, implementation, and computing architecture. [RSA-250 report](https://eprint.iacr.org/2020/697)


### 3.5 Phase 5: Square Root Phase

From the solution of linear algebra, a product that becomes a "perfect square" is constructed on each of the rational and algebraic sides.
On the rational side, $\prod (a-bm)$ becomes the square $X^2$ of some integer $X$, and on the algebraic side, the corresponding product of ideals becomes a perfect square $\gamma^2$ over the algebraic field.
By computing this $\gamma$ over the algebraic field and applying the homomorphism $\phi: \alpha \mapsto m \pmod n$ to the ring of rational integers, the congruence:
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$
is obtained.

Computing the square root over the algebraic field requires deep knowledge of algebraic number theory, using complex algorithms such as **Montgomery's Method**. Finally, $\gcd(X-Y, n)$ is calculated, and if a non-trivial factor is obtained, the factorization is complete.

---

## 4. Are There Classical Algorithms Beyond GNFS?

To date, no classical algorithm has been discovered whose asymptotic complexity falls below $L_n[1/3, c]$ for the factorization of general integers. However, there are some attempts and derivative algorithms to break through theoretical and practical limits.

### 4.1 Multiple Number Field Sieve (MNFS)

As an approach extending GNFS, there is the **Multiple Number Field Sieve (MNFS)** by D. Coppersmith. While GNFS uses two polynomials (rational side and algebraic side), MNFS uses multiple different algebraic side polynomials simultaneously for a single rational side polynomial.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

By utilizing multiple algebraic fields, the probability of "becoming smooth in any of the algebraic fields" can be dramatically increased in each sieving step. Coppersmith succeeded in slightly reducing the constant $c$ in the complexity $L_n[1/3, c]$ through this approach.

However, in practice, the overhead of managing multiple fields is large, and it has not yet led to a decisive breakthrough for [RSA](https://kenji.blog/en/p/modern-cryptography-public-key-hash-signature/) moduli on a practical scale.

### 4.2 Is an $L_n[1/4]$ Class Algorithm Possible?

No general classical factoring algorithm with asymptotic complexity below the usual GNFS form is currently known. That does not prove a better algorithm is impossible. Smooth-number analyses describe known sieving approaches, not a lower bound for every algorithm; the question remains open.
---

## 5. Breakthrough by Quantum Computers: [Shor's Algorithm](https://kenji.blog/en/p/quantum-computing-shors-algorithm/)

While classical computers face the barrier of $L_n[1/3]$, **Shor's Algorithm**, published by Peter Shor in 1994, smashed this barrier by fundamentally changing the computation model itself.

### 5.1 The Impact of Quantum Polynomial Time

Shor's algorithm reduces the integer factorization problem to the "Order Finding Problem". For a certain integer $a$, it is the problem of finding the period (order) $r$ of the function $f(x) = a^x \pmod n$.
Shor uses quantum interference to extract information about the function’s period; this does not mean that all superposed states are read out in parallel.

In terms of computational complexity, the execution time of Shor's algorithm is **quantum polynomial time**, specifically as follows:
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Classical Algorithm (GNFS)"] -->|"Limit"| B["Sub-exponential Time L_n[1/3]"]
  C["Quantum Algorithm (Shor)"] -->|"Breakthrough"| D["Polynomial Time O((log n)^3)"]
  B --> E["Continued use of RSA (Increase key length)"]
  D --> F["RSA vulnerable if a sufficiently capable fault-tolerant quantum computer exists"]
```

### 5.2 Classical Sub-exponential Time vs. Quantum Polynomial Time

Shor factors integers in polynomial time in an idealized quantum model, but that alone does not give a practical cost estimate for a fault-tolerant machine. Gidney and Ekerå estimated about 20 million physical qubits and 8 hours in 2021; Gidney estimated fewer than one million noisy physical qubits and less than a week in 2025 for a different design and assumptions. These are conditional estimates, not demonstrations of breaking RSA-2048; no quantum computer has factored an integer of that size. A gate count or runtime cannot be inferred from $2048^3$ alone. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

Likewise, the asymptotic GNFS formula does not directly yield an operation count or runtime; that requires an explicit cost model and parameters.
## 6. Conclusion: Outlook for the Next Generation

GNFS is the best known general-purpose method, not a proven limit. No general classical algorithm with better asymptotic complexity is known, but there is no proof ruling one out. Practical improvements do not justify time guarantees or claims that RSA will remain secure for decades. Shor resource estimates are conditional and do not describe current hardware. The transition to post-quantum cryptography is guided by applicable standards and official recommendations.

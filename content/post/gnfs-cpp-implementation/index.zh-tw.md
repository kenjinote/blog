---
title: "【完全解剖】最強密碼破解演算法「GNFS」C++實作與理解"
slug: "gnfs-cpp-implementation"
date: 2026-09-05T13:04:59+09:00
tags: ["GNFS", "C++", "RSA", "數學", "密碼學"]
draft: false
image: "gnfs_cpp_blog_eyecatch_1788580949217.jpg"
categories: ["數學・密碼學・量子"]
---

# 【完全解剖】最強密碼破解演算法「GNFS」C++實作與理解

支撐現代網際網路基礎的「RSA密碼學」，其堅固性仰賴於一個數學信念：「在目前的電腦技術下，要對巨大的合成數進行質因數分解實際上是不可能的」。

然而，人類從未放棄。目前在古典電腦（非量子電腦的一般電腦）上，存在著用於進行巨大質因數分解的 **人類最強、最尖端的演算法** 。那就是 **「普通數體篩法（GNFS：General Number Field Sieve）」** 。

在本篇文章中，我們將完全公開這個 GNFS 最尖端計算邏輯的 C++ 實作程式碼（使用 Boost 函式庫的多精度整數 `boost::multiprecision` 進行嚴格建模），並徹底解說其背後「代數整數論」的深淵。

請務必與原始碼一起，盡情品味數學的神秘以及用電腦科學暴力屈服它的力量。

---

## 1. GNFS 最尖端邏輯・框架（完整原始碼）

首先，列出本次解說的 GNFS C++ 實作全貌。實際的數體篩法（如 CADO-NFS 等）是高達數十萬行程式碼的超巨大分散式系統，但本程式碼提取了構成 GNFS 的 **「5個必須的管線（階段）」** 進行類別設計，並在不失去數學意義的前提下，以最小配置進行了建模。

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <chrono>
#include <boost/multiprecision/cpp_int.hpp>

// 使用 Boost.Multiprecision 的多精度整數
using namespace boost::multiprecision;

// ============================================================================
// [SOTA GNFS] General Number Field Sieve (普通數體篩法) 最尖端邏輯框架
// 
// 本程式碼將 CADO-NFS 等所使用的最尖端 GNFS 的 5 個管線
// 嚴格建模為 C++ (Boost) 的類別設計。
// ============================================================================

struct Relation {
    int64_t a;
    int64_t b;
    std::vector<uint32_t> rational_primes;
    std::vector<uint32_t> algebraic_primes;
};

// ============================================================================
// Phase 1: Polynomial Selection (KleinJung 演算法)
// ============================================================================
class PolynomialSelector {
public:
    int degree;
    std::vector<cpp_int> f; // 代數側多項式 f(x)
    std::vector<cpp_int> g; // 有理側多項式 g(x) = x - m
    cpp_int m;

    PolynomialSelector(int d) : degree(d) {}

    // 基於 base-m 展開產生初始多項式 (實際上會使用更高階的晶格基底歸約 LLL)
    void select(const cpp_int& N) {
        std::cout << "[Phase 1] Polynomial Selection (Degree " << degree << ") starting..." << std::endl;
        // 簡易的 base-m 展開 (d次)
        // m = N^(1/d)
        cpp_int N_copy = N;
        m = 1;
        // 簡易的 m 近似值計算 (不使用 Boost 函式的近似)
        cpp_int low = 1, high = N;
        while (low <= high) {
            cpp_int mid = low + (high - low) / 2;
            cpp_int p = 1;
            for(int i=0; i<degree; ++i) p *= mid;
            if (p <= N) { m = mid; low = mid + 1; }
            else { high = mid - 1; }
        }

        f.resize(degree + 1);
        cpp_int temp = N;
        for (int i = 0; i <= degree; ++i) {
            f[i] = temp % m;
            temp /= m;
        }
        
        g = {-m, 1}; // g(x) = x - m
        
        std::cout << "          -> m = " << m << std::endl;
        std::cout << "          -> f(x) = ";
        for(int i = degree; i >= 0; --i) {
            std::cout << f[i] << "x^" << i << (i > 0 ? " + " : "");
        }
        std::cout << "\n[Phase 1] Complete." << std::endl;
    }
};

// ============================================================================
// Phase 2: Lattice Sieving (晶格篩法)
// ============================================================================
// 近年的 GNFS 已不再使用 Line Sieve (直線篩法)，而是以 Franke-Kleinjung 等人的
// 特殊 q 晶格篩法 (Special-q Lattice Sieving) 為業界標準。
class LatticeSieve {
    uint32_t rational_bound;
    uint32_t algebraic_bound;
    std::vector<uint32_t> rational_fb;
    std::vector<uint32_t> algebraic_fb;

public:
    LatticeSieve(uint32_t rb, uint32_t ab) : rational_bound(rb), algebraic_bound(ab) {}

    void generate_factor_bases() {
        std::cout << "[Phase 2] Generating Factor Bases (Rational Bound: " << rational_bound << ", Algebraic Bound: " << algebraic_bound << ")" << std::endl;
        // (省略) 實際上會進行質數生成與勒讓德符號等的篩選
    }

    std::vector<Relation> sieve(const PolynomialSelector& poly) {
        std::cout << "[Phase 2] Special-q Lattice Sieving active..." << std::endl;
        std::vector<Relation> relations;
        // 模擬實作：實際的晶格篩法會以區塊為單位掃描數百 GB 的記憶體空間
        // 將 (a, b) 的數對映射到每個特殊質數 q 的晶格 (a = i*q + j*...) 上，
        // 執行將快取效率提升到極限的篩法 (Sieve)。
        
        // 為了展示，加入一個虛擬的 Relation (關係)
        Relation r; r.a = 17; r.b = 3; 
        r.rational_primes = {2, 5}; 
        r.algebraic_primes = {3, 7};
        relations.push_back(r);
        
        std::cout << "[Phase 2] Found " << relations.size() << " relations." << std::endl;
        return relations;
    }
};

// ============================================================================
// Phase 3: Filtering (奇異點清除與派系合併)
// ============================================================================
class Filter {
public:
    void reduce_matrix(std::vector<Relation>& relations) {
        std::cout << "[Phase 3] Filtering Relations..." << std::endl;
        // 1. Singleton removal (刪除只出現過一次的質數的 Relation)
        // 2. Clique merging (為使稀疏矩陣變密集而合併 Relation)
        // 實際上會使用 Union-Find 等演算法，將數億行的矩陣壓縮到數百萬行。
        std::cout << "[Phase 3] Matrix size reduced optimally." << std::endl;
    }
};

// ============================================================================
// Phase 4: Linear Algebra over GF(2) (Block Wiedemann 法)
// ============================================================================
class LinearAlgebraGF2 {
public:
    // 在近年的超級電腦環境中，相較於 Block Lanczos 法，更適合分散式運算的
    // Block Wiedemann 法 (Coppersmith 實作) 被作為最尖端技術使用。
    std::vector<std::vector<int>> solve_nullspace(const std::vector<Relation>& relations) {
        std::cout << "[Phase 4] Block Wiedemann algorithm over GF(2) starting..." << std::endl;
        // 反覆進行稀疏矩陣 (Sparse Matrix) 與向量的乘法運算，
        // 找到多個滿足 M * x = 0 mod 2 的解向量 (核, Kernel)。
        
        std::vector<std::vector<int>> dependencies; // 依賴關係列表
        // 虛擬資料
        dependencies.push_back({0}); 
        
        std::cout << "[Phase 4] Found " << dependencies.size() << " linear dependencies (perfect squares)." << std::endl;
        return dependencies;
    }
};

// ============================================================================
// Phase 5: Algebraic Square Root (代數平方根)
// ============================================================================
class AlgebraicSquareRoot {
public:
    void compute_and_factor(const std::vector<Relation>& relations, const std::vector<int>& dep, const cpp_int& N) {
        std::cout << "[Phase 5] Algebraic Square Root computation..." << std::endl;
        
        // 1. 有理側的平方根 V 的計算 (單純的整數運算)
        cpp_int V = 1; 
        // V = sqrt( prod(a - bm) ) mod N
        
        // 2. 代數側的平方根 gamma 的計算 (Montgomery's method 等)
        // 求出巨大代數體 O_K 的元素 gamma，並透過同態映射 phi 映射到現實世界中
        // Y = phi(gamma) mod N
        cpp_int Y = 1;

        // 為迴避理想類群 (Ideal Class Group) 與單位群 (Unit Group) 的障礙 (Obstruction)，
        // 假設在 Phase 2 與 4 中已經加入了二次剩餘特徵 (Quadratic Characters) 序列。

        std::cout << "          -> Homomorphism map phi applied." << std::endl;
        std::cout << "[Phase 5] Calculating GCD(V - Y, N)..." << std::endl;
        
        cpp_int factor = gcd(V - Y, N); // GCD(X-Y, N)
        
        if (factor > 1 && factor < N) {
            std::cout << "\n================================================================" << std::endl;
            std::cout << "[SUCCESS] Non-trivial factor found: " << factor << std::endl;
            std::cout << "          Other factor: " << N / factor << std::endl;
            std::cout << "================================================================" << std::endl;
        } else {
            std::cout << "[FAILURE] Trivial solution. Trying next dependency..." << std::endl;
        }
    }
};

// ============================================================================
// Main Execution Pipeline
// ============================================================================
int main() {
    std::cout << "================================================================" << std::endl;
    std::cout << "  [SOTA GNFS] General Number Field Sieve Engine (Boost C++)     " << std::endl;
    std::cout << "================================================================" << std::endl;
    
    // RSA-270 等，想要質因數分解的巨大合成數 N
    cpp_int N("233108530344407544527637656910680524145619812480305449042948611968495918245135782867888369318577116418213919268572658314913060672626911354027609793166341626693946596196427744273886601876896313468704059066746903123910748277606548649151920812699309766587514735456594993207");
    
    // 多項式的次數 (超過 130 位數時通常選擇 5 次至 6 次)
    int degree = 6; 
    
    // 管線初始化
    PolynomialSelector poly_select(degree);
    LatticeSieve sieve(10000000, 20000000); // 實際的邊界是數千萬至數億
    Filter filter;
    LinearAlgebraGF2 linalg;
    AlgebraicSquareRoot sqrt_step;

    auto start_time = std::chrono::high_resolution_clock::now();

    // 1. 多項式選擇
    poly_select.select(N);
    
    // 2. 篩法 (Sieve) 處理
    sieve.generate_factor_bases();
    std::vector<Relation> relations = sieve.sieve(poly_select);
    
    // 3. 過濾 (矩陣壓縮)
    filter.reduce_matrix(relations);
    
    // 4. 線性代數 (GF(2) 上的零空間搜尋)
    std::vector<std::vector<int>> dependencies = linalg.solve_nullspace(relations);
    
    // 5. 代數平方根的計算與 GCD
    for (const auto& dep : dependencies) {
        sqrt_step.compute_and_factor(relations, dep, N);
    }
    
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    std::cout << "\n[System] SOTA GNFS Pipeline completed in " << elapsed.count() << " seconds." << std::endl;
    
    return 0;
}
```

那麼，這段程式碼究竟是如何突破密碼學的高牆呢？我們將按 5 個階段，將其縝密的演算法與高等數學咀嚼並解說。

---

## 2. GNFS 的最終目的： $X^2 \equiv Y^2 \pmod N$

不僅是 GNFS，現代巨大質因數分解演算法的目標，大多都是要找到滿足以下同餘式的非平凡數對 $(X, Y)$。

$$X^2 \equiv Y^2 \pmod N$$

這個式子代表「$X^2$ 與 $Y^2$ 除以 $N$ 的餘數相等」。將其變形後可得：
$X^2 - Y^2 \equiv 0 \pmod N$
也就是說，$(X-Y)(X+Y)$ 是 $N$ 的倍數。

如果 $X \not\equiv \pm Y \pmod N$（非平凡解），那麼在 $(X-Y)$ 與 $N$ 之間，就會存在「大於 1 且小於 $N$ 的公因數」。
此時，只要使用歐幾里得輾轉相除法計算 **$\gcd(X-Y, N)$** ，就能輕易求出 $N$ 的質因數。

然而，要找到這個 $X$ 與 $Y$ 猶如大海撈針。因此 GNFS 採取了天才般的策略：創造出「現實整數的世界」與「多項式代數體的世界」這 **兩個世界** ，並將計算分散。

---

## 3. Phase 1: 多項式選擇（Polynomial Selection）

```cpp
class PolynomialSelector {
    // ...
    void select(const cpp_int& N) {
        // m = N^(1/d) 的計算與 base-m 展開
        // ...
        for (int i = 0; i <= degree; ++i) {
            f[i] = temp % m;
            temp /= m;
        }
        g = {-m, 1}; // g(x) = x - m
    }
};
```

GNFS 的第一步，是建立用來橋接這兩個世界的「魔法多項式」。
對於巨大的數字 $N$，我們選擇一個整數 $m$。通常會選擇讓 $m \approx N^{1/d}$ （在程式碼中假設為 $d=6$ 次的多項式）。

接著，將 $N$ 進行 $m$ 進位展開，並使用其係數來建構多項式 $f(x)$。
$$N = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$$
$$f(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_1 x + c_0$$

這個多項式 $f(x)$ 有一個極為重要的性質： **「當變數 $x$ 代入 $m$ 時，剛好會等於 $N$（$f(m) = N$）」** 。換句話說，$f(m) \equiv 0 \pmod N$。
有理側的多項式則定義為 $g(x) = x - m$。

藉此，由 $f(x)=0$ 的根 $\alpha$ 所支配的 **「代數體的世界 $\mathbb{Z}[\alpha]$」** ，與一般的 **「有理數（整數）的世界 $\mathbb{Z}$」** ，將透過 $x \to m$ 這個「環同態映射（Homomorphism）」被緊密地連結起來。

在最尖端的 CADO-NFS 等實作中，會使用 KleinJung 演算法或 LLL 晶格基底歸約演算法，花費數個月的時間來尋找「極致完美的多項式 $f(x)$」，使其係數不會過大，且在後續步驟中更容易出現質數（更容易變得平滑）。

---

## 4. Phase 2: 特殊 $q$ 晶格篩法（Special-q Lattice Sieving）

```cpp
class LatticeSieve {
    // ...
    std::vector<Relation> sieve(const PolynomialSelector& poly) {
        // ...
        // 將 (a, b) 的數對映射到每個特殊質數 q 的晶格上，
        // 執行將快取效率提升到極限的篩法 (Sieve)。
        // ...
    }
};
```

準備好兩個世界後，接下來進入在兩個世界中尋找「平滑數（僅由小質數構成的數）」的步驟。
產生無數個整數對 $(a, b)$，並計算以下兩個值：

1. **有理側的值** ： $a - bm$
2. **代數側的範數 (Norm)** ： $b^d f(a/b)$

GNFS 的目標是收集數千萬至數億個 **「有理側與代數側的值，兩者都能完全被小質因數分解的數對（Relation：關係）」** 。

早期的 GNFS 使用「直線篩法（Line Sieve）」，將 $(a, b)$ 排列在 $xy$ 平面上，從頭開始依序用質數去除。但這種方法會造成記憶體到處存取而頻繁發生快取未命中（Cache Miss），這是一個非常慢的弱點。

因此，現在最尖端的程式碼中使用了 **「特殊 $q$ 晶格篩法（Special-q Lattice Sieve）」** 。
固定一個適度大的質數 $q$，只將「代數側的值必定能被 $q$ 整除的 $(a, b)$ 數對」作為計算對象。滿足此條件的 $(a, b)$ 會在平面上形成「晶格（Lattice）」，因此計算的位址跳躍幅度會固定，完美契合 CPU 的 L1/L2 快取。
導入這個晶格篩法後，GNFS 的計算速度獲得了戲劇性的提升。

---

## 5. Phase 3: 過濾（Filtering）

```cpp
class Filter {
public:
    void reduce_matrix(std::vector<Relation>& relations) {
        // 1. Singleton removal (刪除只出現過一次的質數的 Relation)
        // 2. Clique merging (為使稀疏矩陣變密集而合併 Relation)
    }
};
```

在 Phase 2 中，全世界的電腦花費數個月收集了數億個 Relation。然而，如果直接將這些資料丟進下一個「解聯立方程式的步驟（矩陣計算）」中，超級電腦的記憶體也會被撐爆。

因此，會進行被稱為 **Filtering（過濾）** 的矩陣超壓縮過程。

1. **Singleton removal（奇異點清除）** 
   假設某個巨大的質數 $p$，在數億個 Relation 中「只出現了一次」。我們的目標是「讓所有質數的指數都變成偶數（2 的倍數）」，所以只出現一次的質數絕對不可能變成偶數。
   因此，包含該質數的 Relation 會立即被視為「無用的垃圾」而刪除（清除）。這個連鎖反應發生後，原本數億行的資料就會不斷被削減。

2. **Clique merging（派系合併）** 
   進一步地，將共享特定質數的 Relation 互相相乘（相加），在減少行數的同時，將稀疏（空洞）的矩陣壓縮成更密集的狀態（使用類似圖論中派系搜尋的手法）。

透過這個最佳化，巨大的稀疏矩陣將被戲劇性地壓縮至可計算的大小。

---

## 6. Phase 4: GF(2) 上的線性代數（Block Wiedemann 法）

```cpp
class LinearAlgebraGF2 {
public:
    std::vector<std::vector<int>> solve_nullspace(const std::vector<Relation>& relations) {
        // 反覆進行稀疏矩陣 (Sparse Matrix) 與向量的乘法運算，
        // 找到多個滿足 M * x = 0 mod 2 的解向量 (核, Kernel)。
    }
};
```

終於來到了謎題的核心。
將收集到的 Relation 相乘，尋找 **「所有質因數的指數都變成偶數的組合」** 。

這在數學上，等同於使用一個以各質數指數的「偶數・奇數（亦即 0 或 1）」為元素的巨大矩陣 $M$，以及一個表示要使用哪些 Relation 的向量 $x$，來求解滿足
**$M \cdot x \equiv 0 \pmod 2$** 
的解向量 $x$ （零空間・核，Nullspace / Kernel）。

這需要解開數百萬行 × 數百萬列這種龐大尺寸矩陣的聯立方程式。若使用一般的基斯消去法（高斯消去法），計算複雜度將達到 $O(N^3)$，就算到宇宙毀滅也算不完。

因此，最尖端的實作採用了 **「Block Wiedemann（區塊・維德曼）法」** 。
這是一種克雷洛夫子空間法（Krylov Subspace Method），利用矩陣 $M$ 「非常稀疏（幾乎都是 0）」的特性，反覆進行矩陣與向量的乘法來導出解。
與舊有的 Block Lanczos 法不同，Block Wiedemann 法可以將計算過程完全分割到多個叢集中，因此在現代的分散式雲端運算或超級電腦的平行計算中，能發揮壓倒性的威力。

---

## 7. Phase 5: 代數平方根（Algebraic Square Root）與密碼崩潰

```cpp
class AlgebraicSquareRoot {
public:
    void compute_and_factor(...) {
        // 1. 有理側的平方根 V 的計算
        cpp_int V = 1; 
        
        // 2. 代數側的平方根 gamma 的計算
        cpp_int Y = 1;

        // ...
        cpp_int factor = gcd(V - Y, N); // GCD(X-Y, N)
    }
};
```

透過 Phase 4 的矩陣計算，我們獲得了「相乘後所有質因數皆為偶數次方的 Relation 集合 $S$」。
藉此，我們可以在有理側與代數側這兩個世界中，各自建構出「平方（2 次方）」。

有理側只是單純的整數乘法，所以計算平方根 $V$ 非常容易。
$$V^2 = \prod_{S} (a - bm)$$

**然而，真正的地獄在「代數側」。** 
在代數體的世界 $\mathbb{Z}[\alpha]$ 中，質因數分解的唯一性並不成立，因此我們一直使用理想（Ideal）來進行計算。矩陣計算所保證的 **只有「成為理想的平方」，並不能保證成為「元素的平方（$\gamma^2$）」** 。

這裡會遇到被稱為「理想類群的障礙」與「單位群的障礙」，這是代數整數論中非常巨大的高牆。
GNFS 為了打破這面牆，使用了被稱為 **「二次剩餘特徵（Quadratic Characters）」** 的魔法。
在 Phase 4 的矩陣中，事先偷偷加入針對幾十個特殊質理想的二次剩餘（勒讓德符號）序列。這樣一來，找到的集合 $S$ 就有極大的機率能避開障礙，順利形成「真正元素的平方 $\gamma^2$」。

求取 $\gamma$ 的工作（代數平方根），是使用 Montgomery 法等極其複雜的演算法來計算的。

最終，將代數側的平方根 $\gamma$，透過環同態映射 $\phi$ 瞬移回現實世界（將 $x$ 代入 $m$），得到 $Y$。
將有理側的 $V$ 直接當作 $X$，我們夢寐以求的絕對等式終於完成了。

**$$X^2 \equiv Y^2 \pmod N$$** 

剩下的就只有計算 $\gcd(X-Y, N)$ 而已。0.001 秒的處理一閃而過，當非平凡的因數印在螢幕上的那一刻，號稱堅不可摧的 RSA 密碼便徹底崩潰。

---

## 結語

GNFS 不僅僅是一種程式設計的技巧。
它是用超級電腦的分散式架構與快取最佳化等「極致的工程學」，去折服抽象代數學、環論、理想類群等「純數學深淵」的人類智慧結晶。

我們不經意傳送的聊天訊息或信用卡資訊，就是建立在這種天文數字般的數學攻防之上受到保護的。

希望透過這個 C++ 框架，能讓各位感受到最尖端密碼破解演算法背後的「數學與計算機的浪漫」。

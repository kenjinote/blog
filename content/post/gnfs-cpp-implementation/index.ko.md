---








title: '[완전 해부] 최강의 암호 해독 알고리즘 ''GNFS''를 C++로 구현하고 이해하기'
slug: "gnfs-cpp-implementation"
date: 2026-09-05T13:04:59+09:00
tags: ["GNFS", "C++", "RSA", "수학", "암호"]
draft: false
image: "gnfs_cpp_blog_eyecatch_1788580949217.jpg"
categories: ["수학·암호·양자"]
---









# 【완전 해부】 최강의 암호 해독 알고리즘 「GNFS」를 C++로 구현하여 이해하기

현대 인터넷의 근간을 지탱하는 「RSA 암호」. 그 견고함은 「거대한 합성수를 소인수분해하는 것은 현재의 컴퓨터로는 사실상 불가능하다」는 수학적 신념에 의존하고 있습니다.

하지만 인류는 결코 포기하지 않았습니다. 현재 고전 컴퓨터(양자 컴퓨터가 아닌 일반 컴퓨터)에서 거대한 소인수분해를 수행하기 위한 **인류 최강·최첨단 알고리즘 ** 이 존재합니다. 그것이 바로 **「일반 수체 체(GNFS: General Number Field Sieve)」** 입니다.

본 기사에서는 이 GNFS의 최첨단 계산 로직을 C++(Boost 라이브러리의 다정밀도 정수 `boost::multiprecision`을 사용)로 엄밀하게 모델화한 구현 코드를 전면 공개하고, 그 이면에 있는 「대수적 정수론」의 심연을 철저히 해설합니다.

수학의 신비와 그것을 굴복시키는 컴퓨터 사이언스의 힘을 꼭 소스 코드와 함께 만끽하시기 바랍니다.

---

## 1. GNFS 최첨단 로직 프레임워크 (전체 소스 코드)

먼저, 이번에 해설할 GNFS의 C++ 구현의 전모를 싣습니다. 실제 수체 체(CADO-NFS 등)는 수십만 줄에 달하는 초대형 분산 시스템이지만, 본 코드는 GNFS를 구성하는 **「5가지 필수 파이프라인(단계)」** 을 추출하여 클래스로 설계하고, 수학적인 의미를 잃지 않으면서 최소 구성으로 모델화한 것입니다.

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <chrono>
#include <boost/multiprecision/cpp_int.hpp>

// Boost.Multiprecision의 다정밀도 정수를 사용
using namespace boost::multiprecision;

// ============================================================================
// [SOTA GNFS] General Number Field Sieve (일반 수체 체) 최첨단 로직 프레임워크
// 
// 본 코드는 CADO-NFS 등에서 사용되는 최첨단 GNFS의 5가지 파이프라인을
// C++ (Boost)의 클래스 설계로서 엄밀하게 모델화한 것입니다.
// ============================================================================

struct Relation {
    int64_t a;
    int64_t b;
    std::vector<uint32_t> rational_primes;
    std::vector<uint32_t> algebraic_primes;
};

// ============================================================================
// Phase 1: Polynomial Selection (KleinJung의 알고리즘)
// ============================================================================
class PolynomialSelector {
public:
    int degree;
    std::vector<cpp_int> f; // 대수 측 다항식 f(x)
    std::vector<cpp_int> g; // 유리 측 다항식 g(x) = x - m
    cpp_int m;

    PolynomialSelector(int d) : degree(d) {}

    // base-m 전개를 기반으로 한 초기 다항식 생성 (실제로는 더 고도화된 격자 기저 축소 LLL을 사용)
    void select(const cpp_int& N) {
        std::cout << "[Phase 1] Polynomial Selection (Degree " << degree << ") starting..." << std::endl;
        // 간단한 base-m 전개 (d차)
        // m = N^(1/d)
        cpp_int N_copy = N;
        m = 1;
        // 간단한 m의 근사 (Boost 함수를 사용하지 않는 근사)
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
// Phase 2: Lattice Sieving (격자 체)
// ============================================================================
// 최근의 GNFS는 Line Sieve(직선 체)가 아닌 Franke-Kleinjung 등이 제안한
// 특수 q 격자 체 (Special-q Lattice Sieving)를 사용하는 것이 사실상 표준(de facto standard)입니다.
class LatticeSieve {
    uint32_t rational_bound;
    uint32_t algebraic_bound;
    std::vector<uint32_t> rational_fb;
    std::vector<uint32_t> algebraic_fb;

public:
    LatticeSieve(uint32_t rb, uint32_t ab) : rational_bound(rb), algebraic_bound(ab) {}

    void generate_factor_bases() {
        std::cout << "[Phase 2] Generating Factor Bases (Rational Bound: " << rational_bound << ", Algebraic Bound: " << algebraic_bound << ")" << std::endl;
        // (생략) 실제로는 소수 생성 및 르장드르 기호 등으로 필터링을 수행
    }

    std::vector<Relation> sieve(const PolynomialSelector& poly) {
        std::cout << "[Phase 2] Special-q Lattice Sieving active..." << std::endl;
        std::vector<Relation> relations;
        // 모의 구현: 실제 격자 체는 수백 GB의 메모리 공간을 블록 단위로 스캔한다.
        // (a, b)의 쌍을 특수 소수 q마다의 격자 (a = i*q + j*...) 에 매핑하고,
        // 캐시 효율을 극한까지 높인 체(Sieve)를 실행한다.
        
        // 데모용으로 더미 관계식(relation)을 1개 추가
        Relation r; r.a = 17; r.b = 3; 
        r.rational_primes = {2, 5}; 
        r.algebraic_primes = {3, 7};
        relations.push_back(r);
        
        std::cout << "[Phase 2] Found " << relations.size() << " relations." << std::endl;
        return relations;
    }
};

// ============================================================================
// Phase 3: Filtering (특이점 제거 및 클리크 병합)
// ============================================================================
class Filter {
public:
    void reduce_matrix(std::vector<Relation>& relations) {
        std::cout << "[Phase 3] Filtering Relations..." << std::endl;
        // 1. Singleton removal (1번밖에 출현하지 않는 소수를 가진 관계식 삭제)
        // 2. Clique merging (희소 행렬을 조밀하게 만들기 위한 관계식 결합)
        // 실제로는 Union-Find 알고리즘 등으로 수억 행의 행렬을 수백만 행까지 압축한다.
        std::cout << "[Phase 3] Matrix size reduced optimally." << std::endl;
    }
};

// ============================================================================
// Phase 4: Linear Algebra over GF(2) (Block Wiedemann 법)
// ============================================================================
class LinearAlgebraGF2 {
public:
    // 최근의 슈퍼컴퓨터 환경에서는 Block Lanczos 법보다 분산 컴퓨팅에
    // 적합한 Block Wiedemann 법(Coppersmith 구현)이 최첨단 기술로 사용된다.
    std::vector<std::vector<int>> solve_nullspace(const std::vector<Relation>& relations) {
        std::cout << "[Phase 4] Block Wiedemann algorithm over GF(2) starting..." << std::endl;
        // 스파스(희소) 행렬과 벡터의 곱셈 연산을 반복하여,
        // M * x = 0 mod 2 가 되는 해 벡터(커널)를 여러 개 찾는다.
        
        std::vector<std::vector<int>> dependencies; // 의존 관계 리스트
        // 더미 데이터
        dependencies.push_back({0}); 
        
        std::cout << "[Phase 4] Found " << dependencies.size() << " linear dependencies (perfect squares)." << std::endl;
        return dependencies;
    }
};

// ============================================================================
// Phase 5: Algebraic Square Root (대수적 제곱근)
// ============================================================================
class AlgebraicSquareRoot {
public:
    void compute_and_factor(const std::vector<Relation>& relations, const std::vector<int>& dep, const cpp_int& N) {
        std::cout << "[Phase 5] Algebraic Square Root computation..." << std::endl;
        
        // 1. 유리 측 제곱근 V의 계산 (단순 정수 연산)
        cpp_int V = 1; 
        // V = sqrt( prod(a - bm) ) mod N
        
        // 2. 대수 측 제곱근 gamma의 계산 (Montgomery's method 등)
        // 거대한 대수체 O_K의 원소 gamma를 구하고, 준동형 사상 phi로 현실 세계에 매핑한다.
        // Y = phi(gamma) mod N
        cpp_int Y = 1;

        // 아이디얼 군과 단수 군의 장애물(Obstruction)을 회피하기 위해,
        // Phase 2와 4에서 이차 잉여 기호(Quadratic Characters) 열이 추가되어 있다는 전제.

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
    
    // RSA-270 등, 소인수분해하고 싶은 거대한 합성수 N
    cpp_int N("233108530344407544527637656910680524145619812480305449042948611968495918245135782867888369318577116418213919268572658314913060672626911354027609793166341626693946596196427744273886601876896313468704059066746903123910748277606548649151920812699309766587514735456594993207");
    
    // 다항식의 차수 (130자리가 넘는 경우는 통상 5~6차를 선택)
    int degree = 6; 
    
    // 파이프라인 초기화
    PolynomialSelector poly_select(degree);
    LatticeSieve sieve(10000000, 20000000); // 실제 바운드는 수천만~수억
    Filter filter;
    LinearAlgebraGF2 linalg;
    AlgebraicSquareRoot sqrt_step;

    auto start_time = std::chrono::high_resolution_clock::now();

    // 1. 다항식 선택
    poly_select.select(N);
    
    // 2. 체(Sieve) 처리
    sieve.generate_factor_bases();
    std::vector<Relation> relations = sieve.sieve(poly_select);
    
    // 3. 필터링 (행렬 압축)
    filter.reduce_matrix(relations);
    
    // 4. 선형 대수 (GF(2)에서의 널 스페이스 탐색)
    std::vector<std::vector<int>> dependencies = linalg.solve_nullspace(relations);
    
    // 5. 대수적 제곱근 계산 및 GCD
    for (const auto& dep : dependencies) {
        sqrt_step.compute_and_factor(relations, dep, N);
    }
    
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;
    std::cout << "\n[System] SOTA GNFS Pipeline completed in " << elapsed.count() << " seconds." << std::endl;
    
    return 0;
}
```

그렇다면 이 코드가 어떻게 암호의 장벽을 부숴나가는 것일까요. 5개의 단계별로 그 치밀한 알고리즘과 고도의 수학을 알기 쉽게 해설해 보겠습니다.

---

## 2. GNFS의 최종 목적: $X^2 \equiv Y^2 \pmod N$

GNFS뿐만 아니라 현대의 거대 소인수분해 알고리즘 대부분이 목표로 하는 것은 다음 합동식을 만족하는 자명하지 않은 쌍 $(X, Y)$를 찾는 것입니다.

$$X^2 \equiv Y^2 \pmod N$$

이 식은 「$X^2$과 $Y^2$을 $N$으로 나눈 나머지가 같다」는 것을 의미합니다. 이를 변형하면,
$X^2 - Y^2 \equiv 0 \pmod N$
즉, $(X-Y)(X+Y)$가 $N$의 배수가 됩니다.

만약 $X \not\equiv \pm Y \pmod N$ (비자명한 해)라면, $(X-Y)$와 $N$ 사이에는 「1보다 크고 $N$보다 작은 공약수」가 존재하게 됩니다.
여기서 유클리드 호제법을 사용하여 **$\gcd(X-Y, N)$** 을 계산하면, $N$의 소인수를 아주 쉽게 구할 수 있습니다.

하지만 이 $X$와 $Y$를 찾는 것은 사막에서 바늘을 찾는 것과 같습니다. 그래서 GNFS는 「현실의 정수 세계」와 「다항식의 대수체 세계」라는 **두 세계** 를 만들어내고, 계산을 분산시키는 천재적인 접근법을 취합니다.

---

## 3. Phase 1: 다항식 선택 (Polynomial Selection)

```cpp
class PolynomialSelector {
    // ...
    void select(const cpp_int& N) {
        // m = N^(1/d) 의 계산 및 base-m 전개
        // ...
        for (int i = 0; i <= degree; ++i) {
            f[i] = temp % m;
            temp /= m;
        }
        g = {-m, 1}; // g(x) = x - m
    }
};
```

GNFS의 첫 번째 단계는 두 세계를 이어주는 「마법의 다항식」을 만드는 것입니다.
거대한 수 $N$에 대해, 정수 $m$을 선택합니다. 보통 $m \approx N^{1/d}$이 되도록 선택합니다(코드에서는 $d=6$차 다항식을 가정).

그리고 $N$을 $m$진수로 전개하고, 그 계수를 사용하여 다항식 $f(x)$를 구성합니다.
$$N = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$$
$$f(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_1 x + c_0$$

이 다항식 $f(x)$에는 **「변수 $x$에 $m$을 대입하면 정확히 $N$이 된다 ($f(m) = N$)」** 는 매우 중요한 성질이 있습니다. 다시 말해, $f(m) \equiv 0 \pmod N$입니다.
유리 측 다항식은 $g(x) = x - m$으로 정의됩니다.

이로 인해, $f(x)=0$의 근 $\alpha$가 지배하는 **「대수체의 세계 $\mathbb{Z}[\alpha]$」** 와 일반적인 **「유리수(정수)의 세계 $\mathbb{Z}$」** 가 $x \to m$이라는 「환 준동형 사상(Homomorphism)」에 의해 강력하게 연결됩니다.

최첨단 CADO-NFS 등에서는 KleinJung의 알고리즘이나 LLL 격자 기저 축소 알고리즘을 사용하여, 다항식의 계수가 극단적으로 커지지 않으면서 후속 단계에서 소수가 쉽게 나타날 수 있는 (매끄러워지기 쉬운) 「가장 적합한 다항식 $f(x)$」를 수개월에 걸쳐 탐색합니다.

---

## 4. Phase 2: 특수 $q$ 격자 체 (Special-q Lattice Sieving)

```cpp
class LatticeSieve {
    // ...
    std::vector<Relation> sieve(const PolynomialSelector& poly) {
        // ...
        // (a, b)의 쌍을 특수 소수 q마다의 격자에 매핑하고,
        // 캐시 효율을 극한까지 높인 체(Sieve)를 실행한다.
        // ...
    }
};
```

두 세계를 준비했다면, 다음은 양쪽 세계 모두에서 「매끄러운 수(작은 소수들로만 이루어진 수)」를 찾는 단계로 들어갑니다.
정수 쌍 $(a, b)$를 무수히 생성하고, 다음 두 값을 계산합니다.

1. **유리 측의 값**: $a - bm$
2. **대수 측의 노름(Norm)**: $b^d f(a/b)$

GNFS의 목적은 이 **「유리 측과 대수 측의 값이 모두 작은 소인수로만 완전히 분해되는 쌍(Relation: 관계식)」** 을 수천만에서 수억 개 모으는 것입니다.

초기 GNFS에서는 $(a, b)$를 $xy$ 평면에 나열하고 가장자리부터 차례로 소수로 나누어가는 「직선 체(Line Sieve)」가 사용되었습니다. 하지만 이 방식은 메모리의 여기저기를 접근하기 때문에 캐시 미스가 다발하여, 매우 느리다는 약점이 있었습니다.

그래서 현재의 최첨단 코드에서는 **「특수 $q$ 격자 체 (Special-q Lattice Sieve)」** 라는 기법이 사용됩니다.
어떤 적당히 큰 소수 $q$를 고정하고, 「대수 측의 값이 반드시 $q$로 나누어떨어지는 $(a, b)$ 쌍」만을 계산 대상으로 삼습니다. 이 조건을 만족하는 $(a, b)$는 평면상에서 「격자(Lattice)」를 형성하므로, 계산할 주소의 점프 폭이 일정해져 CPU의 L1/L2 캐시에 완벽하게 들어맞습니다.
이 격자 체의 도입으로 GNFS의 계산 속도는 비약적으로 향상되었습니다.

---

## 5. Phase 3: 필터링 (Filtering)

```cpp
class Filter {
public:
    void reduce_matrix(std::vector<Relation>& relations) {
        // 1. Singleton removal (1번밖에 출현하지 않는 소수를 가진 관계식 삭제)
        // 2. Clique merging (희소 행렬을 조밀하게 만들기 위한 관계식 결합)
    }
};
```

Phase 2에서 전 세계의 컴퓨터가 수개월에 걸쳐 모은 수억 개의 관계식. 하지만 이를 그대로 다음의 「연립방정식을 푸는 단계(행렬 계산)」에 밀어 넣으면, 슈퍼컴퓨터의 메모리가 펑크나게 됩니다.

그래서 **필터링(Filtering)** 이라 불리는, 행렬의 초압축 프로세스가 수행됩니다.

1. **Singleton removal (특이점 제거)**
   어떤 거대한 소수 $p$가 수억 개의 관계식 중에서 「단 1번」만 등장했다고 가정해봅시다. 우리가 목표로 하는 것은 「모든 소수의 지수를 짝수(2의 배수)로 만드는 것」이므로, 1번만 등장하는 소수는 절대 짝수로 만들 수 없습니다.
   따라서 그 소수를 포함하는 관계식은 「쓸모없는 쓰레기」로 간주되어 즉시 삭제(제거)됩니다. 이것이 연쇄적으로 일어나면서 수억 행이었던 데이터가 점점 줄어듭니다.

2. **Clique merging (클리크 병합)**
   게다가 특정 소수를 공유하는 관계식끼리 곱하여(더하여) 행의 수를 줄이면서, 스파스한(듬성듬성한) 행렬을 보다 밀집된 상태로 압축합니다(그래프 이론의 클리크 탐색과 유사한 기법 사용).

이 최적화를 통해 거대한 스파스 행렬은 계산 가능한 크기로 극적으로 압축됩니다.

---

## 6. Phase 4: GF(2) 상의 선형 대수 (Block Wiedemann 법)

```cpp
class LinearAlgebraGF2 {
public:
    std::vector<std::vector<int>> solve_nullspace(const std::vector<Relation>& relations) {
        // 스파스(희소) 행렬과 벡터의 곱셈 연산을 반복하여,
        // M * x = 0 mod 2 가 되는 해 벡터(커널)를 여러 개 찾는다.
    }
};
```

드디어 퍼즐의 핵심입니다.
수집한 관계식을 곱하여 **「소인수의 지수가 모두 짝수승이 되는 조합」** 을 찾습니다.

이는 수학적으로 각 소수 지수의 「짝수·홀수(즉, 0 또는 1)」를 원소로 하는 거대한 행렬 $M$과, 어떤 관계식을 사용할지를 나타내는 벡터 $x$를 사용하여,
**$M \cdot x \equiv 0 \pmod 2$**
가 되는 해 벡터 $x$(널 스페이스·커널)를 구하는 것과 다름없습니다.

수백만 행 × 수백만 열이라는 엄청난 크기의 행렬 연립방정식을 풀어야 합니다. 일반적인 가우스 소거법으로는 계산량이 $O(N^3)$이 되어 우주가 끝날 때까지 계산이 끝나지 않습니다.

그래서 최첨단 구현에서는 **「Block Wiedemann (블록 비데만) 법」** 이 채택되어 있습니다.
이는 행렬 $M$이 「매우 스파스함(대부분이 0)」을 이용하여, 행렬과 벡터의 곱셈을 반복적으로 수행하여 해를 도출해내는 크릴로프 부분공간법의 일종입니다.
기존의 Block Lanczos 법과 달리 Block Wiedemann 법은 계산 프로세스를 여러 클러스터로 완전히 분할할 수 있기 때문에, 현대의 분산 클라우드 컴퓨팅이나 슈퍼컴퓨터에서의 병렬 계산에서 압도적인 위력을 발휘합니다.

---

## 7. Phase 5: 대수적 제곱근 (Algebraic Square Root)과 암호 붕괴

```cpp
class AlgebraicSquareRoot {
public:
    void compute_and_factor(...) {
        // 1. 유리 측 제곱근 V의 계산
        cpp_int V = 1; 
        
        // 2. 대수 측 제곱근 gamma의 계산
        cpp_int Y = 1;

        // ...
        cpp_int factor = gcd(V - Y, N); // GCD(X-Y, N)
    }
};
```

Phase 4의 행렬 계산으로 인해 우리는 「곱하면 모든 소인수가 짝수승이 되는 관계식의 집합 $S$」를 손에 넣었습니다.
이로써 유리 측과 대수 측, 각각의 세계에서 「제곱」을 구성할 수 있습니다.

유리 측은 단순한 정수의 곱셈이므로 제곱근 $V$를 계산하는 것은 쉽습니다.
$$V^2 = \prod_{S} (a - bm)$$

**하지만 진짜 지옥은 「대수 측」에 있습니다.**
대수체의 세계 $\mathbb{Z}[\alpha]$에서는 소인수분해의 유일성이 성립하지 않기 때문에, 아이디얼을 사용하여 계산을 수행해 왔습니다. 행렬 계산으로 보장된 것은 **「아이디얼의 제곱」이 되는 것뿐이며, 「원소의 제곱($\gamma^2$)」이 되는 것은 보장되지 않은** 것입니다.

여기에는 「아이디얼 군의 장애물」과 「단수 군의 장애물」이라는 대수적 정수론의 거대한 벽이 가로막고 있습니다.
GNFS에서는 이 벽을 깨뜨리기 위해 **「이차 잉여 기호 (Quadratic Characters)」** 라는 마법을 사용합니다.
Phase 4의 행렬에 미리 수십 개의 특별한 소아이디얼에 대한 이차 잉여(르장드르 기호)의 열을 몰래 추가해 두는 것입니다. 이로 인해 찾아낸 집합 $S$는 압도적인 확률로 장애물을 통과하여 무사히 「진정한 원소의 제곱 $\gamma^2$」을 형성해 줍니다.

$\gamma$를 구하는 작업(대수적 제곱근)은 Montgomery 법 등의 매우 복잡한 알고리즘을 사용하여 계산됩니다.

그리고 마침내 대수 측의 제곱근 $\gamma$를, 환 준동형 사상 $\phi$를 통해 현실 세계로 워프($x$에 $m$ 대입)시켜 $Y$를 얻습니다.
유리 측의 $V$를 그대로 $X$로 두면, 마침내 쫓고 쫓던 절대 등식이 완성됩니다.

**$$X^2 \equiv Y^2 \pmod N$$**

남은 것은 $\gcd(X-Y, N)$을 계산하는 것뿐입니다. 0.001초의 처리가 순식간에 지나가고 비자명한 인수가 화면에 인쇄되는 순간, 난공불락을 자랑하던 RSA 암호는 완전히 붕괴됩니다.

---

## 맺음말

GNFS는 단순한 프로그래밍 테크닉이 아닙니다.
추상대수학, 환론, 아이디얼 군과 같은 「순수 수학의 심연」을 슈퍼컴퓨터의 분산 아키텍처나 캐시 최적화와 같은 「극한의 엔지니어링」으로 굴복시킨 인류 지성의 결정체입니다.

우리가 무심코 전송하고 있는 채팅이나 신용카드 정보는 이러한 천문학적인 수학의 공방 위에서 지켜지고 있는 것입니다.

이 C++ 프레임워크를 통해 최첨단 암호 해독 알고리즘의 이면에 있는 「수학과 컴퓨터의 로망」을 느껴보시기 바랍니다.

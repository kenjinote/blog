---
title: 'Existe algum algoritmo além do GNFS (Crivo Geral dos Campos de Números)?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Integer Factorization", "RSA", "Algorithms"]
---

## 1. Introdução: A Fatoração de Inteiros e a Base da Criptografia Moderna

RSA é um entre vários sistemas de chave pública e sua segurança depende, em parte, da dificuldade de fatorar inteiros grandes. A segurança da Internet como um todo, porém, não depende apenas do RSA. Um método eficiente de fatoração ameaçaria os usos baseados em RSA, mas não derrubaria automaticamente toda a infraestrutura de comunicação.

Para fatorar inteiros grandes em geral, o GNFS está entre os métodos clássicos mais conhecidos. Ele foi usado para fatorar números como RSA-768 e RSA-250; números com estrutura especial podem ser mais adequados a métodos como o SNFS. [Relatório do RSA-250](https://eprint.iacr.org/2020/697)

No entanto, criptógrafos e matemáticos sempre se fazem as seguintes perguntas: "Existe algum algoritmo clássico que supere o GNFS?" "Onde está o limite dos computadores clássicos?" e "Como os computadores quânticos irão contornar essa situação?"

Neste artigo, dissecaremos exaustivamente as profundas estruturas matemáticas por trás do GNFS e conduziremos uma análise técnica detalhada da seleção de polinômios, processo de crivagem e etapas de álgebra linear usando o método de Block Wiedemann. Além disso, consideraremos métodos de extensão para GNFS, como as melhorias de Coppersmith, e compararemos e explicaremos as diferenças cruciais entre os algoritmos clássicos de tempo subexponencial (Sub-exponential time) e os algoritmos quânticos de tempo polinomial a partir de uma perspectiva matemática.

---

## 2. Complexidade Assintótica e Notação L (L-notation)

Ao avaliar a complexidade de algoritmos de fatoração, a **Notação L (L-notation)** é usada para expressar o tempo subexponencial relativo ao número de dígitos da entrada $n$, ao invés da notação padrão de tempo polinomial (como $O(n^k)$). A notação L é definida da seguinte forma:

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Aqui, $n$ é o número inteiro a ser fatorado e $\ln n$ é o logaritmo natural, o qual é proporcional ao comprimento em bits de $n$.
- Quando $\alpha = 0$: $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, representando um **tempo polinomial (Polynomial time)** em relação ao comprimento em bits.
- Quando $\alpha = 1$: $L_n[1, c] = \exp(c \ln n) = n^c$, representando um **tempo exponencial (Exponential time)** em relação ao comprimento em bits.
- Quando $0 < \alpha < 1$: Representa um **tempo subexponencial (Sub-exponential time)** localizado entre o tempo polinomial e o tempo exponencial.

A evolução dos algoritmos de fatoração no passado tem sido a história de reduzir gradualmente o valor desse $\alpha$.
- **CFRAC**: tempo esperado heurístico $L_n[1/2,\sqrt{2}]$ ([referência](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS**: tempo esperado heurístico $L_n[1/2,1]$ ([documentação do FLINT](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS**: a estimativa heurística usual é $L_n[1/3,(64/9)^{1/3}]$; não é um limite provado nem um tempo prático diretamente ([análise do NFS](https://arxiv.org/abs/2007.02730)).

---

## 3. Visão Geral do Algoritmo GNFS e Estrutura Matemática

GNFS e QS usam a ideia de congruência de quadrados: procuram $X,Y$ tais que $X^2\equiv Y^2\pmod n$, mas $X\not\equiv\pm Y\pmod n$; então $\gcd(X-Y,n)$ pode fornecer um fator não trivial.

No entanto, a verdadeira essência do GNFS não é fazer isso apenas no corpo dos números racionais $\mathbb{Q}$, mas sim buscar simultaneamente por "números suaves (Smooth numbers)" tanto em uma extensão de corpo chamada Corpo de Números Algébricos (Algebraic Number Field) $\mathbb{Q}(\alpha)$ quanto no corpo dos números racionais, e construir uma relação de congruência por meio de um homomorfismo.

O processo do GNFS é amplamente dividido em 5 fases.

```mermaid
graph TD
  A["Problema de fatoração de inteiros (entrada n)"] --> B["1. Seleção de polinômios (Polynomial Selection)"]
  B --> C["2. Processo de crivagem (Sieving Phase)"]
  C --> D["3. Filtragem (Filtering Phase)"]
  D --> E["4. Álgebra Linear (Linear Algebra Phase)"]
  E --> F["5. Fase da raiz quadrada (Square Root Phase)"]
  F --> G["Saída dos fatores primos p, q"]```

### 3.1 Fase 1: Seleção de polinômios (Polynomial Selection)

O sucesso do GNFS depende fortemente da seleção adequada dos polinômios. O objetivo é encontrar dois polinômios irredutíveis $f_1(x)$ (lado racional) e $f_2(x)$ (lado algébrico) que compartilham uma raiz comum $m$. Ou seja,
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$
satisfazendo.

Normalmente, um polinômio linear $f_1(x) = x - m$ é escolhido para o lado racional, e um polinômio mônico $f_2(x)$ de grau $d$ (tipicamente 5 ou 6) é escolhido para o lado algébrico. A abordagem mais clássica é o **Método de base $m$ (Base-$m$ method)**.
Escolhe-se um inteiro $m = \lfloor n^{1/(d+1)} \rfloor$ próximo à raiz $1/(d+1)$ de $n$ e expande-se $n$ na base $m$.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
Com isso, obtemos o polinômio $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Claramente, $f_2(m) = n \equiv 0 \pmod n$.

Entretanto, em implementações modernas o **Algoritmo de Kleinjung** é utilizado. Ele busca polinômios cujos coeficientes não se tornem extremamente grandes (otimização de Skewness) enquanto otimiza propriedades algébricas (valor $E$ de Murphy e valor $\alpha$), facilitando a geração de números suaves durante o processo de crivagem. Esta etapa por si só requer uma enorme quantidade de recursos computacionais.

### 3.2 Fase 2: Processo de crivagem (Sieving Phase)

Uma vez que os polinômios são determinados, entra-se na fase de "Crivagem (Sieving)", que é a fase mais exigente do ponto de vista computacional do algoritmo. Aqui, buscamos pares $(a, b)$. Este par deve ser coprimo entre si e é requerido que os dois valores seguintes sejam simultaneamente "suaves (Smooth)".

1. **Norma do lado racional**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norma do lado algébrico**: $F_2(a, b) = b^d \cdot f_2(a/b)$

"Suave" significa que o valor pode ser fatorado apenas por números primos menores ou iguais a um limite especificado (Sieve bound). Uma base de fatores (Factor base) para o lado racional e outra para o lado algébrico são preparadas, e números suaves são encontrados eficientemente em um enorme espaço de busca utilizando uma técnica semelhante ao Crivo de Eratóstenes.
Hoje, uma técnica chamada **Crivo em Reticulado (Lattice Sieving)** é dominante, onde se fixa um número primo específico $q$ e realiza-se a crivagem apenas em pares $(a, b)$ em um sub-reticulado no qual tanto o lado racional quanto o algébrico são múltiplos de $q$, alcançando assim uma eficiência extremamente alta.

### 3.3 Fase 3: Filtragem (Filtering Phase)

O número de relações suaves (relations) encontradas no processo de crivagem chega a centenas de milhões, ou até bilhões. No entanto, muitas destas contêm informações inúteis.
O objetivo da filtragem é construir uma enorme matriz esparsa (Sparse Matrix) ao mesmo tempo que reduz a sua dimensionalidade ao máximo possível.

Especificamente, realizam-se as seguintes operações:
- **Remoção de singletons (Singleton removal)**: Excluir as relações que contêm fatores primos que aparecem apenas uma vez.
- **Remoção de cliques / Mesclagem (Clique removal / Merging)**: Multiplicar relações que possuem fatores primos que aparecem duas ou mais vezes, eliminando variáveis para reduzir para um sistema de equações de maior densidade, porém menor dimensionalidade.

Com isso, uma matriz com bilhões de linhas é comprimida em uma enorme matriz esparsa $\mathbf{A}$ (com elementos 0 e 1 sobre o corpo $\mathbb{F}_2$) de nível de dezenas de milhões de linhas.

### 3.4 Fase 4: Álgebra Linear (Linear Algebra Phase)

Aqui, buscamos um vetor não nulo $\mathbf{x}$ que satisfaça $\mathbf{A}\mathbf{x}=\mathbf{0}$ sobre $\mathbb{F}_2$; isto é, um vetor do núcleo (espaço nulo) da matriz esparsa.

Para matrizes esparsas, usam-se métodos iterativos de Krylov, como Block Lanczos e Block Wiedemann. O relatório da fatoração do RSA-250 documenta um cálculo com Block Wiedemann; a escolha e o desempenho dependem da matriz, da implementação e da arquitetura computacional. [Relatório do RSA-250](https://eprint.iacr.org/2020/697)


### 3.5 Fase 5: Raiz quadrada (Square Root Phase)

A partir das soluções da álgebra linear, constrói-se um produto que é um "quadrado perfeito" em ambos os lados, o racional e o algébrico.
No lado racional, $\prod (a-bm)$ torna-se o quadrado $X^2$ de um determinado inteiro $X$, enquanto no lado algébrico o produto dos ideais correspondentes torna-se um quadrado perfeito $\gamma^2$ no corpo de números algébricos.
Ao calcular esse $\gamma$ no corpo de números algébricos e aplicar o homomorfismo ao anel dos inteiros racionais $\phi: \alpha \mapsto m \pmod n$, obtemos a congruência:
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$
obtém-se.

O cálculo da raiz quadrada no corpo de números algébricos utiliza algoritmos complexos, como o **Método de Montgomery**, exigindo um profundo conhecimento em teoria algébrica dos números. Finalmente, $\gcd(X-Y, n)$ é calculado, e se um fator não trivial for obtido, a fatoração estará concluída.

---

## 4. Existe algum algoritmo clássico que supere o GNFS?

Até o momento, não foi descoberto nenhum algoritmo clássico que seja capaz de atingir uma complexidade assintótica abaixo de $L_n[1/3, c]$ para a fatoração de números inteiros gerais. No entanto, existem algumas tentativas e algoritmos derivados voltados a romper esses limites teóricos e práticos.

### 4.1 Crivo de Múltiplos Campos de Números (MNFS: Multiple Number Field Sieve)

Como uma abordagem estendida do GNFS, existe o **Crivo de Múltiplos Campos de Números (MNFS)** de D. Coppersmith. Enquanto o GNFS utiliza 2 polinômios (um lado racional e um algébrico), o MNFS utiliza múltiplos polinômios algébricos diferentes em conjunto com um único polinômio racional.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

Ao usar múltiplos corpos algébricos, a probabilidade de "ser suave em qualquer um dos corpos algébricos" em cada etapa da crivagem aumenta drasticamente. Com essa abordagem, Coppersmith conseguiu reduzir ligeiramente a constante $c$ da complexidade $L_n[1/3, c]$.
No entanto, na prática, a sobrecarga de gerenciar múltiplos corpos é grande, e não houve grandes avanços definitivos em módulos [RSA](https://kenji.blog/pt/p/modern-cryptography-public-key-hash-signature/) em escalas de uso no mundo real.

### 4.2 Algoritmos de classe $L_n[1/4]$ são possíveis?

Não se conhece um algoritmo clássico geral de fatoração com complexidade assintótica inferior à forma usual do GNFS, mas isso não prova que um melhor seja impossível. A análise de números suaves descreve métodos conhecidos, não um limite inferior para todos os algoritmos; a questão continua em aberto.
---

## 5. O Grande Avanço da Computação Quântica: [Algoritmo de Shor](https://kenji.blog/pt/p/quantum-computing-shors-algorithm/)

Enquanto os computadores clássicos enfrentam a barreira de $L_n[1/3]$, o **Algoritmo de Shor ([Shor's Algorithm](https://kenji.blog/pt/p/quantum-computing-shors-algorithm/))**, introduzido por Peter Shor em 1994, destruiu esta parede mudando fundamentalmente o modelo de computação em si.

### 5.1 O impacto do tempo polinomial quântico

O Algoritmo de Shor reduz o problema da fatoração a um "Problema de Busca de Ordem (Order Finding Problem)". Dado um inteiro $a$, é o problema de encontrar o período (ordem) $r$ da função $f(x) = a^x \pmod n$.
Shor usa a interferência quântica para extrair informações sobre o período da função; isso não significa que todos os estados em superposição sejam lidos em paralelo.

Em termos de complexidade computacional, o tempo de execução do Algoritmo de Shor é de **tempo polinomial quântico**, especificamente o seguinte:
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Algoritmo clássico (GNFS)"] -->|"Limite"| B["Tempo subexponencial L_n[1/3]"]
  C["Algoritmo quântico (Shor)"] -->|"Avanço"| D["Tempo polinomial O((log n)^3)"]
  B --> E["Uso contínuo de criptografia RSA (aumento do tamanho da chave)"]
  D --> F["RSA vulnerável se existir um computador quântico tolerante a falhas suficientemente capaz"]
```

### 5.2 Tempo subexponencial clássico vs Tempo polinomial quântico

Shor fatora em tempo polinomial num modelo quântico idealizado, mas isso não informa o custo prático de uma máquina tolerante a falhas. Gidney e Ekerå estimaram em 2021 cerca de 20 milhões de qubits físicos e 8 horas; em 2025, Gidney estimou menos de um milhão de qubits físicos ruidosos e menos de uma semana sob outro projeto e outras hipóteses. São estimativas condicionais, não demonstrações de quebra do RSA-2048; nenhum computador quântico fatorou um inteiro desse tamanho. Não se deduzem portas ou tempo apenas de $2048^3$. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

A fórmula assintótica do GNFS não fornece diretamente operações ou tempo; são necessários um modelo de custo e parâmetros explícitos.
## 6. Conclusão: Perspectivas para a próxima geração

O GNFS é o melhor método geral conhecido, não um limite comprovado. Melhorias práticas não garantem prazos nem que o RSA permanecerá seguro por décadas. As estimativas de Shor são condicionais e não descrevem o hardware atual. A transição pós-quântica segue padrões e recomendações oficiais aplicáveis.

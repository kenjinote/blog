---
title: "A Verdadeira Estrutura Matemática do Crivo Geral dos Corpos de Números (GNFS)"
date: 2026-09-05T02:26:13+09:00
tags: ["Matemática", "Criptografia", "RSA", "GNFS"]
draft: false
image: "rsa_encryption_break_1788542156523.jpg"
categories: ["Matemática, Criptografia e Quântica"]
---

# A Verdadeira Estrutura Matemática do Crivo Geral dos Corpos de Números (GNFS)

O objetivo final do GNFS é encontrar $X, Y$ tais que $X^2 \equiv Y^2 \pmod N$.
Para alcançar isso, os matemáticos construíram uma ponte entre o **"mundo dos inteiros reais"** e o **"mundo dos corpos algébricos"** . Essa ponte é exatamente o "homomorfismo".

## Fase 1: Conectando os mundos com "Homomorfismo"

### 1. Seleção do polinômio e definição das raízes
Para um número composto gigante $N$, escolhemos um inteiro $m$ e um polinômio $f(x)$ tais que $f(m) \equiv 0 \pmod N$.
(Exemplo: Expandimos $N$ na base $m$ e criamos $f(x)$ a partir de seus coeficientes. Neste momento, assumimos que $f(x)$ é irredutível sobre o corpo dos números racionais $\mathbb{Q}$ (não pode ser mais fatorado)).

Em seguida, definimos uma das "raízes complexas" da equação $f(x) = 0$ como $\alpha$.
Naturalmente, $f(\alpha) = 0$. $\alpha$ não é um número inteiro, mas um número complexo envolvendo raízes e números imaginários (um número algébrico).

### 2. Construção de Anéis (Rings) e Homomorfismo
Aqui, preparamos dois "anéis" matemáticos (mundos onde adição e multiplicação são definidas).

*   **Mundo A: $\mathbb{Z}[\alpha]$** (O anel dos inteiros algébricos contendo $\alpha$)
    Um mundo de números expressos na forma $a + b\alpha + c\alpha^2 + \dots$.
*   **Mundo B: $\mathbb{Z}/N\mathbb{Z}$** (O anel dos restos módulo $N$)
    Um mundo de congruências composto apenas por inteiros de $0$ a $N-1$.

Aqui, definimos um mapeamento $\phi$ do Mundo A para o Mundo B da seguinte forma.
**$$\phi : \mathbb{Z}[\alpha] \to \mathbb{Z}/N\mathbb{Z}$$**
**$$\phi(\alpha) = m \pmod N$$**

Este mapeamento $\phi$ é uma operação mágica que substitui exatamente a variável $\alpha$ do Mundo A pelo inteiro $m$ do Mundo B.
Este $\phi$ possui uma propriedade extremamente poderosa chamada **"Homomorfismo de Anéis (Ring Homomorphism)"** .
Homomorfismo é a propriedade de **"teleportar para outro mundo sem destruir a estrutura da adição e multiplicação"** . Em outras palavras, as seguintes equações são válidas:
*   $\phi(X \times Y) = \phi(X) \times \phi(Y)$
*   $\phi(X^2) = \phi(X)^2$

O que isso significa? Se pudermos criar o **"quadrado ($\gamma^2$)"** de algum elemento complexo $\gamma$ no "Mundo A (o mundo de $\alpha$)", e teleportá-lo para o "Mundo B (mundo dos restos)" usando $\phi$, **a forma quadrada $\phi(\gamma)^2$ é perfeitamente preservada** .

---

## Fase 2: O Colapso da Fatoração em Números Primos e o Nascimento dos "Ideais"

No Mundo A ($\mathbb{Z}[\alpha]$), queremos reunir muitos elementos adequados $(a - b\alpha)$ e multiplicá-los para criar um "quadrado perfeito (elemento quadrado)".
Normalmente, faríamos a "fatoração em números primos" de cada $(a - b\alpha)$ coletado e os combinaríamos de forma que os expoentes dos primos fossem todos pares (resolvendo com matrizes) para formar um quadrado.

**No entanto, aqui, a parede desesperadora da álgebra se ergue.**
Em mundos de corpos algébricos como $\mathbb{Z}[\alpha]$, a **"unicidade da fatoração em números primos (qualquer número pode ser expresso de forma única como o produto de primos)"** ensinada no ensino médio **colapsa** .

(Exemplo: Em um certo mundo de corpo algébrico, $6 = 2 \times 3$, mas ao mesmo tempo $6 = (1+\sqrt{-5}) \times (1-\sqrt{-5})$, e não sabemos mais quais são os verdadeiros primos)

Se a fatoração não for única, o quebra-cabeça de "contar o número de primos para torná-los pares" (o método do crivo) é, em princípio, impossível de executar.

### A Salvação de Kummer e Dedekind: "Ideais"
O que salvou esse colapso foi o conceito de **"Ideal (Ideal: número ideal)"** criado pelos matemáticos do século 19.
Pensando não no elemento em si, mas no "conjunto de múltiplos (ideal)" gerado por esse elemento, a fatoração em números primos tornou-se possível novamente.

No anel de inteiros de um corpo algébrico $\mathcal{O}_K$ (um anel mais completo contendo $\mathbb{Z}[\alpha]$), é provado que mesmo que um elemento não possa ser fatorado unicamente, **"um ideal sempre pode ser fatorado unicamente como o produto de 'Ideais Primos ($\mathfrak{p}$)'"** .

Portanto, no GNFS, em vez de fatorar o próprio elemento $(a - b\alpha)$, fatoramos o **ideal principal $\langle a - b\alpha \rangle$ gerado por ele em ideais primos** .

---

## Fase 3: A Norma (Norm) e os Dois Crivos (Sieves)

Então, como sabemos em quais ideais primos o ideal $\langle a - b\alpha \rangle$ é decomposto?
Aqui usamos uma função chamada **"Norma (Norm)"** . A Norma é uma função que converte elementos complexos de corpos algébricos em "inteiros reais normais $\mathbb{Z}$".

A norma do elemento $(a - b\alpha)$ é encontrada por um cálculo polinomial simples $b^d f(a/b)$ ($d$ é o grau de $f(x)$).

Por um teorema algébrico, sabemos que **"se a norma de um certo ideal puder ser completamente fatorada em pequenos números primos (for suave), então o ideal original também pode ser completamente fatorado em pequenos ideais primos"** .

Então, para um grande número de pares de inteiros $(a, b)$, o GNFS calcula os dois seguintes simultaneamente e coleta apenas os pares em que ambos se tornam "números suaves":
1. **Crivo Racional (Rational Sieve)** : $a - bm$ (o valor no mundo real)
2. **Crivo Algébrico (Algebraic Sieve)** : $b^d f(a/b)$ (a norma no mundo dos corpos algébricos)

Coletando dezenas de milhões de pares $(a, b)$ em que ambos são suaves, resolvemos os dados de fatoração de ideais primos (quantos ideais primos estão incluídos) como uma matriz gigante (álgebra linear sobre GF(2)) para encontrar um conjunto $S$ de pares tal que "quando multiplicados, os expoentes de todos os ideais primos se tornem pares".

---

## Fase 4: Os Dois "Obstáculos" e o Grupo de Classes de Ideais

A partir do cálculo da matriz, descobrimos que multiplicar todos os ideais de $(a - b\alpha)$ pertencentes ao conjunto $S$ resulta no quadrado de um certo ideal $I$.
$$\prod_{S} \langle a - b\alpha \rangle = I^2$$

**No entanto, ainda não acabou. A barreira matemática mais profunda e difícil do GNFS está aqui.**

O que queremos no final não é o "quadrado de um ideal", mas o **"quadrado de um elemento ($\gamma^2$)"** para substituir no mapeamento $\phi$.
Só porque se tornou o quadrado de um ideal, não significa necessariamente que o elemento em si é um quadrado. Existem **dois fortes obstáculos matemáticos (Obstructions)** aqui.

### Obstáculo ①: A Barreira do Grupo de Classes de Ideais (Ideal Class Group)
O ideal $I$ nem sempre é um "ideal gerado por um único elemento (ideal principal)".
É impossível extrair um elemento específico $\gamma$ de um ideal que não é principal.

Aqui entra o conceito de **"Grupo de Classes de Ideais (Class Group, $Cl_K$)"** . O grupo de classes de ideais é um grupo que mede "quantos ideais existem no mundo daquele corpo algébrico que não são principais (o quanto a unicidade da fatoração se quebra)".
Mesmo que $\prod \langle a - b\alpha \rangle$ se torne $I^2$, se $I$ não for o elemento de identidade (ideal principal) no grupo de classes de ideais, ele não pode ser trazido de volta ao quadrado de um elemento.

### Obstáculo ②: A Barreira do Grupo de Unidades (Unit Group)
Suponhamos que, por sorte, $I$ fosse o ideal principal $\langle \gamma \rangle$.
Então, teríamos $\prod \langle a - b\alpha \rangle = \langle \gamma^2 \rangle$.
Você pode pensar, "Ótimo, o elemento também é um quadrado!", mas isso é um grande erro.

Ideais (conjuntos de múltiplos) sendo iguais não significa que os elementos sejam perfeitamente iguais. Sempre haverá um desvio por uma **"Unidade (Unit: um número cujo inverso também é um inteiro. Por exemplo, 1 ou -1)"** .
Em outras palavras, a verdadeira equação dos elementos se torna assim:
$$\prod_{S} (a - b\alpha) = u \cdot \gamma^2$$
($u$ é um elemento do grupo de unidades $U_K$)

A menos que esta unidade $u$ em si seja o quadrado de algo, o lado esquerdo nunca pode se tornar um "quadrado perfeito de um elemento".

---

## Fase 5: A Magia de Adleman "Caracteres Quadráticos" (Quadratic Characters)

O obstáculo do grupo de classes de ideais e o obstáculo do grupo de unidades. Como superar esses dois?
Aqui entra o brilhante método dos **"Caracteres Quadráticos (Quadratic Characters)"** , introduzido pelo criptógrafo Leonard Adleman (o "A" do RSA) e outros.

Para determinar "se um certo elemento é um quadrado perfeito no corpo algébrico", usamos a versão de corpos algébricos do Símbolo de Legendre (resíduo quadratique).
Naquela matriz gigante anterior (o quebra-cabeça para tornar pares as contagens de ideais primos), nós **furtivamente adicionamos algumas dezenas de condições extras (colunas) dizendo "os caracteres quadráticos para certos ideais primos especiais $\mathfrak{q}$ também devem ser todos $1$ (par)"** .

Quando encontramos um conjunto $S$ que satisfaz até mesmo essas condições adicionais através de cálculos de matrizes, teoremas profundos da teoria algébrica dos números garantem que **"tanto o obstáculo do grupo de classes de ideais quanto o obstáculo do grupo de unidades desaparecerão naturalmente com uma probabilidade esmagadora"** .

Com isso, finalmente obtemos a verdadeira equação.
$$\prod_{S} (a - b\alpha) = \gamma^2$$

---

## Fase Final: A Fusão dos Mundos e o Colapso Criptográfico

Finalmente, todas as peças do quebra-cabeça estão no lugar.

**[Elementos no Mundo dos Corpos Algébricos (Mundo A)]**
$\gamma^2 = \prod (a - b\alpha)$
(Nós usamos um algoritmo de raiz quadrada para encontrar $\gamma$)

**[Elementos no Mundo Real (Mundo dos Números Racionais)]**
$V^2 = \prod (a - bm)$
(Como esta é uma simples multiplicação de inteiros, $V$ é encontrado normalmente)

Agora é hora daquela ponte mágica que construímos no início, o **homomorfismo $\phi$** .
Nós teleportamos o elemento $\gamma$ do Mundo A para o Mundo B (o mundo dos restos de $N$) usando $\phi$ (o mapeamento onde substituímos $\alpha$ por $m$).
$$Y = \phi(\gamma) \pmod N$$

Por outro lado, levamos o $V$ construído no mundo real diretamente para o mundo dos restos e o chamamos de $X$.
$$X = V \pmod N$$

Devido à propriedade "preservadora de estrutura" do homomorfismo, a relação quadrada que se manteve no Mundo A é perfeitamente preservada no Mundo B (o mundo módulo $N$).
Além disso, como os pares originais $(a, b)$ foram feitos em correspondência nas formas $a - b\alpha$ e $a - bm$, estes $X$ e $Y$ colidem no mundo módulo $N$ e produzem a seguinte equação absoluta.

**$$X^2 \equiv Y^2 \pmod N$$**

Tudo o que resta é rezar para que esses $X$ e $Y$ não sejam soluções triviais ($X \equiv \pm Y$) e calcular
**$\gcd(X - Y, N)$** .

Se for uma solução não trivial, o algoritmo euclidiano avança em 0.001 segundos, e os números primos secretos $p$ e $q$, que são o coração da criptografia RSA, são impressos na tela de saída.

---

Este é o quadro completo do **"Crivo Geral dos Corpos de Números (GNFS)"** , a essência da matemática moderna.

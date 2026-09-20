---
title: "Equação de Pell: O Encanto da Equação Diofantina com Soluções Infinitas e Frações Contínuas"
description: "Um guia detalhado sobre a equação de Pell, sua resolução usando frações contínuas e a geração de infinitas soluções."
slug: "pell-equation"
date: "2026-09-20T15:00:00+09:00"
image: "eyecatch.jpg"
categories:
  - "matemática"
tags:
  - "equação-de-pell"
  - "equação-diofantina"
  - "fração-contínua"
  - "teoria-dos-números"
---

# Introdução

No campo da teoria dos números, a **equação de Pell** (Pell's equation) é conhecida como uma das equações diofantinas mais belas e com profunda fundamentação teórica. Neste artigo, forneceremos uma explicação muito detalhada, começando da definição básica e propriedades desta equação, até um método de solução elegante e eficiente usando frações contínuas (Continued fractions), e o mecanismo de geração de suas infinitas soluções. Para todos os amantes da matemática, abordamos desde a dedução de fórmulas até a visualização de algoritmos e a implementação utilizando uma linguagem de programação.

## 1. O que é a [Equação de Pell](https://kenji.blog/p/pell-equation/)?

A equação de Pell refere-se a uma equação diofantina quadrática em duas variáveis que possui a seguinte forma:

$$ x^2 - ny^2 = 1 $$

Aqui, $n$ é um número inteiro positivo que não é um número quadrado (livre de quadrados ou pelo menos não um quadrado perfeito). Nosso objetivo é encontrar pares de números inteiros desconhecidos $x$ e $y$ que satisfaçam esta equação. Suponhamos por um momento que $n$ é um quadrado perfeito, ou seja, $n = k^2$ (onde $k$ é um inteiro). Então a equação pode ser transformada da seguinte maneira:

$$ x^2 - k^2y^2 = 1 $$
$$ (x - ky)(x + ky) = 1 $$

Como $x$, $y$ e $k$ são todos inteiros, $(x - ky)$ e $(x + ky)$ também devem ser inteiros. As únicas combinações de inteiros cujo produto é 1 são $(1, 1)$ ou $(-1, -1)$. Resolvendo isso, obtemos $y = 0$, o que significa que as únicas soluções são as muito simples: $(x, y) = (\pm 1, 0)$. Portanto, na equação de Pell, a condição de que $n$ não seja um quadrado perfeito é uma premissa essencial para encontrar soluções significativas.

## 2. Contexto Histórico: Pell, Fermat e Antigos Matemáticos Indianos

Embora esta equação leve o nome "Pell", explorar os fatos históricos revela um contexto um tanto estranho. Na verdade, a primeira pessoa na Europa moderna a estudar uma solução geral para esta equação e afirmar fortemente que sempre existe uma solução foi o grande matemático francês **[Pierre de Fermat](https://kenji.blog/p/fermat/)**.

Mais tarde, **[Leonhard Euler](https://kenji.blog/p/euler/)** vinculou erroneamente o nome do matemático inglês **John Pell** a esta equação, e desde então ela tem sido amplamente conhecida como "equação de Pell". O próprio Pell não desempenhou um papel central no método de resolução desta equação.

Retrocedendo ainda mais no tempo, os matemáticos indianos **Brahmagupta** e **Bhāskara II** calcularam soluções para equações deste tipo usando um algoritmo sofisticado chamado método Chakravala, centenas de anos antes de Fermat. A história da exploração por matemáticos desde a antiguidade até a Idade Média e a era moderna está inscrita nesta equação.

## 3. A Diferença entre Soluções Triviais e Não Triviais

Para a equação de Pell $x^2 - ny^2 = 1$, independentemente do valor de $n$, sempre existe a solução $(x, y) = (\pm 1, 0)$. Substituir esses valores na equação dá $1^2 - n \cdot 0^2 = 1$, o que é obviamente verdadeiro. Isso é chamado de **solução trivial** (trivial solution).

Contudo, o que realmente interessa aos matemáticos é uma **solução não trivial** (non-trivial solution) onde $y \neq 0$. Surpreendentemente, se $n$ for um inteiro positivo que não seja um quadrado perfeito, foi matematicamente provado que a equação de Pell possui **infinitas soluções não triviais**. Além disso, dentre essas infinitas soluções, a menor solução onde tanto $x$ quanto $y$ são inteiros positivos é chamada de **solução fundamental** (fundamental solution), e uma vez que esta é encontrada, todas as outras soluções podem ser facilmente geradas por meio de operações algébricas.

## 4. A Profunda Conexão entre Frações Contínuas e a [Equação de Pell](https://kenji.blog/p/pell-equation/)

A ferramenta mais poderosa e padrão para encontrar eficientemente a solução fundamental é a **fração contínua** (Continued fraction). Como o número irracional $\sqrt{n}$ não pode ser representado por uma fração finita, ele pode ser expressado belamente como uma fração contínua regular periódica e infinitamente contínua.

$$ \sqrt{n} = [a_0; \overline{a_1, a_2, \dots, a_k, 2a_0}] $$

Aqui, $a_0$ é a parte inteira de $\sqrt{n}$ (isto é, $\lfloor \sqrt{n} \rfloor$), e a parte sob a linha superior representa a porção periódica da fração contínua. Seja $m$ o comprimento deste período.

O número racional $\frac{p_i}{q_i}$ obtido ao truncar a fração contínua em um certo termo é chamado de **convergente** (convergent). Os convergentes fornecem as melhores aproximações racionais para o número irracional $\sqrt{n}$. Surpreendentemente, a solução fundamental $(x_1, y_1)$ da equação de Pell é diretamente obtida a partir do numerador $p$ e denominador $q$ de um convergente específico na expansão em fração contínua de $\sqrt{n}$. Especificamente, é determinada pelo comprimento do período $m$ da seguinte forma:

- Se o período $m$ é par: A solução fundamental é $(p_{m-1}, q_{m-1})$.
- Se o período $m$ é ímpar: A solução fundamental é $(p_{2m-1}, q_{2m-1})$.

## 5. Encontrando a Solução Fundamental: Uma Explicação Detalhada do Algoritmo

Os convergentes $\frac{p_i}{q_i}$ podem ser calculados muito rapidamente num computador usando as seguintes relações de recorrência.

$$ p_i = a_i p_{i-1} + p_{i-2} $$
$$ q_i = a_i q_{i-1} + q_{i-2} $$

As condições iniciais são configuradas da seguinte forma para permitir que o algoritmo comece sem problemas:
- $p_{-1} = 1, \quad p_{-2} = 0$
- $q_{-1} = 0, \quad q_{-2} = 1$

Cada termo $a_i$ da fração contínua também pode ser encontrado sequencialmente usando apenas operações aritméticas com inteiros. Isto permite cálculos inteiros precisos que eliminam completamente os erros de aritmética de ponto flutuante.

Para visualizar a série de processos na busca por uma solução, preparamos o seguinte diagrama de transição de estado.

```mermaid
flowchart TD
    Start["Início: Inserir inteiro n"] --> CheckSquare["Determinar se n é um quadrado perfeito"]
    CheckSquare --|"Sim"| Trivial["Apenas soluções triviais existem (Fim)"] --> End["Fim"]
    CheckSquare --|"Não"| InitContFrac["Inicializar recorrência para fração contínua"]
    InitContFrac --> CalcNext["Calcular o próximo termo a_i e convergente (p_i, q_i)"]
    CalcNext --> CheckEq["Condição: Avaliar p_i^2 - n * q_i^2 == 1"]
    CheckEq --|"Falso"| CalcNext
    CheckEq --|"Verdadeiro"| Found["Solução fundamental encontrada (x_1, y_1) = (p_i, q_i)"] --> End
```

## 6. Exemplo Específico: Expansão em Fração Contínua e Solução Fundamental para n = 7

Em vez de apenas teoria abstrata, vamos seguir os cálculos para o caso específico de $n = 7$. A equação de Pell se torna $x^2 - 7y^2 = 1$.

Primeiro, a parte inteira de $\sqrt{7}$ é $a_0 = 2$. Repetindo a operação de tomar o recíproco da parte decimal restante e extrair a parte inteira, a expansão em fração contínua de $\sqrt{7}$ é encontrada como a seguir:

$$ \sqrt{7} = [2; \overline{1, 1, 1, 4}] $$

O período é $m = 4$, que é par. Portanto, a solução fundamental deve ser obtida a partir do convergente $\frac{p_3}{q_3}$. Vamos calcular os convergentes em ordem usando as relações de recorrência.

- $i=0$: Quando $a_0=2$, $\frac{p_0}{q_0} = \frac{2}{1}$
- $i=1$: Quando $a_1=1$, $p_1 = 1 \times 2 + 1 = 3$, $q_1 = 1 \times 1 + 0 = 1$. Assim, $\frac{p_1}{q_1} = \frac{3}{1}$
- $i=2$: Quando $a_2=1$, $p_2 = 1 \times 3 + 2 = 5$, $q_2 = 1 \times 1 + 1 = 2$. Assim, $\frac{p_2}{q_2} = \frac{5}{2}$
- $i=3$: Quando $a_3=1$, $p_3 = 1 \times 5 + 3 = 8$, $q_3 = 1 \times 2 + 1 = 3$. Assim, $\frac{p_3}{q_3} = \frac{8}{3}$

Vamos verificar substituindo o $(p_3, q_3) = (8, 3)$ obtido na equação.
$8^2 - 7 \times 3^2 = 64 - 7 \times 9 = 64 - 63 = 1$.
Ele satisfaz perfeitamente a condição, logo essa se torna a solução fundamental $(x_1, y_1) = (8, 3)$ para $n = 7$.

## 7. Gerando Soluções Infinitas: Uma Abordagem Utilizando Matrizes e Recorrências

Uma vez que ao menos uma solução fundamental $(x_1, y_1)$ é encontrada, todas as outras soluções de inteiros positivos $(x_k, y_k)$ podem ser geradas infinitamente a partir da seguinte relação algébrica.

$$ x_k + y_k \sqrt{n} = (x_1 + y_1 \sqrt{n})^k \quad \text{for} \quad k = 1, 2, 3, \dots $$

Ao expandir esta expressão e comparar a parte racional e a parte irracional (o coeficiente de $\sqrt{n}$), obtemos uma relação de recorrência para calcular a próxima solução $(x_{k+1}, y_{k+1})$ a partir da solução anterior $(x_k, y_k)$. Expressar isso no formato de matriz resulta em uma forma muito elegante.

$$
\begin{pmatrix} x_{k+1} \\ y_{k+1} \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix} \begin{pmatrix} x_k \\ y_k \end{pmatrix}
$$

Qualquer $k$-ésima solução também pode ser diretamente calculada usando a exponenciação de matrizes da seguinte forma:

$$
\begin{pmatrix} x_k \\ y_k \end{pmatrix} = \begin{pmatrix} x_1 & n y_1 \\ y_1 & x_1 \end{pmatrix}^{k-1} \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}
$$

Esta propriedade sugere fortemente que as soluções para a equação de Pell não são meramente sequências de números, mas possuem uma estrutura algébrica (uma estrutura de grupo).

## 8. A Identidade de Brahmagupta e o Método Chakravala

Na matemática indiana antiga, um papel central na solução da equação de Pell foi desempenhado pela **identidade de Brahmagupta**. Esta identidade assume a seguinte forma:

$$ (x_1^2 - ny_1^2)(x_2^2 - ny_2^2) = (x_1 x_2 + n y_1 y_2)^2 - n(x_1 y_2 + x_2 y_1)^2 $$

O aspecto brilhante desta identidade é que, ao combinar uma solução $(x_1, y_1)$ para $x^2 - ny^2 = k_1$ e uma solução $(x_2, y_2)$ para $x^2 - ny^2 = k_2$, pode-se sintetizar diretamente uma nova solução $(X, Y)$ tal que $X^2 - nY^2 = k_1 k_2$.

Os matemáticos indianos usaram magistralmente esta poderosa identidade para juntar soluções com pequenos erros, uma após a outra, desenvolvendo, em última análise, o **método Chakravala** para chegar a uma solução com um erro de $1$, isto é, uma solução para a equação de Pell. Este é um marco monumental na história matemática humana, possuindo eficiência igual ou superior à expansão em fração contínua.

## 9. Exemplo de Implementação em Python e Explicação

Agora que entendemos perfeitamente a fundamentação teórica, vamos realmente escrever um programa. O script Python a seguir executa a recorrência para a fração contínua de um $n$ dado e procura pela solução fundamental da equação de Pell. Pelo fato de processar totalmente com aritmética de inteiros, sem utilizar números de ponto flutuante, não há preocupação quanto à perda de precisão.

```python
import math

def is_square(n):
    """
    Uma função para determinar rapidamente se um número n dado é um quadrado perfeito.
    """
    s = math.isqrt(n)
    return s * s == n

def solve_pell(n):
    """
    Calcula a solução fundamental da equação de Pell x^2 - n * y^2 = 1 usando o método de frações contínuas.
    Retorna: Uma tupla da solução fundamental (x, y). Retorna None para quadrados perfeitos.
    """
    if is_square(n):
        return None  # Não tem soluções não triviais para quadrados perfeitos

    # Inicialização para cálculos de frações contínuas
    m = 0
    d = 1
    a0 = math.isqrt(n)
    a = a0
    
    # Configuração inicial para os convergentes (p_{-1}=1, p_{-2}=0, q_{-1}=0, q_{-2}=1)
    num1, num2 = 1, 0  # p_{i-1}, p_{i-2}
    den1, den2 = 0, 1  # q_{i-1}, q_{i-2}
    
    # Primeiro convergente (p_0, q_0)
    num = a0
    den = 1
    
    # Repetir até que a condição x^2 - n*y^2 == 1 seja satisfeita
    while num * num - n * den * den != 1:
        # Calcular o próximo termo a_i da fração contínua
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        
        # Atualizar convergentes p_i, q_i
        num2 = num1
        num1 = num
        den2 = den1
        den1 = den
        
        num = a * num1 + num2
        den = a * den1 + den2

    return num, den

# Exemplo de uso: Quando n = 7
n = 7
solution = solve_pell(n)
if solution:
    x, y = solution
    print(f"Solução fundamental para n={n}: x={x}, y={y}")
    print(f"Verificação: {x}^2 - {n}*{y}^2 = {x**2 - n * y**2}")
```

Quando este código é executado, a solução fundamental $(x, y) = (8, 3)$ é exibida instantaneamente, exatamente como calculamos à mão anteriormente. Se você tentar um valor maior para $n$, como $61$, poderá verificar que a solução se torna números enormes ($x = 1766319049, y = 226153980$), permitindo que você sinta verdadeiramente a profundidade da equação de Pell.

## 10. Ponte para a Teoria Algébrica dos Números: Relação com o Teorema das Unidades de Dirichlet

A equação de Pell não é meramente um quebra-cabeça de inteiros. Na matemática moderna, ela se posiciona como uma porta de entrada vital para a teoria dos **corpos quadráticos reais** $\mathbb{Q}(\sqrt{n})$.

As soluções da equação de Pell correspondem intimamente às **unidades** (elementos cujos inversos também são inteiros algébricos) no anel de inteiros algébricos de um corpo quadrático real. A solução fundamental corresponde à **unidade fundamental** que gera este grupo de unidades, e o fato de que existem infinitas soluções para a equação de Pell pode ser visto como um caso especial de um teorema mais avançado, o **teorema das unidades de Dirichlet**. Compreender as propriedades da unidade fundamental é extremamente crucial para pesquisar profundamente fórmulas para o número de classes de corpos quadráticos e a estrutura das classes de ideais.

## 11. Conclusão

Neste artigo, exploramos detalhadamente uma das mais fascinantes equações diofantinas, a **equação de Pell**, de seus fundamentos às suas aplicações. Explicamos o fato surpreendente de que sempre há infinitas soluções não triviais para qualquer $n$ não quadrado, um algoritmo eficiente para busca de soluções usando expansões em frações contínuas, e o dinamismo de sintetizar novas soluções, uma após a outra, a partir da solução fundamental gerada usando matrizes.

O fato de que problemas clássicos considerados por Fermat e Brahmagupta há centenas de anos podem ser belamente implementados como algoritmos modernos de computador, e, além disso, se conectarem à teoria algébrica avançada dos números, evoca um romance matemático profundo e atemporal. Esperamos que você aproveite esta oportunidade para usar o código Python e explorar o mundo da equação de Pell para vários valores de $n$ e entrar em contato com as propriedades profundas dos números.

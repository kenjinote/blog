---
title: "Séries de Taylor e Maclaurin: A Magia de Aproximar Funções Complexas com Polinômios"
description: "Uma explicação detalhada das séries de Taylor e Maclaurin, os segredos do cálculo, dos significados intuitivos às derivações matemáticas e aplicações em programação e física."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Cálculo"
  - "Série de Taylor"
  - "Série de Maclaurin"
  - "Aproximação de Funções"
---

## Introdução

Um **polinômio de Taylor** aproxima uma função perto de um ponto, fazendo coincidir o valor da função e um número finito de derivadas nesse ponto. A soma infinita construída com esses coeficientes é a **série de Taylor**; quando o centro é zero, ela é chamada de **série de Maclaurin**. A convergência da série e a igualdade de sua soma com a função original precisam ser verificadas separadamente.

Usando as funções exponencial e trigonométricas como exemplos, explicaremos como determinar os coeficientes, sob quais condições as igualdades são válidas e como limitar o erro de truncamento. Ao final, apresentamos um exemplo didático em Python para aproximar $\sin x$ perto de zero.

## Por que Aproximar Funções com Polinômios?

Para começar, por que é necessário representar uma função como um polinômio ( $a + bx + cx^2 + \dots$ )?

```mermaid
flowchart LR
    A["Função analítica perto do centro"] -->|"Expansão de Taylor no intervalo de convergência"| B["Série de potências"]
    B -->|"Truncar em termos finitos"| C["Aproximação polinomial"]
    C -->|"Apenas aritmética básica"| D["Cálculo computacional de alta velocidade"]
```

Aproximar uma função não linear por um polinômio pode simplificar a avaliação, a derivação e a integração. Depois de fixados os coeficientes, o polinômio pode ser avaliado com adições e multiplicações. O termo de resto e os erros numéricos permitem avaliar onde a aproximação é útil e qual é sua precisão.

## Compreensão Intuitiva da Série de Maclaurin

Primeiro, consideremos a **expansão de Maclaurin**, que aproxima uma função perto de $x=0$.
Suponha que $f$ tenha as derivadas necessárias perto de zero. Escolhemos um grau finito $n$ e determinamos os coeficientes do seguinte polinômio $P_n$:

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Os coeficientes são determinados igualando o valor da função e as derivadas em zero. A condição da segunda derivada abaixo se aplica quando $n\ge2$.

1. **Condição sobre o valor**: $P_n(0)=f(0)$ fornece $c_0=f(0)$. O termo constante iguala o valor da função em zero.
2. **Condição sobre a primeira derivada**: $P_n'(0)=f'(0)$ fornece $c_1=f'(0)$. O polinômio $P_1(x)=f(0)+f'(0)x$ é a aproximação pela reta tangente em zero.
3. **Condição sobre a segunda derivada**: Exigimos $P_n''(0)=f''(0)$. Como $P_n''(0)=2c_2$, obtemos $c_2=f''(0)/2!$. Na presença de termos de grau superior, a derivada completa $P_n''(x)$ não é, em geral, a constante $2c_2$.
4. **Condição geral**: Para $k\le n$, impor $P_n^{(k)}(0)=f^{(k)}(0)$ determina $c_k=f^{(k)}(0)/k!$. O resto descrito adiante limita o erro perto do centro.

## Fórmula e Derivação da Série de Maclaurin

Se $f$ é infinitamente diferenciável, esses coeficientes definem sua série de Maclaurin. Entretanto, para escrever uma igualdade com $f(x)$ como as seguintes, a série precisa convergir para $f(x)$ no ponto considerado. Isso ocorre em uma vizinhança adequada de zero quando $f$ é analítica ali. Ser infinitamente diferenciável não é suficiente.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Escrito usando a notação sigma, fica assim:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Aqui, $f^{(n)}(0)$ é o valor obtido ao diferenciar a função $f(x)$ $n$ vezes e substituir $x=0$, e $n!$ representa o fatorial de $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Séries de Maclaurin de Funções Típicas

As séries da exponencial, do seno e do cosseno apresentadas a seguir convergem para as respectivas funções para todo $x$ real. Os argumentos trigonométricos são medidos em radianos.

### 1. Função exponencial $e^x$

A função exponencial $f(x)=e^x$ continua sendo $e^x$ ao ser derivada qualquer número de vezes. Assim, todas as suas derivadas em zero valem $1$ ($f^{(n)}(0)=1$).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Funções trigonométricas $\sin x$ e $\cos x$

Ao derivar $\sin x$ repetidamente, as derivadas seguem o ciclo $\cos x, -\sin x, -\cos x, \sin x, \dots$. Em $x=0$, apenas as derivadas de ordem ímpar são diferentes de zero; as de ordem par valem $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

Da mesma forma, para $\cos x$, apenas os termos de ordem par permanecem.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Extensão para a Série de Taylor

Ao mover o centro de zero para $a$, obtemos a série de Taylor. Se $f$ é analítica perto de $a$, a igualdade abaixo vale onde a série representa a função original. Aproximações que pressupõem apenas um número finito de derivadas são tratadas com um polinômio de Taylor finito e seu resto, como veremos adiante.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

Esta fórmula demonstra seu poder quando você deseja prever o valor de uma função em um local ligeiramente afastado de $x=a$ ( $x = a + \Delta x$ ).

## Aplicações das Séries de Taylor

### Aproximação Linear na Física

Na física, aproximações lineares por polinômios de Taylor são frequentes. Para um pêndulo, medimos o ângulo $\theta$ em radianos e supomos $|\theta|\ll1$. Podemos então usar a aproximação de primeiro grau do seno:

$$ \sin \theta \approx \theta \quad (\text{quando } \theta \text{ é suficientemente pequeno}) $$

Essa aproximação lineariza a equação do pêndulo e fornece um período independente da amplitude dentro da aproximação de pequena amplitude. O período real de um pêndulo simples depende da amplitude; a mesma aproximação não pode ser aplicada a oscilações grandes.

### Programação e Computação Numérica

A avaliação numérica de funções usa vários métodos, incluindo aproximações polinomiais. O módulo `math` do CPython é composto principalmente por interfaces para a biblioteca matemática de C da plataforma; os algoritmos dependem dessa implementação. O exemplo didático a seguir soma poucos termos perto de zero, por exemplo para $|x|\le1$, e não reproduz a implementação interna da biblioteca padrão.

```python
import math

def approx_sin(x, terms=10):
    """
    Exemplo didático de soma finita de Maclaurin para sin(x) perto de zero
    x: Ângulo em radianos
    terms: Número de termos somados (inteiro positivo; 10 neste exemplo)
    """
    result = 0.0
    for n in range(terms):
        # Calcular cada termo: (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Teste: x = 1.0 radiano (aprox 57.3 graus)
x_val = 1.0
print(f"Valor aproximado: {approx_sin(x_val)}")
print(f"Valor de math.sin (para comparação): {math.sin(x_val)}")
```

## Raio de Convergência e Teorema de Taylor

O **raio de convergência** $R$ é um número que indica a distância ao centro $a$ dentro da qual uma série de potências converge, $|x-a|<R$; não é o nome do intervalo. Também podem ocorrer $R=0$ e $R=\infty$. Os extremos $|x-a|=R$ precisam ser examinados separadamente. Por exemplo, a série de Maclaurin de $\ln(1+x)$ tem raio 1 e é igual à função para $-1<x\le1$ real. Ela converge condicionalmente em $x=1$ e diverge em $x=-1$.

Para uma aproximação finita, suponha que $f$ seja de classe $C^{n+1}$ no intervalo que liga $a$ a $x$. O teorema de Taylor fornece:

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Aqui, $\xi$ está entre $a$ e $x$. Se $|f^{(n+1)}|\le M$ no intervalo, então $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. Para estabelecer a igualdade entre uma função e sua série de Taylor infinita, pode-se verificar que esse resto tende a zero quando $n\to\infty$.

O código anterior soma 10 termos, até $x^{19}$. Como o coeficiente de grau 20 do seno é zero, o teorema de Taylor limita o erro de truncamento em $x=1$ por $1/21!$, aproximadamente $1.96\times10^{-20}$. Esse limite se refere à soma finita calculada exatamente nos números reais; o erro de arredondamento das operações de ponto flutuante do Python é separado. A saída de `math.sin` também é um valor de ponto flutuante para comparação, não o valor matemático exato.

### Uma função suave que não é representada por sua série de Taylor

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

Essa função é infinitamente diferenciável e todas as suas derivadas em zero são nulas. Portanto, sua série de Taylor em zero é identicamente zero e converge para todo $x$. No entanto, para $x>0$, temos $g(x)>0$, de modo que a soma da série não coincide com a função original. O exemplo distingue a convergência de uma série da igualdade de sua soma com a função.

## Conclusão

Os polinômios de Taylor fornecem aproximações locais, e os termos de resto limitam seus erros. Ao usar uma série de Taylor como igualdade, é preciso verificar o intervalo de convergência e se a soma coincide com a função original. Essas distinções ajudam a determinar a precisão e o campo de aplicação das aproximações na física e na computação numérica.

## Referências

- [NIST DLMF §1.4(vi): Teorema de Taylor e restos para uma variável real](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A: Basic Analysis §§4.3 e 5.4 (analiticidade, suavidade, série logarítmica e exemplo não analítico)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24: Aproximação do pêndulo para pequenas amplitudes e dependência da amplitude](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math: Funções matemáticas e detalhes da implementação do CPython](https://docs.python.org/3.12/library/math.html)

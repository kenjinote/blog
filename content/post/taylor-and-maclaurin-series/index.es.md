---
title: "Series de Taylor y Maclaurin: La magia de aproximar funciones complejas con polinomios"
description: "Una explicación detallada de las series de Taylor y Maclaurin, los secretos del cálculo, desde los significados intuitivos hasta las derivaciones matemáticas y sus aplicaciones en programación y física."
slug: "taylor-and-maclaurin-series"
date: "2026-09-20T14:30:00+09:00"
lastmod: 2026-10-24
image: "eyecatch.jpg"
categories: ["mathematics"]
tags:
  - "Cálculo"
  - "Serie de Taylor"
  - "Serie de Maclaurin"
  - "Aproximación de funciones"
---

## Introducción

Un **polinomio de Taylor** aproxima una función cerca de un punto haciendo coincidir su valor y un número finito de derivadas en ese punto. La suma infinita construida con estos coeficientes es la **serie de Taylor**; si el centro es cero, se denomina **serie de Maclaurin**. La convergencia de la serie y la igualdad de su suma con la función original deben comprobarse por separado.

Con ejemplos de funciones exponenciales y trigonométricas, explicaremos cómo determinar los coeficientes, bajo qué condiciones son válidas las igualdades y cómo acotar el error al truncar la serie. Al final se incluye un ejemplo didáctico en Python para aproximar $\sin x$ cerca de cero.

## ¿Por qué aproximar funciones con polinomios?

Para empezar, ¿por qué es necesario representar una función como un polinomio ( $a + bx + cx^2 + \dots$ )?

```mermaid
flowchart LR
    A["Función analítica cerca del centro"] -->|"Desarrollo de Taylor dentro de su intervalo de convergencia"| B["Serie de potencias"]
    B -->|"Truncar en términos finitos"| C["Aproximación polinómica"]
    C -->|"Solo aritmética básica"| D["Cálculo computacional de alta velocidad"]
```

Aproximar una función no lineal mediante un polinomio puede simplificar su evaluación, derivación e integración. Una vez determinados los coeficientes, el polinomio se evalúa con sumas y multiplicaciones. El resto y los errores numéricos permiten juzgar dónde resulta útil la aproximación y con qué precisión.

## Comprensión intuitiva de la serie de Maclaurin

Consideremos primero el **desarrollo de Maclaurin**, que aproxima una función cerca de $x=0$.
Supongamos que $f$ tiene las derivadas necesarias cerca de cero. Elegimos un grado finito $n$ y determinamos los coeficientes del siguiente polinomio $P_n$:

$$ P_n(x) = c_0 + c_1 x + c_2 x^2 + \dots + c_n x^n $$

Los coeficientes se determinan igualando el valor y las derivadas en cero. La condición de segunda derivada que sigue corresponde al caso $n\ge2$.

1. **Condición sobre el valor**: $P_n(0)=f(0)$ da $c_0=f(0)$. El término constante iguala el valor de la función en cero.
2. **Condición sobre la primera derivada**: $P_n'(0)=f'(0)$ da $c_1=f'(0)$. El polinomio $P_1(x)=f(0)+f'(0)x$ es la aproximación por la recta tangente en cero.
3. **Condición sobre la segunda derivada**: Exigimos $P_n''(0)=f''(0)$. Como $P_n''(0)=2c_2$, resulta $c_2=f''(0)/2!$. Si hay términos de grado superior, la derivada completa $P_n''(x)$ no es, en general, la constante $2c_2$.
4. **Condición general**: Para $k\le n$, imponer $P_n^{(k)}(0)=f^{(k)}(0)$ determina $c_k=f^{(k)}(0)/k!$. El resto descrito más adelante acota el error cerca del centro.

## Fórmula y derivación de la serie de Maclaurin

Si $f$ es infinitamente derivable, estos coeficientes permiten construir su serie de Maclaurin. Sin embargo, para escribir una igualdad con $f(x)$ como las siguientes, la serie debe converger a $f(x)$ en el punto considerado. Esto ocurre en un entorno adecuado de cero si $f$ es analítica allí. Ser infinitamente derivable no basta.

$$ f(x) = f(0) + f'(0)x + \frac{f''(0)}{2!}x^2 + \frac{f^{(3)}(0)}{3!}x^3 + \dots $$

Escrito usando la notación sigma, se ve así:

$$ f(x) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!} x^n $$

Aquí, $f^{(n)}(0)$ es el valor obtenido al diferenciar la función $f(x)$ $n$ veces y sustituir $x=0$, y $n!$ representa el factorial de $n$ ( $n \times (n-1) \times \dots \times 1$ ).

## Series de Maclaurin de funciones típicas

Las siguientes series de la función exponencial, el seno y el coseno convergen a sus respectivas funciones para todo $x$ real. Los argumentos trigonométricos se expresan en radianes.

### 1. Función exponencial $e^x$

La función exponencial $f(x)=e^x$ sigue siendo $e^x$ al derivarla cualquier número de veces. Por tanto, todas sus derivadas en cero valen $1$ ($f^{(n)}(0)=1$).

$$ e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots = \sum_{n=0}^{\infty} \frac{x^n}{n!} $$

### 2. Funciones trigonométricas $\sin x$ y $\cos x$

Al derivar repetidamente $\sin x$, las derivadas siguen el ciclo $\cos x, -\sin x, -\cos x, \sin x, \dots$. En $x=0$, solo las derivadas de orden impar son distintas de cero; las de orden par valen $0$.

$$ \sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1} $$

De manera similar, para $\cos x$, solo quedan los términos de orden par.

$$ \cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n} $$

## Extensión a la serie de Taylor

Al trasladar el centro de cero a $a$ se obtiene la serie de Taylor. Si $f$ es analítica cerca de $a$, la siguiente igualdad se cumple donde la serie representa la función. Las aproximaciones que solo suponen un número finito de derivadas se tratan con un polinomio de Taylor finito y su resto, como veremos más adelante.

$$ f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \dots = \sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x-a)^n $$

Esta fórmula demuestra su poder cuando desea predecir el valor de una función en un lugar ligeramente alejado de $x=a$ ( $x = a + \Delta x$ ).

## Aplicaciones de las series de Taylor

### Aproximación lineal en física

En física se usan con frecuencia aproximaciones lineales mediante polinomios de Taylor. Para un péndulo, expresamos el ángulo $\theta$ en radianes y suponemos $|\theta|\ll1$. Entonces se utiliza la aproximación de primer grado del seno:

$$ \sin \theta \approx \theta \quad (\text{cuando } \theta \text{ es suficientemente pequeño}) $$

Esta aproximación linealiza la ecuación del péndulo y da un período independiente de la amplitud dentro de la aproximación de pequeña amplitud. El período real de un péndulo simple depende de la amplitud; no se puede aplicar la misma aproximación a oscilaciones grandes.

### Programación y cálculo numérico

La evaluación numérica de funciones utiliza diversos métodos, entre ellos aproximaciones polinómicas. El módulo `math` de CPython recurre principalmente a la biblioteca matemática de C de la plataforma; los algoritmos concretos dependen de esa implementación. El siguiente ejemplo didáctico suma pocos términos cerca de cero, por ejemplo para $|x|\le1$, y no reproduce la implementación interna de la biblioteca estándar.

```python
import math

def approx_sin(x, terms=10):
    """
    Ejemplo didáctico de suma finita de Maclaurin para sin(x) cerca de cero
    x: Ángulo en radianes
    terms: Número de términos que se suman (entero positivo; 10 en el ejemplo)
    """
    result = 0.0
    for n in range(terms):
        # Calcular cada término: (-1)^n * x^(2n+1) / (2n+1)!
        sign = (-1) ** n
        numerator = x ** (2 * n + 1)
        denominator = math.factorial(2 * n + 1)
        result += sign * (numerator / denominator)
    return result

# Prueba: x = 1.0 radián (aprox 57.3 grados)
x_val = 1.0
print(f"Valor aproximado: {approx_sin(x_val)}")
print(f"Valor de math.sin (para comparar): {math.sin(x_val)}")
```

## Radio de convergencia y Teorema de Taylor

El **radio de convergencia** $R$ es un número que expresa la distancia al centro $a$ dentro de la cual converge una serie de potencias, $|x-a|<R$; no es el nombre del intervalo. También pueden darse $R=0$ y $R=\infty$. Los extremos $|x-a|=R$ deben estudiarse por separado. Por ejemplo, la serie de Maclaurin de $\ln(1+x)$ tiene radio 1 y es igual a la función para $-1<x\le1$ real. En $x=1$ converge condicionalmente y en $x=-1$ diverge.

Para una aproximación finita, supongamos que $f$ es de clase $C^{n+1}$ en el intervalo que une $a$ con $x$. El teorema de Taylor da:

$$
f(x)=P_{n,a}(x)+R_n(x),\qquad P_{n,a}(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
$$

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1}
$$

Aquí $\xi$ está entre $a$ y $x$. Si $|f^{(n+1)}|\le M$ en el intervalo, entonces $|R_n(x)|\le M|x-a|^{n+1}/(n+1)!$. Para demostrar que una función es igual a su serie de Taylor infinita, se puede comprobar que este resto tiende a cero cuando $n\to\infty$.

El código anterior suma 10 términos, hasta $x^{19}$. Como el coeficiente de grado 20 del seno es cero, el teorema de Taylor acota el error de truncamiento en $x=1$ por $1/21!$, aproximadamente $1.96\times10^{-20}$. Esta cota corresponde a la suma finita calculada exactamente en los números reales; el error de redondeo de las operaciones de coma flotante de Python es distinto. La salida de `math.sin` también es un valor de coma flotante para comparar, no el valor matemático exacto.

### Una función suave que no coincide con su serie de Taylor

$$
g(x)=\begin{cases}e^{-1/x},&x>0,\\0,&x\le0.\end{cases}
$$

Esta función es infinitamente derivable y todas sus derivadas en cero son nulas. Por tanto, su serie de Taylor en cero es idénticamente cero y converge para todo $x$. Sin embargo, para $x>0$ se tiene $g(x)>0$, de modo que la suma de la serie no coincide con la función original. El ejemplo distingue la convergencia de una serie de la igualdad de su suma con la función.

## Conclusión

Los polinomios de Taylor proporcionan aproximaciones locales y los restos acotan sus errores. Al utilizar una serie de Taylor como igualdad, hay que comprobar su intervalo de convergencia y si su suma coincide con la función original. Estas distinciones ayudan a determinar la precisión y el ámbito de aplicación de las aproximaciones en física y cálculo numérico.

## Referencias

- [NIST DLMF §1.4(vi): Teorema de Taylor y restos para una variable real](https://dlmf.nist.gov/1.4#vi)
- [MIT 18.100A: Basic Analysis §§4.3 y 5.4 (analiticidad, suavidad, serie logarítmica y ejemplo no analítico)](https://ocw.mit.edu/courses/18-100a-real-analysis-fall-2020/mit18_100af20_basic_analysis.pdf)
- [MIT 16.07 Lecture 24: Aproximación del péndulo de pequeña amplitud y dependencia de la amplitud](https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/c0c881f96f4ff4e21f082c88e8b015d6_MIT16_07F09_Lec24.pdf)
- [Python 3.12 math: Funciones matemáticas y detalles de implementación de CPython](https://docs.python.org/3.12/library/math.html)

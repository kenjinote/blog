---
title: "Teorema de los números primos (Prime Number Theorem) - La ley que establece que la distribución de los números primos se aproxima a una función logarítmica"
description: "Una explicación profunda sobre el Teorema de los números primos (Prime Number Theorem), un hito matemático sobre la regularidad de la aparición de los números primos. Desde la función contadora de números primos hasta su relación con la hipótesis de Riemann."
slug: "prime-number-theorem"
date: 2026-09-14T13:11:00+09:00
image: "eyecatch.jpg"
categories: ["mathematics", "algorithms"]
tags:
  - "Teorema de los números primos"
  - "Hipótesis de Riemann"
  - "Números primos"
  - "Matemáticas"
  - "Teoría analítica de números"
---

## ¿Qué es el teorema de los números primos?

Uno de los resultados más hermosos en el campo de las matemáticas es el **Teorema de los números primos** ([Prime Number Theorem](https://kenji.blog/es/p/prime-number-theorem/), PNT). Demuestra que los números primos, que a primera vista parecen aparecer de manera irregular y aleatoria, poseen una regularidad sorprendentemente suave cuando se observan macroscópicamente.

Específicamente, si definimos la "cantidad de números primos menores o iguales a un número real $x$" como $\pi(x)$ (la función contadora de números primos), el teorema establece que cuando $x$ es muy grande, $\pi(x)$ se aproxima asintóticamente a $x / \ln(x)$.

$$ \lim_{x \to \infty} \frac{\pi(x)}{x / \ln(x)} = 1 $$

Aquí, $\ln(x)$ representa el logaritmo natural (de base $e$). Este teorema enuncia el sorprendente hecho de que la distribución de los números primos está profundamente conectada con el logaritmo natural.

### Función contadora de números primos $\pi(x)$

La función contadora de números primos $\pi(x)$ es una función que cuenta la cantidad de números primos menores o iguales a $x$. Por ejemplo:

- $\pi(10) = 4$ (2, 3, 5, 7)
- $\pi(100) = 25$
- $\pi(1000) = 168$

A medida que los valores se hacen más grandes, encontrar números primos se vuelve más difícil, y el intervalo entre sus apariciones se amplía gradualmente. Sin embargo, su "densidad" general se vuelve predecible.

```mermaid
graph TD;
    A["Número natural x"] -->|"Contar números primos"| B["Función contadora de números primos π(x)"];
    B -->|"Aproximar"| C["x / ln("x")"];
    C -->|"Aumentar la precisión"| D["Integral logarítmica Li("x")"];
```

## Contexto histórico: De la conjetura de Gauss a la demostración

La historia del teorema de los números primos se remonta a finales del siglo XVIII. El genio matemático [Carl Friedrich Gauss](https://kenji.blog/es/p/gauss/), con apenas 15 años, se dio cuenta al observar tablas de números primos que la frecuencia de su aparición estaba relacionada con funciones logarítmicas. Por la misma época, [Adrien-Marie Legendre](https://kenji.blog/es/p/legendre/) también formuló de manera independiente una conjetura similar.

Sin embargo, no lograron demostrar esto rigurosamente.

El gran avance en la demostración llegó en 1859 con el revolucionario artículo de [Bernhard Riemann](https://kenji.blog/es/p/riemann/) "Sobre el número de primos menores que una magnitud dada". [Riemann](https://kenji.blog/es/p/riemann/) presentó un enfoque completamente nuevo, utilizando una función compleja, la **función zeta** $\zeta(s)$, para transformar el problema de la distribución de los números primos en un problema sobre el plano complejo.

$$ \zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ primo}} \left(1 - \frac{1}{p^s}\right)^{-1} $$

Esta fórmula del producto de Euler (Euler product formula) es una relación sumamente importante que conecta una función sobre la suma de todos los números naturales (lado izquierdo) con un producto infinito exclusivamente sobre números primos (lado derecho).

Posteriormente, en 1896, Jacques Hadamard y Charles de la Vallée Poussin, de forma independiente y basándose en las ideas de [Riemann](https://kenji.blog/es/p/riemann/), completaron la demostración del teorema de los números primos. La clave de sus demostraciones fue mostrar que "la función zeta de [Riemann](https://kenji.blog/es/p/riemann/) $\zeta(s)$ no tiene ceros en la recta $\operatorname{Re}(s) = 1$ del plano complejo".

## Una aproximación de mayor precisión: Integral logarítmica $\operatorname{Li}(x)$

Aunque $x / \ln(x)$ expresa el teorema de los números primos de manera simple, para aproximar la cantidad real de números primos $\pi(x)$, la **integral logarítmica** (Logarithmic Integral, $\operatorname{Li}(x)$) introducida por Gauss es mucho mejor.

La integral logarítmica se define de la siguiente manera:

$$ \operatorname{Li}(x) = \int_{2}^{x} \frac{dt}{\ln(dt)} $$

El teorema de los números primos también se puede reescribir como $\pi(x) \sim \operatorname{Li}(x)$.

$$ \lim_{x \to \infty} \frac{\pi(x)}{\operatorname{Li}(x)} = 1 $$

De hecho, cuando $x = 10^{10}$:
- $\pi(10^{10}) = 455,052,511$
- $10^{10} / \ln(10^{10}) \approx 434,294,481$ (error de aproximadamente 4.5%)
- $\operatorname{Li}(10^{10}) \approx 455,055,614$ (error de solo 3103)

Podemos ver lo excelente que es la aproximación dada por la integral logarítmica.

## Profunda relación con la hipótesis de [Riemann](https://kenji.blog/es/p/riemann/)

Inseparablemente ligado al teorema de los números primos está la **Hipótesis de [Riemann](https://kenji.blog/es/p/riemann/)** ([Riemann](https://kenji.blog/es/p/riemann/) Hypothesis), considerada el problema sin resolver más importante de las matemáticas.

La hipótesis de [Riemann](https://kenji.blog/es/p/riemann/) afirma que "todos los ceros no triviales de la función zeta de [Riemann](https://kenji.blog/es/p/riemann/) $\zeta(s)$ se encuentran en la recta con parte real igual a $1/2$ (la línea crítica)".

Si se demuestra que la hipótesis de [Riemann](https://kenji.blog/es/p/riemann/) es correcta, se obtendría la estimación más fuerte posible para el término de error (la diferencia entre $\pi(x)$ y $\operatorname{Li}(x)$) en el teorema de los números primos. Específicamente, se sabe que existe una constante $C$ tal que,

$$ |\pi(x) - \operatorname{Li}(x)| \le C \sqrt{x} \ln(x) $$

se cumple. Esto significa que "los números primos están distribuidos de manera tan extremadamente regular que son indistinguibles de una distribución completamente aleatoria". En otras palabras, el teorema de los números primos habla de la distribución "promedio" de los primos, mientras que la hipótesis de [Riemann](https://kenji.blog/es/p/riemann/) habla de los límites de esa "fluctuación (error)".

## Comprobando el teorema de los números primos en Python

Usemos la programación para observar el comportamiento del teorema de los números primos.

```python
import math
import matplotlib.pyplot as plt

def sieve_of_eratosthenes(limit):
    """
    Enumera los números primos usando la criba de Eratóstenes
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    
    primes = [p for p in range(2, limit) if is_prime[p]]
    return primes

def pi(x, primes):
    """
    Devuelve la cantidad de números primos menores o iguales a x
    """
    import bisect
    return bisect.bisect_right(primes, x)

limit = 1000000
primes = sieve_of_eratosthenes(limit)

x_values = [10**i for i in range(1, 7)]
pi_values = [pi(x, primes) for x in x_values]
approx_values = [x / math.log(x) for x in x_values]

print(f"{'x':<10} | {'π(x)':<10} | {'x / ln(x)':<15} | {'Proporción'}")
print("-" * 55)
for i in range(len(x_values)):
    x = x_values[i]
    pi_x = pi_values[i]
    approx = approx_values[i]
    ratio = pi_x / approx
    print(f"{x:<10} | {pi_x:<10} | {approx:<15.2f} | {ratio:.4f}")
```

Al ejecutar este código, se puede observar cómo a medida que $x$ crece, la proporción $\pi(x) / (x/\ln(x))$ se acerca a 1. Esta es una de las evidencias más contundentes del teorema de los números primos.

## Aplicación en la criptografía moderna

Las propiedades de los números primos no son solo un objeto fascinante en las matemáticas puras, sino también un elemento crucial que sustenta la infraestructura de seguridad de la sociedad moderna.

Los sistemas de criptografía de clave pública, como el cifrado [RSA](https://kenji.blog/es/p/modern-cryptography-public-key-hash-signature/), aprovechan la propiedad de que "es extremadamente difícil factorizar números enteros enormes". El teorema de los números primos garantiza la probabilidad con la que se pueden encontrar "números primos de tamaño adecuado" necesarios para generar claves criptográficas.

Por ejemplo, la probabilidad de que un número impar aleatorio de 1024 bits sea primo se estima en aproximadamente $1 / (1024 \times \ln(2) / 2) \approx 1 / 355$. Esto significa que con unos pocos cientos de pruebas de primalidad, existe una alta probabilidad de encontrar el número primo gigante necesario, y sin el teorema de los números primos, sería imposible construir sistemas criptográficos eficientes.

## Conclusión

El teorema de los números primos es uno de los teoremas más hermosos que encarna el "orden dentro del caos" en las matemáticas. El hecho de que una ley fundamental de la naturaleza como la función logarítmica esté oculta en la distribución aparentemente aleatoria de los números primos sigue fascinando a muchos matemáticos.

Este campo, pionero gracias a genios como Gauss, [Riemann](https://kenji.blog/es/p/riemann/) y Hadamard, sigue estando a la vanguardia de las matemáticas modernas a través de ese gigantesco problema sin resolver que es la hipótesis de [Riemann](https://kenji.blog/es/p/riemann/). El misterio de los números primos es profundo, y la exploración continuará hasta el día en que comprendamos el panorama completo.

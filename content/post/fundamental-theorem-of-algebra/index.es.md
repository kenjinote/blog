---
title: "Teorema Fundamental del Álgebra: Demostración de que una Ecuación de Grado n Siempre Tiene n Raíces Complejas"
description: "Una explicación detallada de la historia, el significado intuitivo y la hermosa demostración del teorema fundamental del álgebra utilizando análisis complejo (teorema de Liouville)."
slug: "fundamental-theorem-of-algebra"
date: "2026-09-24T16:08:36+09:00"
image: "eyecatch.jpg"
categories:
  - "Matemáticas"
tags:
  - "Álgebra"
  - "Análisis complejo"
  - "Demostración"
  - "Teorema"
---

## Introducción: La Búsqueda de Ecuaciones y Raíces

La historia de las matemáticas es también la historia de la búsqueda de números desconocidos. Cuando estudiamos ecuaciones cuadráticas en la escuela secundaria, aprendemos la fórmula cuadrática. Sin embargo, si nos limitamos al ámbito de los números reales, rápidamente notamos que hay ecuaciones con "sin solución real". Por ejemplo, la ecuación $x^2 + 1 = 0$ no tiene solución en el sistema de números reales. Esto se debe a que el cuadrado de cualquier número real $x$ siempre es mayor o igual a $0$, y sumar $1$ nunca puede dar $0$.

Para resolver este problema, se introdujo un número hipotético cuyo cuadrado es $-1$, a saber, la unidad imaginaria $i$. El sistema de números que incluye esta unidad se llama números complejos. Al introducir números complejos, las soluciones de $x^2 + 1 = 0$ se pueden encontrar como $x = \pm i$.

Aquí surge una gran pregunta: "Si expandimos el sistema de números a los números complejos, ¿podemos decir que cualquier ecuación siempre tendrá una solución?" O bien, "¿Alguna vez necesitaremos introducir otro nuevo tipo de número?"

Las matemáticas proporcionan una respuesta muy clara y hermosa a esta pregunta. Ese es el tema de este artículo: el **[Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/)**. Este teorema afirma que "cualquier polinomio de grado $n$ con coeficientes complejos siempre tiene una raíz (solución) dentro de los números complejos". En otras palabras, dentro del vasto océano de los números complejos, la solución a cualquier ecuación siempre existe, garantizando que no hay necesidad de inventar más números nuevos.

En este artículo, explicaremos este **[Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/)** en detalle, comenzando desde sus antecedentes históricos, pasando a un enfoque intuitivo basado en la topología, y finalmente presentando una demostración rigurosa y hermosa usando análisis complejo.

## Antecedentes Históricos del [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/)

El **[Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/)** no se demostró de la noche a la mañana. Muchos grandes matemáticos lucharon por lograr una demostración completa, sin dudar nunca de la verdad del teorema.

En el siglo XVII, matemáticos como [René Descartes](https://kenji.blog/es/p/descartes/) y Albert Girard ya sabían empíricamente que "una ecuación de grado $n$ debería tener $n$ raíces". Sin embargo, dentro del marco matemático de la época, no había un medio riguroso para demostrarlo.

Al entrar en el siglo XVIII, gigantes matemáticos como Jean le Rond d'Alembert y [Leonhard Euler](https://kenji.blog/es/p/euler/) intentaron la demostración. D'Alembert publicó una demostración en 1746, y el teorema a veces se llama "teorema de d'Alembert" en Francia; sin embargo, según los estándares modernos, su demostración carecía de rigor topológico en ciertas áreas. Euler también intentó mostrar que cualquier polinomio con coeficientes reales podía factorizarse en el producto de polinomios lineales y cuadráticos, pero dejó una brecha lógica.

La primera demostración esencialmente completa de este teorema inexpugnable fue dada nada menos que por [Carl Friedrich Gauss](https://kenji.blog/es/p/gauss/). En su disertación doctoral de 1799, señaló las fallas en las demostraciones de los matemáticos precedentes y presentó una demostración basada en la intuición geométrica. Gauss proporcionó cuatro demostraciones diferentes para este teorema a lo largo de su vida, indicando la importancia que le atribuía.

La demostración más estándar y elegante hoy en día se considera la basada en la teoría del análisis complejo, construida por el matemático francés Joseph [Liouville](https://kenji.blog/es/p/liouville/) y otros. En la segunda mitad de este artículo, introduciremos la demostración utilizando el teorema de [Liouville](https://kenji.blog/es/p/liouville/).

## Enunciado Preciso del Teorema

Primero, describamos la afirmación del teorema en términos matemáticamente precisos.

**Teorema ([Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/))**
Para cualquier número natural $n \ge 1$ y coeficientes complejos $a_0, a_1, \dots, a_n$ (donde $a_n \neq 0$), se define un polinomio $P(z)$ de la siguiente manera:

$$
P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0
$$

Entonces, la ecuación $P(z) = 0$ tiene al menos una solución en el plano complejo. Es decir, existe un número complejo $\alpha$ tal que $P(\alpha) = 0$.

A primera vista, solo dice "al menos una", pero al combinarlo con el teorema del resto de polinomios, podemos derivar fácilmente la afirmación más fuerte de que "una ecuación de grado $n$ tiene exactamente $n$ soluciones complejas, contando multiplicidades". (Este punto se explicará en detalle en la sección "Corolario del Teorema" a continuación).

## Comprensión Intuitiva: Enfoque Topológico

Antes de profundizar en la demostración rigurosa, captemos una imagen intuitiva de por qué se cumple este teorema. Aquí, introducimos un enfoque utilizando el concepto de "índice de curva" (Winding number) de la topología.

Representemos un punto en el plano complejo en forma polar como $z = R e^{i\theta}$. Aquí, $R$ es la distancia (radio) desde el origen, y $\theta$ es el ángulo.

Consideremos el polinomio $P(z) = a_n z^n + a_{n-1} z^{n-1} + \dots + a_0$. Si $R$ es muy grande, el valor absoluto de $z$ se vuelve masivo, y el valor del polinomio está casi completamente dominado por el término de mayor grado $a_n z^n$. Es decir, cuando $R$ es lo suficientemente grande, podemos aproximar $P(z) \approx a_n z^n$.

Ahora, supongamos que dejamos que $z$ viaje en un círculo completo a lo largo de un círculo gigante de radio $R$. A medida que $\theta$ cambia de $0$ a $2\pi$, el ángulo de $z^n$ se convierte en $n\theta$, cambiando de $0$ a $2n\pi$. Esto significa que la trayectoria trazada por $P(z)$ se convierte en una curva cerrada que se enrolla alrededor del origen del plano complejo exactamente $n$ veces.

A continuación, imagine el proceso de reducir continuamente este radio $R$. A medida que $R$ disminuye gradualmente, la curva cerrada trazada por $P(z)$ también se deforma continuamente. Eventualmente, cuando $R = 0$, la curva se reduce a un solo punto, $P(0) = a_0$.

La continuidad es la clave aquí. Un bucle grande que inicialmente se enrollaba alrededor del origen $n$ veces finalmente se reduce a un solo punto que no contiene el origen. Topológicamente, es imposible que el bucle se reduzca continuamente a un punto lejos del origen sin cruzar el origen. En otras palabras, en algún lugar del proceso de contracción, esta curva debe pasar por el origen ($0$).

El momento en que la curva pasa por el origen, significa exactamente que existe un $z$ tal que $P(z) = 0$. Esta es la razón intuitiva por la cual siempre debe existir una solución.

```mermaid
flowchart TD
    %% Descripción general del mapeo de curvas
    A["Círculo grande de radio R centrado en el origen"] -->|"Mapeo por el polinomio P("z")"| B["Curva cerrada en el plano complejo"]
    B -->|"Cuando R es suficientemente grande"| C["Curva que se enrolla alrededor del origen n veces"]
    C -->|"Reduciendo continuamente R a 0"| D["La curva también se encoge continuamente hacia el origen"]
    D -->|"Continuidad topológica"| E["Debe pasar por el origen en el camino"]
    E -->|"P("z") = 0"| F["Se demuestra la existencia de una raíz"]
```

## Preparación del Análisis Complejo: Teorema de [Liouville](https://kenji.blog/es/p/liouville/)

Habiendo obtenido una comprensión intuitiva, ahora introduciremos la demostración más hermosa y rigurosa de las matemáticas modernas. Esta demostración utiliza un arma poderosa del análisis complejo: el **Teorema de [Liouville](https://kenji.blog/es/p/liouville/)**.

El análisis complejo es el campo que se ocupa del cálculo de funciones de variables complejas. A diferencia de las funciones de números reales, la diferenciabilidad (holomorfía) de las funciones complejas es una condición extremadamente fuerte; una función compleja que es diferenciable incluso una sola vez tiene la asombrosa propiedad de ser infinitamente diferenciable y capaz de expandirse en una serie de Taylor.

Una función que es diferenciable (holomorfa) sobre todo el plano complejo se llama **función entera**. Los polinomios $P(z)$ y la función exponencial $e^z$ son ejemplos típicos de funciones enteras.

El teorema de [Liouville](https://kenji.blog/es/p/liouville/) es un teorema profundamente poderoso con respecto a estas funciones enteras.

**Teorema (Teorema de [Liouville](https://kenji.blog/es/p/liouville/))**
Toda función entera acotada debe ser una función constante.

Aquí, "acotada" significa que para todos los números complejos $z$, el valor absoluto de la función $|f(z)|$ no excede un cierto número real $M$; es decir, existe un $M$ tal que $|f(z)| \le M$.

En el mundo de los números reales, una función como $f(x) = \sin(x)$ es diferenciable sobre toda la recta numérica y está acotada por $-1 \le \sin(x) \le 1$. No es una función constante. Sin embargo, el teorema de [Liouville](https://kenji.blog/es/p/liouville/) afirma que esto nunca puede suceder en el mundo complejo. Si una función es holomorfa sobre todo el plano complejo y su valor no diverge hacia el infinito, es meramente una constante plana.

## Demostración Rigurosa del [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/)

Demostremos ahora el [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/) usando el teorema de [Liouville](https://kenji.blog/es/p/liouville/). Te sorprenderá la brillantez de esta demostración. Aquí, usamos una demostración por contradicción (reducción al absurdo).

**Demostración**

Supongamos que para cualquier polinomio $P(z) = a_n z^n + \dots + a_1 z + a_0$ de grado $n$ ($n \ge 1$) con coeficientes complejos (donde $a_n \neq 0$), la ecuación $P(z) = 0$ no tiene solución en el plano complejo.

Es decir, supongamos que $P(z) \neq 0$ para todos los números complejos $z$.

Luego, defina una nueva función $f(z)$ de la siguiente manera:

$$
f(z) = \frac{1}{P(z)}
$$

Por nuestra suposición, el denominador $P(z)$ nunca llega a ser $0$, por lo que esta función $f(z)$ no tiene singularidades (puntos donde el denominador es $0$) en ninguna parte del plano complejo. Puesto que el polinomio $P(z)$ es holomorfo (diferenciable) en todas partes, su recíproco también es holomorfo siempre que no sea igual a $0$. Por lo tanto, $f(z)$ es una función holomorfa sobre todo el plano complejo, es decir, una **función entera**.

A continuación, examinamos el comportamiento de $f(z)$ a medida que $|z|$ se acerca al infinito. Usando la desigualdad triangular, cuando $|z|$ es lo suficientemente grande, la magnitud del valor absoluto del polinomio $P(z)$ está dominada por el término de mayor grado, divergiendo así hacia el infinito.

Estrictamente hablando, a medida que $|z| \to \infty$,

$$
|P(z)| = |z|^n \left| a_n + \frac{a_{n-1}}{z} + \dots + \frac{a_0}{z^n} \right| \to \infty
$$

El hecho de que el valor absoluto de $P(z)$ diverja hacia el infinito significa que el valor absoluto de su recíproco $f(z) = 1/P(z)$ converge a $0$.

Es decir,

$$
\lim_{|z| \to \infty} |f(z)| = 0
$$

Un límite de $0$ significa que fuera de un círculo con un radio $R$ suficientemente grande, el valor puede estar acotado, por ejemplo, $|f(z)| \le 1$.
Por otro lado, dentro de la región del disco cerrado (una región cerrada acotada) que incluye el interior del círculo de radio $R$, una función continua debe tener un valor máximo.
Por lo tanto, tanto fuera como dentro del círculo, el valor absoluto de $f(z)$ nunca excede un cierto límite superior finito. Es decir, $f(z)$ es una función **acotada**.

Hasta este punto, hemos demostrado que $f(z)$ es tanto una "función entera" como "acotada".
Aquí, aplicamos el **teorema de [Liouville](https://kenji.blog/es/p/liouville/)**. Una función entera acotada debe ser una constante. Por lo tanto, existe un número complejo $c$ tal que para todo $z$,

$$
f(z) = c
$$

Sin embargo, puesto que $\lim_{|z| \to \infty} f(z) = 0$, esta constante $c$ debe ser $0$.
Es decir, $f(z) = 0$ para todo $z$.

Pero como $f(z) = \frac{1}{P(z)}$, es imposible que la función fraccional sea igual a $0$ (porque el numerador es $1$). Esta es una clara contradicción.

Esta contradicción surgió de nuestra suposición de que "$P(z) = 0$ no tiene solución en el plano complejo".
Por lo tanto, por contradicción, se demuestra que $P(z) = 0$ tiene al menos una solución en el plano complejo.

(Fin de la demostración)

## Corolario del Teorema: Factorización en Factores Lineales

El [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/) garantiza la existencia de "al menos una solución". Al combinar este hecho con el **Teorema del factor** para la división de polinomios, podemos demostrar que un polinomio se puede factorizar completamente en un producto de términos lineales.

Dado un polinomio $P_n(z)$ de grado $n$, el [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/) establece que existe una solución $\alpha_1$ tal que $P_n(\alpha_1) = 0$. Según el Teorema del factor, $P_n(z)$ tiene a $(z - \alpha_1)$ como factor. Es decir, se puede factorizar de la siguiente manera:

$$
P_n(z) = (z - \alpha_1) P_{n-1}(z)
$$

Aquí, $P_{n-1}(z)$ es un polinomio de grado $n-1$. Si $n-1 \ge 1$, podemos aplicar nuevamente el [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/) para encontrar una solución $\alpha_2$ para $P_{n-1}(z)$. Repitiendo esto $n$ veces, podemos factorizarlo completamente de la siguiente manera:

$$
P_n(z) = a_n (z - \alpha_1)(z - \alpha_2) \dots (z - \alpha_n)
$$

A partir de este resultado, podemos derivar la conclusión profundamente hermosa y completa de que **"una ecuación de grado $n$ con coeficientes complejos tiene exactamente $n$ soluciones, contando multiplicidades"**. Por esto se llama el "Teorema Fundamental".

Además, para los polinomios donde todos los coeficientes son números reales, si $\alpha$ es una solución, su conjugado complejo $\overline{\alpha}$ también debe ser una solución. Utilizando esta propiedad, también podemos derivar el hecho de que "cualquier polinomio con coeficientes reales se puede factorizar completamente en un producto de polinomios lineales y cuadráticos dentro de los números reales".

## Conclusión

En este artículo, hemos analizado en detalle el [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/), cubriendo sus antecedentes históricos, intuición topológica y demostración analítica compleja utilizando el teorema de [Liouville](https://kenji.blog/es/p/liouville/).

A primera vista, es un teorema sobre ecuaciones algebraicas, pero el hecho de que su demostración más elegante tome prestado el poder del análisis (cálculo) y la topología demuestra la profundidad de las matemáticas y la belleza de cómo diferentes campos están estrechamente entrelazados.

La larga búsqueda de la humanidad para encontrar las raíces de las ecuaciones ganó el vasto escenario del plano complejo a través de la introducción de los nuevos números imaginarios, y la integridad de este escenario fue demostrada por el [Teorema Fundamental del Álgebra](https://kenji.blog/es/p/fundamental-theorem-of-algebra/). Este teorema se convirtió en la llave que abrió las brillantes puertas que conducen a la teoría de [Galois](https://kenji.blog/es/p/galois/) y la geometría algebraica, que forman la base de las matemáticas modernas.

---








title: "GNFS"
date: 2026-09-05T02:26:13+09:00
tags: ["Matemáticas", "Criptografía", "RSA", "GNFS"]
draft: false
image: "rsa_encryption_break_1788542156523.jpg"
categories: ["Matemáticas, Criptografía y Cuántica"]
---









# La verdadera estructura matemática de la Criba General del Cuerpo de Números (GNFS)

El objetivo final de GNFS es encontrar $X, Y$ tales que $X^2 \equiv Y^2 \pmod N$.
Para lograr esto, los matemáticos construyeron un puente entre el **"mundo real de los números enteros"** y el **"mundo de los cuerpos algebraicos"**. Ese puente es el "homomorfismo".

## Etapa 1: Conectando mundos con el "Homomorfismo" (Homomorphism)

### 1. Selección de polinomios y definición de raíces
Para un número compuesto gigante $N$, elegimos un entero $m$ y un polinomio $f(x)$ de manera que $f(m) \equiv 0 \pmod N$.
(Ejemplo: expandimos $N$ en base $m$, y formamos $f(x)$ a partir de sus coeficientes. Aquí asumimos que $f(x)$ es irreducible sobre el cuerpo de los números racionales $\mathbb{Q}$ (no se puede factorizar más)).

A continuación, definimos una de las "raíces complejas" de la ecuación $f(x) = 0$ como $\alpha$.
Naturalmente, $f(\alpha) = 0$. $\alpha$ no es un entero, sino un número complejo (número algebraico) que puede incluir raíces o números imaginarios.

### 2. Construcción de Anillos (Rings) y Homomorfismos
Aquí preparamos dos "anillos" matemáticos (mundos donde se definen la suma y la multiplicación):

*   **Mundo A: $\mathbb{Z}[\alpha]$** (el anillo de enteros algebraicos que contiene a $\alpha$)
    Un mundo de números expresados en la forma $a + b\alpha + c\alpha^2 + \dots$.
*   **Mundo B: $\mathbb{Z}/N\mathbb{Z}$** (el anillo de restos módulo $N$)
    Un mundo de congruencias (módulos) compuesto solo por números enteros del $0$ al $N-1$.

Aquí, definimos el siguiente mapeo (función) $\phi$ del Mundo A al Mundo B:
**$$\phi : \mathbb{Z}[\alpha] \to \mathbb{Z}/N\mathbb{Z}$$**
**$$\phi(\alpha) = m \pmod N$$**

Este mapeo $\phi$ es una operación mágica que reemplaza exactamente la variable $\alpha$ del Mundo A por el entero $m$ del Mundo B.
Este $\phi$ tiene una propiedad extremadamente poderosa llamada **"Homomorfismo de Anillos" (Ring Homomorphism)**.
Un homomorfismo es la propiedad de **"transportarse a otro mundo sin destruir la estructura de sumas y multiplicaciones"**. Es decir, se cumplen las siguientes ecuaciones:
*   $\phi(X \times Y) = \phi(X) \times \phi(Y)$
*   $\phi(X^2) = \phi(X)^2$

Qué significa esto. Si podemos crear un **"cuadrado ($\gamma^2$)"** de algún elemento complejo $\gamma$ en el "Mundo A (el mundo de $\alpha$)", al transportarlo al "Mundo B (el mundo de los restos)" con $\phi$, **la forma del cuadrado $\phi(\gamma)^2$ se conservará perfectamente**.

---

## Etapa 2: El colapso de la factorización prima y el nacimiento del "Ideal" (Ideal)

Queremos recolectar muchos elementos apropiados $(a - b\alpha)$ dentro del Mundo A ($\mathbb{Z}[\alpha]$) y multiplicarlos juntos para crear un "cuadrado perfecto".
Normalmente, factorizaríamos cada $(a - b\alpha)$ en "factores primos" y los combinariamos para que los exponentes de los números primos sean todos pares (resolviéndolo con matrices) para formar un cuadrado.

**Sin embargo, aquí nos encontramos con un muro algebraico desesperante.**
En un mundo de cuerpos algebraicos como $\mathbb{Z}[\alpha]$, **se derrumba la "unicidad de la factorización prima" (la idea que nos enseñaron de que cualquier número puede expresarse como el producto de números primos de una sola manera)**.

(Ejemplo: en cierto mundo de cuerpos algebraicos, $6 = 2 \times 3$, y al mismo tiempo $6 = (1+\sqrt{-5}) \times (1-\sqrt{-5})$, haciendo imposible saber cuáles son los verdaderos primos).

Si la factorización prima no es única, el rompecabezas de "contar el número de primos para hacerlos pares" (la criba) es en principio imposible de ejecutar.

### La salvación de Kummer y Dedekind: el "Ideal"
Lo que salvó a las matemáticas de este colapso fue el concepto de **"Ideal" (número ideal)** creado por los matemáticos del siglo XIX.
Al pensar en el "conjunto de múltiplos (ideal)" generado por un elemento en lugar del elemento en sí, volvieron a hacer posible la factorización prima.

En el anillo de enteros de un cuerpo algebraico $\mathcal{O}_K$ (un anillo más completo que contiene a $\mathbb{Z}[\alpha]$), aunque los elementos no puedan ser factorizados de manera única, se ha demostrado que **"los ideales siempre pueden ser factorizados de forma única como un producto de 'ideales primos ($\mathfrak{p}$)'"**.

Por lo tanto, en GNFS, no descomponemos el elemento $(a - b\alpha)$ en sí, sino que hacemos la **factorización en ideales primos del ideal principal $\langle a - b\alpha \rangle$** que este genera.

---

## Etapa 3: Norma (Norm) y las dos Cribas (Sieves)

Entonces, ¿cómo sabemos en qué ideales primos se descompone el ideal $\langle a - b\alpha \rangle$?
Aquí utilizamos una función llamada **"Norma" (Norm)**. La norma es una función que convierte los elementos complejos de los cuerpos algebraicos en "números enteros reales ordinarios $\mathbb{Z}$".

La norma del elemento $(a - b\alpha)$ se calcula mediante un simple cálculo polinomial $b^d f(a/b)$ (donde $d$ es el grado de $f(x)$).

Por teoremas algebraicos, sabemos que **"si la norma de un ideal se descompone completamente en primos pequeños (es un número liso o 'smooth'), entonces su ideal original también se descompone completamente en ideales primos pequeños"**.

Por lo tanto, GNFS calcula simultáneamente lo siguiente para una gran cantidad de pares de enteros $(a, b)$, y recolecta solo los pares donde ambos son "números lisos":
1. **Criba Racional (Rational Sieve)**: $a - bm$ (valor en el mundo real)
2. **Criba Algebraica (Algebraic Sieve)**: $b^d f(a/b)$ (norma en el mundo del cuerpo algebraico)

Recolecta decenas de millones de pares $(a, b)$ donde ambos son lisos, resuelve los datos de factorización prima de los ideales (cuántos ideales primos están incluidos) como una matriz gigante (álgebra lineal sobre GF(2)), y encuentra un conjunto de pares $S$ de manera que "cuando se multiplican, los exponentes de todos los ideales primos se vuelven pares".

---

## Etapa 4: Dos "Obstáculos" que se interponen y el Grupo de Clases de Ideales

Mediante cálculos de matrices, encontramos que multiplicar todos los ideales de $(a - b\alpha)$ que pertenecen al conjunto $S$ resulta en el cuadrado de cierto ideal $I$.
$$\prod_{S} \langle a - b\alpha \rangle = I^2$$

**Sin embargo, esto aún no ha terminado. Aquí es donde se encuentra el muro matemático más profundo y difícil de GNFS.**

Lo que finalmente queremos no es el "cuadrado de un ideal", sino el **"cuadrado de un elemento ($\gamma^2$)"** para sustituirlo en el mapeo $\phi$.
El hecho de que se haya convertido en el cuadrado de un ideal no significa que el elemento en sí sea un cuadrado. Aquí existen **dos obstáculos matemáticos (Obstructions) formidables**.

### Obstáculo 1: El muro del Grupo de Clases de Ideales (Ideal Class Group)
El ideal $I$ no es necesariamente un "ideal generado por un solo elemento (ideal principal)".
Es imposible extraer un elemento concreto $\gamma$ de un ideal que no sea principal.

Aquí entra el concepto de **"Grupo de Clases de Ideales" (Class Group, $Cl_K$)**. El grupo de clases de ideales es un grupo que mide "cuántos ideales que no son principales existen en ese mundo del cuerpo algebraico (qué tan destruida está la unicidad de la factorización prima)".
Incluso si $\prod \langle a - b\alpha \rangle$ se convierte en $I^2$, si $I$ no es el elemento identidad (ideal principal) en el grupo de clases de ideales, no podemos retroceder al cuadrado de un elemento.

### Obstáculo 2: El muro del Grupo de Unidades (Unit Group)
Supongamos que por suerte $I$ era un ideal principal $\langle \gamma \rangle$.
Entonces tenemos que $\prod \langle a - b\alpha \rangle = \langle \gamma^2 \rangle$.
Podrías pensar "¡Genial, el elemento también es un cuadrado!", pero estarías muy equivocado.

Que los ideales (conjuntos de múltiplos) sean iguales no significa que los elementos sean completamente iguales. Siempre ocurre una desviación por una **"Unidad" (Unit: un número cuyo inverso multiplicativo también es entero. Por ejemplo, 1 o -1)**.
Es decir, la verdadera igualdad de los elementos es la siguiente:
$$\prod_{S} (a - b\alpha) = u \cdot \gamma^2$$
($u$ es un elemento del grupo de unidades $U_K$)

A menos que esta unidad $u$ sea en sí misma un cuadrado (elemento cuadrático) de algo, el lado izquierdo nunca podrá ser un "cuadrado perfecto de un elemento".

---

## Etapa 5: La magia de Adleman, "Caracteres Cuadráticos" (Quadratic Characters)

Los obstáculos del grupo de clases de ideales y del grupo de unidades. ¿Cómo los superamos?
Aquí es donde entra la genial técnica introducida por el criptógrafo Leonard Adleman (la "A" de RSA) y otros: los **"Caracteres Cuadráticos" (Quadratic Characters)**.

Para determinar "si un elemento es un cuadrado perfecto dentro de un cuerpo algebraico", utilizamos una versión para cuerpos algebraicos del símbolo de Legendre (residuo cuadrático).
En la matriz gigante anterior (el rompecabezas para hacer que el número de ideales primos sea par), **añadimos en secreto unas cuantas decenas de condiciones (columnas) adicionales para que "los caracteres cuadráticos para algunos ideales primos especiales $\mathfrak{q}$ también sean todos $1$ (pares)"**.

Cuando encontramos un conjunto $S$ que incluso satisface estas condiciones adicionales mediante el cálculo de matrices, por los teoremas profundos de la teoría de números algebraicos, se garantiza que **"los obstáculos tanto del grupo de clases de ideales como del grupo de unidades desaparecerán naturalmente con una probabilidad abrumadora"**.

Con esto, por fin obtenemos la verdadera ecuación.
$$\prod_{S} (a - b\alpha) = \gamma^2$$

---

## Etapa Final: La fusión de los mundos y el colapso criptográfico

Por fin, todas las piezas del rompecabezas están en su lugar.

**[Elementos del Mundo del Cuerpo Algebraico (Mundo A)]**
$\gamma^2 = \prod (a - b\alpha)$
(De aquí usamos un algoritmo de raíz cuadrada para encontrar $\gamma$)

**[Elementos del Mundo Real (Mundo de los Números Racionales)]**
$V^2 = \prod (a - bm)$
(Como esta es una simple multiplicación de enteros, podemos encontrar la raíz cuadrada $V$ normalmente)

Ahora, es el turno del puente mágico que construimos al principio: **el homomorfismo $\phi$**.
Transportamos el elemento $\gamma$ del Mundo A al Mundo B (el mundo de restos módulo $N$) usando $\phi$ (el mapeo que sustituye $\alpha$ por $m$).
$$Y = \phi(\gamma) \pmod N$$

Por otro lado, tomamos la $V$ que creamos en el mundo real directamente al mundo de los restos y la llamamos $X$.
$$X = V \pmod N$$

Debido a la propiedad de "conservar estructuras" del homomorfismo, la relación de los cuadrados que se sostenía en el Mundo A se preserva perfectamente en el Mundo B (el mundo módulo $N$).
Además, dado que el par original $(a, b)$ fue creado correspondientemente en la forma $a - b\alpha$ y $a - bm$, estas $X$ e $Y$ chocan en el mundo módulo $N$ y producen la siguiente igualdad absoluta:

**$$X^2 \equiv Y^2 \pmod N$$**

El resto es rezar para que $X$ e $Y$ no sean una solución trivial ($X \equiv \pm Y$), y calcular:
**$\gcd(X - Y, N)$**

Si es una solución no trivial, el algoritmo de Euclides correrá en 0.001 segundos e imprimirá en la pantalla de salida el corazón del cifrado RSA: los primos secretos $p$ y $q$.

---

Esta es la **forma completa de la "Criba General del Cuerpo de Números (GNFS)"**, que reúne lo mejor de las matemáticas modernas.

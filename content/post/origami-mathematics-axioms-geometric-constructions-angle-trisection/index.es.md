---
title: "¿Puede el plegado de papel superar a la regla y el compás? La matemática profunda del origami"
date: 2026-10-14T01:00:00+09:00
draft: false
slug: "origami-mathematics-axioms-geometric-constructions-angle-trisection"
tags:
  - Matemáticas
  - Geometría
  - Álgebra abstracta
  - Ingeniería del origami
  - Historia de la ciencia
categories:
  - Matemáticas
image: "eyecatch.jpg"
math: true
---

Durante dos milenios, los <strong>tres problemas clásicos de la geometría griega</strong> permanecieron irresueltos:
1. <strong>La trisección del ángulo</strong>: dividir cualquier ángulo en tres partes iguales usando solo regla y compás.
2. <strong>La duplicación del cubo (problema de Delos)</strong>: construir el lado de un cubo con el doble de volumen ($\sqrt[3]{2}$).
3. <strong>La cuadratura del círculo</strong>: construir un cuadrado con el área de un círculo ($\sqrt{\pi}$).

En 1837, Pierre Wantzel demostró que la regla y el compás están restringidos a extensiones de cuerpos de grado $2^k$. Como trisecar ángulos y duplicar cubos exige resolver polinomios cúbicos irreducibles ($x^3 - 3x - 1 = 0$ y $x^3 - 2 = 0$) de grado 3, su construcción euclidiana es <strong>absolutamente imposible</strong>.

Sin embargo, el siglo XX trajo una revelación deslumbrante:
<strong>¡Doblando una hoja cuadrada de papel, la trisección del ángulo y la construcción de $\sqrt[3]{2}$ se resuelven en segundos con exactitud geométrica impecable!</strong>

El arte tradicional del <strong>origami</strong> es en realidad un <strong>computador analógico capaz de resolver ecuaciones de tercer grado</strong>.

---

## 1. Los axiomas de Huzita-Hatori

Doblar papel equivale a realizar una reflexión respecto a una línea recta. Entre 1989 y 2001, Huzita, Justin y Hatori consolidaron los siete axiomas fundamentales del origami:

```mermaid
flowchart TD
    A1["Axioma 1: Doblar línea por 2 puntos (lineal)"]
    A2["Axioma 2: Doblar punto sobre punto (mediatriz: lineal)"]
    A3["Axioma 3: Doblar línea sobre línea (bisectriz: lineal)"]
    A4["Axioma 4: Doblar perpendicular a una línea por un punto (lineal)"]
    A5["Axioma 5: Doblar punto sobre línea pasando por otro punto (cuadrático)"]
    A7["Axioma 7: Doblar punto sobre línea perpendicular a otra línea (cuadrático)"]
    A6["Axioma 6: Doblar DOS puntos simultáneamente sobre DOS líneas.<br/>【Tangente común a dos parábolas: ¡Ecuación cúbica!】"]
end
```

El <strong>Axioma 6</strong> es la clave que supera los límites euclidianos.

---

## 2. Por qué el Axioma 6 resuelve ecuaciones cúbicas

Todo pliegue que lleva un punto $P$ a una línea $L$ es la mediatriz del segmento, lo que corresponde a una <strong>recta tangente a la parábola</strong> con foco $P$ y directriz $L$.

El Axioma 6 busca una recta simultáneamente tangente a dos parábolas $\mathcal{P}_1$ y $\mathcal{P}_2$. La ecuación que determina la pendiente $m$ de esta tangente común es una <strong>ecuación cúbica general</strong>:

$$
A m^3 + B m^2 + C m + D = 0
$$

---

## 3. Trisección de Abe y duplicación de Messer

- <strong>Trisección del ángulo de Abe (1980)</strong>: Hisashi Abe descubrió un procedimiento que divide cualquier ángulo agudo en tres ángulos congruentes usando el Axioma 6.
- <strong>Duplicación del cubo de Messer (1986)</strong>: Peter Messer construyó $\sqrt[3]{2}$ en una hoja cuadrada aplicando el Axioma 6.
- <strong>Cuerpo de números del origami $\mathcal{O}$</strong>: Con grado de extensión $[\mathbb{Q}(\alpha) : \mathbb{Q}] = 2^a 3^b$, ¡el heptágono regular (7 lados) y el eneágono regular (9 lados) son perfectamente construibles!

---

## 4. Plegabilidad plana: Teoremas de Kawasaki y Maekawa

- <strong>Teorema de Kawasaki</strong>: Un vértice se pliega plano si y solo si la suma de ángulos alternos es $180^\circ$ ($\theta_1 + \theta_3 + \dots = 180^\circ$).
- <strong>Teorema de Maekawa</strong>: La diferencia entre pliegues en monte ($M$) y en valle ($V$) en un vértice interior es siempre $\pm 2$ ($M - V = \pm 2$).

---

## 5. Aplicaciones en ingeniería moderna

- <strong>Pliegue Miura (Miura-ori)</strong>: Despliegue con un grado de libertad para paneles solares espaciales (telescopio James Webb).
- <strong>Stents médicos</strong>: Tubos que se expanden dentro de vasos sanguíneos.
- <strong>Metamateriales auxéticos</strong>: Materiales con coeficiente de Poisson negativo que se expanden lateralmente al estirarse.

---

## 6. Conclusión

El origami demuestra que los límites matemáticos son artefactos de los instrumentos elegidos. La maleabilidad del papel libera a la geometría de sus antiguas cadenas.

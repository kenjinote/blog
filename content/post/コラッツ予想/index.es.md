---
title: '¿Qué es la conjetura de Collatz? Verificando con Python el problema matemático sin resolver donde cualquier número siempre termina en 1'
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Conjetura de Collatz", "Matemáticas", "Programación", "Algoritmos"]
draft: false
image: "img.webp"
categories: ["Matemáticas, Criptografía, Cuántica"]
description: '¿Si se repite ''dividir a la mitad si es par, y multiplicar por 3 y sumar 1 si es impar'', siempre se llega a 1? Explicamos de forma sencilla las curiosas reglas de la ''conjetura de Collatz'', un famoso problema matemático no resuelto. Además, escribiremos un programa en Python para simular si la secuencia de números realmente converge a 1.'
---

# ¿Es verdad que "cualquier número siempre termina en 1"? ── Jugando con la conjetura de Collatz

¡Hola! Soy kenji.

De repente, si escuchas "una regla donde cualquier número finalmente se convierte en 1",
¿no te parece un poco extraño?

> Por ejemplo, 19, 87, o incluso 1000000.
> Si sigues una regla simple y vas alterando el número, por alguna razón siempre converge a "1" al final.

Esa historia de ensueño es la **Conjetura de Collatz (Collatz Conjecture)**.

---

## Para empezar, ¿qué es la conjetura de Collatz?

Primero, presentaré la regla.

* Inicio: Elige cualquier **número entero positivo**
* Operación:

    * Si es par → divídelo a la mitad (n → n / 2)
    * Si es impar → multiplícalo por 3 y suma 1 (n → 3n + 1)

Si repites esto una y otra vez, la conjetura dice que **cualquier número llegará finalmente a 1**.

Por ejemplo, si empezamos con el `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Efectivamente se convirtió en "1". ¡Bienvenido a casa!

---

## Hagámoslo con código: Collatz en Python

Bueno, en estos casos ¡es más rápido probar con código!
Imprimamos la "Secuencia de Collatz" en Python.

```python
def collatz(n):
    steps = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps.append(n)
    return steps

# Ejemplo: empezar desde 19
print(collatz(19))
```

Al ejecutarlo:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Llega magníficamente al 1.
Hace bastantes desvíos, pero ¡llega a la meta al final!


Por cierto, si empezamos desde el **27**, también llegará a 1 de la misma manera.

```
print(collatz(27))
```

Al ejecutarlo:

```
[27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322, 161, 484, 242,
121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350,
175, 526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167,
502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479,
1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911,
2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732,
866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35,
106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

¡Increíble, toma 111 pasos!

Además, hay momentos en los que se infla a más de 9000 por el camino.
Es un patrón de desviarse muchísimo antes de llegar a la meta.

---

## Y entonces, ¿qué tiene de increíble?

Lo sorprendente de esta conjetura es que:

> **Aunque no se ha demostrado, parece que con cualquier número se convierte en 1**

¿Eh? Entonces, ¿qué pasa con 1 billón, o 10 mil billones...?

Para los que pensaron eso, muy perspicaces.
En realidad, se ha verificado mediante computadoras hasta aproximadamente "2 elevado a la potencia de 68",
y **todos llegan a 1**. Increíble...

Pero, **no se ha demostrado teóricamente que "siempre será así"**.
A esto se le llama un "problema no resuelto" en el mundo de las matemáticas.

---

## ¿Por qué se convierte en "1"? El enfoque desde la teoría de la probabilidad (contexto matemático)

Parece magia que cualquier número termine siendo 1, pero desde un **punto de vista probabilístico**, existe una razón lógica para pensar "bueno, parece probable".

Si aplicamos `3n + 1` a un número impar $n$, la respuesta siempre será un **número par**.
Por lo tanto, en el siguiente paso siempre se dividirá por 2, siendo efectivamente $\frac{3n + 1}{2} \approx 1.5n$.

Y la probabilidad de que ese número vuelva a ser par es de $\frac{1}{2}$.
Si es par, se dividirá nuevamente por 2 para ser $0.75n$, que es menor que el número original.

Aunque no es matemáticamente estricto, se sabe que si se toma la media geométrica del "multiplicador" al saltar de un número impar al siguiente impar, **es de aproximadamente $\frac{3}{4}$ veces** (modelo probabilístico heurístico).
En otras palabras, **en promedio los valores tienden a reducirse**, por lo que finalmente son absorbidos y caen hacia el 1.

## ¿Qué pasa si cambiamos un poco la regla? (Comparación con otras conjeturas)

"Entonces, ¿y si en vez de multiplicarlo por 3, lo multiplicamos por 5?" dan ganas de pensar eso, ¿verdad?
De hecho, esto se conoce como el **problema $5n + 1$**, y en este caso, no todos los números convergen a 1.

En el caso de $5n + 1$, se ha confirmado que existen múltiples bucles diferentes (ciclos), y también se ha señalado la posibilidad de que existan números que continúan creciendo infinitamente (divergencia).
Además, en el caso del **problema $3n - 1$**, aparte del bucle "$1 \to 2 \to 1$", también existe otro bucle diferente como "$5 \to 14 \to 7 \to 20 \to 10 \to 5$".

Esto nos hace entender el delicado equilibrio sobre el cual se sustenta la propiedad de la conjetura de Collatz de que "todo converge a 1 (el bucle $4 \to 2 \to 1$)".

---

## El punto de llegada de la humanidad ①: Los límites de la fuerza bruta computacional

Actualmente, matemáticos y entusiastas de la informática de todo el mundo continúan calculando incesantemente la conjetura de Collatz utilizando computación distribuida (proyectos que agrupan el poder de cálculo de los PC del mundo) y GPUs.

Hasta el año 2020, se ha verificado por computadora que la conjetura de Collatz es cierta (finalmente llega a 1) para todos los valores iniciales inferiores a ¡**$2^{68}$ (aproximadamente 295 trillones)**!

Sin embargo, en el mundo de las matemáticas no se puede decir "como lo hemos comprobado hasta 295 trillones, todo debe ser correcto". En un océano infinito de números, incluso $2^{68}$ no es más que "la primera gota".

---

## El punto de llegada de la humanidad ②: La indecidibilidad y el gran avance de Terence Tao

Ante la pregunta "¿Por qué nadie puede demostrarlo?", en 1972 el genio matemático británico John Conway demostró que un problema ligeramente extendido de la conjetura de Collatz es **"indecidible" (Turing complete)**.
Este es un hecho aterrador que afecta a la raíz misma de la informática, indicando que, dependiendo de las reglas, "en principio no existe un algoritmo para determinar si llegará o no a 1". La conjetura de Collatz en sí misma podría ser incluso una proposición indemostrable bajo el marco de las matemáticas modernas.

Sin embargo, en 2019, finalmente se produjo un gran avance.
Uno de los matemáticos más brillantes de la era moderna, **Terence Tao**, demostró utilizando ecuaciones diferenciales parciales y técnicas de probabilidad que "(aunque no se puede decir estrictamente de todos) **para casi todos los valores iniciales, la secuencia de Collatz finalmente llega a un valor mucho menor que el número original**".

Esto no es una demostración completa de que "todo se convierte en 1", pero asombró a la comunidad matemática mundial al ser **el punto más cercano que la humanidad ha alcanzado de la verdad de la conjetura de Collatz**.

---

## ¿Y quién es este señor Collatz?

Llegados a este punto, seguro estarás pensando "¿Y quién es Collatz en primer lugar?".
¡Aquí te lo presento!

* Nombre: **Lothar Collatz**
* Nacionalidad: Alemán
* Años de vida: 1910 - 1990
* Profesión: Matemático (destacado en los campos de análisis funcional y teoría de números)

Propuso esta conjetura en 1937, y desde entonces, a lo largo de más de 80 años, **nadie ha podido demostrarla ni refutarla**.

Por cierto, este problema es tan simple pero a la vez tan profundo,
que incluso Paul Erdős (un matemático súper famoso) llegó a decir algo como esto:

> "Las matemáticas aún no están maduras para tratar con Collatz"

Es decir, la teoría de que las matemáticas de la humanidad aún no han alcanzado el nivel de este misterio...

---

## No se necesitan "fórmulas matemáticas difíciles"

Lo bueno de la conjetura de Collatz es que **cualquiera puede jugar con ella**.

Se puede hacer con papel y lápiz.
Si escribes el código en Python, puedes probarlo automáticamente.
Y a pesar de eso, **los matemáticos más avanzados la enfrentan muy en serio**.

No sé a ti, pero a mí me resulta fascinante.

---

## Extra: Código para probarlo todo de una vez

Aquí te dejo también un código para probar muchos números de una vez.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (Pasos: {len(steps)-1})")
```

Esto imprimirá las secuencias de Collatz para los números del "1 al 20" de una sola pasada.

---

## Conclusión: Este mundo, sin duda, es asombroso

Y esa es la conjetura de Collatz.

* Aunque es súper simple
* Nadie puede demostrarla
* Es un gran problema en el mundo de las matemáticas

Es una entidad que parece un concentrado de misterio.

Incluso los principiantes en programación pueden probarla, ¡así que anímate a jugar con ella!

---

## Enlaces recomendados (para los interesados)

* [Wikipedia: Conjetura de Collatz](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
* [Paper de Terence Tao (en inglés)](https://arxiv.org/abs/1909.03562)
* ¡También es divertido crear una versión visualizada en Python! (La haré si hay solicitudes)

---

Si hay quienes quieren conocer más temas de este tipo de "Matemáticas misteriosas × Programación",
no duden en pedir "Enséñame más" sin ningún compromiso.
¡Con el tiempo iré presentando varias cosas, como la hipótesis de Riemann o temas sobre números primos!

---

📮 ¡Fin!

---

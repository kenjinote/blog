---








title: "La conjetura de Collatz"
slug: "コラッツ予想"
date: 2025-07-15T18:03:03+09:00
tags: ["Conjetura de Collatz", "Matemáticas", "Programación", "Algoritmos"]
draft: false
image: "img.png"
categories: ["Matemáticas, Criptografía y Cuántica"]
---









# ¿Es cierto que "cualquier número termina en 1"? ── Jugando con la Conjetura de Collatz

¡Hola! Soy kenji.

De repente, si escuchas sobre "una regla donde cualquier número termina finalmente en 1",
¿no te parece un poco extraño?

> Por ejemplo, el 19, el 87 o incluso el 1000000.
> Si sigues una regla simple y manipulas el número, por alguna razón siempre converge a "1" al final.

Esta historia que parece un sueño es la **Conjetura de Collatz (Collatz Conjecture)**.

---

## Para empezar, ¿qué es la Conjetura de Collatz?

Primero, presentaré la regla.

* Inicio: Elige cualquier **entero positivo**
* Operación:

    * Si es par → divídelo a la mitad (n → n / 2)
    * Si es impar → multiplícalo por 3 y suma 1 (n → 3n + 1)

Si repites esto una y otra vez, la conjetura es que **cualquier número finalmente llegará a 1**.

Por ejemplo, si empezamos con el `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

Efectivamente llegó a "1". ¡Bienvenido de vuelta!

---

## Hagámoslo con código: Collatz en Python

Bueno, en estos casos ¡es más rápido probar con código!
Imprimamos la "secuencia de Collatz" en Python.

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

# Ejemplo: empezando con 19
print(collatz(19))
```

Al ejecutarlo:

```
[19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
```

Llega perfectamente al 1.
Da bastantes rodeos, pero al final ¡alcanza la meta!


Por cierto, incluso si empiezas con 29, también llegará a 1 de la misma manera.

```
pythonprint(collatz(29))
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

¡Vaya, toma 111 pasos!

Y además, hay momentos en los que se infla por encima de 9000.
Es un patrón que da muchísimas vueltas antes de llegar a la meta.

---

## Y, al final, ¿qué tiene de increíble?

Lo increíble de esta conjetura es,

> **Aunque no está comprobada, parece que funciona con cualquier número y termina en 1**

Es justo eso.

¿Eh? Entonces, ¿qué pasa con 1 billón, o 1 trillón...?

Si pensaste eso, eres muy perspicaz.
De hecho, usando computadoras se ha verificado hasta aproximadamente "2 elevado a 68",
y **todos llegan a 1**. Increíble...

Pero, **no se ha demostrado teóricamente que "todos lo hagan"**.
Esto es lo que en el mundo de las matemáticas se llama un "problema no resuelto".

---

## ¿Quién es el Sr. Collatz?

Y, al leer hasta aquí, seguro piensas "¿y quién es Collatz?".
¡Lo presentaré adecuadamente!

* Nombre: **Lothar Collatz**
* Nacionalidad: Alemán
* Nacimiento: 1910 - 1990
* Profesión: Matemático (destacado en análisis funcional y teoría de números)

Propuso esta conjetura en 1937, y
después de eso, durante más de 80 años **nadie ha podido demostrarla ni refutarla**.

Por cierto, este problema es tan simple pero tan profundo,
que incluso el famoso Paul Erdős (un matemático súper famoso) dijo:

> "Las matemáticas aún no están listas para la conjetura de Collatz"

En otras palabras, la teoría es que las matemáticas de la humanidad aún no han alcanzado este misterio...

---

## No se necesitan "fórmulas matemáticas difíciles"

Lo bueno de la conjetura de Collatz es que **cualquiera puede jugar**.

Puedes hacerlo si tienes papel y bolígrafo.
Si escribes el código en Python, puedes probarlo automáticamente.
Y aun así, **los matemáticos más avanzados lo están intentando en serio**.

No sé, ¿no te emociona?

---

## Bonus: Código para probar de una vez

También dejaré un código para probar varios números a la vez.

```python
for n in range(1, 21):
    steps = collatz(n)
    print(f"{n}: {steps} (pasos: {len(steps)-1})")
```

Esto imprimirá la secuencia de Collatz del "1 al 20" de una vez.

---

## Conclusión: Este mundo, al final, es misterioso

Así que, la conjetura de Collatz.

* Aunque es súper simple
* Nadie puede probarlo
* Es un gran problema en el mundo de las matemáticas

Es como una masa de misterio.

¡Incluso los principiantes en programación pueden probarlo, así que anímate a jugar!

---

## Enlaces recomendados (para interesados)

* [Wikipedia: Conjetura de Collatz](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)
* [Artículo de Terence Tao (en inglés)](https://arxiv.org/abs/1909.03562)
* ¡También es divertido crear una versión visual en Python! (Lo haré si hay peticiones)

---

Si quieres conocer más de este tipo de temas "Matemáticas misteriosas × Programación",
no dudes en pedirme "cuéntame más".
¡Pronto te presentaré la Hipótesis de Riemann, historias sobre números primos y muchas cosas más!

---

📮 ¡Fin!

---

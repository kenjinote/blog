---



title: "'¿Qué es la paradoja del cumpleaños?'"
date: 2024-04-02T01:20:50+09:00
tags: ["Matemáticas", "Paradojas"]
draft: false
math: true
image: "img.png"
categories: ["Matemáticas, Criptografía, Cuántica"]
---




## ¿Conoces la paradoja del cumpleaños?

Voy a contarte algo un poco curioso.
¿Cuántas personas crees que tienen que reunirse para que la probabilidad de que "haya personas con el mismo cumpleaños" sea alta?

Por ejemplo, como un año tiene 365 días, si te dicen que "si se reúnen 23 personas, la probabilidad de que alguien comparta cumpleaños es de más del 50%"... de alguna manera parece ir en contra de la intuición, ¿verdad?

Pero esto, **realmente es más del 50%.**

---

## ¿Por qué ocurre esto?

Este fenómeno se llama la "paradoja del cumpleaños".
El nombre incluye "paradoja", pero tiene una razón matemática sólida.

Si el número de personas es "n", **la probabilidad de que nadie comparta cumpleaños** se puede calcular con la siguiente fórmula:

```
P(nadie comparte) = 365/365 × 364/365 × 363/365 × ... × (365 - n + 1)/365
```

Al restar esto de 1, se obtiene "la probabilidad de que alguien comparta cumpleaños".

---

## Al mirar los resultados...

| Número de personas | Probabilidad de que haya personas con el mismo cumpleaños |
| --- | ------------------ |
| 10 personas | Aprox. 11.7%             |
| 20 personas | Aprox. 41.1%             |
| 23 personas | **Aprox. 50.7% (¡Atención aquí!)** |
| 30 personas | Aprox. 70.6%             |
| 70 personas | **¡Sorprendentemente aprox. 99.9%!**     |

Es decir, con solo **23 personas**, hay más de la mitad de probabilidad de que alguien comparta cumpleaños.
Parece bastante aplicable a una clase en la escuela o a una reunión en el trabajo.

---

## Resumen: La brecha entre la intuición y las matemáticas es interesante

La "paradoja del cumpleaños" es un ejemplo interesante de cómo nuestra intuición y la probabilidad matemática real difieren.
¡Saber este tipo de cosas puede ser divertido para una charla casual o un juego de preguntas!

---

## Enlaces de referencia

* [Paradoja del cumpleaños (Wikipedia)](https://es.wikipedia.org/wiki/Paradoja_del_cumplea%C3%B1os)

---
title: 'El problema de la bella durmiente: ¿la probabilidad de la moneda es 1/2 o 1/3? Un problema complejo que divide la teoría de la probabilidad'
slug: 'sleeping-beauty-paradox'
description: '"Ahora que has despertado, ¿cuál es la probabilidad de que la moneda haya salido cara?" A pesar de su configuración muy simple, explicamos la última paradoja que mantiene a matemáticos y filósofos de todo el mundo divididos en la "facción de 1/2" y la "facción de 1/3" debatiendo hasta el día de hoy.'
date: '2026-09-10T09:00:00+09:00'
image: 'img/sleeping_beauty.jpg'
math: true
mermaid: true
categories:
  - 'Paradojas matemáticas'
  - 'Teoría de la probabilidad'
tags:
  - 'Paradoja'
  - 'Probabilidad condicional'
  - 'Teorema de Bayes'
  - 'Filosofía'
---

## 1. Las reglas de un experimento extraño

Tú (la bella durmiente) has sido elegida como sujeto de un cierto experimento científico.
El experimento se lleva a cabo de domingo a miércoles. La noche del domingo, te dan una pastilla para dormir y te quedas dormida.

Después de que te duermas, el experimentador lanza **una moneda justa** (una moneda con una probabilidad exactamente de 1/2 de salir cara o cruz). Luego, dependiendo del resultado, te despertará con el siguiente horario:

**【Si el resultado del lanzamiento de la moneda es "cara"】**
- Te despertarán solo una vez el lunes y te harán una pregunta. Después de eso, te volverán a dormir y no te despertarás hasta que termine el experimento (el miércoles).

**【Si el resultado del lanzamiento de la moneda es "cruz"】**
- Te despertarán el lunes y te harán una pregunta. Después de eso, te darán una medicina especial (una medicina que borra la memoria) y te volverás a dormir.
- Te despertarán nuevamente el martes y te harán la misma pregunta. Después de eso, te volverán a dormir y el experimento terminará (el miércoles).

※ Debido al efecto de la medicina que borra la memoria, cuando despiertas no puedes recordar en absoluto "qué día de la semana es hoy" ni "si te han despertado en el pasado".

```mermaid
graph TD
    Sunday["Domingo: La bella durmiente duerme"] --> Toss{"Lanzamiento de moneda"}
    
    Toss -->|Cara (1/2)| Mon_Heads["Lunes: Despertar + Pregunta<br>(Luego el experimento termina)"]
    Toss -->|Cruz (1/2)| Mon_Tails["Lunes: Despertar + Pregunta<br>(Luego se borra la memoria)"]
    
    Mon_Tails --> Tue_Tails["Martes: Despertar + Pregunta<br>(Luego el experimento termina)"]
    
    style Toss fill:#ff9999,stroke:#333
    style Mon_Heads fill:#aaffaa,stroke:#333
    style Mon_Tails fill:#aaffaa,stroke:#333
    style Tue_Tails fill:#aaffaa,stroke:#333
```

Ahora bien, es lunes (o martes) y te has despertado.
No hay reloj ni calendario en la habitación, así que no sabes qué día es hoy.

Entonces, el experimentador llega y te hace esta pregunta:
**"En tu estado actual de vigilia, ¿cuál crees que es la probabilidad de que la moneda que se lanzó haya salido 'cara'?"**

Eres una belleza con grandes conocimientos matemáticos. Ahora bien, ¿qué respondes?

---

## 2. Dos facciones en choque: ¿1/2 o 1/3?

Este problema fue ideado en la década de 1990 y publicado en una revista académica por el filósofo Adam Elga en el año 2000.
La probabilidad de la moneda puede parecer obvia, pero de hecho, en torno a este problema, matemáticos, estadísticos y filósofos de todo el mundo se han dividido exactamente por la mitad en dos bandos: **"La facción de 1/2 (Halfers)"** y **"La facción de 1/3 (Thirders)"**, y continúan debatiendo ferozmente hasta el día de hoy.

Escuchemos la "lógica perfecta" de cada bando.

### Argumento de "La facción de 1/2 (Halfers)"
> "Como la moneda es una moneda justa sin trucos, la probabilidad de que salga cara es naturalmente 1/2.
> Sin importar cuántas veces el experimentador me despierte o me borre la memoria después de que me haya dormido, eso **no afecta en absoluto el resultado físico de la moneda**.
> La probabilidad en el momento en que se lanzó la moneda era de 1/2, y no he obtenido ninguna información nueva (pistas para adivinar si fue cara o cruz) por haberme despertado. Por lo tanto, la probabilidad sigue siendo 1/2."

Esta es una opinión muy razonable que enfatiza los fenómenos físicos objetivos y la no actualización de la información.

### Argumento de "La facción de 1/3 (Thirders)"
> "El hecho mismo de que estés 'despierta' es la información que cambia la probabilidad.
> Supongamos que repetimos este experimento 100 veces (100 semanas).
> La moneda debería salir 'cara' 50 veces y 'cruz' 50 veces.
> 
> - En las 50 semanas en que sale cara, te despiertas solo una vez el lunes $\rightarrow$ **El número de veces que te despiertas con 'cara' es de 50 veces**
> - En las 50 semanas en que sale cruz, te despiertas dos veces, el lunes y el martes $\rightarrow$ **El número de veces que te despiertas con 'cruz' es de 100 veces**
> 
> En otras palabras, de un total de 150 situaciones en las que te despiertas, hay 50 veces para el 'patrón de despertar con cara' y 100 veces para el 'patrón de despertar con cruz'.
> ¡Por lo tanto, la probabilidad de que el despertar que estás experimentando ahora sea 'cara' es 50 / 150 = **1/3**!"

Esta es una opinión sólida basada en el "frecuentismo" o el "principio antrópico", que incorpora la situación misma de "existir (observar) en este momento" en el cálculo como un elemento del espacio de probabilidad.

---

## 3. Intentando calcular con el Teorema de Bayes

También hay intentos de desentrañar este problema utilizando el "Teorema de Bayes", una herramienta para actualizar matemáticamente las probabilidades.
Organicemos la lógica de "La facción de 1/3" desde la perspectiva de la probabilidad condicional.

Al despertar, el estado será uno de los siguientes tres:
1. $E_1$: La moneda es "cara" y hoy es "lunes"
2. $E_2$: La moneda es "cruz" y hoy es "lunes"
3. $E_3$: La moneda es "cruz" y hoy es "martes"

La probabilidad de obtener "cara" es $1/2$, y la probabilidad de obtener "cruz" es $1/2$.
Sin embargo, en el caso de cruz, como "lunes" y "martes" son completamente simétricos (no se pueden distinguir porque no hay memoria), se considera que la probabilidad de que ocurra $E_2$ y $E_3$ es igual.

Dado que la suma total de las probabilidades debe ser $1$, si asignamos cada despertar como un "evento (punto de observación)" independiente con igual probabilidad:
$P(E_1) = 1/3$
$P(E_2) = 1/3$
$P(E_3) = 1/3$
Por lo tanto, la conclusión es que la "probabilidad de que fuera cara ($P(E_1)$)" es $1/3$.

Por otro lado, "La facción de 1/2" contraargumenta que, para empezar, "los lunes y martes cuando la moneda es cruz ($E_2$ y $E_3$) son eventos dependientes que simplemente se derivan del resultado de una misma moneda, y es incorrecto contarlos como probabilidades independientes".

---

## 4. ¿Por qué no se resuelve este problema?

La razón por la cual "El problema de la bella durmiente" atormenta tanto a los académicos no se debe a un simple error de cálculo o ilusión.
Es porque este problema toca la cuestión fundamental más profunda de la teoría de la probabilidad, a saber, la pregunta filosófica: **"¿Qué es exactamente la probabilidad?"**

- Para la **facción de 1/2**, la probabilidad es "la propiedad física de la moneda" o "un hecho objetivo".
- Para la **facción de 1/3**, la probabilidad es "el grado de creencia del observador (la bella)" o "la frecuencia con la que se observa".

Un tema profundo que también se conecta con el "problema de la medición" en la mecánica cuántica y el "principio antrópico" en cosmología (la idea de calcular inversamente las probabilidades del universo a partir del hecho de que existimos) está condensado en este simple experimento de lanzamiento de una moneda.

## 5. Resumen

Si fueras el sujeto de este experimento, ¿responderías "1/2" o "1/3" al despertar?

Cualquiera que respondas, matemáticos de clase mundial estarán a tus espaldas para defenderte.
Cómo definiciones matemáticas aparentemente simples colapsan tan pronto como se vinculan con conceptos problemáticos como la "subjetividad" y la "existencia" humanas. Las paradojas continúan sacudiendo nuestro sentido común hoy en día.

---
title: "¿Ver una manzana azul prueba que 'los cuervos son negros'? : Los cuervos de Hempel"
description: "¿Se puede probar la hipótesis de que 'los cuervos son negros' sin ver un solo cuervo? La paradoja de la inducción creada por la equivalencia lógica."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "hempels-ravens"
image: "img/hempels_ravens.jpg"
math: true
mermaid: true
categories: ["Paradojas Matemáticas", "Lógica"]
tags: ["Paradoja", "Inducción", "Equivalencia Lógica", "Contraposición"]
---

¿Cómo prueban las teorías los científicos? Normalmente, utilizan la "inducción", que consiste en observar el mundo y recopilar datos.
Por ejemplo, si quisieras probar la hipótesis de que "todos los cuervos son negros", observarías cuervos en todo el mundo y confirmarías uno por uno que son negros.

Sin embargo, en la década de 1940, el lógico Carl Hempel señaló una extraña laguna lógica oculta en este método científico obvio.
Esta es la paradoja de los **cuervos de Hempel (Hempel's Ravens)**, que afirma que **"solo ver una manzana azul o zapatos rojos sirve como evidencia de que 'los cuervos son negros'"**.

## Sustitución lógica: La magia de la contraposición

Para entender el argumento de Hempel, es necesario recordar el concepto de **"contraposición"** que se aprende en matemáticas de secundaria.

En lógica, si una proposición "Si A entonces B" es verdadera, su contrapositiva "Si no es B entonces no es A" también debe ser verdadera (esto se llama equivalencia lógica).

Hipótesis $H_1$: **"Todos los cuervos son negros (Si es un cuervo, es negro)"**

Tomemos la contrapositiva de esta hipótesis $H_1$.
Se convierte en "Si no es negro, no es un cuervo".

Hipótesis $H_2$: **"Todo lo que no es negro, no es un cuervo"**

Según las reglas de la lógica, $H_1$ y $H_2$ tienen **exactamente el mismo significado (equivalencia)**. Si una se prueba, la otra se prueba automáticamente.

## Probar los cuervos sin ver cuervos

Ahora, para confirmar la hipótesis $H_1$ (los cuervos son negros), cada vez que encontramos un cuervo negro, la certeza (evidencia) de la hipótesis se fortalece un poco.
Todos están de acuerdo con esto.

Sin embargo, dado que $H_1$ y $H_2$ tienen el mismo significado, encontrar evidencia para la hipótesis $H_2$ (lo que no es negro no es un cuervo) debería servir directamente como evidencia para la hipótesis $H_1$.

Entonces, ¿cuál es la evidencia para $H_2$?
Solo necesitas encontrar "algo que no sea negro y no sea un cuervo".

- Supongamos que hay una **"manzana azul"** sobre la mesa. Esta no es negra ni es un cuervo. Por lo tanto, es evidencia que apoya a $H_2$.
- Había **"zapatos rojos"** en el armario. Estos tampoco son negros ni son cuervos. Es evidencia para $H_2$.
- Hay una **"nube blanca"** flotando en el cielo. Esta también es evidencia para $H_2$.

Dado que la evidencia para $H_2$ tiene el mismo valor que la evidencia para $H_1$, lógicamente se extrae la siguiente conclusión extraña.

**"Cuantas más manzanas azules o zapatos rojos observes en una habitación, más se demuestra la validez de la hipótesis de que 'todos los cuervos son negros'"**

```mermaid
graph TD
    A["Proposición H1: Todos los cuervos son negros"] <-->|Equivalencia Lógica (Contraposición)| B["Proposición H2: Lo que no es negro no es un cuervo"]
    
    C["Observación: Cuervo negro"] -->|Sirve de evidencia| A
    D["Observación: Manzana azul"] -->|Sirve de evidencia| B
    
    D -.->|¿Por lo tanto esto también debería ser evidencia?| A
    
    style A fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#2196F3,stroke:#333,color:#fff
    style D fill:#FF9800,stroke:#333,color:#fff
```

## ¿Por qué es contraintuitivo?

No hay ningún ornitólogo en el mundo que profundice su convicción de que "los cuervos son negros" mirando una manzana azul. Aunque debería ser lógicamente impecable, ¿por qué nuestro sentido común lo rechaza?

En el mundo de la filosofía y la estadística se han propuesto varios enfoques para esta paradoja.

### 1. Solución bayesiana (Diferencia en la cantidad de información)

El contraargumento más convincente desde la perspectiva de la estadística moderna (probabilidad bayesiana) se centra en la diferencia en la "fuerza de la evidencia (cantidad de información)".

Hay abrumadoramente más "cosas que no son negras" en el mundo que "cosas negras", y astronómicamente más "cosas que no son cuervos" que "cuervos".

Cuando ves una manzana azul, sin duda es evidencia de que "todos los cuervos son negros", pero **su valor como evidencia (el grado de aumento de probabilidad) está infinitamente cerca de cero**.
Incluso si se confirma una de las innumerables "cosas que no son negras" en el vasto universo, el aumento en la probabilidad de que "los cuervos sean negros" tiene aproximadamente el mismo impacto que quitar un solo grano de arena del desierto. Por otro lado, encontrar directamente un solo cuervo negro tiene un valor de evidencia abrumadoramente mayor.

En resumen, la solución bayesiana es que lógicamente "una manzana azul es evidencia", pero en la práctica "se puede ignorar porque su valor como evidencia es igual a cero".

### 2. Los límites de la "ornitología de interior"

Esta paradoja pone de relieve cuán frágiles son las premisas sobre las que se basa el núcleo de la ciencia, la "inducción (derivar leyes generales a partir de la observación)". Si nos basamos únicamente en la equivalencia lógica, sería posible hacer "ornitología de interior", donde podríamos verificar cualquier ley del universo ("todos los cisnes son blancos", "todos los alienígenas no son verdes", etc.) simplemente observando la basura en nuestra habitación sin salir a la calle.

Los cuervos de Hempel es una paradoja muy interesante que muestra que las palabras "evidencia" y "prueba" que usamos inconscientemente no pueden ser capturadas del todo solo por las reglas de la lógica simbólica pura.

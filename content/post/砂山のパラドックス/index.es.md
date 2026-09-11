---
title: "¿Cuándo deja de ser un montón de arena al quitar un grano?: La paradoja del montón"
description: "¿Dónde está el límite entre un 'montón de arena' y lo que no lo es? Una paradoja filosófica que desafía la esencia de la ambigüedad, desde la antigua Grecia."
date: 2026-09-10T21:00:00+09:00
draft: false
slug: "sorites-paradox"
image: "img/sorites_paradox.jpg"
math: true
mermaid: true
categories: ["Paradojas matemáticas", "Filosofía", "Lógica"]
tags: ["Paradoja", "Ambigüedad", "Sorites", "Lógica difusa"]
---

Imagina que tienes frente a ti un magnífico montón de arena compuesto por 10.000 granos. Cualquiera diría que esto es un "montón de arena".
Ahora quitas un solo grano. 9.999 granos. ¿Sigue siendo un montón de arena, verdad?
Quitas otro grano. 9.998 granos. Esto también sigue siendo un montón de arena.

Repitamos esta operación.
Quitar un solo grano no debería convertir un "montón de arena" en "algo que no es un montón de arena". Sin embargo, si repetimos esta lógica indefinidamente, al final solo quedará un único grano de arena.

**¿Un grano de arena es un "montón de arena"?**

Por supuesto, nadie llamaría "montón de arena" a un solo grano. Sin embargo, nunca negamos la premisa de que "quitar un grano no cambia el hecho de que siga siendo un montón de arena". En algún punto la lógica se quiebra, pero **¿en qué grano exactamente dejó de ser un montón de arena?**

Esta es la **"Paradoja del montón (Paradoja de Sorites)"**, que se remonta al filósofo de la antigua Grecia Eubúlides, del siglo IV a.C.

## Estructura lógica

Esta paradoja puede expresarse en forma de silogismo de la siguiente manera:

**Premisa 1**: Una colección de 10.000 granos de arena es un "montón de arena".
**Premisa 2**: Si se quita un grano de un montón de arena, sigue siendo un "montón de arena".
**Conclusión**: Por lo tanto, un solo grano de arena también es un "montón de arena".

Tanto la premisa 1 como la premisa 2 suenan muy razonables por separado. Sin embargo, al aplicar la premisa 2 repetidamente, se llega a una conclusión claramente errónea.

```mermaid
graph LR
    A["10.000 granos = montón"] -->|Quitar 1 grano| B["9.999 granos = montón"]
    B -->|Quitar 1 grano| C["9.998 granos = montón"]
    C -->|...repetir...| D["100 granos = ¿montón?"]
    D -->|Quitar 1 grano| E["10 granos = ¿montón?"]
    E -->|Quitar 1 grano| F["1 grano = ¿montón?"]
    
    style A fill:#4CAF50,color:#fff
    style D fill:#FF9800,color:#fff
    style E fill:#FF5722,color:#fff
    style F fill:#F44336,color:#fff,stroke-width:3px
```

## ¿Por qué esta paradoja no tiene solución?

El núcleo de la paradoja del montón de arena radica en que **la palabra "montón de arena" es esencialmente ambigua**.
No existe una definición clara (un umbral) de "cuántos granos se necesitan para que sea un montón de arena". Este tipo de concepto se denomina **"predicado vago (vague predicate)"**.

Nuestro lenguaje cotidiano está lleno de palabras ambiguas como estas.

- **"Alto"**: ¿a partir de cuántos centímetros? Una persona de 180 cm es "alta". ¿Y si le quitamos 1 mm? ¿Y otro mm más?
- **"Rico"**: ¿a partir de cuánto patrimonio? Con 10.000 millones de yenes eres "rico". ¿Y si pierdes 1 yen?
- **"Calvo"**: ¿con cuántos cabellos o menos? Con 0 cabellos eres "calvo". ¿Y si te crece uno?

Todos estos casos tienen exactamente la misma estructura que la paradoja del montón de arena.

## Enfoques de los filósofos

### 1. Enfoque epistemológico (el límite sí existe)

Este enfoque sostiene que "en realidad existe un límite claro entre montón y no-montón, pero los seres humanos simplemente no tienen la capacidad de reconocerlo".
Por ejemplo, existiría un límite exacto como "5.837 granos es un montón, pero 5.836 granos no lo es", solo que nosotros no podemos saberlo.

Desde el punto de vista lógico es una postura elegante, pero muchas personas sentirán intuitivamente que algo no encaja.

### 2. Lógica difusa (valores de verdad graduales)

En la lógica clásica solo hay dos opciones: "verdadero o falso". En la lógica difusa, los valores pueden situarse "en algún punto entre 0 y 1".

Por ejemplo:
- 10.000 granos de arena: "grado de montón = 1,0 (completamente montón)"
- 5.000 granos: "grado de montón = 0,7"
- 100 granos: "grado de montón = 0,1"
- 1 grano: "grado de montón = 0,0 (completamente no-montón)"

Este método es práctico, pero no resuelve completamente la paradoja. Porque surge una nueva ambigüedad: "¿cuál es la diferencia entre un grado de montón de 0,7 y 0,699?".

### 3. Supervaluacionismo (Supervaluationism)

Según este enfoque, se consideran simultáneamente todos los límites razonables posibles para la palabra "montón de arena". Si todos los límites coinciden en que es un "montón de arena", entonces es "definitivamente un montón de arena"; si todos coinciden en que es "no-montón", entonces es "definitivamente no un montón de arena"; y el área donde las opiniones difieren se clasifica como "indeterminada".

## Impacto en la sociedad moderna

La paradoja del montón de arena no es un simple juego de palabras; también causa problemas serios en el mundo real de las leyes y las políticas.

- **Mayoría de edad**: A los 17 años y 364 días eres "menor" y a los 18 años y 0 días eres "adulto". ¿Qué cambia esencialmente en un día?
- **Umbral de pobreza**: Si tus ingresos anuales están 1 yen por debajo del estándar eres "pobre", y si están 1 yen por encima no lo eres.
- **Regulaciones ambientales**: Si las emisiones de contaminantes superan el límite en 0,001 mg es ilegal. Si están exactamente en el límite, es legal.

El lenguaje y el pensamiento humano contienen ambigüedad por naturaleza, y quizás sea imposible dividir el mundo en dicotomías claras. La paradoja del montón de arena es una paradoja que muestra los límites fundamentales de la inteligencia humana y que ha desconcertado a los filósofos durante más de 2.400 años.

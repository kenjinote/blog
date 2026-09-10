---
title: 'La paradoja de San Petersburgo: ¿Cuánto pagarías por un juego con un valor esperado "infinito"?'
slug: 'st-petersburg-paradox'
description: 'Un juego que matemáticamente debería hacerte "ganar dinero infinitamente". Sin embargo, nadie en la realidad pagaría una gran suma por él. Explicaremos esta histórica paradoja que puso de manifiesto la discrepancia entre la teoría de la probabilidad y la psicología humana (utilidad), convirtiéndose en la base de la economía moderna.'
date: '2026-09-10T05:00:00+09:00'
image: 'img/st_petersburg.jpg'
math: true
mermaid: true
categories:
  - 'Paradojas matemáticas'
  - 'Teoría de la probabilidad'
tags:
  - 'Paradoja'
  - 'Valor esperado'
  - 'Economía'
  - 'Bernoulli'
---

## 1. El juego de los sueños con un valor esperado "infinito"

Mientras caminas por un casino, un crupier te invita a jugar a un nuevo juego de lanzamiento de moneda.

**[Reglas del juego]**
1. Pagas una cuota de entrada para empezar a jugar.
2. Lanzas una moneda. Si sale **cara**, el premio se duplica y puedes volver a lanzar.
3. Si sale **cruz**, el juego termina. Recibirás el dinero acumulado hasta ese momento.

El premio inicial comienza en 2 dólares.
- Si sale cruz en el primer lanzamiento, recibes **2 dólares** y termina.
- Si sale cara en el primero y cruz en el segundo, recibes **4 dólares** y termina.
- Si sale cara en el primero, cara en el segundo y cruz en el tercero, recibes **8 dólares** y termina.
- ...Y así sucesivamente, mientras siga saliendo cara, el premio se duplica: 16 dólares, 32 dólares, 64 dólares...

```mermaid
graph TD
    Start["Inicio del juego"] --> Toss1{"1er lanzamiento de moneda"}
    
    Toss1 -->|Cruz (1/2)| End1["Fin: Ganas 2 dólares"]
    Toss1 -->|Cara (1/2)| Toss2{"2do lanzamiento de moneda"}
    
    Toss2 -->|Cruz (1/2)| End2["Fin: Ganas 4 dólares"]
    Toss2 -->|Cara (1/2)| Toss3{"3er lanzamiento de moneda"}
    
    Toss3 -->|Cruz (1/2)| End3["Fin: Ganas 8 dólares"]
    Toss3 -->|Cara (1/2)| Toss4{"..."}
    
    Toss4 -.->|Mientras más consecutivas sean| Infinite["¡El premio se duplica infinitamente!"]
```

Ahora, te hago una pregunta.
**Si la entrada para este juego costara "10.000 dólares", ¿participarías?**

Probablemente, la mayoría de la gente respondería "No". Porque hay un 50% de probabilidades de que salga cruz en el primer lanzamiento y ganar solo 2 dólares, perdiendo así mucho dinero.

Sin embargo, si hacemos los cálculos fielmente a la teoría de probabilidades matemáticas (valor esperado), descubrimos un hecho sorprendente. **Matemáticamente hablando, deberías participar en este juego incluso si la entrada costara 10.000 dólares o 1 millón de dólares, incluso si tuvieras que pedir prestado todo el dinero que tienes.**

¿Por qué ocurre esto?

---

## 2. Calculemos el valor esperado

Para determinar matemáticamente si un juego es "rentable o perjudicial", utilizamos un indicador llamado **"valor esperado"**.
El valor esperado es un número que representa "cuánto dinero ganarías en promedio por vez si jugaras a ese juego repetidamente". La fórmula se calcula **sumando todos los resultados de "(premio recibido) × (su probabilidad)"**.

Calculemos el valor esperado de este juego.

- **Probabilidad de que salga cruz en el 1er lanzamiento:** $\frac{1}{2}$
  El premio es de $2$ dólares.
  Contribución al valor esperado = $2 \times \frac{1}{2} = 1$ dólar

- **Probabilidad de que salga cruz en el 2do lanzamiento:** Sale cara y luego cruz, por lo tanto $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$
  El premio es de $4$ dólares.
  Contribución al valor esperado = $4 \times \frac{1}{4} = 1$ dólar

- **Probabilidad de que salga cruz en el 3er lanzamiento:** Sale cara, cara, y cruz, por lo tanto $(\frac{1}{2})^3 = \frac{1}{8}$
  El premio es de $8$ dólares.
  Contribución al valor esperado = $8 \times \frac{1}{8} = 1$ dólar

- **Probabilidad de que salga cruz en el enésimo ($n$) lanzamiento:** $(\frac{1}{2})^n$
  El premio es de $2^n$ dólares.
  Contribución al valor esperado = $2^n \times (\frac{1}{2})^n = 1$ dólar

Es decir, no importa en qué lanzamiento termine el juego, el valor esperado de ese escenario es **siempre "1 dólar"**.
Como el juego puede continuar infinitamente, si sumamos todos estos valores esperados obtenemos lo siguiente:

$$ \text{Valor esperado total} = 1 + 1 + 1 + 1 + \dots = \infty \text{ (infinito)} $$

La respuesta obtenida por las matemáticas fue: **"El valor esperado de este juego es infinito"**.
Dado que el valor esperado es infinito, no importa cuán alta sea la cuota de entrada, teóricamente es un "juego rentable" sin lugar a dudas.

Esta es la **"Paradoja de San Petersburgo"**, planteada por Nicolaus Bernoulli en 1713.
El resultado matemático correcto (que tiene un valor infinito) y el sentido común humano realista (que solo querría pagar unos pocos dólares) están en una fuerte contradicción.

---

## 3. El descubrimiento de la "utilidad" que resuelve la discrepancia entre las matemáticas y los seres humanos

Quien resolvió esta paradoja fue el genial matemático Daniel Bernoulli, primo de Nicolaus. (Recibe este nombre porque presentó su artículo en la Academia de Ciencias de San Petersburgo).

Daniel profundizó en la psicología humana.
Él pensó que **"los seres humanos no juzgan las cosas por la 'cantidad absoluta' de dinero, sino por la 'satisfacción (utilidad)' que el dinero les proporciona"**.

A esto se le llama la **"ley de la utilidad marginal decreciente"**.

### El valor del dinero disminuye según la cantidad que poseas
Por ejemplo, si estás muriendo de sed en un desierto, el primer vaso de agua tiene un valor (satisfacción) por el que "pagarías hasta 10.000 dólares". Sin embargo, a medida que bebes el segundo y tercer vaso, el valor de un vaso de agua disminuye gradualmente. Al llegar al décimo vaso, probablemente dirías "ya no lo quiero ni aunque sea gratis".

Lo mismo ocurre con el dinero.
- "10.000 dólares" para alguien con cero ahorros tienen un valor inmenso que puede salvarle la vida.
- Sin embargo, "10.000 dólares" para Elon Musk, con un patrimonio de miles de millones, solo tienen el mismo valor (satisfacción) que una moneda tirada en la calle.

En otras palabras, aunque el premio aumente infinitamente de 2 dólares $\rightarrow$ 4 dólares $\rightarrow$ 8 dólares $\rightarrow$ 16 dólares..., **la "alegría (utilidad)" que siente un ser humano no aumenta infinitamente en proporción a la cantidad**.

---

## 4. Recalcular el valor esperado usando la "utilidad"

Daniel Bernoulli asumió que "el valor (utilidad) del dinero que siente un ser humano es proporcional al logaritmo ($\log$) de la cantidad".

Si llamamos $x$ a la cantidad de dinero, expresemos el valor (utilidad) humano $u(x)$ mediante una función logarítmica (aquí consideraremos un modelo simple con base 2).

- Utilidad de un premio de $2$ dólares: $\log_2(2) = 1$
- Utilidad de un premio de $4$ dólares: $\log_2(4) = 2$
- Utilidad de un premio de $8$ dólares: $\log_2(8) = 3$
- Utilidad de un premio de $2^n$ dólares: $\log_2(2^n) = n$

La cantidad de dinero se duplica, pero la "alegría" humana solo aumenta poco a poco: 1, 2, 3...
Usemos esta "utilidad" para calcular de nuevo el valor esperado (**utilidad esperada**).

$$ \text{Utilidad esperada} = \sum_{n=1}^{\infty} \left( n \times \left(\frac{1}{2}\right)^n \right) $$
$$ = 1 \cdot \frac{1}{2} + 2 \cdot \frac{1}{4} + 3 \cdot \frac{1}{8} + 4 \cdot \frac{1}{16} + \dots $$

Si calculamos la suma de esta serie infinita, el resultado no es "infinito", sino que **converge a "2"**.
Si calculamos a la inversa la cantidad de dinero que corresponde a una utilidad de "2", obtenemos $2^2 = 4$ dólares.

Es decir, al recalcular incorporando la psicología humana (utilidad), obtenemos una respuesta extremadamente sensata y realista: **"El valor de este juego, según la percepción humana, es de aproximadamente '4 dólares'"**.
Es por eso que no nos sentimos inclinados a pagar 10.000 dólares por jugar.

---

## 5. Resumen: La paradoja que abrió las puertas de la economía

La paradoja de San Petersburgo fue una paradoja revolucionaria que demostró matemáticamente que el número objetivo llamado "cantidad de dinero" y el valor subjetivo llamado "satisfacción humana" no concuerdan.

El concepto de "utilidad (Utility)" propuesto por Daniel Bernoulli se convirtió, tras 200 años, en la base más importante de la microeconomía moderna y la ingeniería financiera (como la teoría de carteras).
Nuestro comportamiento de adquirir seguros o diversificar inversiones también se puede explicar completamente mediante este mecanismo psicológico humano de la "utilidad marginal decreciente (el dolor de una gran pérdida es mucho mayor que la alegría de una gran ganancia)".

Un simple problema matemático sobre un juego de azar sirvió como catalizador para desentrañar la mente humana y dar origen a la vasta disciplina de la economía.

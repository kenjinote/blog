---
title: "Dimensión Fractal y Medida de Hausdorff: La Ciencia de las Dimensiones Fraccionarias y la Autosimilitud Más Allá de la Barrera Entera"
description: "El conjunto de Mandelbrot, la paradoja de la costa y las dimensiones fraccionarias entre 1 y 2 dimensiones. El orden natural revelado por la geometría y la teoría de la medida."
slug: "fractal-dimension-hausdorff-measure"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "physics"]
tags: ["fractal", "hausdorff-dimension", "mandelbrot", "measure-theory"]
image: "eyecatch.jpg"
---

## Introducción: Repensando el concepto de dimensión

El espacio que experimentamos cotidianamente se reconoce como un espacio euclidiano de 3 dimensiones. Una línea sobre el papel es unidimensional, un plano es bidimensional y un cuerpo sólido es tridimensional. Esta es una intuición firme que ha sido la base de la percepción espacial humana durante miles de años desde Euclides en la antigua Grecia. Sin embargo, al observar las formas complejas de la naturaleza, este paradigma de "dimensión entera" se enfrenta a una limitación decisiva. Las nubes no son esferas, las montañas no son conos y las costas no son arcos circulares. Muchas de las formas que se encuentran en el mundo natural, como las ramas de los árboles, las redes de vasos sanguíneos y las trayectorias de los rayos, tienen una "rugosidad" (roughness) que es fundamentalmente diferente de los objetos de la geometría euclidiana suave.

La "geometría fractal" nació como un nuevo lenguaje matemático para describir esta complejidad del mundo natural. Y lo que sustenta su raíz teórica es el concepto de "medida de Hausdorff" y la "dimensión de Hausdorff" asociada, conceptos nacidos de las profundidades del análisis real y la teoría de la medida. En este artículo, explicaremos exhaustivamente cómo se definen y calculan las dimensiones fractales, y cómo se aplican a la comprensión de los fenómenos naturales, desde la geometría intuitiva hasta la rigurosa teoría de la medida.

---

## Capítulo 1: Los límites de la geometría euclidiana y la "rugosidad de la naturaleza"

### La pregunta de Benoit Mandelbrot "¿Cuánto mide la costa de Gran Bretaña?"

Hay una famosa pregunta que simboliza el amanecer de la geometría fractal. "¿Cuánto mide la costa de Gran Bretaña?" (How Long Is the Coast of Britain?), es el título de un artículo publicado por Benoit Mandelbrot en la revista científica "Science" en 1967.

A primera vista, esta pregunta parece ser un mero problema de topografía. Sin embargo, en el fondo se esconde una profunda paradoja. Supongamos que aproximamos la costa para medir su longitud utilizando una regla de cierta longitud (por ejemplo, longitud $\eta = 100 \text{ km}$). ¿Qué sucede con la longitud total medida si hacemos que la longitud de la regla sea cada vez más pequeña ($\eta = 10 \text{ km}, 1 \text{ km}, 1 \text{ m}, \dots$)? Si se trata de una curva suave (como un círculo o una parábola), a medida que la regla se hace más pequeña, converge a un cierto valor finito constante. Esta es la definición clásica de la longitud de una curva (longitud de arco).

Sin embargo, esto no ocurre con las costas reales. Cuanto más pequeña sea la regla, más pequeñas serán las ensenadas y las irregularidades de las rocas que antes pasaban desapercibidas entre las reglas, y la longitud de la costa aumentará infinitamente. En otras palabras, en el límite donde la escala de medición $\eta$ se acerca a $0$, la longitud de la costa $L(\eta)$ diverge hasta el infinito.

### El efecto Richardson

Este fenómeno fue descubierto empíricamente por el meteorólogo Lewis Fry Richardson. Richardson midió las longitudes de las fronteras y costas de varios países a diferentes escalas y descubrió que la siguiente ley de potencias se cumple entre la escala de medición $\eta$ y la longitud medida $L(\eta)$:

$$ L(\eta) \propto \eta^{1-D} $$

Aquí, $D$ es una constante, y cuanto más compleja sea la costa, mayor será el valor de $D$. El propio Richardson trató a $D$ como una constante empírica, pero Mandelbrot le dio una interpretación matemática profunda. Es decir, consideró que este $D$ representa la "dimensión" del objeto.

En el caso de una curva unidimensional suave, $D=1$, y $L(\eta) \propto \eta^0 = 1$, por lo que la longitud converge a un valor constante. Sin embargo, en el caso de límites extremadamente complejos como la costa de Gran Bretaña, $D \approx 1.25$, y dado que $1 - D = -0.25 < 0$, a medida que $\eta \to 0$, se obtiene $L(\eta) \to \infty$. Esta dimensión de número real, mayor que $1$ y menor que $2$, fue el primer brote de la "dimensión fractal".

---

## Capítulo 2: Autosimilitud y dimensión de similitud

La palabra fractal (fractal) proviene de la palabra latina "fractus" (roto, fragmentado), acuñada por Mandelbrot. Una de las características más fundamentales de un fractal es la "autosimilitud" (self-similarity). Se refiere a la propiedad de que cuando se amplía el todo, contiene la misma estructura que el todo en sí mismo.

Aprovechando esta autosimilitud, podemos derivar una definición intuitiva de dimensión llamada "Dimensión de Similitud" (Similarity Dimension).

### Derivación intuitiva de la dimensión de similitud $D$

Consideremos las propiedades de las figuras euclidianas suaves.
- Si un segmento de línea unidimensional se reduce a una escala de $1/r$, se necesitan $r^1$ segmentos reducidos para formar el segmento original.
- Si un cuadrado bidimensional se reduce a $1/r$ en cada lado, se necesitan $r^2$ cuadrados pequeños para formar el cuadrado original.
- Si un cubo tridimensional se reduce a $1/r$ en cada lado, se necesitan $r^3$ cubos pequeños para formar el cubo original.

En general, cuando una figura en un espacio de dimensión $d$ se reduce a $1/r$, el número de copias necesarias $N$ para reconstruir la figura original satisface la relación:
$$ N = r^d $$
Tomando el logaritmo de ambos lados de esta ecuación,
$$ \log N = d \log r $$
y resolviendo para la dimensión $d$, se puede definir de la siguiente manera:

$$ d = \frac{\log N}{\log r} $$

La "dimensión de similitud" es una extensión de esta definición a figuras autosimilares que no tienen una dimensión entera.

$$ D_s = \frac{\log N}{\log(1/r)} $$

Aquí, $r$ es la tasa de reducción ($0 < r < 1$), y $N$ es el número necesario de estas figuras reducidas para cubrir completamente la figura original. (Si $r$ se toma como la tasa de reducción, el denominador es $\log(1/r)$. Tenga en cuenta la definición de los símbolos, ya que en el ejemplo anterior $r$ era el factor de aumento).

### Conjunto de Cantor (Cantor Set)

Introducido por Georg Cantor en 1883, este conjunto es uno de los contraejemplos más importantes en la teoría de la medida.
El método de construcción es el siguiente:
1. Comience con el intervalo $[0, 1]$ (paso 0).
2. Elimine el tercio central $(1/3, 2/3)$ (paso 1: los intervalos son $[0, 1/3] \cup [2/3, 1]$).
3. Elimine el tercio central de cada intervalo restante.
4. Repita esto infinitamente.

El conjunto obtenido en el límite (el conjunto ternario de Cantor) tiene autosimilitud. Está compuesto por $2$ copias del todo reducidas a $1/3$.
Por lo tanto, la dimensión de similitud es
$$ D = \frac{\log 2}{\log 3} \approx 0.6309 $$
Este es un conjunto que es mayor que 0 dimensiones (puntos) y menor que 1 dimensión (líneas). Sorprendentemente, la medida de Lebesgue (longitud) de este conjunto es $0$, pero contiene un número infinito no numerable de puntos.

### Curva de Koch (Koch Curve)

Es una curva continua pero no diferenciable en ninguna parte, ideada por Helge von Koch en 1904.
1. Divida un segmento de línea en 3 partes iguales.
2. Reemplace la sección central por dos lados de un triángulo equilátero que tiene a esta sección como base.
3. Repita esto para todos los segmentos de línea.

En una operación, la longitud del segmento se multiplica por $4/3$. Si se repite infinitamente, la longitud se convierte en $(4/3)^\infty \to \infty$ (longitud infinita). Por otro lado, el área encerrada por esto (el copo de nieve de Koch) es finita. La dimensión de similitud de esta curva, que tiene un área cero y una longitud infinita, se forma mediante el agrupamiento de $N = 4$ copias con una tasa de reducción $r = 1/3$, por lo que
$$ D = \frac{\log 4}{\log 3} \approx 1.2618 $$

### Alfombra de Sierpinski (Sierpinski Gasket)

Es una figura que se obtiene repitiendo la operación de ahuecar un triángulo invertido en el centro de un triángulo equilátero.
Dado que consta de $N = 3$ copias con una tasa de reducción $r = 1/2$, la dimensión de similitud es
$$ D = \frac{\log 3}{\log 2} \approx 1.5849 $$
El área (medida de Lebesgue bidimensional) es 0, pero la longitud unidimensional es infinita.

---

## Capítulo 3: Definición rigurosa de la medida exterior de Hausdorff y la dimensión de Hausdorff

La dimensión de similitud es intuitiva y fácil de calcular, pero solo se puede aplicar a figuras que tengan una "autosimilitud estricta". Para determinar la dimensión de los fractales en la naturaleza y los conjuntos matemáticamente complejos (conjuntos donde la autosimilitud se rompe), es necesaria una definición rigurosa y universal de dimensión basada en el análisis real y la teoría de la medida. Esa es la "Dimensión de Hausdorff" (Hausdorff Dimension).

En 1918, Felix Hausdorff amplió el método de la teoría de la medida de Carathéodory para definir la medida exterior de dimensión $d$ para cualquier número real no negativo $d$.

### $\delta$-cubrimiento ($\delta$-cover)

Considere un subconjunto $E$ de $\mathbb{R}^n$. Para cualquier $\delta > 0$, si una familia de subconjuntos $\{U_i\}_{i=1}^\infty$ de $E$ satisface
$$ E \subset \bigcup_{i=1}^\infty U_i \quad \text{y} \quad \operatorname{diam}(U_i) \leq \delta $$
a esto se le llama un **$\delta$-cubrimiento** de $E$. Aquí, $\operatorname{diam}(U_i)$ es el diámetro (distancia suprema) $\sup_{x,y \in U_i} \|x - y\|$ de $U_i$.

### Medida exterior de Hausdorff $\mathcal{H}^d(E)$

Fijamos un número real no negativo $d \geq 0$. Para cualquier $\delta$-cubrimiento $\{U_i\}$ de $E$, consideramos la suma de la potencia $d$ de cada diámetro, y tomamos su límite inferior.

$$ \mathcal{H}_\delta^d(E) = \inf \left\{ \sum_{i=1}^\infty (\operatorname{diam} U_i)^d \mathrel{\Big|} \{U_i\} \text{ es un } \delta\text{-cubrimiento de } E \right\} $$

A medida que $\delta$ se hace más pequeño, las condiciones de cubrimiento se vuelven más estrictas, por lo que el conjunto de los límites inferiores se estrecha, y $\mathcal{H}_\delta^d(E)$ es monótonamente no decreciente. Por lo tanto, el límite de $\delta \to 0$ existe (incluyendo $\infty$).

$$ \mathcal{H}^d(E) = \lim_{\delta \to 0} \mathcal{H}_\delta^d(E) = \sup_{\delta > 0} \mathcal{H}_\delta^d(E) $$

A esta $\mathcal{H}^d(E)$ se le llama **medida de Hausdorff de dimensión $d$**. En términos de teoría de la medida, esta es una medida exterior con integridad de Borel (que satisface la condición de Carathéodory), y se convierte en una verdadera medida que satisface la aditividad numerable en la familia de conjuntos de Borel.

En el caso de una dimensión entera $d = n$, $\mathcal{H}^n(E)$ difiere de la medida de Lebesgue habitual de dimensión $n$ solo por una multiplicación constante (si se ajusta la constante de normalización, coinciden completamente).

### La dimensión de Hausdorff $\dim_H(E)$ como un valor crítico de salto

La propiedad más importante de la medida de Hausdorff es el comportamiento de $\mathcal{H}^d(E)$ cuando se cambia el valor de $d$.
Supongamos que para un cierto $d$, $\mathcal{H}^d(E) < \infty$. Entonces, para cualquier $s > d$,
$$ \sum (\operatorname{diam} U_i)^s = \sum (\operatorname{diam} U_i)^{s-d} (\operatorname{diam} U_i)^d \leq \delta^{s-d} \sum (\operatorname{diam} U_i)^d $$
Cuando $\delta \to 0$, $\delta^{s-d} \to 0$, por lo que $\mathcal{H}^s(E) = 0$.
Por el contrario, si $\mathcal{H}^s(E) > 0$, entonces para cualquier $d < s$, $\mathcal{H}^d(E) = \infty$.

Es decir, a medida que $d$ aumenta desde $0$, $\mathcal{H}^d(E)$ siempre es $\infty$ hasta un cierto punto crítico, y muestra un "salto" extremo en el que siempre se convierte en $0$ más allá de ese punto crítico. El valor de $d$ en este punto crítico se define como la **Dimensión de Hausdorff (Hausdorff Dimension)**.

$$ \dim_H(E) = \inf \{ d \geq 0 \mid \mathcal{H}^d(E) = 0 \} = \sup \{ d \geq 0 \mid \mathcal{H}^d(E) = \infty \} $$

La abrumadora belleza de esta definición reside en el hecho de que la dimensión está determinada única y estrictamente para los subconjuntos de cualquier espacio métrico, incluso si el conjunto objetivo $E$ no tiene autosimilitud o es un conjunto patológico. Las dimensiones de Hausdorff del conjunto de Cantor y la curva de Koch coinciden exactamente con la dimensión de similitud descrita anteriormente.

---

## Capítulo 4: Dimensión de recuento de cajas (dimensión de capacidad), dimensión de información y dimensión de empaquetamiento

La dimensión de Hausdorff es el concepto matemáticamente más refinado, pero no es adecuado para cálculos numéricos o análisis de datos experimentales (debido a la necesidad de encontrar el límite inferior a partir de infinitos patrones de recubrimiento y luego tomar el límite). Por lo tanto, en matemáticas aplicadas y física, se utilizan definiciones más computables de la dimensión fractal.

### Dimensión de recuento de cajas (Dimensión de capacidad, Box-counting Dimension)

El espacio se divide en una cuadrícula (rejilla) con una longitud de lado $\varepsilon$, y se cuenta el número de cajas (puntos de cuadrícula) $N(\varepsilon)$ que se cruzan con el conjunto objetivo $E$. Entonces, la dimensión de recuento de cajas $\dim_B(E)$ se define de la siguiente manera:

$$ \dim_B(E) = \lim_{\varepsilon \to 0} \frac{\log N(\varepsilon)}{-\log \varepsilon} $$

Esta definición es sumamente práctica y constituye la base del algoritmo (método de cobertura) para estimar la dimensión fractal en el análisis de imágenes y otros campos. Sin embargo, también tiene deficiencias matemáticas. Por ejemplo, la dimensión de recuento de cajas del conjunto de números racionales $\mathbb{Q} \cap [0,1]$ es $1$, pero la dimensión de Hausdorff es $0$ porque es un conjunto numerable. En general, se cumple que $\dim_H(E) \leq \dim_B(E)$.

### Dimensión de información (Information Dimension) y dimensión generalizada

Si un conjunto fractal tiene una distribución no uniforme, simplemente contar cajas no es suficiente. Suponiendo que la medida (probabilidad) contenida en cada caja $i$ es $P_i$, la dimensión de información $D_1$ se define utilizando la entropía de Shannon $I(\varepsilon) = - \sum P_i \log P_i$:

$$ D_1 = \lim_{\varepsilon \to 0} \frac{\sum P_i \log P_i}{\log \varepsilon} $$

Además, esto evoluciona hacia el concepto de la dimensión generalizada (dimensión de Rényi) $D_q$ en la teoría "multifractal" basada en la entropía generalizada de Alfréd Rényi.

### Dimensión de empaquetamiento (Packing Dimension)

La dimensión de empaquetamiento $\dim_P(E)$, introducida por Tricot en la década de 1980, es un concepto dual a la dimensión de Hausdorff. Mientras que la dimensión de Hausdorff toma el enfoque de "recubrir el conjunto", la dimensión de empaquetamiento toma el enfoque de "empaquetar esferas dentro del conjunto".
Estrictamente hablando, se cumple la relación $\dim_H(E) \leq \dim_P(E) \leq \dim_{\overline{B}}(E)$ (dimensión de recuento de cajas superior), convirtiéndola en una herramienta muy poderosa en el análisis probabilístico de conjuntos.

---

## Capítulo 5: Sistemas dinámicos complejos del conjunto de Mandelbrot y el conjunto de Julia

Cuando se habla de geometría fractal, es imposible evitar el mundo de los sistemas dinámicos complejos (Complex Dynamics). En particular, el "conjunto de Mandelbrot" (Mandelbrot set), generado a partir de un mapa cuadrático extremadamente simple en el plano complejo, se considera una de las figuras más complejas y hermosas en la historia de las matemáticas.

### Mapa cuadrático complejo $z_{n+1} = z_n^2 + c$

Consideremos un sistema dinámico parametrizado por un número complejo $c \in \mathbb{C}$. Partiendo de un valor inicial $z_0 = 0$, generamos una sucesión $\{z_n\}$ utilizando la siguiente fórmula de recurrencia:

$$ z_{n+1} = z_n^2 + c $$

El conjunto de parámetros $c$ para los cuales esta sucesión no diverge a medida que $n \to \infty$ y permanece acotada, se llama **conjunto de Mandelbrot $\mathcal{M}$**.

$$ \mathcal{M} = \left\{ c \in \mathbb{C} \mathrel{\Big|} \sup_{n} |z_n| < \infty, \text{ con } z_0 = 0 \right\} $$

Por otro lado, si se fija $c$ y se varía el valor inicial $z_0$, el (límite del) conjunto de valores iniciales para los cuales la sucesión permanece acotada se llama **conjunto de Julia (Julia set)**. El conjunto de Mandelbrot funciona como un catálogo (espacio de parámetros de conectividad) para los innumerables conjuntos de Julia que existen.

### Teorema de Shishikura sobre la dimensión de Hausdorff de la frontera

La frontera $\partial \mathcal{M}$ del conjunto de Mandelbrot tiene una estructura fractal de complejidad inimaginable. No importa cuánto se amplíe, siguen apareciendo copias infinitamente reducidas de pequeños conjuntos de Mandelbrot (mini-Mandelbrots), conectados por innumerables filamentos.

¿Cuál es la medida matemática de la "complejidad" de esta frontera? En 1998, el matemático japonés Mitsuhiro Shishikura demostró un teorema monumental en sistemas dinámicos complejos.

**Teorema (Shishikura, 1998)**
La dimensión de Hausdorff de la frontera $\partial \mathcal{M}$ del conjunto de Mandelbrot es exactamente $2$.
$$ \dim_H(\partial \mathcal{M}) = 2 $$

El hecho de que su dimensión de Hausdorff alcance $2$, que es la dimensión del propio espacio, a pesar de ser una simple frontera ("línea" unidimensional) en un plano (bidimensional), significa que $\partial \mathcal{M}$ se ondula, se pliega y tiene innumerables estructuras diminutas que llenan el espacio hasta el límite en el plano complejo. Sin embargo, el saber si su medida de Lebesgue bidimensional (área) es positiva sigue siendo un problema pendiente extremadamente difícil en las matemáticas modernas.

---

## Capítulo 6: Fractales en la física y el mundo natural

La geometría fractal y la dimensión de Hausdorff han trascendido los límites de las matemáticas puras y han tenido un impacto disruptivo en las ciencias naturales en general, como la física, la biología y la cosmología. La naturaleza parece haber elegido la geometría fractal en lugar de la geometría euclidiana.

### Turbulencia (Turbulence) y mecánica de fluidos

La "turbulencia", el fenómeno más esotérico en la mecánica de fluidos, tiene una estructura fractal. Según la teoría de la cascada de energía (de Richardson y Kolmogorov), los grandes vórtices en la turbulencia se rompen en vórtices más pequeños, y este proceso se repite de manera autosimilar. Calcular la dimensión fractal de la región donde ocurre la disipación de energía (estructura disipativa) es uno de los enfoques hacia el esclarecimiento matemático de las ecuaciones de Navier-Stokes.

### La trayectoria del movimiento browniano $D=2$

El "movimiento browniano (proceso de Wiener)" es el fenómeno en el que partículas diminutas se mueven de forma irregular en líquidos o gases. Si dibujamos la trayectoria de esta partícula en el espacio, la trayectoria será infinitamente irregular y no diferenciable en ninguna parte.
Sorprendentemente, la dimensión de Hausdorff de la trayectoria del movimiento browniano estándar en un espacio de dimensiones $n \geq 2$ es estrictamente $2$ con probabilidad 1.
$$ \dim_H(\text{Brownian path}) = 2 \quad \text{almost surely} $$
Esto indica que, aunque es una curva generada a partir de un parámetro de tiempo unidimensional, explora el espacio con tanta densidad que tiene una extensión espacial equivalente al área de un espacio bidimensional.

### Estructura a gran escala de las galaxias (Cosmología)

Al mirar el cielo nocturno, las estrellas parecen estar dispersas aleatoriamente, pero cuando la distribución de las galaxias a gran escala en el universo se mapea tridimensionalmente (como en el Sloan Digital Sky Survey), surge la "estructura a gran escala del universo" que consiste en supercúmulos en forma de filamentos y gigantescos vacíos (voids). El análisis de la función de correlación de esta distribución de materia sugiere que tiene autosimilitud con una dimensión fractal de $D \approx 1.2$ a $2.0$ a una cierta escala. La autoorganización de la materia debido a la gravedad está produciendo fractales.

### Red de transporte óptima de los alvéolos y los vasos sanguíneos

Los fractales también son omnipresentes en el campo de la biología. Los pulmones humanos (la estructura de ramificación de los bronquios), el sistema cardiovascular y las redes neuronales del cerebro tienen estructuras fractales.
¿Por qué la selección natural eligió los fractales? Es porque es la solución óptima para "empaquetar un área de superficie infinita en un volumen (espacio) finito". La ramificación fractal de los bronquios maximiza el área de superficie para el intercambio de oxígeno mientras mantiene constante el volumen de los pulmones, y minimiza la pérdida de energía para bombear la sangre a las células en cada rincón del cuerpo. El mecanismo de optimización de la vida es perfectamente coherente con las leyes matemáticas de las dimensiones fractales.

## Conclusión: La continuidad de las dimensiones y una nueva visión de la naturaleza

La "dimensión entera" que nos dio la geometría euclidiana fue un modelo de aproximación extremadamente útil para que el cerebro humano simplificara y comprendiera el mundo. Sin embargo, los "fractales" y la "dimensión de Hausdorff" creados por el desarrollo de la teoría de la medida y la intuición de Mandelbrot han demostrado que las dimensiones no toman valores discretos de $0, 1, 2, 3$, sino que pueden existir como un continuo de números reales.

La dimensión de Hausdorff es la medida definitiva para cuantificar la "rugosidad", los "detalles infinitos" y el "orden que se esconde dentro del caos" presentes en el mundo natural. Desde las costas, los árboles, los relámpagos y la estructura del universo, hasta la estructura de nuestros propios cuerpos, se puede decir que el fractal es el lenguaje de diseño universal del cosmos.

El hecho de que la teoría de la medida (la medida exterior de Hausdorff), que es la cumbre de la abstracción matemática, describa la realidad del mundo físico con tanta precisión nos deja una fuerte impresión de la misteriosa correspondencia que existe entre las matemáticas y las ciencias naturales. La geometría fractal ha cambiado fundamentalmente la forma en que vemos el mundo.

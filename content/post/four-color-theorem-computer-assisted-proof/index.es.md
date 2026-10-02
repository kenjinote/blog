---
title: "El teorema de los cuatro colores y la revolución de las matemáticas computacionales: un enigma de 100 años y la filosofía de la demostración por máquina"
description: "Historia de las matemáticas en torno al problema de la coloración de mapas planos. Desde la falsa demostración de Kempe hasta la primera demostración asistida por computadora de Appel y Haken, y la redefinición de la 'belleza' matemática."
slug: "four-color-theorem-computer-assisted-proof"
date: "2026-10-03T05:00:00+09:00"
categories: ["mathematics", "computer-science"]
tags: ["graph-theory", "combinatorics", "formal-proof", "mathematics-history"]
image: "eyecatch.jpg"
---

Uno de los teoremas más famosos, y al mismo tiempo más controvertidos, en la historia de las matemáticas es el "Teorema de los cuatro colores" (Four Color Theorem). Aunque es una afirmación tan simple que incluso un niño de primaria puede entenderla: "cuatro colores son suficientes para colorear cualquier mapa plano de modo que las regiones adyacentes tengan colores diferentes", su demostración requirió más de un siglo de tiempo y un cambio de paradigma que sacudió los cimientos de la disciplina matemática: la "demostración por computadora".

En este artículo, desentrañaremos la totalidad del teorema de los cuatro colores desde perspectivas matemáticas, históricas y filosóficas, comenzando con una simple pregunta en 1852, pasando por los desafíos y fracasos de los genios, hasta alcanzar el pináculo de las matemáticas modernas que se han aliado con la nueva inteligencia de las computadoras. En particular, exploraremos temas matemáticos profundos, como la estructura geométrica de la falsa demostración de Kempe y el contraejemplo de Heawood, la demostración completa del teorema de los cinco colores, las matemáticas del método de descarga, el algoritmo de Appel y Haken, los detalles de la demostración formal usando Coq, y la relación con la complejidad NP-completa.

## Capítulo 1: 1852, la ingenua pregunta de Francis Guthrie y su sublimación en la teoría de grafos

### Planteamiento del problema de la coloración de mapas
La historia comienza en 1852 con Francis Guthrie, un joven que acababa de graduarse del University College de Londres en el Reino Unido. Mientras coloreaba un mapa de los condados de Inglaterra, notó un hecho peculiar: "¿Acaso no son suficientes 4 colores para colorear cualquier mapa, por complejo que sea, de forma que los condados adyacentes tengan colores distintos?".

Francis compartió esta pregunta con su hermano menor, Frederick Guthrie, quien entonces estudiaba matemáticas en el University College. Frederick le presentó el problema a su supervisor académico, Augustus De Morgan, uno de los principales matemáticos de la época. De Morgan se sintió inmediatamente atraído por la intriga del problema y lo compartió por carta con sus amigos, incluido William Rowan Hamilton. Este fue el momento en que nació el "problema de los cuatro colores", que brilla con luz propia en la historia de las matemáticas.

### El teorema de los poliedros de Euler y la dualidad de los grafos planos
Para tratar el problema de colorear mapas con rigor matemático, es indispensable formularlo en el marco de la teoría de grafos. Si consideramos cada región (país o estado) en el mapa como un "Vértice" (Vertex) y conectamos las regiones adyacentes con una "Arista" (Edge), obtenemos un "Grafo Plano" (Planar Graph) donde las aristas no se cruzan en el plano. Esta transformación se conoce como la operación de tomar el "Grafo Dual" (Dual Graph). Las fronteras del mapa original corresponden a las aristas del grafo, y las caras corresponden a los vértices.

El problema de los cuatro colores se reduce al problema de coloración de vértices (Vertex Coloring Problem) de grafos: "¿Es posible colorear los vértices de cualquier grafo plano con 4 colores de manera que los vértices adyacentes tengan colores diferentes?".

Aquí, el teorema de los poliedros descubierto por Leonhard Euler juega un papel extremadamente importante. En un grafo plano conexo, si $V$ es el número de vértices, $E$ el número de aristas y $F$ el número de caras, se cumple la siguiente relación invariante:

$$V - E + F = 2$$

Al combinar este teorema con las propiedades básicas de los grafos planos, se pueden derivar fuertes restricciones sobre la estructura de un grafo plano. Supongamos que el grafo es un grafo simple, sin aristas múltiples ni bucles (self-loops), y consideremos además un "Grafo Plano Maximal" (Maximal Planar Graph), donde todas las caras son triángulos. Como cualquier grafo plano puede convertirse en un grafo plano maximal añadiendo aristas sin aumentar el número cromático, es suficiente demostrar el teorema de los cuatro colores para los grafos planos maximales.

En un grafo plano maximal, cada cara está rodeada por exactamente 3 aristas. Como una arista limita exactamente 2 caras, se establece estrictamente la siguiente relación entre el número de caras y el número de aristas:

$$3F = 2E$$

Sustituyendo esto en la fórmula de Euler para eliminar $F$. Si sustituimos $F = \frac{2}{3}E$ en $V - E + F = 2$, tenemos:

$$V - E + \frac{2}{3}E = 2 \implies V - \frac{1}{3}E = 2 \implies 3V - E = 6 \implies E = 3V - 6$$

En un grafo plano simple general, dado que una cara está rodeada por 3 o más aristas, tenemos $3F \leq 2E$, lo que lleva a la siguiente desigualdad:

$$E \leq 3V - 6$$

Esta desigualdad muestra que hay un límite estricto en la densidad de aristas en un grafo plano. A partir de aquí, consideremos el grado de cada vértice (Degree, $\deg(v)$). La suma de los grados de todos los vértices en un grafo es exactamente el doble del número de aristas (Lema del apretón de manos).

$$\sum_{v \in V} \deg(v) = 2E$$

Usando la desigualdad anterior $2E \leq 6V - 12$, tenemos:

$$\sum_{v \in V} \deg(v) \leq 6V - 12$$

Dividiendo ambos lados por el número de vértices $V$, obtenemos el grado promedio de los vértices:

$$\frac{1}{V} \sum_{v \in V} \deg(v) \leq 6 - \frac{12}{V} < 6$$

El hecho de que el grado promedio sea estrictamente menor que 6 demuestra matemáticamente y por completo que "al menos un vértice debe tener un grado de 5 o menos". Es decir, en cualquier grafo plano simple, existe al menos un vértice con grado 1, 2, 3, 4 o 5. Este hecho es el punto de partida más fundamental del concepto de "configuración inevitable", que se describirá más adelante, y el pilar absoluto en la demostración del teorema de los cuatro colores.

## Capítulo 2: La "demostración" de Alfred Kempe y su colapso 11 años después

### El concepto de las cadenas de Kempe y la brillante "demostración"
En 1879, Alfred Bray Kempe, un abogado y matemático británico, publicó finalmente una "demostración" del problema de los cuatro colores en las revistas "Nature" y "American Journal of Mathematics". Su demostración fue extremadamente ingeniosa y fue aceptada como correcta por la comunidad matemática mundial durante los 11 años siguientes.

El núcleo de la demostración de Kempe fue una idea revolucionaria que hoy se conoce como la "Cadena de Kempe" (Kempe Chain). Él utilizó inducción matemática. Asumió que el teorema de los cuatro colores era válido para todos los grafos planos con $k$ vértices e intentó demostrar que también se cumplía para grafos con $k+1$ vértices.

Por el teorema de Euler mencionado anteriormente, en un grafo plano $G$ con $k+1$ vértices siempre existe un vértice $v$ de grado 5 o menos. Consideremos el grafo $G'$ obtenido al eliminar el vértice $v$ y las aristas conectadas a él de $G$. Como $G'$ tiene $k$ vértices, por la hipótesis de inducción puede ser coloreado con 4 colores (aquí, rojo, azul, verde y amarillo). Luego, se intenta restaurar $v$ y colorearlo.

1. **Si el grado de $v$ es 3 o menos:** El vértice $v$ tiene como máximo 3 vértices adyacentes. Por lo tanto, al menos 1 de los 4 colores no está siendo utilizado por los vértices adyacentes. La demostración se completa pintando $v$ con el color no utilizado.
2. **Si el grado de $v$ es 4:** Supongamos que los 4 vértices adyacentes a $v$ ($v_1, v_2, v_3, v_4$ en el sentido de las agujas del reloj) están coloreados con colores diferentes (rojo, azul, verde, amarillo). Ahora consideremos el subgrafo extraído de todo el grafo que contiene solo los vértices coloreados de "rojo" y "verde", y las aristas que los conectan. Si $v_1$ (rojo) y $v_3$ (verde) no están conectados dentro de este subgrafo rojo-verde (es decir, no hay un camino de $v_1$ a $v_3$ siguiendo solo vértices rojos y verdes), entonces podemos invertir los colores (rojo a verde y verde a rojo) de la componente conexa que contiene a $v_1$. Esto se llama "inversión de la cadena de Kempe". Después de la inversión, $v_1$ se vuelve verde, y los colores circundantes se reducen a 3 colores: azul, verde, verde y amarillo. Esto permite colorear $v$ de rojo. Si $v_1$ y $v_3$ están conectados, debido a las propiedades topológicas del grafo plano (Teorema de la curva de Jordan), el camino rojo-verde que conecta $v_1$ y $v_3$ separa a $v_2$ (azul) de $v_4$ (amarillo). Por lo tanto, $v_2$ y $v_4$ nunca pueden estar conectados por una cadena de Kempe azul-amarilla, y podemos invertir la componente azul-amarilla que contiene a $v_2$. En cualquier caso, los colores alrededor de $v$ se pueden reducir a 3, lo que permite colorear $v$.
3. **Si el grado de $v$ es 5:** Consideremos el caso en el que los 5 vértices adyacentes a $v$, $v_1, v_2, v_3, v_4, v_5$, están coloreados con rojo, azul, verde, amarillo y rojo respectivamente (como son 5, un color se repite). Kempe extendió la lógica del caso de grado 4, y argumentó que combinando hábilmente la inversión de 2 cadenas de Kempe diferentes (por ejemplo, la cadena rojo-verde y la cadena rojo-amarilla), siempre se podrían reducir los colores alrededor de $v$ a 3 o menos. Su método aplicaba doblemente la lógica de que si una está conectada, la otra está separada.

Esta demostración era intuitiva, hermosa y parecía no tener lagunas lógicas. Los matemáticos de la época creyeron sin dudar que el problema de los cuatro colores se había resuelto por completo con esto.

### El grafo de contraejemplo de Heawood: el defecto fatal del "cruce de cadenas de Kempe dobles"
Sin embargo, en 1890, un matemático llamado Percy John Heawood, que entonces tenía 29 años, leyó cuidadosamente el artículo de Kempe y descubrió un salto lógico fatal en la argumentación respecto al vértice de grado 5.

Kempe había asumido implícitamente que al invertir dos cadenas de Kempe (por ejemplo, una azul-verde y otra azul-amarilla) por separado, se podían invertir independientemente una de la otra. Sin embargo, Heawood demostró de manera geométrica y rigurosa que si estas dos cadenas compartían algunos vértices, al invertir la primera cadena el estado de coloración del grafo cambiaba, y la conectividad de la segunda cadena se veía alterada.

Heawood construyó un grafo de contraejemplo específico (ahora conocido como el "grafo de Heawood" o sus derivados, un grafo plano maximal de 25 vértices). En este grafo, si se aplica el algoritmo de Kempe para reducir los colores alrededor del vértice $v$ de grado 5, al momento de invertir la cadena azul-verde, la cadena azul-amarilla (que originalmente no estaba conectada) se conecta. Si luego se invierte la cadena azul-amarilla, los vértices verdes invertidos previamente vuelven a su color original, resultando en un bucle donde el número de colores no disminuye.

El "intercambio simultáneo de cadenas de Kempe dobles" de Kempe fue una falacia resultante de subestimar el complejo entrelazamiento de los grafos planos; no lograba mantener a nivel global las relaciones de separación topológica local. Con este descubrimiento, la demostración de Kempe del teorema de los cuatro colores se derrumbó por completo.

### La demostración matemática completa del teorema de los cinco colores
Aunque la demostración de Kempe se derrumbó, Heawood no solo destruyó. Reconoció que la idea de Kempe (la cadena de Kempe) en sí misma era extremadamente útil, y la empleó para demostrar rigurosamente el "Teorema de los cinco colores" (Five Color Theorem): "todo grafo plano siempre puede colorearse con 5 colores". El proceso completo de demostración del teorema de los cinco colores es el siguiente:

**Teorema:** Todo grafo plano $G$ puede colorearse en sus vértices con 5 colores.
**Demostración:** Se usa inducción matemática sobre el número de vértices $n$.
El caso $n \leq 5$ es trivial. Asumimos que todos los grafos planos con $n=k$ pueden colorearse con 5 colores, y consideramos un grafo plano $G$ con $n=k+1$.
Por el hecho derivado de la fórmula de Euler, en $G$ siempre existe un vértice $v$ de grado 5 o menos.
El grafo $G' = G - \{v\}$ obtenido al quitar $v$ de $G$ tiene $k$ vértices, por lo que por la hipótesis de inducción puede colorearse con 5 colores (Color 1, Color 2, Color 3, Color 4, Color 5).
Consideremos restaurar $v$ manteniendo la coloración de $G'$.
- **Caso 1: Cuando $\deg(v) < 5$.** Como los vértices adyacentes a $v$ son a lo sumo 4, al menos 1 de los 5 colores no es usado por los vértices adyacentes. Ese color se le puede asignar a $v$.
- **Caso 2: Cuando $\deg(v) = 5$.** Supongamos que los 5 vértices adyacentes a $v$, $v_1, v_2, v_3, v_4, v_5$ (ubicados en el sentido de las agujas del reloj) están todos coloreados con colores diferentes (en orden Color 1, Color 2, Color 3, Color 4, Color 5). (Si el mismo color se usa 2 o más veces, quedará más de un color sin usar, que se le puede pintar a $v$).
Ahora, en el grafo $G'$, consideremos el subgrafo inducido compuesto solo por los vértices coloreados con Color 1 y Color 3, y sea $C_{13}$ la componente conexa que contiene a $v_1$ (esta es la cadena de Kempe).
  - **Subcaso 2a: Cuando $v_3 \notin C_{13}$.** Es decir, cuando no hay un camino de $v_1$ a $v_3$ que pase solo por los vértices de Color 1 y Color 3. En este caso, incluso si se invierten los colores de todos los vértices en $C_{13}$ (Color 1 $\leftrightarrow$ Color 3), la validez de la coloración se mantiene. Tras la inversión, $v_1$ pasa a tener el Color 3, y como $v_3$ también tiene el Color 3, el Color 1 deja de existir alrededor de $v$. Por lo tanto, a $v$ se le puede pintar el Color 1.
  - **Subcaso 2b: Cuando $v_3 \in C_{13}$.** Es decir, cuando existe un camino $P_{13}$ que conecta $v_1$ y $v_3$ compuesto de vértices del Color 1 y Color 3. Al combinar este camino $P_{13}$ con el vértice $v$ y las aristas $(v, v_1), (v, v_3)$, se forma una curva cerrada (ciclo) en el plano. Por la naturaleza de los grafos planos (Teorema de la curva de Jordan), este ciclo divide el plano en un interior y un exterior.
  Los vértices $v_2$ y $v_4$ están ubicados en lados opuestos (uno adentro y otro afuera) de este ciclo.
  Ahora consideremos la cadena de Kempe $C_{24}$ compuesta por vértices coloreados con Color 2 y Color 4. Si asumimos que $v_2$ y $v_4$ están conectados por esta cadena, debe existir un camino $P_{24}$ que conecte $v_2$ y $v_4$. Sin embargo, $P_{24}$ debe correr por el grafo plano sin cruzarse, y no puede atravesar el ciclo formado por $P_{13}$ (lo cual contradice la definición de grafo plano).
  Por lo tanto, el camino de Color 2 y Color 4 que conecta $v_2$ y $v_4$ no existe bajo ninguna circunstancia. En otras palabras, la cadena de Kempe de Color 2 - Color 4, $C_{24}$, que contiene a $v_2$, no incluye a $v_4$.
  Así, si invertimos los colores en $C_{24}$ (Color 2 $\leftrightarrow$ Color 4), $v_2$ tomará el Color 4, y el Color 2 desaparecerá de alrededor de $v$. Finalmente, a $v$ se le puede pintar el Color 2.

Por todo lo expuesto, en todos los casos es posible colorear $v$, y el teorema de los cinco colores queda completamente demostrado por inducción matemática. $\blacksquare$

Esta demostración aprovecha la topología de los grafos planos (Teorema de la curva de Jordan) de manera exquisitamente hermosa, mostrando cuán robusto es el concepto de "cadena de Kempe" de Kempe cuando se aplica a una sola cadena sin intersecciones. Sin embargo, el camino hacia los "cuatro colores" se adentrará a partir de aquí en un inmenso mar computacional, atravesando los nuevos paradigmas de "reducibilidad" y "conjunto inevitable".

## Capítulo 3: Las matemáticas del método de descarga (Discharging Method) y la derivación de configuraciones inevitables

Después de Heawood, los matemáticos empezaron a asumir que existía un "contraejemplo mínimo" (Minimum Counterexample) que no podía colorearse con cuatro colores, y comenzaron a explorar por reducción al absurdo qué tipo de estructura debía (o no debía) tener. Aquí es donde se vuelven importantes dos poderosos conceptos: "Configuración reducible" (Reducible Configuration) y "Conjunto inevitable" (Unavoidable Set).

### Reducibilidad (Reducibility)
Una configuración reducible es un arreglo local de vértices (patrón) que "si todo el grafo no se puede colorear con cuatro colores (es el contraejemplo mínimo), entonces tal patrón no puede existir en absoluto dentro del grafo".
Por ejemplo, "un vértice de grado 3 o menor" o "un vértice de grado 4" son configuraciones reducibles. Porque, como se mencionó antes, usando la reducción con la cadena de Kempe, si llegaran a existir, el problema podría reducirse a un grafo más pequeño, lo que contradice el supuesto de ser el "contraejemplo mínimo".
En 1913, George David Birkhoff demostró que una configuración específica de 6 vértices llamada el "Diamante de Birkhoff" también era reducible. El descubrimiento de configuraciones reducibles progresaba, pero si no se podía garantizar que estuvieran "siempre presentes" en el grafo, no llevaría a una demostración.

### Estructura matemática del método de descarga (Discharging Method)
La estrategia definitiva para demostrar el teorema de los cuatro colores se resume en: **"encontrar un conjunto inevitable compuesto íntegramente por configuraciones reducibles"**.
Un conjunto inevitable es una lista de configuraciones tal que "cualquier grafo plano (más precisamente, un grafo plano maximal) debe contener al menos una de las configuraciones del conjunto".

El arma extremadamente poderosa para construir y probar este conjunto inevitable es el "Método de descarga" (Discharging Method), perfeccionado por Heinrich Heesch. El método de descarga es una técnica casi mágica en la teoría de grafos para demostrar teoremas estructurales, utilizando una analogía con el concepto de carga en electromagnetismo.

El proceso matemático del método de descarga es el siguiente:
1. **Asignación de carga inicial:**
   A cada vértice $v$ del grafo plano maximal, se le asigna una carga inicial (Initial Charge) $ch(v)$ de la siguiente manera:
   $$ch(v) = 6 - \deg(v)$$
   Por la ecuación $\sum_{v} (6 - \deg(v)) = 12$ derivada de la fórmula de Euler, la suma total de la carga inicial en todo el grafo es estrictamente 12 (un valor positivo).
   En este caso, un vértice de grado 5 tiene carga $+1$, un vértice de grado 6 tiene $0$, y un vértice de grado 7 o superior tiene carga negativa. (Como podemos asumir que el contraejemplo mínimo no tiene vértices de grado 4 o menor, consideramos el grado mínimo como 5).

2. **Definición de las reglas de transferencia de carga (Discharging Rules):**
   Luego, se definen reglas para transferir la carga entre vértices adyacentes. La idea básica es "fluir (descargar) la carga desde un vértice con carga positiva (es decir, grado 5) hacia un vértice con carga negativa (vértices de grados más altos, de grado 7 o más)".
   Por ejemplo, se pueden establecer cientos de reglas detalladas, como "Si un vértice $v$ de grado 5 es adyacente a un vértice $u$ de grado 7, transfiere $\frac{1}{5}$ de carga de $v$ a $u$".

3. **Derivación de la contradicción e identificación de configuraciones inevitables:**
   Según las reglas definidas, se completan todas las transferencias de carga (Discharging). Dado que la transferencia de carga es simplemente un intercambio interno en el grafo, la suma total de las cargas sigue siendo 12 (positivo) después de la transferencia.
   $$ \sum_{v \in V} ch'(v) = 12 > 0 $$
   (donde $ch'(v)$ es la carga del vértice $v$ tras la transferencia)
   Que la suma total sea positiva significa que **"incluso después del movimiento de las cargas, debe existir al menos un vértice con una carga positiva"**.

   Aquí, se analiza la carga final $ch'(v)$ de cada vértice basándose en la estructura local (el patrón de grados del vértice y sus adyacentes). Si se puede probar que "un vértice que carece de una cierta configuración particular siempre terminará con una carga final de cero o menos bajo las reglas de descarga", entonces para que la carga final sea positiva, esa "configuración particular" debe estar forzosamente en algún lugar del grafo.
   De esta manera, el listado exhaustivo de todos los patrones de configuraciones locales que dan lugar a una carga final positiva conforma el "conjunto inevitable".

Heesch estaba convencido de que usando este método de descarga se podría construir un conjunto inevitable compuesto de una cantidad finita (probablemente miles) de configuraciones reducibles. Sin embargo, la complejidad computacional para determinar si una configuración es "reducible" explota exponencialmente con la longitud de su frontera. Era imposible para un cálculo manual humano comprobar la reducibilidad de miles de configuraciones, ni siquiera dedicando toda una vida a ello.

## Capítulo 4: 1976, el algoritmo de verificación por computadora de Appel y Haken

### Definición de la D-reducción y C-reducción
En la década de 1970, Kenneth Appel y Wolfgang Haken de la Universidad de Illinois iniciaron un proyecto histórico fusionando el método de descarga de Heesch con el poder de cómputo de las computadoras.

La tarea computacional más intensa que abordaron fue la "evaluación de reducibilidad" de configuraciones. Hay principalmente dos tipos de reducibilidad:
- **D-reducibilidad (D-reducibility / Direct reducibility):** Consiste en comprobar, para todos los posibles patrones de 4 colores del anillo (Ring) fronterizo que rodea una configuración, si dicha coloración puede extenderse hacia el interior, o si puede transformarse en un patrón extensible al interior invirtiendo las cadenas de Kempe de la frontera. Si esto se confirma, se puede afirmar de inmediato que la configuración no está incluida en el contraejemplo mínimo.
- **C-reducibilidad (C-reducibility / Contracting reducibility):** Si hay un patrón que falla en la prueba de D-reducibilidad, se considera un grafo más pequeño en el que se "contrae" (colapsa múltiples vértices en uno) una parte de la configuración. Este enfoque muestra que, si el grafo contraído es 4-coloreable, entonces el grafo original también es 4-coloreable.

### Algoritmo para la comprobación de colorabilidad de la frontera en anillo
La computadora (IBM 360) se encargó de ejecutar algoritmos para determinar la D-reducibilidad y C-reducibilidad de una enorme cantidad de candidatas a configuraciones.

Supongamos que una configuración $C$ tiene un anillo fronterizo $R$ (de longitud $k$). Las combinaciones de coloración con 4 colores de los vértices en el anillo pueden llegar a ser hasta $4^k$, lo que sigue siendo un número inmenso incluso teniendo en cuenta las simetrías. Por ejemplo, si la longitud del anillo es $k=14$, es necesario verificar la validez de cerca de 200,000 patrones de coloración de fronteras.
El algoritmo procedió de la siguiente manera:
1. Generar el conjunto de todos los patrones válidos de 4 colores del anillo fronterizo $R$.
2. Probar todos los métodos reales para colorear el interior de la configuración $C$ con 4 colores, y registrar con qué patrón fronterizo coincide (si es extendible internamente).
3. Para aquellos patrones fronterizos que no se puedan extender internamente, simular la inversión de las cadenas de Kempe. Si la inversión lleva a un patrón que ya se sabe que es "extendible internamente", entonces ese patrón inicial se considera "resuelto".
4. Repetir esta búsqueda de transiciones de inversión, y si todos los patrones fronterizos pueden resolverse, entonces la configuración $C$ se determina como "D-reducible".

A medida que aumentaba la longitud de la frontera, el tiempo de cálculo explotaba. Por tanto, Appel y Haken se limitaron a configuraciones con anillos de una longitud máxima de 14 y ajustaron a fondo las reglas de descarga para construir el conjunto inevitable dentro de esos límites. Este proceso de ajuste en sí mismo consistió en un enorme proceso de ensayo y error continuo entre los humanos y la computadora. El proceso interactivo de "los humanos modifican las reglas de descarga, la computadora genera posibles conjuntos inevitables y prueba la reducibilidad, y al ver las configuraciones fallidas los humanos modifican nuevamente las reglas" continuó durante varios años.

### 1200 horas de cálculo y el "Q.E.D."
En 1976, finalmente encontraron un conjunto inevitable de **1,936** configuraciones, derivado mediante reglas de descarga meticulosamente elaboradas. Y tras más de 1200 horas de ejecución del mainframe en la Universidad de Illinois, la computadora verificó que cada una de esas 1,936 configuraciones era D-reducible o C-reducible.

Ellos escribieron brevemente en el resumen de su artículo:
*"Every planar map is four colorable." (Todo mapa plano es coloreable con cuatro colores).*

El sello de correos del departamento de matemáticas de la Universidad de Illinois llevaba impreso con orgullo "FOUR COLORS SUFFICE (Cuatro colores bastan)". Este fue un evento monumental en la historia de las matemáticas, la primera vez en que una computadora se encargó de los pasos deductivos centrales en la demostración de un teorema.

## Capítulo 5: La conmoción en la comunidad matemática y la filosofía de la "Demostración"

El anuncio de Appel y Haken causó profunda confusión y un acalorado debate, en lugar de júbilo, en la comunidad matemática.

### ¿Una demostración ilegible para un humano es matemática?
En la tradición matemática que se remonta a la antigua Grecia, una "demostración" ha sido algo en lo que los matemáticos humanos pueden seguir los pasos lógicos uno por uno y entenderla y convencerse desde el fondo de su corazón. Se creía que el proceso de demostración albergaba conocimientos profundos sobre "por qué se cumple un teorema" y la belleza de su estructura.

Sin embargo, la demostración del teorema de los cuatro colores era ajena a esto. El artículo solo contenía una lista de 1,936 configuraciones y una explicación del algoritmo informático. El rastro (registro de ejecución) real de las verificaciones de reducibilidad era tan inmenso que ni siquiera se podía imprimir en papel. Es imposible para cualquier matemático brillante, aunque dedique toda su vida, seguir los cálculos a mano y comprobar que no hay defectos lógicos.

Se originó una situación sin precedentes: "Para creer en la veracidad de la demostración, uno debe creer que el hardware de la computadora no funcionó mal, y que el programa en lenguaje ensamblador escrito por Appel y Haken no contenía errores de código".

El filósofo de la ciencia Thomas Tymoczko criticó que la demostración había decaído desde la búsqueda de una verdad apriorística de las matemáticas puras hacia una ciencia empírica o experimental como la física. La propia definición de la acción de "demostrar" enfrentaba una crisis epistemológica.

### Refutaciones y simplificación por RSST
Appel y Haken contrarrestaron estas críticas: "Las matemáticas no son sólo demostraciones hermosas. Existen problemas intrínsecamente complejos que exigen enormes divisiones de casos, y si superan los límites del cerebro humano, pedir ayuda al poder de la máquina es una evolución inevitable".

Para disipar las dudas, muchos matemáticos intentaron simplificar y volver a verificar la demostración. En 1997, Neil Robertson, Daniel P. Sanders, Paul Seymour y Robin Thomas (conocidos colectivamente como RSST) publicaron una nueva demostración que mejoraba el método de descarga haciéndolo más sistemático y fácil de verificar para humanos, y redujo el tamaño del conjunto inevitable de 1,936 a 633 configuraciones. El algoritmo fue refinado y se completaba en cuestión de horas.

Sin embargo, esto seguía dependiendo de "los cálculos de reducibilidad realizados por computadora". Aún no se ha encontrado una "demostración hermosa de papel y lápiz" completamente comprensible para la intuición humana (y muchos especialistas en teoría de grafos creen que, en principio, dicha demostración no existirá).

## Capítulo 6: La demostración formal completa de Georges Gonthier mediante Coq

¿Qué debería hacerse para disipar matemáticamente y por completo la ansiedad de que "el programa pudiera tener fallos"? La respuesta final a esto es la "Formalización" (Formalization) completa usando un "Asistente de demostración de teoremas" (Proof Assistant).

En 2005, Georges Gonthier del Instituto Nacional de Investigación en Informática y Automática de Francia (INRIA) y Microsoft Research, junto con Benjamin Werner, lograron formalizar con éxito la demostración del teorema de los cuatro colores desde cero, utilizando el asistente de demostración Coq.

### Hipermapas (Hypermap) y la formalización de la topología combinatoria
Coq es un sistema que parte de los axiomas matemáticos para describir y verificar computacionalmente pruebas según un sistema extremadamente riguroso de reglas lógicas (Cálculo de construcciones inductivas: Calculus of Inductive Constructions).

El mayor logro de Gonthier fue traducir el objeto intuitivo y geométrico de los grafos planos a una estructura combinatoria y algebraica perfecta que la computadora podía manejar. Para representar las relaciones de vértices, aristas y caras del grafo, definió una estructura de datos llamada "Hipermapa finita" (Hypermap). Este es un método que representa el grafo como un conjunto de "dardos" (medias aristas) y grupos de permutaciones sobre estos. Como resultado, teoremas topológicos como la fórmula de Euler y el teorema de la curva de Jordan se formalizaron completamente como la lógica combinatoria de conjuntos finitos y teoría de grupos.

### Demostración de la validez del programa de demostración en sí
Además, Gonthier abandonó el "programa de verificación escrito en C" usado por Appel-Haken y RSST, e implementó él mismo el algoritmo de comprobación de reducibilidad utilizando el lenguaje interno de Coq (Gallina). Luego, **probó matemáticamente en Coq la validez del propio algoritmo, es decir: "Si este algoritmo de validación genera 'True', entonces la configuración es verdaderamente reducible".**

Gracias a esto, la fiabilidad de la demostración cambió de manera decisiva. Ya no había que preocuparse por los "bugs en el algoritmo". Esto se debe a que, siempre y cuando el núcleo de verificación lógica en el que se basa Coq (implementado con cientos de líneas de código extremadamente simples y maduras, utilizando índices de De Bruijn, etc.) procese correctamente las reglas de inferencia lógica, está garantizado matemáticamente que el inmenso árbol de demostración construido por Gonthier es absolutamente correcto.

Este es un nuevo pináculo para las "demostraciones" en matemáticas. Es la evolución de la "Demostración Informal" (Informal Proof) que los humanos leen y entienden, hacia la "Demostración Formal" (Formal Proof) en la que las máquinas garantizan la integridad lógica. El teorema de los cuatro colores se convirtió así en el primer gran teorema no trivial en la historia en alcanzar este límite extremo de rigor.

## Capítulo 7: El problema de la 4-coloración de grafos planos y la paradoja NP-completa

Finalmente, veamos el teorema de los cuatro colores desde la perspectiva de la teoría de la complejidad computacional (Computational Complexity Theory). Aquí existe un fenómeno extremadamente interesante similar a una paradoja.

El problema de la coloración en grafos generales (determinar si un grafo dado puede colorearse con $k$ colores) es uno de los problemas "NP-completos" (NP-complete) más famosos en las ciencias de la computación. En particular, se ha demostrado que el "Problema de la 3-coloración de grafos planos" (Planar 3-Colorability) es NP-completo. Es decir, a menos que $\text{P} = \text{NP}$, se cree que no existe un algoritmo de tiempo polinomial que pueda determinar si un grafo plano puede colorearse con 3 colores.

Entonces, ¿qué pasa con el "Problema de la 4-coloración de grafos planos" (Planar 4-Colorability)? Intuitivamente, uno podría pensar que si con 3 colores es NP-completo, de igual manera será difícil (NP-completo) con 4 colores.

Sin embargo y de forma sorprendente, **la complejidad computacional del problema de 4-coloración de grafos planos (el problema de decisión) es $O(1)$, es decir, "tiempo constante (trivial)".**
Esto es porque el teorema de los cuatro colores garantiza que "todos los grafos planos pueden colorearse con 4 colores", por lo que un algoritmo simplemente necesita imprimir "Sí" sin siquiera mirar el grafo de entrada y siempre será 100% correcto. Este es un hermoso ejemplo de cómo la fuerte garantía de existencia de un teorema reduce la complejidad del problema de decisión al límite absoluto.

Sin embargo, esta es solo una historia sobre el problema de decisión (Decision Problem) de "si se puede colorear o no". **Construir un algoritmo de coloración (Search Problem) sobre "cómo colorearlo en la práctica con 4 colores"** es una historia diferente.
Si implementamos los procedimientos de demostración de Appel-Haken o RSST como algoritmos, se puede obtener un algoritmo que encuentra de hecho una coloración de 4 colores para un grafo plano dado de $N$ vértices. Se ha demostrado que el algoritmo basado en la demostración de RSST produce una 4-coloración en tiempo polinomial con una complejidad de peor caso de $O(N^2)$.

En otras palabras, aunque intentar colorear un grafo plano con 3 colores podría tomar tanto tiempo como la edad del universo (NP-completo), al añadir un cuarto color, el beneficio de la estructura matemática subyacente al teorema de los cuatro colores produce la existencia de un algoritmo rápido (de $O(N^2)$). Este es un hecho fascinante y extremadamente misterioso en la intersección de las matemáticas y la informática.

## Conclusión: El legado del Teorema de los Cuatro Colores

El inocente problema de colorear mapas del joven británico de 1852 comenzó como un simple rompecabezas. Sin embargo, después de más de un siglo, abrió un vasto nuevo campo de las matemáticas, la teoría de grafos; desarrolló la teoría algorítmica; y finalmente enfrentó a la humanidad a las profundas preguntas filosóficas de "¿Pueden las computadoras demostrar teoremas matemáticos?" y "¿Qué es la verdad matemática?".

La historia del teorema de los cuatro colores es una donde colisionan violentamente los límites de la intuición humana y las posibilidades del nuevo motor lógico llamado máquina. Hoy en día, otros grandes y difíciles problemas también han sido demostrados por completo mediante verificación formal utilizando asistentes de demostración de teoremas, tales como la conjetura de Kepler (proyecto Flyspeck por Thomas Hales en 2014) y el teorema de Feit-Thompson.

Cuando coloreamos un mapa de manera casual con cuatro colores, escondidos bajo sus pliegues se hallan en múltiples capas la estética de los poliedros de Euler, el genial fracaso de Kempe, la refutación estricta de Heawood, las matemáticas de las descargas de Heesch, la trayectoria de miles de horas de parpadeos en los cálculos de los supercomputadores, y la lógica de los hipermapas finitos de Coq. El teorema de los cuatro colores, sin duda, perdurará en la historia como el estudio de caso supremo que muestra cómo las matemáticas se expanden más allá del marco del pensamiento humano.

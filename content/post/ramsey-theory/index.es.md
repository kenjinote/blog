---
title: "Teoría de Ramsey: siempre surge el orden del desorden — Demostración de relaciones entre 6 personas con colores"
description: "En cualquier grupo de 6 personas, siempre existen 3 que se conocen mutuamente o 3 que no se conocen entre sí. Demostramos el número de Ramsey R(3,3)=6 con diagramas a color, el contraejemplo para 5 personas, la verificación de las 32.768 configuraciones y sus aplicaciones a secuencias y redes."
date: 2026-09-16T20:05:00+09:00
image: "eyecatch.png"
categories: ["matemáticas"]
tags: ["Teoría de Ramsey", "Teoría de grafos", "Combinatoria", "Principio del palomar", "Python"]
slug: "ramsey-theory"
math: true
---

## 1. Al reunir a 6 personas, siempre aparece un trío

Supongamos que 6 personas asisten a una fiesta. Algunas se conocen desde hace tiempo, mientras que otras se ven por primera vez. Las relaciones de conocimiento mutuo pueden ser tan intrincadas como se quiera. Aun así, siempre se cumple una de las siguientes dos afirmaciones:

- **Cualesquiera 2 de las 3 personas se conocen entre sí.**
- **Cualesquiera 2 de las 3 personas son desconocidas entre sí.**

No se trata de que «casi siempre se encuentren». Sin importar cómo se organicen las relaciones, siempre se encontrarán sin excepción. Además, el número 6 es el mínimo. Con 5 personas, es posible crear una configuración que no contenga ninguno de estos dos tríos.

Esta pequeña sorpresa es la puerta de entrada a la **teoría de Ramsey**. Trata sobre la «regularidad inevitable»: por muy compleja que sea la división de una estructura grande, si esta es lo suficientemente grande, es completamente imposible evitar la aparición de ciertas subestructuras pequeñas y ordenadas.

Sin embargo, esto no significa que surja cualquier patrón arbitrario del desorden. Para convertirse en una afirmación matemática precisa, primero debemos definir el objeto de estudio, la cantidad de categorías para clasificarlo y la forma exacta que buscamos. Empecemos con un ejemplo intuitivo que se puede dibujar con 6 puntos en una hoja de papel.

## 2. Representar las relaciones humanas con líneas rojas y azules

### Convenciones del modelo

En este artículo, consideraremos que «conocerse» es una relación simétrica. Si A conoce a B, entonces B también conoce a A, y cada pareja se clasifica de forma exclusiva en «se conocen» o «no se conocen».

Las relaciones unilaterales (como conocer solo de nombre) o aquellas donde no está claro si se conocen no se incluyen en este modelo. Además, «no conocerse» no significa «llevarse mal» o «ser enemigos».

Representamos a las personas como puntos y sus relaciones como líneas:

| Elemento del diagrama | Significado |
|---|---|
| Punto (vértice) | 1 participante |
| Línea continua roja | Ambos se conocen mutuamente |
| Línea discontinua azul | Ambos no se conocen entre sí |
| Triángulo formado por 3 lados del mismo color | El trío buscado |

Como conectamos todos los pares posibles de personas, esto constituye un **grafo completo**. Un grafo completo de $n$ vértices se denota como $K_n$, y su número de aristas es el siguiente:

$$
\binom{n}{2}=\frac{n(n-1)}{2}
$$

Para 6 personas, hay 15 aristas. El hecho de que «A conozca a B y a C» no basta para que los 3 se conozcan mutuamente; la arista entre B y C también debe ser roja. Recuerda que la condición exige que **los 3 lados** del triángulo tengan el mismo color.

En lo sucesivo, llamaremos **triángulo monocromático** a un triángulo cuyos lados sean todos rojos o todos azules. Para garantizar la legibilidad incluso si los colores resultan difíciles de distinguir, en las figuras las aristas rojas se representan con líneas continuas y las azules con líneas discontinuas.

## 3. Demostración de que siempre existe en un grupo de 6 personas

La única herramienta necesaria para esta demostración es el [principio del palomar](../pigeonhole-principle-hash-collision/). Utilizaremos un hecho sumamente simple: «si se distribuyen 5 objetos en 2 categorías, al menos una categoría contendrá 3 objetos».

### Paso 1: Centrarse en una sola persona

Elijamos arbitrariamente a una persona cualquiera de las 6 y llamémosla A. Desde A salen 5 líneas hacia las otras 5 personas. Como cada una es roja o azul, al menos 3 de ellas deben compartir el mismo color:

$$
\left\lceil\frac{5}{2}\right\rceil=3
$$

Aquí, $\lceil x\rceil$ denota la función techo (el entero más pequeño mayor o igual que $x$). También se puede entender diciendo que si hubiera a lo sumo 2 rojas y 2 azules, sumarían a lo sumo 4 líneas, lo cual no basta para colorear las 5.

Supongamos que hay al menos 3 aristas rojas y llamemos B, C y D a las personas en sus extremos. Las aristas A–B, A–C y A–D son todas rojas. Si en cambio hubiera al menos 3 azules, bastaría intercambiar «rojo» por «azul» en el siguiente razonamiento para llegar a la misma conclusión.

### Paso 2: Analizar las conexiones entre B, C y D

Para las 3 aristas entre ellos (B–C, B–D y C–D), solo existen dos casos posibles:

**Caso 1: Hay al menos una línea roja.** Por ejemplo, si B–C es roja, dado que A–B y A–C ya son rojas, A, B y C forman un triángulo rojo. Los colores de las otras 2 aristas no importan.

**Caso 2: No hay ninguna línea roja.** En tal caso, B–C, B–D y C–D deben ser todas azules. Por lo tanto, B, C y D forman un triángulo azul.

![Diagrama de demostración: al elegir 3 aristas del mismo color desde A, si hay una arista roja entre los 3 vértices restantes se forma un triángulo rojo; de lo contrario, se forma un triángulo azul](six-person-proof.svg)

Las aristas grises y las omitidas en la figura corresponden a partes cuyo color no es necesario determinar para la demostración. En el grafo completo real, cada una de ellas también estará pintada de rojo o de azul.

Con esto queda demostrado que, sin importar cómo se coloree el grafo, siempre existirá un triángulo monocromático. No es necesario examinar las 15 aristas: **las 5 aristas que parten de un solo vértice y las relaciones entre los 3 vecinos seleccionados bastan para cubrir todas las posibilidades**. [Explicación en material universitario](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory)

## 4. ¿Por qué 5 personas no son suficientes?

«6 personas son suficientes» y «6 personas es el mínimo» son dos afirmaciones distintas. Para demostrar que 6 es el mínimo, debemos construir un contraejemplo con 5 personas que no cumpla la condición.

Coloquemos a 5 personas en los vértices de un pentágono regular. Coloreamos de rojo las 5 aristas del perímetro exterior (personas adyacentes). Las 5 diagonales restantes las coloreamos todas de azul.

![Contraejemplo de 5 personas con el perímetro del pentágono en rojo y las diagonales en azul, sin triángulos en ningún color](five-person-counterexample.svg)

Si observamos solo las aristas rojas, forman un ciclo que rodea el pentágono. No importa qué 3 personas elijamos, es imposible cerrar un triángulo usando solo aristas rojas. Si observamos solo el color azul, parece una estrella de cinco puntas; pero si cambiamos el orden en el que recorremos los vértices, también es un ciclo simple que une los 5 vértices. En azul tampoco hay ningún triángulo.

Nótese que las intersecciones de las líneas de la estrella no son nuevos vértices; las únicas personas corresponden a los 5 puntos de la A a la E. Aunque el cruce de líneas dibuje visualmente pequeños triángulos, no corresponden a los triángulos que contamos en este problema.

Dado que es posible evitar tanto un trío rojo como un trío azul, 5 personas no garantizan la propiedad. Junto con la afirmación de que «con 6 personas siempre ocurre», queda establecido que el número mínimo es exactamente 6.

## 5. Este «tamaño mínimo» se llama número de Ramsey

Cuando se colorean las aristas de un grafo completo de rojo y azul, al número mínimo de vértices necesario para garantizar la aparición de un $K_s$ rojo o un $K_t$ azul se le denomina **número de Ramsey**, denotado como $R(s,t)$.

Un $K_s$ rojo significa que todas las aristas entre los $s$ vértices seleccionados son rojas; no basta con que estén conectados por caminos rojos. Como $K_3$ es un triángulo, la conclusión obtenida hasta aquí se resume en una sola línea:

$$
R(3,3)=6
$$

El teorema de Ramsey establece que, para cualesquiera $s, t$ finitos prefijados, existe tal número finito. Sin embargo, que «exista» es muy distinto a que «su valor mínimo sea fácil de calcular». Aunque la demostración para triángulos fue breve, a medida que el grupo monocromático buscado crece, el cálculo se vuelve abrumadoramente difícil.

Una cota superior fundamental viene dada por la siguiente relación de recurrencia:

$$
R(s,t)\leq R(s-1,t)+R(s,t-1)
\qquad(s,t\geq3)
$$

Llamemos $N$ al miembro derecho y elijamos 1 vértice entre los $N$ vértices. Si hay al menos $R(s-1,t)$ vértices conectados a él por aristas rojas, entre ellos debe existir un $K_{s-1}$ rojo o un $K_t$ azul. En el primer caso, al añadir el vértice original obtenemos un $K_s$ rojo; en el segundo caso, el objetivo ya se ha cumplido.

Si no hay tantas conexiones rojas, entonces habrá al menos $R(s,t-1)$ vértices conectados por aristas azules. Basta aplicar el mismo argumento con el color opuesto. Esta es una generalización directa de la demostración anterior: «centrarse en un vértice y agrupar a los vecinos del mismo color».

Partiendo de los valores frontera $R(2,t)=t$ y $R(s,2)=s$, esta relación permite construir sucesivamente cotas superiores finitas. No obstante, al tratarse de una desigualdad, el valor obtenido no es necesariamente el mínimo estricto. Es crucial distinguir entre el «tamaño garantizado» y el «mínimo estrictamente necesario».

## 6. Diferencia entre «casi siempre» y «siempre sin excepción»

A modo de experimento, consideremos ahora colorear cada arista de forma mutuamente independiente de rojo o azul con probabilidad $1/2$. Este modelo probabilístico no es necesario para la demostración, pero ayuda a visualizar el contraste de los resultados.

Si contamos las coloraciones manteniendo las etiquetas A, B, C... en los vértices, el número total de coloraciones posibles viene dado por:

$$
2^{\binom{n}{2}}
$$

(Las configuraciones que resultan equivalentes por rotación o permutación de nombres se cuentan como distintas). Para 6 personas, hay $2^{15}=32.768$ combinaciones posibles. Al analizar todos los casos de 3 a 6 personas, se obtienen los siguientes resultados:

| Personas | Total de coloraciones | Coloraciones sin triángulos monocromáticos | Proporción con triángulos monocromáticos |
|---|---:|---:|---:|
| 3 personas | 8 | 6 | 25,00% |
| 4 personas | 64 | 18 | 71,88% |
| 5 personas | 1024 | 12 | 98,83% |
| 6 personas | 32768 | 0 | 100,00% |

![Comparación del porcentaje de existencia de triángulos monocromáticos entre 3 y 6 personas. Con 5 personas es del 98,83% pero quedan 12 contraejemplos; con 6 personas alcanza el 100%](coloring-probability.svg)

Incluso con 5 personas, si se colorea al azar, hay un triángulo monocromático aproximadamente el 98,83% de las veces. Alguien que hiciera unas pocas pruebas podría pensar erróneamente que «con 5 personas también siempre existe». Sin embargo, quedan 12 contraejemplos entre las 1.024 combinaciones. Existe una diferencia conceptual categórica entre una probabilidad alta y la ausencia total de contraejemplos.

Esta tabla muestra proporciones bajo coloraciones independientes y equiprobables; no pretende sugerir que las relaciones humanas reales se formen de manera aleatoria e independiente al 50%. En contraste, el teorema para 6 personas no depende de la probabilidad: se cumple sin importar cuán sesgadas o asimétricas sean las relaciones.

### En promedio, ¿cuántos se encuentran?

Para 3 vértices fijos hay 3 aristas, lo que da $2^3 = 8$ formas de colorearlas. De ellas, solo 2 (todas rojas o todas azules) son monocromáticas, por lo que la probabilidad es $2/8 = 1/4$. Si denotamos por $T$ el número de triángulos monocromáticos, por la linealidad de la esperanza tenemos:

$$
E[T]=\binom{n}{3}\frac14
$$

Para 6 personas, el promedio es de 5 triángulos. Aunque los distintos triángulos pueden compartir aristas y por tanto no ser independientes, la suma de esperanzas no requiere independencia.

Sin embargo, que la esperanza sea positiva no garantiza que exista en todas las coloraciones posibles. Para 5 personas el promedio es de 2,5 triángulos y, aun así, existen configuraciones con 0. No confundir el «caso promedio» con el «peor de los casos» es otra valiosa lección que ofrece la teoría de Ramsey.

## 7. Python para verificar las 32.768 combinaciones

El siguiente código funciona únicamente con la biblioteca estándar de Python. Asignamos el valor 0 al rojo y 1 al azul, haciendo corresponder el color de cada arista con un bit de un número binario. Luego se eligen combinaciones de 3 vértices y se comprueba si las 3 aristas que los conectan son del mismo color.

```python
from itertools import combinations

def check_all(n):
    edges = list(combinations(range(n), 2))
    edge_index = {edge: i for i, edge in enumerate(edges)}
    triples = [
        [edge_index[e] for e in combinations(vertices, 2)]
        for vertices in combinations(range(n), 3)
    ]
    total = 1 << len(edges)
    without_triangle = 0
    minimum = len(triples)

    for coloring in range(total):
        count = 0
        for i, j, k in triples:
            if ((coloring >> i) & 1) == ((coloring >> j) & 1) == ((coloring >> k) & 1):
                count += 1
        without_triangle += (count == 0)
        minimum = min(minimum, count)

    return total, without_triangle, minimum

for n in range(3, 7):
    total, missing, minimum = check_all(n)
    print(f"{n} personas: total {total}, sin triángulos {missing}, mínimo {minimum}")
```

```text
3 personas: total 8, sin triángulos 6, mínimo 0
4 personas: total 64, sin triángulos 18, mínimo 0
5 personas: total 1024, sin triángulos 12, mínimo 0
6 personas: total 32768, sin triángulos 0, mínimo 2
```

El hallazgo de que el «mínimo es 2» para 6 personas es un resultado ligeramente más fuerte que nuestra primera demostración. De hecho, si denotamos el número de aristas rojas que inciden en cada vértice como $r_v$ y el de aristas azules como $b_v$, se tiene que $r_v+b_v=5$ y, por lo tanto, $r_vb_v\leq6$.

En cualquier triángulo no monocromático existen exactamente dos vértices donde confluyen una arista roja y una azul. Por consiguiente, al contar los pares de «una arista roja y una azul» en cada vértice, contamos cada triángulo no monocromático exactamente dos veces. Dado que hay un total de $\binom{6}{3} = 20$ triángulos posibles, podemos demostrar que:

$$
T=\binom63-\frac12\sum_{v=1}^{6}r_vb_v
\geq20-\frac12\cdot6\cdot6=2
$$

Además, si dividimos los 6 vértices en dos grupos de 3, coloreando de rojo las aristas internas de cada grupo y de azul las que conectan ambos grupos, se obtienen exactamente dos triángulos rojos y cero triángulos azules. Por ende, el valor mínimo de 2 es exacto.

Esta búsqueda exhaustiva es factible para números pequeños, pero el total de coloraciones crece a un ritmo de $2^{n(n-1)/2}$. Como la ejecución se ralentiza drásticamente al aumentar el número de personas, aquí nos limitamos de 3 a 6. Las gráficas y la distribución detallada se pueden consultar en el [script de reproducción](generate_graphs.py) y en el [JSON con los resultados del cálculo](calculation-results.json).

## 8. Aplicación 1: «Conexión total» o «desconexión total» en redes

Sustituyamos la noción de «conocerse» por la de conexión directa entre dispositivos. Supongamos que tenemos 6 dispositivos y cada par se clasifica en «conectado directamente» o «sin conexión directa». Mientras las conexiones sean no dirigidas, el mismo teorema se aplica de manera idéntica.

En consecuencia, siempre existirá un grupo de 3 dispositivos donde todos los pares estén directamente conectados entre sí, o bien un grupo de 3 dispositivos en el que no exista conexión directa entre ningún par. El primero corresponde a un **clique** (o clan) de 3 vértices; el segundo, a un **conjunto independiente** de 3 vértices. Cabe destacar que «sin conexión directa» no implica la imposibilidad de comunicarse a través de nodos intermedios.

Esta perspectiva también resulta útil para verificar el diseño de tareas con compatibilidad o incompatibilidad por pares, o en redes de interrelación pequeñas. Si planteamos como requisito «evitar tanto que 3 tareas sean totalmente compatibles entre sí como que 3 tareas sean totalmente incompatibles», el teorema nos permite saber de antemano que, con 6 elementos, cumplir dicho requisito es imposible.

Sin embargo, el teorema no nos permite elegir cuál de los dos casos se manifestará. Puede ocurrir que necesitemos 3 elementos compatibles y solo aparezca un trío de incompatibles. Además, el hecho de que sean compatibles por pares no garantiza que los recursos basten para ejecutar los 3 simultáneamente, lo cual debe verificarse por separado. La garantía matemática se restringe estrictamente a las relaciones binarias especificadas.

## 9. Aplicación 2: Extraer subsecuencias crecientes o decrecientes de secuencias desordenadas

Dispongamos en orden 6 números distintos entre sí. Para dos posiciones donde $i$ precede a $j$ ($i < j$), unimos ambas posiciones con una arista roja si $a_i\lt a_j$, y con una arista azul si $a_i\gt a_j$.

Esto representa una 2-coloración del grafo completo de 6 vértices. Por lo tanto, garantizamos la existencia de al menos un triángulo monocromático. Si denotamos las tres posiciones ordenadas como $i\lt j\lt k$, en el caso de un triángulo rojo tenemos:

$$
a_i\lt a_j\lt a_k
$$

y en el caso de un triángulo azul:

$$
a_i\gt a_j\gt a_k
$$

Esto significa que **siempre es posible extraer 3 términos crecientes o 3 términos decrecientes preservando el orden original**. No es necesario que los términos sean consecutivos; a una selección que preserva el orden relativo original se le llama subsecuencia.

![Diagrama que muestra la extracción de la subsecuencia creciente 1, 2, 3 a partir de la secuencia 4, 1, 5, 2, 6, 3 eligiendo las posiciones originales 2, 4 y 6](monotone-subsequence.svg)

En la secuencia de la figura, $4,1,5,2,6,3$, al elegir los elementos en las posiciones 2.ª, 4.ª y 6.ª obtenemos $1,2,3$. No hemos reordenado los números de menor a mayor, sino que los hemos extraído respetando su orden de aparición original.

Esto se relaciona directamente con la idea de hallar subestructuras regulares dentro de secuencias de datos. No obstante, que los 3 puntos seleccionados sean crecientes no constituye una prueba de que la serie completa tenga una tendencia al alza. Si se trata de un patrón que necesariamente debe aparecer en cualquier secuencia, su sola presencia no representa un fenómeno extraordinario.

Cabe señalar que, para este problema de secuencias, 6 términos no es el mínimo estricto: de hecho, con solo 5 términos distintos ya se garantiza una subsecuencia monótona (creciente o decreciente) de longitud 3. Este es un caso particular del teorema de Erdős-Szekeres para subsecuencias monótonas. Dado que las coloraciones derivadas de secuencias numéricas están restringidas por la transitividad del orden ($\lt$ y $\gt$), se obtienen resultados más fuertes que con una 2-coloración arbitraria de aristas. [Material de clases sobre subsecuencias monótonas](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf)

## 10. Conclusión: Incluso en el desorden, existen patrones inevitables

Al representar las relaciones entre 6 personas con rojo y azul y analizar únicamente las 5 aristas que parten de una sola persona, hemos demostrado que siempre aparece un triángulo monocromático. Dado que el pentágono de 5 personas proporciona un contraejemplo, el número de Ramsey correspondiente es $R(3,3)=6$.

Los tres puntos clave para recordar son:

- **«Siempre» no significa «con alta probabilidad» en un experimento aleatorio.** Con 5 personas la probabilidad es de aproximadamente el 98,83%, pero persisten contraejemplos; con 6 personas no queda ninguno.
- **La existencia de un patrón no equivale a su significado causal.** La presencia de un triángulo monocromático o una subsecuencia creciente no define por sí sola las propiedades globales ni las causas del conjunto analizado.
- **Toda garantía requiere delimitar su alcance y condiciones.** Es fundamental clarificar si la relación es simétrica, si todo par se clasifica estrictamente en dos categorías y qué subestructura concreta se busca.

La fascinación de la teoría de Ramsey no radica en que un todo complejo se vuelva sencillo. Aunque el sistema general conserve toda su complejidad, es imposible erradicar por completo pequeños núcleos de orden en su interior. A partir de unos pocos trazos en un papel, podemos constatar el alcance de esta profunda intuición matemática.

### Referencias

- Ohio State University, [Ramsey Theory](https://ximera.osu.edu/math/combinatorics/combinatoricsBook/combinatoricsBook/combinatorics/ramseyTheory/ramseyTheory): Explicación sobre la 2-coloración de aristas y números de Ramsey pequeños.
- Yuval Wigderson, PCMI 2025, [Extremal graph theory and Ramsey theory: Lecture 10](https://ywigderson.math.ethz.ch/math/static/pcmi2025/Notes10.pdf): Material de cátedra sobre el pensamiento de Ramsey, incluyendo subsecuencias monótonas.

Las figuras, la tabla de enumeración exhaustiva y las distribuciones de probabilidad y recuento de este artículo fueron generadas con el script en Python adjunto.

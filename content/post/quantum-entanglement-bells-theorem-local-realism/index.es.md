---
title: "Entrelazamiento Cuántico y el Teorema de Bell: La Última Derrota de Einstein y el Amanecer de la Revolución de la Información Cuántica"
description: "'Acción espeluznante a distancia' y la paradoja EPR. El teorema de Bell y los experimentos de Aspect que demostraron el fracaso del realismo local, y el camino hacia el Premio Nobel."
slug: "quantum-entanglement-bells-theorem-local-realism"
date: "2026-10-03T05:00:00+09:00"
categories: ["physics", "quantum"]
tags: ["quantum-entanglement", "bells-theorem", "quantum-information", "physics-history"]
image: "eyecatch.jpg"
---

# Entrelazamiento Cuántico y el Teorema de Bell: La Última Derrota de Einstein y el Amanecer de la Revolución de la Información Cuántica

El "entrelazamiento cuántico" (Quantum Entanglement) es el mayor misterio de la física moderna y, al mismo tiempo, su herramienta más poderosa. Junto a él, el "teorema de Bell", que destrozó la intuición humana del "realismo local". Estos no son meros juegos teóricos de la física, sino que nos enfrentan a la naturaleza fundamental del universo y, además, constituyen la base de tecnologías de próxima generación como las computadoras cuánticas y la criptografía cuántica.

En este artículo, explicaremos con gran detalle desde el histórico artículo EPR de Einstein y otros en 1935, la lucha de las teorías de variables ocultas, la histórica derivación de la desigualdad de John Stewart Bell, la demostración matemática de la desigualdad CHSH y su máxima violación en la mecánica cuántica (el límite de Tsirelson), hasta el drama épico de la verificación experimental por Aspect y otros que culminó en el Premio Nobel de Física 2022, todo desde la perspectiva de la física, la ciencia de la información cuántica y la filosofía de la ciencia. Además, profundizaremos con ecuaciones matemáticas en la negación completa del realismo local mediante el estado GHZ de entrelazamiento de múltiples partículas, el protocolo estricto de la teleportación cuántica y los métodos de cuantificación del entrelazamiento.

---

## Capítulo 1: 1935, El Contraataque de Einstein

Mientras la mecánica cuántica era formulada en la década de 1920 por la Escuela de Copenhague (Niels Bohr, Werner Heisenberg, entre otros), Albert Einstein albergaba una profunda insatisfacción con su interpretación probabilística y no determinista. Su famosa frase "Dios no juega a los dados" refleja su rechazo a la naturaleza estocástica subyacente a la mecánica cuántica.

En 1935, Einstein, junto con Boris Podolsky y Nathan Rosen, publicó un artículo histórico que quedaría en los anales de la física: "¿Puede considerarse completa la descripción mecánico-cuántica de la realidad física?" (Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?), conocido como el "artículo EPR". El propósito de este trabajo era demostrar lógicamente que la mecánica cuántica era "incompleta", es decir, que debían existir "variables ocultas" que aún desconocíamos.

### Definición de Localidad y Realidad

Para comprender la lógica del artículo EPR, es necesario captar con precisión dos conceptos fundamentales que Einstein y sus colegas asumieron como premisas.

1. **Realismo (Realism)**:
   La idea de que, independientemente de si es observado o no, un sistema físico posee propiedades (valores) físicas definidas. En el artículo EPR se definió: "Si, sin perturbar en modo alguno el estado de un sistema físico, podemos predecir con certeza (con probabilidad 1) el valor de una cantidad física, entonces existe un elemento de realidad física correspondiente a esa cantidad". En otras palabras, el objeto posee determinísticamente sus atributos antes de la medición, algo que es de sentido común en la mecánica clásica.
2. **Localidad (Locality)**:
   Un principio basado en la teoría de la relatividad que establece que, en dos regiones espacialmente separadas, una operación o medición realizada en una no puede afectar instantáneamente a la realidad física de la otra región más rápido que la velocidad de la luz. Según la teoría de la relatividad especial, la transmisión de información a una velocidad superior a la de la luz conduciría a la ruptura de la causalidad, por lo que cualquier interacción física está sujeta al límite de la velocidad de la luz.

### "Acción espeluznante a distancia" (Spooky action at a distance) y la Paradoja EPR

El artículo EPR presentaba el siguiente experimento mental.
Imaginemos dos partículas, A y B, que se han separado a una gran distancia después de haber interactuado fuertemente entre sí. En el marco de la mecánica cuántica, estas dos partículas se encuentran en un estado "entrelazado" (Entangled) y se describen mediante una función de onda global.

Supongamos que medimos la posición $x_A$ de la partícula A. Debido a la ley de conservación del momento, entre otras, una vez que la posición de A queda determinada, la posición $x_B$ de la partícula B también queda determinada instantáneamente. Por otro lado, si medimos el momento $p_A$ de la partícula A, el momento $p_B$ de la partícula B se determinará instantáneamente.
Según la mecánica cuántica, la posición y el momento son magnitudes físicas no conmutativas ($[x, p] = i\hbar$) y no pueden tener valores definidos simultáneamente (principio de incertidumbre de Heisenberg). Sin embargo, la elección de la medición sobre A (si medir la posición o el momento) parece determinar instantáneamente el estado de B (si está en un estado de posición definida o de momento definido) superando la velocidad de la luz.

Si la "localidad" es correcta, es imposible que una medición sobre A afecte instantáneamente a B. Einstein denominó a esto "acción espeluznante a distancia" (Spukhafte Fernwirkung / Spooky action at a distance) y lo criticó duramente. Por lo tanto, concluyeron que B debía poseer de antemano valores definidos tanto para la posición como para el momento (variables ocultas) antes de ser medido, y que la mecánica cuántica, incapaz de describir completamente ambas propiedades, era una "teoría incompleta". Esta paradoja se convirtió en el primer paso hacia la comprensión fundamental del entrelazamiento en la posterior teoría de la información cuántica.

---

## Capítulo 2: El Dilema de la Teoría de Variables Ocultas y la Mecánica de Bohm

Tras la publicación del artículo EPR, los físicos se volcaron a explorar la hipótesis de que "la mecánica cuántica es correcta pero incompleta, y tal vez exista una teoría determinista (teoría de variables ocultas) en un nivel más profundo".

### El "Teorema de Imposibilidad" erróneo de von Neumann

Quien arrojó un jarro de agua fría sobre este debate fue el genial matemático John von Neumann. En su libro de 1932 "Fundamentos matemáticos de la mecánica cuántica", presentó una demostración (teorema de imposibilidad) de que es matemáticamente imposible construir una "teoría de variables ocultas" que ofrezca las mismas predicciones que la mecánica cuántica.
La autoridad de von Neumann era abrumadora, y durante las décadas siguientes, la creencia de que "la búsqueda de variables ocultas carece de sentido" dominó la comunidad física.

Sin embargo, como se descubriría más tarde, la demostración de von Neumann incluía una suposición extremadamente restrictiva y no física como "condición que deben cumplir las variables ocultas" (la suposición de que la aditividad del valor esperado de las cantidades físicas no conmutativas: $\langle A+B \rangle = \langle A \rangle + \langle B \rangle$ se cumple incluso a nivel de variables ocultas), por lo que, de hecho, no era una demostración completa. Grete Hermann notó este defecto muy pronto, pero no se le prestó atención en ese momento.

### Mecánica de Bohm: Una Teoría de Variables Ocultas No Local

En 1952, David Bohm rompió el teorema de imposibilidad de von Neumann y construyó una "teoría de variables ocultas" determinista (la mecánica de Bohm o teoría de de Broglie-Bohm) que proporcionaba predicciones perfectamente consistentes con la mecánica cuántica.
En la teoría de Bohm, las partículas siempre poseen una posición definida (variable oculta) y son guiadas por un "potencial cuántico" que se extiende por todo el universo. Este potencial $Q = -\frac{\hbar^2}{2m}\frac{\nabla^2 R}{R}$, obtenido al convertir la ecuación de Schrödinger a coordenadas polares, tiene la peculiar propiedad de no depender de la distancia ni decaer.

Pero la mecánica de Bohm tenía un precio enorme. Dado que el potencial cuántico afecta instantáneamente a todo el espacio, esta teoría era intrínsecamente "no local". La "acción espeluznante a distancia" que Einstein tanto detestaba, la mecánica de Bohm la incorporaba como fundamento central de la teoría.
Einstein también adoptó una actitud negativa hacia la teoría de Bohm, calificándola de "solución barata", y siguió creyendo en la existencia de una teoría de variables ocultas "local".

---

## Capítulo 3: El Estado Singlete de las Partículas de Espín 1/2 y la Predicción Rigurosa de la Mecánica Cuántica

Antes de avanzar a la desigualdad de Bell, desarrollemos completamente el proceso de cálculo riguroso de la notación bra-ket utilizando las matrices de Pauli para la correlación del entrelazamiento predicha por la mecánica cuántica. Este es el núcleo de la mecánica cuántica que luego entraría en conflicto con el realismo local.

Supongamos que se genera un par de partículas de espín 1/2 que se encuentran en un "estado singlete" (Singlet State) con un espín total de cero. Este estado $|\psi^-\rangle$ se describe de la siguiente manera:

$$ |\psi^-\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\rangle_A \otimes |\downarrow\rangle_B - |\downarrow\rangle_A \otimes |\uparrow\rangle_B \right) $$

Aquí, $|\uparrow\rangle$ y $|\downarrow\rangle$ representan los estados propios (base $z$) del espín hacia arriba ($+1$) y hacia abajo ($-1$), respectivamente. A menudo se escribe de forma simplificada como $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$.

Alice mide el espín de su partícula en la dirección $\vec{a}$, y Bob en la dirección $\vec{b}$. Los vectores de dirección son vectores unitarios, y en un sistema de coordenadas esféricas se pueden expresar como $\vec{a} = (\sin\theta_a\cos\phi_a, \sin\theta_a\sin\phi_a, \cos\theta_a)$.
Los operadores de medición de espín en cada dirección se expresan utilizando las matrices de Pauli $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ como $\sigma_a = \vec{a} \cdot \vec{\sigma}$ y $\sigma_b = \vec{b} \cdot \vec{\sigma}$.

Lo que queremos conocer es el valor esperado del producto de los resultados de la medición de Alice y Bob $\langle \sigma_a \otimes \sigma_b \rangle$. Para calcular esto, expandiremos según la definición del valor esperado.

$$ \langle \psi^- | (\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma}) | \psi^- \rangle $$

Primero, como propiedad de las matrices de Pauli, consideremos $\vec{a} \cdot \vec{\sigma} = a_x \sigma_x + a_y \sigma_y + a_z \sigma_z$. Un truco ingenioso para simplificar los cálculos es aprovechar que el estado singlete $|\psi^-\rangle$ es invariante bajo rotaciones (tiene la misma forma en cualquier base). Sin embargo, aquí realizaremos una expansión completa mediante un enfoque algebraico más directo.

El operador $(\vec{a} \cdot \vec{\sigma}) \otimes (\vec{b} \cdot \vec{\sigma})$ se expande de la siguiente manera:
$$ \sum_{i \in \{x,y,z\}} \sum_{j \in \{x,y,z\}} a_i b_j (\sigma_i \otimes \sigma_j) $$

Por la linealidad del valor esperado, tenemos:
$$ \sum_{i,j} a_i b_j \langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle $$
Aquí, evaluaremos $\langle \psi^- | \sigma_i \otimes \sigma_j | \psi^- \rangle$ para cada componente.

Para $|\psi^-\rangle = \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle)$:
- Para $\sigma_z \otimes \sigma_z$:
  $\sigma_z \otimes \sigma_z |01\rangle = (+1)(-1)|01\rangle = -|01\rangle$
  $\sigma_z \otimes \sigma_z |10\rangle = (-1)(+1)|10\rangle = -|10\rangle$
  Por lo tanto, $\sigma_z \otimes \sigma_z |\psi^-\rangle = -|\psi^-\rangle$, y el valor esperado es $-1$.
- Para $\sigma_x \otimes \sigma_x$:
  $\sigma_x \otimes \sigma_x |01\rangle = |10\rangle$
  $\sigma_x \otimes \sigma_x |10\rangle = |01\rangle$
  Por lo tanto, $\sigma_x \otimes \sigma_x \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle) = \frac{1}{\sqrt{2}}(|10\rangle - |01\rangle) = -|\psi^-\rangle$, y el valor esperado es $-1$.
- Para $\sigma_y \otimes \sigma_y$:
  Dado que $\sigma_y |0\rangle = i|1\rangle, \sigma_y |1\rangle = -i|0\rangle$,
  $\sigma_y \otimes \sigma_y |01\rangle = (i|1\rangle) \otimes (-i|0\rangle) = |10\rangle$
  $\sigma_y \otimes \sigma_y |10\rangle = (-i|0\rangle) \otimes (i|1\rangle) = |01\rangle$
  Por lo tanto, $\sigma_y \otimes \sigma_y |\psi^-\rangle = -|\psi^-\rangle$, y el valor esperado es $-1$.

Por otro lado, los valores esperados de componentes diferentes (por ejemplo, $\sigma_x \otimes \sigma_y$) son todos $0$.
Esto se debe a que $\sigma_x \otimes \sigma_y |01\rangle = |1\rangle \otimes (-i|0\rangle) = -i|10\rangle$, y al tomar el producto interno con $\langle \psi^-|$, desaparece debido a la ortogonalidad.

Por lo tanto, los únicos términos distintos de cero son aquellos donde $i=j$,
$$ \sum_{i} a_i b_i \langle \psi^- | \sigma_i \otimes \sigma_i | \psi^- \rangle = \sum_{i} a_i b_i (-1) = - (a_x b_x + a_y b_y + a_z b_z) = - \vec{a} \cdot \vec{b} $$
así se deduce estrictamente.
Si el ángulo formado entre los vectores $\vec{a}$ y $\vec{b}$ es $\theta$, por la definición del producto punto, $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = \cos\theta$ (dado que son vectores unitarios de longitud 1).
Por lo tanto, la correlación predicha por la mecánica cuántica se expresa en la siguiente ecuación maravillosamente simple:

$$ E(\vec{a}, \vec{b}) = \langle \sigma_a \otimes \sigma_b \rangle = - \cos\theta $$

Esta poderosa correlación de $-\cos\theta$ es la fuente del "comportamiento peculiar cuántico" que las teorías clásicas de variables ocultas jamás podrían reproducir.

---

## Capítulo 4: El Impacto de John Stewart Bell y la Derivación Rigurosa de la Desigualdad CHSH

En 1964, el físico irlandés John Stewart Bell, que realizaba investigaciones en física de partículas en el CERN, dedicaba su tiempo libre al estudio de los problemas fundamentales de la mecánica cuántica. Considerando la no localidad de la mecánica de Bohm, formuló la siguiente profunda pregunta:

"¿Es realmente posible reproducir todas las predicciones de la mecánica cuántica utilizando una teoría de variables ocultas 'local' como deseaba Einstein?"

Bell elevó este problema, que había sido apenas un debate filosófico, a un formato experimentalmente verificable a través de una formulación matemática rigurosa. Este es el "Teorema de Bell" (Bell's Theorem) y la "Desigualdad de Bell", que brillan en la historia de la ciencia.
Y en 1969, John Clauser, Michael Horne, Abner Shimony y Richard Holt (CHSH) derivaron una versión ampliada de la desigualdad, la "desigualdad CHSH", que podía ser verificada en experimentos reales.

### Los Supuestos del Realismo Local y el Desarrollo Algebraico e Integral de la Desigualdad CHSH

Supongamos que Alice elige configurar su aparato de medición en $a$ o $a'$, y Bob elige $b$ o $b'$.
Sea $\lambda$ la "variable oculta" basada en el realismo local, y sea $\rho(\lambda)$ su función de densidad de probabilidad. Como la probabilidad está normalizada,
$$ \int \rho(\lambda) d\lambda = 1 $$

El resultado de la medición de Alice, $A$, está determinado únicamente por la orientación de su medición $a$ y $\lambda$, sin depender de la orientación de medición $b$ de Bob (localidad).
De manera similar, el resultado de la medición de Bob, $B$, está determinado únicamente por $b$ y $\lambda$ (localidad). Además, los resultados ya están determinados antes de la medición (realismo). Dado que los resultados son $+1$ o $-1$,
$$ A(a, \lambda) = \pm 1, \quad B(b, \lambda) = \pm 1 $$
$$ A(a', \lambda) = \pm 1, \quad B(b', \lambda) = \pm 1 $$

La función de correlación (valor esperado) de los resultados de medición de Alice y Bob se obtiene integrando sobre la variable oculta $\lambda$.
$$ E(a, b) = \int A(a, \lambda) B(b, \lambda) \rho(\lambda) d\lambda $$

Aquí consideramos la siguiente cantidad $S(\lambda)$, que es el núcleo de la desigualdad CHSH:
$$ S(\lambda) = A(a, \lambda)B(b, \lambda) + A(a, \lambda)B(b', \lambda) + A(a', \lambda)B(b, \lambda) - A(a', \lambda)B(b', \lambda) $$

Factorizamos esta ecuación utilizando el resultado de medición de Alice:
$$ S(\lambda) = A(a, \lambda) \left[ B(b, \lambda) + B(b', \lambda) \right] + A(a', \lambda) \left[ B(b, \lambda) - B(b', \lambda) \right] $$

Aquí se introduce un paso lógico crucial. Tanto $B(b, \lambda)$ como $B(b', \lambda)$ toman necesariamente los valores $+1$ o $-1$.
Por lo tanto, al considerar su suma y su diferencia, solo existen dos casos posibles:

- Caso 1: Cuando $B(b, \lambda) = B(b', \lambda)$
  La suma es $B(b, \lambda) + B(b', \lambda) = \pm 2$, y la diferencia es $B(b, \lambda) - B(b', \lambda) = 0$.
- Caso 2: Cuando $B(b, \lambda) = -B(b', \lambda)$
  La suma es $B(b, \lambda) + B(b', \lambda) = 0$, y la diferencia es $B(b, \lambda) - B(b', \lambda) = \pm 2$.

En cualquier caso, uno de los dos paréntesis $\left[ \dots \right]$ será invariablemente $\pm 2$, y el otro será $0$.
Además, el término $A(a, \lambda)$ o $A(a', \lambda)$ que multiplica al $\pm 2$ superviviente también es $\pm 1$.
Por lo tanto, para cualquier valor de la variable oculta $\lambda$, se cumple algebraicamente lo siguiente:
$$ S(\lambda) = \pm 2 $$

Es decir, tomando el valor absoluto:
$$ |S(\lambda)| = 2 $$

Para hallar el valor esperado $S$ de este $S(\lambda)$, multiplicamos por la distribución de probabilidad $\rho(\lambda)$ e integramos en todo el espacio.
$$ |S| = \left| \int S(\lambda) \rho(\lambda) d\lambda \right| \le \int |S(\lambda)| \rho(\lambda) d\lambda $$
Usando $|S(\lambda)| = 2$ y $\int \rho(\lambda) d\lambda = 1$, obtenemos:
$$ |S| \le \int 2 \rho(\lambda) d\lambda = 2 $$

Este valor esperado $S$ puede expandirse como la suma y resta de las funciones de correlación individuales:
$$ S = E(a, b) + E(a, b') + E(a', b) - E(a', b') $$

Por consiguiente, se deriva la "Desigualdad CHSH":
$$ |E(a, b) + E(a, b') + E(a', b) - E(a', b')| \le 2 $$

Si el universo se rige por el "realismo local", este es el **límite absoluto que nunca puede ser superado**.

### Violación Máxima Cuántica (Límite de Tsirelson)

Recordemos la predicción de la mecánica cuántica deducida en el Capítulo 3: $E(\vec{a}, \vec{b}) = -\cos\theta$.
Supongamos que Alice y Bob ajustan sus medidores en los siguientes ángulos:
- $a = 0$
- $a' = \pi/2$
- $b = \pi/4$
- $b' = -\pi/4$

(※Nota: Al usar la polarización de fotones, el coeficiente difiere del espín 1/2 y es $E = \cos(2\theta)$, pero la esencia es la misma incluso si calculamos con los ajustes de espín anteriores).
Las diferencias angulares entre cada configuración son:
$|a - b| = \pi/4$
$|a - b'| = \pi/4$
$|a' - b| = \pi/4$
$|a' - b'| = 3\pi/4$

Sustituyendo en la predicción de la mecánica cuántica:
$E(a, b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a, b') = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b) = -\cos(\pi/4) = -1/\sqrt{2}$
$E(a', b') = -\cos(3\pi/4) = +1/\sqrt{2}$

Insertando esto en el lado izquierdo $S$ de la desigualdad CHSH:
$$ S = \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) + \left( -\frac{1}{\sqrt{2}} \right) - \left( +\frac{1}{\sqrt{2}} \right) = -\frac{4}{\sqrt{2}} = -2\sqrt{2} $$
El valor absoluto es $|S| = 2\sqrt{2} \approx 2.828$.

Supera claramente el límite del realismo local de $2$ ($2.828 > 2$). Este valor máximo alcanzable por la mecánica cuántica se denomina **Límite de Tsirelson (Tsirelson Bound)**. Mediante esta demostración matemática rigurosa se comprobó que el realismo local es absolutamente irreconciliable con las predicciones de la mecánica cuántica.

---

## Capítulo 5: Entrelazamiento de Múltiples Partículas y el Rechazo de "Todo o Nada" al Realismo Local

El Teorema de Bell se basaba en la "desigualdad" de correlaciones estadísticas. Sin embargo, en 1989, Daniel Greenberger, Michael Horne y Anton Zeilinger demostraron que si consideramos el estado entrelazado de 3 partículas (estado GHZ), es posible refutar por completo el realismo local mediante una sola medición paradójica, sin necesidad de recurrir a desigualdades ni probabilidades estadísticas. A esto se le conoce como la demostración "All-or-Nothing" o el "Teorema GHZ".

### Propiedades del Estado GHZ
El estado GHZ de tres partículas de espín 1/2 se define de la siguiente manera:
$$ |GHZ\rangle = \frac{1}{\sqrt{2}} \left( |\uparrow\uparrow\uparrow\rangle - |\downarrow\downarrow\downarrow\rangle \right) $$

Apliquemos el siguiente producto de operadores de Pauli:
1. $X_1 Y_2 Y_3 = \sigma_x^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_y^{(3)}$
2. $Y_1 X_2 Y_3 = \sigma_y^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_y^{(3)}$
3. $Y_1 Y_2 X_3 = \sigma_y^{(1)} \otimes \sigma_y^{(2)} \otimes \sigma_x^{(3)}$
4. $X_1 X_2 X_3 = \sigma_x^{(1)} \otimes \sigma_x^{(2)} \otimes \sigma_x^{(3)}$

Usando:
$\sigma_x |\uparrow\rangle = |\downarrow\rangle, \sigma_x |\downarrow\rangle = |\uparrow\rangle$
$\sigma_y |\uparrow\rangle = i|\downarrow\rangle, \sigma_y |\downarrow\rangle = -i|\uparrow\rangle$

Aplicando $X_1 Y_2 Y_3$ a $|GHZ\rangle$:
$X_1 Y_2 Y_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\rangle (i|\downarrow\rangle) (i|\downarrow\rangle) = -|\downarrow\downarrow\downarrow\rangle$
$X_1 Y_2 Y_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\rangle (-i|\uparrow\rangle) (-i|\uparrow\rangle) = -|\uparrow\uparrow\uparrow\rangle$
Por lo tanto,
$X_1 Y_2 Y_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (-|\downarrow\downarrow\downarrow\rangle + |\uparrow\uparrow\uparrow\rangle) = |GHZ\rangle$
y el valor propio es $+1$. Por simetría, los valores propios de $Y_1 X_2 Y_3$ y $Y_1 Y_2 X_3$ también son $+1$.

Por otro lado, al aplicar $X_1 X_2 X_3$:
$X_1 X_2 X_3 |\uparrow\uparrow\uparrow\rangle = |\downarrow\downarrow\downarrow\rangle$
$X_1 X_2 X_3 |\downarrow\downarrow\downarrow\rangle = |\uparrow\uparrow\uparrow\rangle$
Por lo tanto,
$X_1 X_2 X_3 |GHZ\rangle = \frac{1}{\sqrt{2}} (|\downarrow\downarrow\downarrow\rangle - |\uparrow\uparrow\uparrow\rangle) = -|GHZ\rangle$
y el valor propio es $-1$. La mecánica cuántica predice estos resultados con certeza (probabilidad 1).

### Demostración Algebraica del Fracaso del Realismo Local
Bajo el realismo local, asumimos que los resultados de medición están determinados por variables ocultas preexistentes.
Sean los resultados de medición en la dirección X e Y para la partícula 1, $m_x^1, m_y^1 \in \{+1, -1\}$ respectivamente. Los definimos del mismo modo para las partículas 2 y 3.
Dado que deben coincidir con las predicciones de $+1$ de la mecánica cuántica, un modelo de realismo local debe satisfacer las siguientes tres ecuaciones:
1. $m_x^1 m_y^2 m_y^3 = +1$
2. $m_y^1 m_x^2 m_y^3 = +1$
3. $m_y^1 m_y^2 m_x^3 = +1$

Multipliquemos estas tres ecuaciones:
$(m_x^1 m_y^2 m_y^3)(m_y^1 m_x^2 m_y^3)(m_y^1 m_y^2 m_x^3) = +1 \times +1 \times +1 = +1$
Simplificando el lado izquierdo, cada $m_y^i$ se multiplica dos veces, por lo que $(m_y^i)^2 = 1$.
$m_x^1 m_x^2 m_x^3 (m_y^1)^2 (m_y^2)^2 (m_y^3)^2 = m_x^1 m_x^2 m_x^3 = +1$

En otras palabras, mientras nos adhiramos al realismo local, el resultado de medir $X_1 X_2 X_3$ siempre debe ser $+1$.
Sin embargo, como vimos antes, la rigurosa predicción de la mecánica cuántica (y el resultado experimental real) es $-1$.
$+1$ y $-1$. Sin siquiera necesitar una desigualdad estadística, en una única medición, el realismo local y la mecánica cuántica entran en una contradicción definitiva, demostrando así la corrección de la mecánica cuántica.

(※A propósito, en el entrelazamiento de 3 partículas, existe también el estado W $|W\rangle = \frac{1}{\sqrt{3}}(|100\rangle + |010\rangle + |001\rangle)$ que posee propiedades distintas al estado GHZ, gozando de una robustez en la que el entrelazamiento no se destruye completamente aun si se pierde una partícula).

---

## Capítulo 6: Aplicaciones en la Ciencia de la Información Cuántica y la Expansión Rigurosa de la Teleportación Cuántica

El entrelazamiento pasó de ser el objeto de una paradoja a transformarse en un "recurso de información". El ejemplo representativo de esto es la "teleportación cuántica". Propuesta en 1993 por Charles Bennett y otros, fue demostrada experimentalmente por primera vez en 1997 por el grupo de Anton Zeilinger (ganador del Premio Nobel 2022).

### Desarrollo Matemático del Protocolo de Teleportación Cuántica

Supongamos que Alice posee un estado cuántico desconocido $|\phi\rangle = \alpha|0\rangle + \beta|1\rangle$ y quiere transferirlo a Bob, quien está muy lejos. ($|\alpha|^2 + |\beta|^2 = 1$)
De acuerdo con el teorema de no clonación cuántica (No-cloning theorem), no es posible copiar este estado para enviarlo. Además, si lo medimos, el estado colapsa y es imposible conocer con exactitud los valores de $\alpha$ y $\beta$.

Por eso, Alice y Bob comparten de antemano un par de partículas entrelazadas (par EPR), específicamente el siguiente estado de Bell $|\Phi^+\rangle$:
$$ |\Phi^+\rangle_{AB} = \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$

Alice tiene en sus manos la partícula que desea enviar (llamada partícula C) y una de las mitades del par EPR (partícula A). Bob tiene la otra mitad del par EPR (partícula B). El estado inicial de todo el sistema es:
$$ |\psi_{total}\rangle = |\phi\rangle_C \otimes |\Phi^+\rangle_{AB} = (\alpha|0\rangle_C + \beta|1\rangle_C) \otimes \frac{1}{\sqrt{2}}(|0\rangle_A |0\rangle_B + |1\rangle_A |1\rangle_B) $$
Expandiendo:
$$ \frac{1}{\sqrt{2}} \left( \alpha|000\rangle + \alpha|011\rangle + \beta|100\rangle + \beta|111\rangle \right) $$
(※Los subíndices siguen el orden $C, A, B$)

Aquí, Alice realiza una "medición de Bell" (Bell measurement) sobre la partícula C y la partícula A en su poder. Esto es una medición que proyecta las dos partículas en la base de los siguientes 4 estados de Bell:
$|\Phi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)$
$|\Psi^\pm\rangle_{CA} = \frac{1}{\sqrt{2}}(|01\rangle \pm |10\rangle)$

Usando esto para reescribir $|00\rangle, |01\rangle, |10\rangle, |11\rangle$ y reestructurar el estado completo del sistema agrupando en la base de Bell $|\cdot\rangle_{CA}$, sorprendentemente se transforma en lo siguiente:
$$ |\psi_{total}\rangle = \frac{1}{2} \left[ |\Phi^+\rangle_{CA}(\alpha|0\rangle_B + \beta|1\rangle_B) + |\Phi^-\rangle_{CA}(\alpha|0\rangle_B - \beta|1\rangle_B) + |\Psi^+\rangle_{CA}(\alpha|1\rangle_B + \beta|0\rangle_B) + |\Psi^-\rangle_{CA}(\alpha|1\rangle_B - \beta|0\rangle_B) \right] $$

Cuando Alice realiza la medición de Bell, el sistema colapsa en uno de estos 4 términos con una probabilidad de 1/4.
1. Si Alice obtiene $|\Phi^+\rangle$, el estado de Bob se vuelve $\alpha|0\rangle + \beta|1\rangle = |\phi\rangle$, y la transferencia ya se ha completado (Operador unitario $I$).
2. Si obtiene $|\Phi^-\rangle$, el estado de Bob es $\alpha|0\rangle - \beta|1\rangle$. Bob puede aplicar el operador de Pauli $Z$ ($\sigma_z$) para volver a $|\phi\rangle$.
3. Si obtiene $|\Psi^+\rangle$, el estado de Bob es $\alpha|1\rangle + \beta|0\rangle$. Bob puede aplicar el operador de Pauli $X$ ($\sigma_x$) para volver a $|\phi\rangle$.
4. Si obtiene $|\Psi^-\rangle$, el estado de Bob es $\alpha|1\rangle - \beta|0\rangle$. Bob aplica $Z$ seguido de $X$ ($XZ$ o $i\sigma_y$) para volver a $|\phi\rangle$.

Alice transmite a Bob el resultado de su medición (2 bits de información clásica: 00, 01, 10, 11) mediante una comunicación normal (teléfono o internet). Como esta comunicación no supera la velocidad de la luz, no contradice la teoría de la relatividad. Dependiendo de los 2 bits recibidos, Bob aplica el operador de Pauli correspondiente y logra restaurar magistralmente el estado cuántico desconocido $|\phi\rangle$.
Este es el protocolo completo de la teleportación cuántica.

---

## Capítulo 7: Cuantificación del Entrelazamiento (Quantification)

El entrelazamiento no es simplemente una cuestión de "existir" o "no existir"; es posible cuantificar "qué tan fuertemente está entrelazado". En la teoría de la información cuántica, este es un tema de investigación sumamente importante.

### 1. Entropía de Entrelazamiento de von Neumann
La medida estándar para evaluar el grado de entrelazamiento de un sistema bipartito $AB$ en un estado puro es la entropía de von Neumann. Sea la matriz de densidad de todo el sistema $\rho_{AB} = |\psi\rangle\langle\psi|$, y trazamos (reducimos) el sistema B para obtener la matriz de densidad reducida del sistema A: $\rho_A = \text{Tr}_B(\rho_{AB})$.
En este caso, la entropía de entrelazamiento $S$ se define como:
$$ S(\rho_A) = -\text{Tr}(\rho_A \log_2 \rho_A) $$
En estados máximamente entrelazados, como los estados de Bell, $\rho_A$ se convierte en un estado completamente mixto (proporcional a la matriz identidad), y $S = 1$ (su valor máximo). Intuitivamente, expresa la esencia del entrelazamiento: "A pesar de que el estado global se conoce por completo, si observamos únicamente una parte (el sistema A), no tenemos ninguna información en absoluto (parece aleatorio)".

### 2. Concurrencia (Concurrence)
Como una medida para cuantificar el entrelazamiento de sistemas de dos cúbits, incluidos los estados mixtos, William Wootters y otros concibieron la "Concurrencia $C(\rho)$".
Para una matriz de densidad $\rho$, calculamos el estado con espín invertido $\tilde{\rho} = (\sigma_y \otimes \sigma_y) \rho^* (\sigma_y \otimes \sigma_y)$ (donde $\rho^*$ es el conjugado complejo).
Sean los valores propios de la matriz $R = \sqrt{\sqrt{\rho} \tilde{\rho} \sqrt{\rho}}$, ordenados de mayor a menor, $\lambda_1, \lambda_2, \lambda_3, \lambda_4$, la concurrencia se define como:
$$ C(\rho) = \max(0, \lambda_1 - \lambda_2 - \lambda_3 - \lambda_4) $$
$C(\rho)$ toma valores de $0$ (sin entrelazamiento) a $1$ (entrelazamiento máximo). Posee una propiedad matemática muy poderosa: permite calcular directamente otra medida llamada "Entanglement of Formation" a partir de este valor.

### 3. Negatividad (Negativity)
La negatividad $\mathcal{N}(\rho)$ es una medida basada en el concepto de transposición parcial.
Dada una matriz de densidad $\rho$ del sistema bipartito $AB$, tomamos la transpuesta parcial solo respecto a la base del sistema B, denotada como $\rho^{T_B}$. Si $\rho$ es un estado no entrelazado (separable), todos los valores propios de $\rho^{T_B}$ serán no negativos (Criterio de positividad de la transpuesta parcial o criterio PPT de Peres-Horodecki).
A la inversa, si existe algún valor propio negativo, es evidencia de entrelazamiento. La negatividad se define utilizando la norma de traza $||\cdot||_1$ de $\rho^{T_B}$ de la siguiente forma:
$$ \mathcal{N}(\rho) = \frac{||\rho^{T_B}||_1 - 1}{2} $$
Esto equivale a la suma de los valores absolutos de los valores propios negativos, y por ser fácil de calcular, es un indicador extremadamente útil en el estudio del entrelazamiento de sistemas multidimensionales y multipartitos.

---

## Capítulo 8: Verificación Experimental y el Cierre Total de las Brechas (Loopholes)

La teoría estaba completa y las aplicaciones asomaban a la vista. Lo único que quedaba era interrogar a la naturaleza en el laboratorio para ver a qué leyes obedecía realmente.

### El Experimento del Conmutador de Alain Aspect (1982)
Se debe descartar la posibilidad de que, después de que Alice y Bob deciden los ángulos de sus medidores, esa información viaje a una velocidad igual o inferior a la de la luz y llegue al otro lado para influir en las "variables ocultas". A esto se le conoce como la "brecha de localidad" (Locality Loophole).
El francés Alain Aspect y su equipo lograron realizar un experimento en el que, mediante el uso de dispositivos acústico-ópticos, alteraban de forma ultra rápida y aleatoria la configuración del ángulo de medición mientras los fotones aún viajaban desde la fuente hacia los medidores. De esta manera crearon una situación (aislamiento espacial) donde ni siquiera las señales a la velocidad de la luz podrían transmitir información, logrando observar majestuosamente la violación de la desigualdad. La "acción espeluznante a distancia" de Einstein se había hecho realidad.

### El Desafío Definitivo: El Experimento Perfecto sin Brechas (2015)
Incluso después de los experimentos de Aspect, persistía un mínimo margen de objeción debido a la baja eficiencia de detección (la "brecha de muestreo justo" o Fair-sampling Loophole, que argumentaba que los fotones no detectados eran justo aquellos que poseían variables ocultas "convenientes").
Sin embargo, en 2015, varios grupos de investigación de la Universidad Tecnológica de Delft (Países Bajos), la Universidad de Viena (Austria) y el NIST (Estados Unidos) lograron simultáneamente cerrar las principales brechas en una "Prueba de Bell sin brechas" (Loophole-free Bell test). En el experimento de Delft, al entrelazar los espines de electrones en centros NV de diamantes separados por 1.3 km, se bloquearon definitivamente la brecha de localidad y la brecha de detección, clavando el último clavo en el ataúd del realismo local.

---

## A Modo de Conclusión: La Luz Derivada de la Derrota de Einstein

En 2022, el Premio Nobel de Física fue otorgado a Alain Aspect, John Clauser y Anton Zeilinger, quienes establecieron de manera decisiva los cimientos de la mecánica cuántica.

Einstein odiaba la naturaleza probabilística y no local de la mecánica cuántica, y escribió el artículo EPR para criticarla. Sin embargo, irónicamente, sus afiladas críticas destacaron claramente el concepto de "entrelazamiento" y, a través del genio de Bell, allanaron el camino para que la humanidad lograra comprender verdaderamente la conexión no local del universo y aprovecharla como tecnología.

La "última derrota" de Einstein no fue en absoluto un estancamiento de la física, sino el gran amanecer en el que la humanidad adquirió un lenguaje completamente nuevo para el universo: la información cuántica.

---
*Redacción: Escritor de Tecnología Científica e Información Cuántica*
*Este artículo es una exposición académica integral que abarca desde los fundamentos de la mecánica cuántica hasta las tecnologías de información cuántica de vanguardia.*

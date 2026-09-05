---
title: ''¿Qué es la "Criba General del Cuerpo de Números (GNFS)", las matemáticas más fuertes de la humanidad que rompen el cifrado de Internet?''
date: 2026-09-05T02:09:08+09:00
tags: ["Matemáticas", "Criptografía", "RSA", "GNFS"]
draft: false
image: "gnfs_two_worlds_1788542142485.jpg"
categories: ["Matemáticas, Criptografía y Cuántica"]
---

# ¿Qué es la "Criba General del Cuerpo de Números (GNFS)", las matemáticas más fuertes de la humanidad que rompen el cifrado de Internet?

El Internet que usamos todos los días. Los mensajes de LINE, YouTube, las compras en Amazon, todas las comunicaciones están protegidas por "cifrado".
Actualmente, el representante del cifrado más utilizado en todo el mundo es el "Cifrado RSA".

La clave de la defensa del cifrado RSA es muy simple. Utiliza la propiedad matemática de que **"la factorización de números primos gigantescos no puede ser resuelta ni siquiera por computadoras"**.
Por ejemplo, si es "15", se sabe inmediatamente que es "3 × 5", pero en el momento en que esto se convierte en un "número de 270 dígitos", incluso reuniendo las supercomputadoras de todo el mundo llevaría cientos de millones de años resolverlo.

Sin embargo, los matemáticos tampoco se han quedado callados. Para romper este cifrado inexpugnable, la humanidad ha creado un algoritmo (procedimiento de cálculo) parecido a la magia llamado **"Criba General del Cuerpo de Números (GNFS: General Number Field Sieve)"**.

En este artículo, sin usar términos técnicos en absoluto, explicaremos paso a paso y de manera completa el truco por el cual este "algoritmo más fuerte de la humanidad" rompe el cifrado, solo con conocimientos de **matemáticas de secundaria (factorización de primos, álgebra, máximo común divisor)**!

---

## Capítulo 1: El objetivo de descifrar el código es "la fórmula de tercer año de secundaria"

El mayor ataque especial para enfrentar la factorización de números primos gigantes. Es esta fórmula que se aprende en tercer año de secundaria.

> **$X^2 - Y^2 = (X + Y)(X - Y)$**

Puede que pienses: "¿Eh, se puede romper un cifrado con una fórmula tan básica?". Sin embargo, esta es precisamente la llave maestra que lo revela todo.

El objetivo principal para romper el cifrado es, para un número gigante $N$,
encontrar **"números ($X$ e $Y$) cuyo residuo al dividir $X^2$ e $Y^2$ por $N$ sea el mismo"**.

### ¿Por qué se puede descifrar el código si "el residuo es el mismo"?
Supongamos que el "residuo al dividir por $N$" de dos números, $X^2$ e $Y^2$, es el mismo.
Que el residuo sea el mismo significa que existe la regla de que **la resta "$X^2 - Y^2$" siempre se divide exactamente por $N$ (es un múltiplo de $N$)**.

Aquí, supongamos que el número gigante $N$ usado en el cifrado está hecho por la multiplicación de dos números primos secretos ($p$ y $q$) ($N = p \times q$).

Al factorizar $X^2 - Y^2$, se convierte en **$(X - Y)(X + Y)$**.
El hecho de que esto sea un múltiplo de $N$ significa que en algún lugar de esta multiplicación están escondidos los números primos secretos $p$ y $q$.

Aquí ocurre un milagro.
La probabilidad de que los dos números primos $p$ y $q$ se separen en habitaciones diferentes, **"$p$ va a la habitación de $(X - Y)$" y "$q$ va a la habitación de $(X + Y)$"**, es matemáticamente del **50% (un medio)**.

Con solo el número primo $p$ entrando en la habitación de $(X - Y)$, calculemos el **"máximo común divisor (la pieza común más grande)"** de $(X - Y)$ y $N$.
* Contenido de $(X - Y)$ = $p \times$ algún número
* Contenido de $N$ = $p \times q$
  ¡La única pieza común es **"$p$"**!

Es decir, en el momento en que se calcula el máximo común divisor, el número primo oculto $p$ cae, ¡y el cifrado se descifra por completo! (*El máximo común divisor se puede calcular en un instante incluso en un teléfono inteligente si usas el "Algoritmo de Euclides").

**[Breve columna: ¿Por qué al cuadrado? ¿No se puede al cubo o al doble?]**
> Si es "$2X - 2Y$", se convierte en $2(X - Y)$ y como solo hay una habitación, no se pueden separar los números primos. Si es "$X^3 - Y^3$", el tamaño de las habitaciones se desequilibra y el cálculo se vuelve innecesariamente pesado. Para separar los números primos en dos, la opción más eficiente que se divide bellamente en dos habitaciones es "al cuadrado".

---

## Capítulo 2: ¿Cómo buscar X e Y? "El rompecabezas de recolectar tarjetas de números primos"

Ya sabemos el objetivo. Sin embargo, incluso si buscas al azar "$X^2$ e $Y^2$ que tengan el mismo residuo", no lo encontrarás hasta que se acabe la vida útil del universo.
Por eso, los matemáticos idearon un método genial llamado **"el rompecabezas de recolectar tarjetas de números primos"**.

### Paso 1: Recolectar solo el oro en polvo (números suaves) con un tamiz
Primero, preparamos un número adecuado $Z$, lo elevamos al cuadrado y calculamos el residuo $W$ al dividirlo por $N$.
(El mundo del residuo de $Z^2 = W$)

Factorizamos el residuo $W$ resultante. Aquí, solo cuando aparece un **"$W$ compuesto solo de números primos pequeños como 2, 3, 5, 7, etc."**, guardamos esa fórmula como una "tarjeta ganadora", y si se mezclan números primos grandes, la tiramos.
Es como la tarea de tirar piedras grandes con un tamiz en un río y recolectar solo el polvo de oro.

### Paso 2: El rompecabezas de hacer todo "número par"
Por ejemplo, supongamos que se reunieron las siguientes tres tarjetas de polvo de oro:
* Tarjeta A: $Z_1^2 = 2^3 \times 3^1$
* Tarjeta B: $Z_2^2 = 2^1 \times 5^1$
* Tarjeta C: $Z_3^2 = 3^1 \times 5^1$

Multipliquemos todo esto.
El lado derecho se convierte en $(2^3 \times 3^1) \times (2^1 \times 5^1) \times (3^1 \times 5^1)$,
y al organizarlo todo junto queda **"$2^4 \times 3^2 \times 5^2$"**.

¡Increíblemente, la cantidad de números primos se ha vuelto "4, 2, 2", **todos en cantidades pares**!
El hecho de que todos sean cantidades pares significa que si reducimos la cantidad total a la mitad, se convierte en el "cuadrado de algo".
Es decir, $(2^2 \times 3^1 \times 5^1)^2 = (60)^2$.

Dado que el lado izquierdo es $(Z_1 \times Z_2 \times Z_3)^2$, ¡con esto finalmente se completa el tan esperado par de "$X^2 = Y^2$" que es
**$X = (Z_1 \times Z_2 \times Z_3)$**
**$Y = 60$**!

Dado que a las computadoras se les da muy bien el rompecabezas de calcular si la cantidad de números primos es "par o impar (0 o 1)", con este método pueden encontrar $X$ e $Y$ a alta velocidad.

---

## Capítulo 3: El muro de la desesperación que se interpone

¡Con esto se puede romper cualquier cifrado!... Eso pensarías, pero surge un gran problema.
Si el número $N$ del cifrado tiene hasta "100 dígitos", se puede resolver con este método (llamado criba cuadrática), pero cuando $N$ se convierte en "200 dígitos, 300 dígitos", el $W$ que aparece en el medio del cálculo se vuelve demasiado grande.

Cuando los números se vuelven demasiado grandes, de repente dejan de aparecer los "números hechos solo de primos pequeños (polvo de oro)". Se vuelve más difícil que buscar una lente de contacto en el desierto, y ya no se pueden juntar en absoluto las tarjetas para resolver el rompecabezas.

Aquí finalmente aparece el arma definitiva de la humanidad, la **"Criba General del Cuerpo de Números (GNFS)"**.

---

## Capítulo 4: La idea más fuerte de la humanidad: Crear "dos mundos"

La idea genial de GNFS es: **"Como calculamos solo en el mundo real, los números se vuelven enormes. Entonces, hagamos un 'mundo oculto' usando polinomios (expresiones algebraicas) y dividamos el peso del cálculo en dos"**.

### La magia de las expresiones algebraicas
GNFS convierte un número gigante $N$ en una expresión algebraica usando un número base $m$.
Por ejemplo, si $N=100$, usando $m=4$, $100 = 4^3 + 2(4^2) + 4$.
Usando la letra $x$, convertimos esto en la expresión (el mundo oculto) **$f(x) = x^3 + 2x^2 + x$**.

Lo interesante de esta expresión es que tiene la propiedad de que **"si sustituyes la letra $x$ por $m$ (4 en el ejemplo anterior), siempre puedes regresar (teletransportarte) al número real $N$"**.

### Buscar oro en polvo en dos mundos al mismo tiempo
GNFS crea muchos pares de números enteros $(a, b)$ y realiza los siguientes dos cálculos al mismo tiempo:
1. **El mundo real**: $a - b \times m$
2. **El mundo algebraico**: el valor de calcular $a - b \times x$ con las reglas del álgebra

Al dividir el problema en dos mundos, el tamaño de los números manejados se vuelve drásticamente menor (más ligero). Es la imagen de partir una roca gigante en dos para convertirla en piedras fáciles de manejar.

Luego, con un tamiz (criba), se recolectan solo los pares milagrosos $(a, b)$ que son **"tanto en el mundo real como en el mundo algebraico, 'hechos solo de números primos pequeños (polvo de oro)'"**. Este es el origen del nombre "Criba del Cuerpo de Números".

### El momento en que finalmente se rompe el cifrado
Cuando se reúnen decenas de millones de "tarjetas de polvo de oro" de ambos mundos, utilizando los cálculos de matrices gigantes de una supercomputadora, descubrimos las "combinaciones donde la cantidad de números primos se vuelve toda par" que hicimos en el Capítulo 2.

Una vez que se encuentra la combinación,
* Sea el número al cuadrado creado en el mundo real **$X^2$**
* Sea la expresión al cuadrado creada en el mundo algebraico **$Y(x)^2$**

Finalmente, sustituimos $x$ en el $Y(x)$ del mundo algebraico por $m$, para teletransportarlo y unirlo al mundo real.
Entonces, como magia matemática, se completa estrictamente el estado en que **"el residuo de $X^2$ y $Y^2$ es el mismo"**!

El resto es como en el Capítulo 1, si calculamos el máximo común divisor de $X - Y$ y $N$, el inexpugnable cifrado RSA colapsa estruendosamente, y los números primos secretos hacen su aparición.

---

## Conclusión: Las matemáticas no terminan

Es posible que hayas pensado: "¡Genial, con GNFS se puede romper cualquier cifrado!".
Sin embargo, el cifrado RSA tampoco se queda atrás. Lo que se utiliza en el Internet actual es un número gigantesco monstruoso llamado "RSA-2048 (unos 617 dígitos)".

Aunque GNFS es el algoritmo más fuerte de la humanidad, se dice que incluso para resolver 270 dígitos (RSA-270), llevaría miles o decenas de miles de años incluso conectando las computadoras de todo el mundo. Por ahora, nuestros datos de LINE o bancos están a salvo.

Sin embargo, ¿qué pasaría si apareciera **"una magia para encontrar $X$ e $Y$ en un instante sin importar cuán grande sea el número"**?
En realidad, la existencia más cercana a eso es la **"computadora cuántica (Algoritmo de Shor)"** actualmente en desarrollo. Usando las propiedades ondulatorias de la mecánica cuántica, se ha demostrado matemáticamente que se puede ignorar el molesto rompecabezas de recolección de tarjetas y encontrar la respuesta en un solo intento.

La interminable batalla de ingenio entre los creadores de cifrados (defensa) y los creadores de algoritmos para romperlos (ataque).
Saber que la "factorización de primos" o el "álgebra" que se aprenden en la secundaria son en realidad armas que luchan ferozmente en la vanguardia de la seguridad mundial, ¿no hace que las clases de matemáticas parezcan un poco más interesantes?

¡Podrías ser tú, que estás leyendo este artículo, quien descubra el algoritmo más fuerte del futuro!

--- 
*(※Este artículo conceptualiza el encanto matemático del criptoanálisis para estudiantes de secundaria. El GNFS real se calcula estrictamente usando matemáticas universitarias avanzadas, como el grupo de clases de ideales de cuerpos algebraicos y homomorfismos)*

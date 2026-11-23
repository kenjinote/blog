---
title: '¿Existe un algoritmo que supere a GNFS (Criba General del Cuerpo de Números)?'
slug: "beyond-gnfs-integer-factorization-algorithms"
date: "2026-09-11T09:00:00+09:00"
lastmod: "2026-11-23T09:00:00+09:00"
image: "img/eyecatch.jpg"
math: true
mermaid: true
categories: ["mathematics", "cryptography"]
tags: ["GNFS", "Factorización de enteros", "RSA", "Algoritmos"]
---

## 1. Introducción: La factorización de enteros y la base de la criptografía moderna

RSA es uno de varios sistemas de clave pública y su seguridad se basa, en parte, en la dificultad de factorizar enteros grandes. Sin embargo, la seguridad de Internet en su conjunto no depende solo de RSA. Un método eficiente de factorización amenazaría los usos basados en RSA, pero no derrumbaría automáticamente toda la infraestructura de comunicaciones.

Para factorizar enteros grandes generales, GNFS es uno de los métodos clásicos más conocidos. Se ha utilizado para factorizar números como RSA-768 y RSA-250; los números con estructura especial pueden ser más adecuados para métodos como SNFS. [Informe de RSA-250](https://eprint.iacr.org/2020/697)

Sin embargo, los criptógrafos y matemáticos siempre se han planteado las siguientes preguntas: "¿Existe algún algoritmo clásico que supere a GNFS?", "¿Dónde están los límites de los ordenadores clásicos?" y "¿Cómo cambiarán los ordenadores cuánticos esta situación?".

En este artículo, analizaremos en profundidad la profunda estructura matemática detrás de GNFS y realizaremos un análisis técnico detallado de la selección de polinomios, el proceso de cribado y los pasos de álgebra lineal utilizando el algoritmo de Wiedemann por bloques. Además, consideraremos los métodos de extensión de GNFS a través de las mejoras de Coppersmith y otros, y compararemos y explicaremos las diferencias decisivas entre los algoritmos clásicos de tiempo subexponencial (Sub-exponential time) y los algoritmos cuánticos de tiempo polinómico desde una perspectiva matemática.

---

## 2. Complejidad asintótica y notación L (L-notation)

Al evaluar la complejidad de los algoritmos de factorización de enteros, en lugar de utilizar la notación estándar de tiempo polinómico (como $O(n^k)$), se utiliza la **notación L (L-notation)** para expresar el tiempo subexponencial con respecto al número de dígitos de la entrada $n$. La notación L se define de la siguiente manera:

$$
L_n[\alpha, c] = \exp \left( (c + o(1)) (\ln n)^\alpha (\ln \ln n)^{1-\alpha} \right)
$$

Aquí, $n$ es el número entero a factorizar, y $\ln n$ es el logaritmo natural, el cual es proporcional a la longitud de bits de $n$.
- Caso $\alpha = 0$: $L_n[0, c] = \exp(c \ln \ln n) = (\ln n)^c$, lo que representa un **tiempo polinómico (Polynomial time)** con respecto a la longitud de bits.
- Caso $\alpha = 1$: $L_n[1, c] = \exp(c \ln n) = n^c$, lo que representa un **tiempo exponencial (Exponential time)** con respecto a la longitud de bits.
- Caso $0 < \alpha < 1$: Se sitúa entre el tiempo polinómico y el tiempo exponencial, lo que resulta en un **tiempo subexponencial (Sub-exponential time)**.

La historia de la evolución de los algoritmos de factorización de enteros ha sido también la historia de la reducción gradual de este valor $\alpha$.
- **CFRAC**: tiempo esperado heurístico $L_n[1/2,\sqrt{2}]$ ([referencia](https://cacr.uwaterloo.ca/hac/about/chap3.pdf)).
- **MPQS/QS**: tiempo esperado heurístico $L_n[1/2,1]$ ([documentación de FLINT](https://flintlib.org/doc/algorithms/number-theory/quadratic-sieve.html)).
- **GNFS**: la estimación heurística habitual es $L_n[1/3,(64/9)^{1/3}]$; no es una cota demostrada ni un tiempo práctico directo ([análisis de NFS](https://arxiv.org/abs/2007.02730)).

---

## 3. Visión general del algoritmo GNFS (Criba General del Cuerpo de Números) y su estructura matemática

GNFS y QS utilizan la idea de congruencia de cuadrados: buscan $X,Y$ tales que $X^2\equiv Y^2\pmod n$ y $X\not\equiv\pm Y\pmod n$; entonces $\gcd(X-Y,n)$ puede dar un factor no trivial.

Sin embargo, la esencia de GNFS es que no realiza esto solo en el cuerpo de los números racionales $\mathbb{Q}$, sino que busca simultáneamente "números suaves (Smooth numbers)" tanto en un cuerpo de extensión llamado cuerpo de números algebraicos (Algebraic Number Field) $\mathbb{Q}(\alpha)$ como en el cuerpo de los números racionales, y construye la relación de congruencia a través de un homomorfismo.

El proceso de GNFS se divide principalmente en 5 fases.

```mermaid
graph TD
  A["Problema de factorización (entrada n)"] --> B["1. Selección de polinomios (Polynomial Selection)"]
  B --> C["2. Fase de cribado (Sieving Phase)"]
  C --> D["3. Fase de filtrado (Filtering Phase)"]
  D --> E["4. Fase de álgebra lineal (Linear Algebra Phase)"]
  E --> F["5. Fase de raíz cuadrada (Square Root Phase)"]
  F --> G["Salida de factores primos p, q"]```

### 3.1 Fase 1: Selección de polinomios (Polynomial Selection)

El éxito de GNFS depende en gran medida de la elección adecuada de los polinomios. El objetivo es encontrar dos polinomios irreducibles, $f_1(x)$ (lado racional) y $f_2(x)$ (lado algebraico), que compartan una raíz común $m$. Es decir, satisfacen:
$f_1(m) \equiv f_2(m) \equiv 0 \pmod n$

Generalmente, para el polinomio del lado racional se elige una expresión lineal $f_1(x) = x - m$, y para el polinomio del lado algebraico $f_2(x)$ se elige un polinomio mónico de grado $d$ (típicamente 5 o 6). El enfoque más clásico es el **método de base $m$ (Base-$m$ method)**.
Se elige un entero $m = \lfloor n^{1/(d+1)} \rfloor$ que se aproxima a $n$ elevado a $1/(d+1)$, y se expande $n$ en base $m$.
$n = c_d m^d + c_{d-1} m^{d-1} + \dots + c_1 m + c_0$
De este modo, se obtiene el polinomio $f_2(x) = c_d x^d + c_{d-1} x^{d-1} + \dots + c_0$. Obviamente, $f_2(m) = n \equiv 0 \pmod n$.

Sin embargo, en las implementaciones modernas se utiliza el **algoritmo de Kleinjung**. Éste optimiza las propiedades algebraicas (como el valor $E$ de Murphy o el valor $\alpha$) evitando que los coeficientes del polinomio se vuelvan extremadamente grandes (optimización de asimetría o Skewness), y busca polinomios que faciliten la generación de números suaves en el proceso de cribado. Solamente en este paso se invierten enormes recursos computacionales.

### 3.2 Fase 2: Fase de cribado (Sieving Phase)

Una vez que se deciden los polinomios, se entra en la fase de "cribado (Sieving)", que es la que soporta la mayor carga computacional del algoritmo. Aquí se busca un par $(a, b)$. Se requiere que este par sea coprimo, y que los dos valores siguientes sean simultáneamente "suaves (Smooth)".

1. **Norma en el lado racional**: $F_1(a, b) = b \cdot f_1(a/b) = a - bm$
2. **Norma en el lado algebraico**: $F_2(a, b) = b^d \cdot f_2(a/b)$

"Suave" significa que puede ser factorizado únicamente por números primos que se encuentren por debajo de un límite especificado (Sieve bound). Se preparan una base de factores (Factor base) para el lado racional y otra para el lado algebraico, y sobre un enorme espacio de búsqueda, se descubren eficientemente los números suaves utilizando un enfoque similar a la Criba de Eratóstenes.
En la actualidad, la técnica principal es el método conocido como **criba de retículos (Lattice Sieving)**, en la cual, al fijar un número primo específico $q$, se criban únicamente los pares $(a, b)$ de una subred que hacen que tanto el lado racional como el algebraico sean múltiplos de $q$, logrando así una eficiencia extremadamente alta.

### 3.3 Fase 3: Fase de filtrado (Filtering Phase)

El número de relaciones suaves encontradas en el proceso de cribado puede alcanzar cientos o miles de millones. Sin embargo, estas también incluyen mucha información inútil.
El objetivo del filtrado es construir una enorme matriz dispersa (Sparse Matrix) y, al mismo tiempo, reducir su dimensión lo máximo posible.

Específicamente se realizan las siguientes operaciones:
- **Eliminación de relaciones únicas (Singleton removal)**: Se eliminan las relaciones que contienen factores primos que aparecen solo una vez.
- **Eliminación y fusión de clanes (Clique removal / Merging)**: Las relaciones con factores primos que aparecen dos o más veces se multiplican entre sí para eliminar variables, contrayéndolas en un sistema de ecuaciones más denso, pero de menor dimensión.

Como resultado, una matriz de miles de millones de filas se comprime a una enorme matriz dispersa $\mathbf{A}$ de unos pocos millones de filas (cuyos elementos son 0 y 1 sobre el cuerpo $\mathbb{F}_2$).

### 3.4 Fase 4: Fase de álgebra lineal (Linear Algebra Phase)

Aquí buscamos un vector no nulo $\mathbf{x}$ tal que $\mathbf{A}\mathbf{x}=\mathbf{0}$ sobre $\mathbb{F}_2$; es decir, un vector del núcleo (espacio nulo) de la matriz dispersa.

Para matrices dispersas se usan métodos iterativos de Krylov como Block Lanczos y Block Wiedemann. El informe de factorización de RSA-250 documenta un cálculo con Block Wiedemann; la elección y el rendimiento dependen de la matriz, la implementación y la arquitectura de cómputo. [Informe de RSA-250](https://eprint.iacr.org/2020/697)


### 3.5 Fase 5: Fase de raíz cuadrada (Square Root Phase)

A partir de la solución del álgebra lineal, se construye un producto que será un "cuadrado perfecto" tanto en el lado racional como en el algebraico.
En el lado racional, el producto $\prod (a-bm)$ se convierte en el cuadrado $X^2$ de algún entero $X$, y en el lado algebraico, el producto de los ideales correspondientes se convierte en un cuadrado perfecto $\gamma^2$ sobre el cuerpo de los números algebraicos.
Al calcular este $\gamma$ en el cuerpo de los números algebraicos y aplicar el homomorfismo $\phi: \alpha \mapsto m \pmod n$ hacia el anillo de los enteros racionales, se obtiene la congruencia:
$X^2 \equiv \phi(\gamma)^2 \equiv Y^2 \pmod n$

Para el cálculo de la raíz cuadrada en el cuerpo de los números algebraicos se utilizan algoritmos complejos como el **método de Montgomery (Montgomery's Method)**, lo cual exige un profundo conocimiento de la teoría de números algebraicos. Finalmente, se calcula $\gcd(X-Y, n)$ y, si se obtiene un factor no trivial, la factorización de enteros estará completada.

---

## 4. ¿Existe un algoritmo clásico que supere a GNFS?

Hasta la fecha, no se ha descubierto ningún algoritmo clásico para la factorización de enteros generales cuya complejidad asintótica caiga por debajo de $L_n[1/3, c]$. Sin embargo, existen varios algoritmos derivados e intentos de superar los límites teóricos y prácticos.

### 4.1 Criba Múltiple del Cuerpo de Números (MNFS: Multiple Number Field Sieve)

Como un enfoque extendido de GNFS, existe la **Criba Múltiple del Cuerpo de Números (MNFS)** de D. Coppersmith. En GNFS se utilizan 2 polinomios (lado racional y lado algebraico), pero en MNFS se utilizan varios polinomios algebraicos diferentes simultáneamente contra un solo polinomio racional.

$$ f_1(x), f_{2,1}(x), f_{2,2}(x), \dots, f_{2,V}(x) $$

Al utilizar múltiples cuerpos algebraicos, se puede aumentar drásticamente la probabilidad de que "sea suave en alguno de los cuerpos algebraicos" en cada paso del cribado. Coppersmith logró reducir ligeramente la constante $c$ de la complejidad computacional $L_n[1/3, c]$ mediante este enfoque.

Sin embargo, en la práctica, la carga adicional (overhead) de gestionar múltiples cuerpos es enorme y no se ha logrado un avance decisivo frente al módulo [RSA](https://kenji.blog/es/p/modern-cryptography-public-key-hash-signature/) a una escala de aplicación práctica.

### 4.2 ¿Es posible un algoritmo de la clase $L_n[1/4]$?

No se conoce un algoritmo clásico general de factorización con complejidad asintótica inferior a la forma habitual de GNFS, pero eso no demuestra que uno mejor sea imposible. Los análisis de números suaves describen métodos de cribado conocidos, no una cota inferior para todos los algoritmos; la cuestión sigue abierta.
---

## 5. El gran avance gracias a la computación cuántica: El algoritmo de Shor

Mientras que los ordenadores clásicos se enfrentan a la barrera de $L_n[1/3]$, el **algoritmo de Shor ([Shor's Algorithm](https://kenji.blog/es/p/quantum-computing-shors-algorithm/))**, presentado por Peter Shor en 1994, destruyó esta barrera al cambiar fundamentalmente el propio modelo de cálculo.

### 5.1 El impacto del tiempo polinómico cuántico

El algoritmo de Shor reduce el problema de factorización de enteros al "Problema de encontrar el orden (Order Finding Problem)". Dado cierto entero $a$, es el problema de encontrar el período (orden) $r$ de la función $f(x) = a^x \pmod n$.
Shor utiliza la interferencia cuántica para extraer información sobre el período de la función; esto no significa que todos los estados superpuestos se lean en paralelo.

Desde el punto de vista de la complejidad computacional, el tiempo de ejecución del algoritmo de Shor es de **tiempo polinómico cuántico**, concretamente de la siguiente manera:
$$ O((\log n)^3) $$

```mermaid
graph LR
  A["Algoritmo clásico (GNFS)"] -->|"Límite"| B["Tiempo subexponencial L_n[1/3]"]
  C["Algoritmo cuántico (Shor)"] -->|"Gran avance"| D["Tiempo polinómico O((log n)^3)"]
  B --> E["Uso continuo del cifrado RSA (Aumento de longitud de clave)"]
  D --> F["RSA vulnerable si existe un ordenador cuántico tolerante a fallos suficientemente capaz"]
```

### 5.2 Tiempo subexponencial clásico vs Tiempo polinómico cuántico

Shor factoriza en tiempo polinómico en un modelo cuántico idealizado, pero eso no da por sí solo un coste práctico para una máquina tolerante a fallos. Gidney y Ekerå estimaron en 2021 unos 20 millones de cúbits físicos y 8 horas; en 2025, Gidney estimó menos de un millón de cúbits físicos con ruido y menos de una semana con otro diseño y otros supuestos. Son estimaciones condicionadas, no demostraciones de ruptura de RSA-2048; ningún ordenador cuántico ha factorizado un entero de ese tamaño. No se pueden deducir puertas ni tiempo únicamente de $2048^3$. [2021](https://doi.org/10.22331/q-2021-04-15-433) · [2025](https://arxiv.org/abs/2505.15917)

La fórmula asintótica de GNFS tampoco proporciona directamente operaciones ni tiempo; hacen falta un modelo de costes y parámetros explícitos.
## 6. Conclusión: Perspectivas hacia la próxima generación

GNFS es el mejor método general conocido, no un límite demostrado. No se conoce un algoritmo clásico general con mejor complejidad asintótica, pero tampoco hay una prueba que lo descarte. Las mejoras prácticas no justifican garantías de tiempo ni afirmar que RSA será seguro durante décadas. Las estimaciones de Shor son condicionales y no describen el hardware actual. La transición poscuántica sigue las normas y recomendaciones oficiales aplicables.

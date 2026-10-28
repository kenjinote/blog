---
title: 'Código de muestra en C simple para generar e identificar números primos dentro de un rango especificado'
slug: "Número primoを生成するC言語コード"
tags: ["C", "Números primos", "Algoritmos", "Matemáticas"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Enumera primos mediante división por tentativa en C17, con validación de entrada, prevención de desbordamientos, ejemplos y límites de aplicación."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

Este programa en C17 usa división por tentativa para comprobar números y enumerar los primos desde 1 hasta un límite superior `n`, incluido. Un primo es un entero mayor o igual que 2; por tanto, los límites 0 y 1 no producen ningún primo. Introduce un único entero decimal entre 0 e `INT_MAX`.

## Código

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>
#include <ctype.h>
#include <string.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    for (int i = 5; i <= num / i; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    if (n < 2) {
        putchar('\n');
        return;
    }
    printf("2");
    for (int i = 3; i <= n; ) {
        if (isPrime(i)) printf(" %d", i);
        if (i > n - 2) break;
        i += 2;
    }
    putchar('\n');
}

bool readLimit(int *n) {
    char line[128];
    if (fgets(line, sizeof line, stdin) == NULL) return false;
    if (strchr(line, '\n') == NULL) {
        int next = getchar();
        if (next != '\n' && next != EOF) return false;
        if (ferror(stdin)) return false;
    }

    errno = 0;
    char *end;
    long value = strtol(line, &end, 10);
    if (end == line || errno == ERANGE || value < 0 || value > INT_MAX)
        return false;
    while (isspace((unsigned char)*end)) ++end;
    if (*end != '\0') return false;
    *n = (int)value;
    return true;
}

int main(void) {
    int n;
    printf("Introduce un límite superior (0 a %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Entrada no válida. Introduce un entero de 0 a %d.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Primos de 1 a %d:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Compilación y ejemplo de ejecución

Guarda el programa como `primes.c`. En un entorno con GCC, ejecuta `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes` y después `./primes`. Al introducir `30`, se muestra un encabezado seguido de esta línea:

```text
2 3 5 7 11 13 17 19 23 29
```

El límite 2 produce `2`; 0 y 1 producen una línea vacía. Se lee una línea de texto de hasta 127 bytes, sin contar el salto de línea. Se permiten espacios en blanco al principio y al final, así como un `+` inicial. Los valores negativos, las líneas vacías, el texto que no representa un entero, los valores fuera de rango, las líneas demasiado largas y los errores de lectura hacen que el programa termine con un error. Solo se procesa la primera línea; las posteriores no se utilizan.

## Funcionamiento de la prueba y de la entrada

1. `isPrime` devuelve falso para los valores menores o iguales que 1, y verdadero para 2 y 3. Para los demás múltiplos de 2 o 3 devuelve falso. Después comprueba `i` e `i + 2` para `i = 5, 11, 17, ...`. Los divisores candidatos tienen la forma `6k - 1` o `6k + 1`; no son múltiplos de 6, y tampoco todos los números de estas formas son primos.
2. Todo número compuesto tiene un divisor primo menor o igual que su raíz cuadrada. Por eso basta con continuar mientras `i <= num / i`. Para enteros positivos, esta condición cubre el mismo rango que `i * i <= num`, evitando el desbordamiento de la multiplicación en `int`. No hace falta calcular una raíz cuadrada en coma flotante.
3. `printPrimes` solo imprime una línea vacía si el límite es menor que 2. En caso contrario, imprime 2 y comprueba los candidatos impares. Si `i > n - 2`, sale antes de sumar, lo que evita el desbordamiento del último `i += 2`, incluso con un límite igual a `INT_MAX`.
4. `readLimit` lee con `fgets`, comprueba el puntero al final de la conversión y `ERANGE` de `strtol`, y verifica el rango de 0 a `INT_MAX` antes de convertir a `int`. El argumento de `isspace` se convierte a `unsigned char`. Ignorar el retorno de `scanf("%d", &n)` puede llevar a usar un `n` sin inicializar tras una entrada fallida. Tampoco se puede suponer que un resultado fuera del rango de `int` se trate como un simple fallo de conversión.

## Alcance

`INT_MAX` depende de la implementación. Con un `int` de 32 bits vale 2,147,483,647, pero C no exige ese valor en todos los sistemas. Poder representar un límite no significa que se puedan imprimir rápidamente todos los primos hasta él.

Esta implementación sirve para aprender división por tentativa. La prueba de un número realiza, como máximo, una cantidad de divisiones proporcional a su raíz cuadrada; para enumerar todos los candidatos, una cota superior aproximada es `O(n sqrt(n))` divisiones. Aquí se cuenta cada división como una operación: no se trata de complejidad en bits ni de un tiempo medido. Para enumerar primos en un intervalo grande, considera la criba de Eratóstenes. Este programa no es un generador de primos criptográficos. Para comprobar enteros grandes, consulta el [artículo sobre Miller–Rabin](https://kenji.blog/es/p/cpp-fast-prime-testing-miller-rabin/).

Las reglas de entrada y aritmética entera de C pueden consultarse en los apartados 6.5, 7.4, 7.21.6.2, 7.21.7.2 y 7.22.1.4 del [borrador de comité C11 N1570 de WG14](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).

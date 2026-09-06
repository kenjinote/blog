---






title: "Código en C para generar números primos"
date: 2024-08-24T09:38:10+09:00
tags: ["C", "Números primos", "Algoritmos", "Matemáticas"]
draft: false
image: "img.png"
categories: ["Matemáticas, Criptografía y Cuántica"]
---







A continuación, se muestra un código en C simple que genera números primos dentro de un rango especificado. En este ejemplo, se enumeran los números primos del 1 al n.

```cpp
#include <stdio.h>
#include <stdbool.h>

bool isPrime(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    
    for (int i = 5; i * i <= num; i += 6) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

void printPrimes(int n) {
    printf("2 ");
    for (int i = 3; i <= n; i += 2) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }
    printf("\n");
}

int main() {
    int n;
    printf("Ingrese el valor maximo del rango para generar numeros primos: ");
    scanf("%d", &n);
    printf("Los numeros primos de 1 a %d son los siguientes:\n", n);
    printPrimes(n);
    return 0;
}
```

Este código funciona de la siguiente manera:

1. Función isPrime: Determina si un número dado es primo. Por razones de eficiencia, primero verifica si es divisible por 2 y 3, y luego procede a verificar en múltiplos de 6.
2. Función printPrimes: Imprime los números primos dentro del rango especificado. El 2 se imprime primero, y luego solo se verifican los números impares.
3. Función main: Pide al usuario que ingrese el valor máximo del rango y luego imprime los números primos dentro de ese rango.

Al compilar y ejecutar este código, se mostrarán los números primos dentro del rango especificado.

---
title: "Código C para gerar números primos"
slug: "codigo-c-para-gerar-numeros-primos"
date: 2024-08-24T09:38:10+09:00
tags: ["C", "Números primos", "Algoritmo", "Matemática"]
draft: false
image: "img.png"
categories: ["Matemática, Criptografia e Quântica"]
---

Abaixo está um código C simples que gera números primos dentro de um intervalo especificado. Neste exemplo, enumeramos números primos de 1 a n.

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
    printf("Digite o valor máximo do intervalo para gerar números primos: ");
    scanf("%d", &n);
    printf("Os números primos de 1 a %d são:\n", n);
    printPrimes(n);
    return 0;
}
```

Este código funciona da seguinte forma:

1. Função isPrime: Determina se um determinado número é primo. Por uma questão de eficiência, primeiro verifica-se se é divisível por 2 e 3 e, em seguida, prossegue verificando em múltiplos de 6.
2. Função printPrimes: Gera números primos dentro de um intervalo especificado. O 2 é impresso primeiro e, em seguida, apenas os números ímpares são verificados.
3. Função main: Solicita que o usuário insira o valor máximo do intervalo e imprime os números primos dentro desse intervalo.

Se você compilar e executar este código, os números primos dentro do intervalo especificado serão exibidos.

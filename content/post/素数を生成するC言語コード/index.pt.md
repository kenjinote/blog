---
title: 'Código de exemplo simples em C para gerar e determinar números primos em um intervalo especificado'
slug: "Número Primoを生成するC言語コード"
tags: ["C", "Números primos", "Algoritmo", "Matemática"]
draft: false
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Liste primos com divisão por tentativa em C17, evitando estouros de inteiros e validando a entrada com fgets e strtol. Exemplos e limites de aplicação."
date: 2024-08-24T09:38:10+09:00
lastmod: 2026-10-28
---

Este programa em C17 usa divisão por tentativa para testar números e listar os primos de 1 até um limite superior `n`, inclusive. Um primo é um inteiro maior ou igual a 2; portanto, limites de 0 ou 1 não produzem primos. Digite um único inteiro decimal entre 0 e `INT_MAX`.

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
    printf("Digite um limite superior (0 a %d): ", INT_MAX);
    fflush(stdout);
    if (!readLimit(&n)) {
        fprintf(stderr, "Entrada inválida. Digite um inteiro de 0 a %d.\n", INT_MAX);
        return EXIT_FAILURE;
    }
    printf("Primos de 1 a %d:\n", n);
    printPrimes(n);
    return EXIT_SUCCESS;
}
```

## Compilação e exemplo de execução

Salve como `primes.c`. Em um ambiente com GCC, execute `gcc -std=c17 -Wall -Wextra -O2 primes.c -o primes` e depois `./primes`. Ao digitar `30`, o programa mostra um cabeçalho seguido desta linha:

```text
2 3 5 7 11 13 17 19 23 29
```

O limite 2 produz `2`; 0 ou 1 produz uma linha vazia. A entrada é uma linha de texto de até 127 bytes, sem contar a quebra de linha. Espaços em branco no início e no fim e um `+` inicial são permitidos. Valores negativos, linhas vazias, texto que não representa um inteiro, valores fora do intervalo, linhas longas demais e falhas de leitura causam um erro e encerram o programa. Apenas a primeira linha é processada; as seguintes não são usadas.

## Como funcionam o teste e o tratamento da entrada

1. `isPrime` retorna falso para valores menores ou iguais a 1 e verdadeiro para 2 e 3. Para os demais múltiplos de 2 ou 3, retorna falso. Depois testa `i` e `i + 2` para `i = 5, 11, 17, ...`. Os candidatos a divisor têm a forma `6k - 1` ou `6k + 1`, e não são múltiplos de 6. Nem todo número dessas formas é primo.
2. Todo número composto tem um divisor primo menor ou igual à sua raiz quadrada. Assim, basta continuar enquanto `i <= num / i`. Para inteiros positivos, essa condição cobre o mesmo intervalo que `i * i <= num`, evitando o estouro da multiplicação em `int`. Não é necessário calcular uma raiz quadrada em ponto flutuante.
3. `printPrimes` imprime apenas uma linha vazia quando o limite é menor que 2. Caso contrário, imprime 2 e testa os candidatos ímpares. Se `i > n - 2`, sai antes de somar, evitando o estouro do último `i += 2`, mesmo quando o limite é `INT_MAX`.
4. `readLimit` lê com `fgets`, verifica o ponteiro para o fim da conversão e `ERANGE` de `strtol`, e confirma o intervalo de 0 a `INT_MAX` antes de converter para `int`. O argumento de `isspace` é convertido para `unsigned char`. Ignorar o retorno de `scanf("%d", &n)` pode levar ao uso de um `n` não inicializado após uma entrada malsucedida. Também não se pode presumir que um resultado fora do intervalo de `int` seja tratado como uma simples falha de conversão.

## Aplicabilidade

`INT_MAX` depende da implementação. Com um `int` de 32 bits, vale 2,147,483,647, mas C não exige esse valor em todas as implementações. Poder representar um limite não significa que listar todos os primos até ele será rápido.

Esta implementação serve para aprender divisão por tentativa. O teste de um número usa, no máximo, uma quantidade de divisões proporcional à sua raiz quadrada; para listar todos os candidatos, um limite superior aproximado é `O(n sqrt(n))` divisões. Aqui cada divisão conta como uma operação: não se trata de complexidade em bits nem de tempo medido. Para listar primos em intervalos grandes, considere a peneira de Eratóstenes. Este programa não é um gerador de primos criptográficos. Para testar inteiros grandes, consulte o [artigo sobre Miller–Rabin](https://kenji.blog/pt/p/cpp-fast-prime-testing-miller-rabin/).

As regras das funções de entrada e da aritmética inteira de C estão nas seções 6.5, 7.4, 7.21.6.2, 7.21.7.2 e 7.22.1.4 do [rascunho de comitê C11 N1570 do WG14](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf).

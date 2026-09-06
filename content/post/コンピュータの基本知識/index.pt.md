---
title: "Conhecimentos Básicos de Computador"
slug: "コンピュータの基本知識"
date: 2024-09-19T01:10:20+09:00
tags: ["Computador", "Conhecimentos Básicos"]
draft: false
image: "img.png"
categories: ["TI e Tecnologia"]
---

# Conhecimentos Básicos de Computador

Esta página explica o que é um computador.

## Definição de Computador
Um computador é uma máquina que possui os seguintes 5 dispositivos:

1. Dispositivo de entrada
2. Dispositivo de saída
3. Dispositivo de armazenamento
4. Dispositivo de controle
5. Dispositivo lógico e aritmético

Resumidamente, um computador é uma máquina que realiza um `processamento` específico para uma dada `entrada` e `produz` o resultado.
Ele pode `armazenar` dados inseridos como `entrada`, realizar `operações aritméticas` e `produzir saídas`. O `controle` tem o papel de controlar os 4 dispositivos mencionados acima.

## O que é necessário para operar um computador
Para operar um computador, são necessários programas (software) além dos dispositivos (hardware).

Os programas instruem o computador sobre o tipo de processamento a ser realizado. Eles são escritos num formato que o computador possa compreender.

Um exemplo de programa é mostrado abaixo:
Um programa que calcula a soma de 1 até um número inteiro fornecido.
```
#include <iostream>
using namespace std;

int main() {
    // Alocação de memória necessária
    int n, sum = 0;
    
    // Saída
    cout << "Digite um número inteiro: ";
    
    // Entrada 
    cin >> n;
    
    // Operação
    for (int i = 1; i <= n; i++) { // Operação
        sum += i;
    }
    
    // Saída
    cout << "A soma de 1 até " << n << " é " << sum << "." << endl;
    
    // Fim
    return 0;
}
```

O programa é convertido em código de máquina por um compilador e transformado num formato que o computador possa executar.

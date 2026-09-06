---
title: "Como listar números primos menores que 1000 usando o Crivo de Eratóstenes"
slug: "Como listar números primos menores que 1000 usando o Crivo de Eratóstenes"
date: 2023-04-09T12:54:24+09:00
tags: ["Crivo de Eratóstenes", "Números primos", "Matemática", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["Matemática, Criptografia, Quântica"]
---

## O que é o Crivo de Eratóstenes?

O Crivo de Eratóstenes é um algoritmo para encontrar todos os números primos até um determinado limite.
O algoritmo é simples e pode ser implementado através das seguintes etapas:

1. Crie um array booleano com N elementos e inicialize todos os elementos como verdadeiros (true).
2. Defina os elementos nas posições 0 e 1 do array como falsos (pois 0 e 1 não são números primos).
3. Se o 2º elemento do array for verdadeiro, imprima 2 como número primo.
4. Defina todos os múltiplos de 2 a partir de $2^2$ como falsos (*).
5. Se o 3º elemento do array for verdadeiro, imprima 3 como número primo.
6. Defina todos os múltiplos de 3 a partir de $3^2$ como falsos.
7. Repita o mesmo processo para o 4º, 5º, ..., e N-ésimo elementos.

* O motivo de começar a definir como falsos os múltiplos a partir do quadrado (ex: $2^2$) é que os números menores que o quadrado já foram processados (já foram marcados ou listados).

![](Animation_Sieb_des_Eratosthenes.gif)


## Implementação em Rust

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![true; n+1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..=n {
        if is_prime[i] {
            println!("{}", i);
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
    }
}
```

## Versão levemente otimizada

Podemos otimizar um pouco a implementação considerando os seguintes pontos:

- Inicializar o array com falso (false) em vez de verdadeiro (true) (isso é mais rápido).
- Uma vez que múltiplos de 2 não são números primos, pule o processo de definir múltiplos de 2 como falso.
- Não é necessário iterar até n; listar os números primos até a raiz quadrada de n é suficiente para encontrar todos os primos menores ou iguais a n.

```
fn main() {
    let n = 1000;
    let mut is_prime = vec![false; n+1];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }
    for i in 3..=((n as f64).sqrt() as usize) {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i * 2;
            }
        }
    }
    for i in (2..=n).filter(|&x| is_prime[x]) {
        println!("{}", i);
    }
}
```

## Referência
- [Crivo de Eratóstenes (Wikipedia)](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)

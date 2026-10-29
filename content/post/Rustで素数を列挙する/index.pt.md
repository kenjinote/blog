---
title: 'Como criar um programa que enumera números primos em Rust e exemplos de código'
slug: "RustでNúmero Primoを列挙する"
tags: ["Rust","Números Primos","Algoritmo"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "Liste primos em Rust dividindo por primos conhecidos. Limites pequenos, corte na raiz quadrada, iteração do vetor e incrementos dentro do intervalo."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

Este exemplo em Rust guarda os primos encontrados e os usa na divisão por tentativa. `primes_up_to(max)` retorna uma lista de primos até o limite, inclusive. Existem 168 primos menores ou iguais a 1000; 0 e 1 não são primos. Não é uma implementação de crivo.

## Código

```rust
fn primes_up_to(max: usize) -> Vec<usize> {
    if max < 2 {
        return Vec::new();
    }
    let mut primes = vec![2];
    let mut n = 3;
    while n <= max {
        let mut is_prime = true;
        for &p in &primes {
            if p > n / p {
                break;
            }
            if n % p == 0 {
                is_prime = false;
                break;
            }
        }
        if is_prime {
            primes.push(n);
        }
        if max - n < 2 {
            break;
        }
        n += 2;
    }
    primes
}

fn main() {
    for p in primes_up_to(1000) {
        println!("{}", p);
    }
}
```

## Execução e limites pequenos

Salve como `primes.rs` e compile com `rustc --edition=2021 primes.rs -o primes`. No Windows, use `primes.exe` como nome do executável. A execução imprime 168 linhas, começando por 2 e terminando em 997. Estes exemplos foram executados com Rust 1.90.0.

`primes_up_to(0)` e `primes_up_to(1)` retornam um vetor vazio; `primes_up_to(2)` retorna `[2]`, `primes_up_to(3)` retorna `[2, 3]`, e `primes_up_to(10)` retorna `[2, 3, 5, 7]`. O tipo do parâmetro, `usize`, exclui limites negativos. Este programa não analisa a entrada padrão.

## Como funcionam o teste e o laço

1. Retorne um resultado vazio para um limite menor que 2. Caso contrário, guarde 2 e teste apenas os candidatos ímpares de 3 até o limite. O limite é verificado antes de processar cada candidato, portanto o limite 2 não adiciona 3.
2. Um candidato composto `n` tem um fator primo menor ou igual à sua raiz quadrada. Esses primos já estão na lista a partir dos candidatos anteriores. Se uma divisão não deixar resto, rejeite o candidato. Se nenhum divisor foi encontrado quando `p > n / p`, não é necessário continuar a divisão por tentativa. A divisão inteira positiva expressa a condição da raiz quadrada sem calcular `p * p` nem uma raiz em ponto flutuante.
3. `for &p in &primes` toma a lista emprestada, recebe referências sucessivas e copia cada valor `usize` para `p`. Um primo novo só é adicionado depois que esse laço termina. O `for p in primes_up_to(1000)` final retira os valores do vetor retornado e os imprime. A [documentação de Vec do Rust](https://doc.rust-lang.org/std/vec/struct.Vec.html) distingue a iteração por empréstimo da iteração que assume a propriedade do vetor e o consome.
4. Dentro de `n <= max`, `max - n` não pode ser negativo. Se a distância restante for menor que 2, saia antes de somar; caso contrário, execute `n += 2`. Assim, o incremento não ultrapassa o limite.

## Aplicabilidade

O programa original com limite fixo 1000 também imprime corretamente 168 primos. Porém, trocar apenas o limite para 0, 1 ou 2 produz valores 2 ou 3 fora do intervalo, pois o limite não é verificado antes do processamento. A função reutilizável aqui trata essas fronteiras.

A lista guarda um `usize` por primo descoberto. Os metadados do vetor e a capacidade alocada também precisam de memória. Um limite superior aproximado para as divisões é `O(max sqrt(max))`, contando uma divisão como uma operação; não é tempo medido nem complexidade em bits. Limites maiores exigem mais tempo e armazenamento, sem garantia de listar rapidamente primos até limites arbitrariamente grandes. Para intervalos grandes, veja o [artigo sobre o crivo de Eratóstenes](https://kenji.blog/pt/p/crivo-de-erat%C3%B3stenes%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEn%C3%BAmero-primo%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). Não é um gerador de primos criptográficos.

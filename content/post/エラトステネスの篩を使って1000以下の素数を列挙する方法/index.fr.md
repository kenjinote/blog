---
title: "Comment lister les nombres premiers inférieurs à 1000 en utilisant le Crible d'Ératosthène"
slug: "Comment lister les nombres premiers inférieurs à 1000 en utilisant le Crible d'Ératosthène"
date: 2023-04-09T12:54:24+09:00
tags: ["Crible d'Ératosthène", "Nombres premiers", "Mathématiques", "Rust"]
draft: false
math: true
image: "img.png"
categories: ["Mathématiques, Cryptographie, Quantique"]
---

## Qu'est-ce que le Crible d'Ératosthène ?

Le Crible d'Ératosthène est un algorithme utilisé pour trouver tous les nombres premiers jusqu'à une limite donnée.
L'algorithme est simple et peut être implémenté via les étapes suivantes :

1. Créer un tableau booléen de N éléments et initialiser tous les éléments à vrai (true).
2. Définir les 0ème et 1er éléments du tableau sur faux (false) (car 0 et 1 ne sont pas premiers).
3. Si le 2ème élément du tableau est vrai, afficher 2 comme nombre premier.
4. Définir tous les multiples de 2 supérieurs ou égaux à $2^2$ sur faux (*).
5. Si le 3ème élément du tableau est vrai, afficher 3 comme nombre premier.
6. Définir tous les multiples de 3 supérieurs ou égaux à $3^2$ sur faux.
7. Répéter le même processus pour les 4ème, 5ème, ..., et N-ième éléments.

* La raison pour laquelle on commence à marquer comme faux à partir du carré du nombre est que les nombres inférieurs au carré ont déjà été traités lors des étapes précédentes.

![](Animation_Sieb_des_Eratosthenes.gif)


## Implémentation en Rust

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

## Version légèrement optimisée

Nous pouvons optimiser légèrement l'implémentation en considérant les points suivants :

- Initialiser le tableau à faux (false) au lieu de vrai (true) (cela est plus rapide).
- Puisque les multiples de 2 ne sont pas des nombres premiers, ignorer l'étape visant à définir les multiples de 2 sur faux.
- Il n'est pas nécessaire de boucler jusqu'à n ; trouver les nombres premiers jusqu'à la racine carrée de n suffit pour trouver tous les nombres premiers inférieurs ou égaux à n.

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

## Référence
- [Crible d'Ératosthène (Wikipedia)](https://ja.wikipedia.org/wiki/%E3%82%A8%E3%83%A9%E3%83%88%E3%82%B9%E3%83%86%E3%83%8D%E3%82%B9%E3%81%AE%E7%AF%A9)

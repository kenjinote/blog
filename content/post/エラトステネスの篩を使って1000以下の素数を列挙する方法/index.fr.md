---
title: 'Qu''est-ce que le crible d''Ératosthène ? Algorithme et implémentation pour énumérer les nombres premiers jusqu''à 1000'
slug: "Crible d'Ératosthèneを使って1000以下のNombre premierを列挙する方法"
tags: ["Crible d'Ératosthène", "Nombres premiers", "Mathématiques", "Rust"]
draft: false
math: true
image: "img.webp"
categories: ["math-cryptography-quantum"]
description: "Énumérez les 168 nombres premiers jusqu’à 1000 en Rust : départ au carré, candidats impairs, bornes 0 et 1, complexité et limites mémoire."
date: 2023-04-09T12:54:24+09:00
lastmod: 2026-10-29
---

Le crible d’Ératosthène énumère tous les nombres premiers jusqu’à une borne supérieure `n`, incluse. Ces programmes Rust affichent les 168 nombres premiers inférieurs ou égaux à 1000. La borne est incluse ; 0 et 1 ne sont pas premiers.

## Étapes du crible et départ au carré

1. Allouez `n + 1` éléments booléens pour utiliser les indices de 0 à `n`. La version de base les initialise à vrai, puis marque 0 et 1 comme faux. Pour une borne inférieure à 2, elle renvoie un résultat vide avant d’accéder à l’indice 1.
2. Examinez les candidats `p` dans l’ordre croissant à partir de 2. Si la marque est encore vraie, `p` est premier : marquez ses multiples comme faux à partir de $p^2$, avec un pas de `p`. Ne marquez pas `p` lui-même.
3. L’élimination des multiples ne nécessite que les candidats vérifiant $p^2\le n$, car tout entier composé a un facteur premier inférieur ou égal à sa racine carrée.
4. Enfin, parcourez de 2 à `n` et affichez tous les nombres dont la marque reste vraie. L’intervalle de sortie ne se limite pas à la racine carrée.

Un multiple $kp$ inférieur à $p^2$, avec $2\le k<p$, a déjà été éliminé par un facteur premier de `k` inférieur à `p`. Cela ne signifie pas que tous les nombres plus petits ont déjà été énumérés.

![Animation du crible sur les nombres de 2 à 120](Animation_Sieb_des_Eratosthenes.gif)

Image : SKopp, version mise à jour par Suricata, [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Animation_Sieb_des_Eratosthenes.gif), [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Le fichier n’a pas été modifié. L’illustration couvre 2 à 120, tandis que les programmes ci-dessous utilisent la borne 1000.

## Implémentation de base en Rust

```rust
fn sieve(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![true; len];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut p = 2;
    while p <= n / p {
        if is_prime[p] {
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < p {
                    break;
                }
                multiple += p;
            }
        }
        p += 1;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve(1000) {
        println!("{}", prime);
    }
}
```

Enregistrez dans `sieve.rs` et compilez avec `rustc --edition=2021 sieve.rs -o sieve`. Sous Windows, utilisez `sieve.exe` comme nom d’exécutable. Le programme affiche 168 lignes : la première contient 2 et la dernière 997. Ces exemples ont été exécutés avec Rust 1.90.0.

`sieve(0)` et `sieve(1)` renvoient un vecteur vide ; `sieve(2)` renvoie `[2]`. La condition `p <= n / p` garantit que `p * p` n’est calculé que si le carré est dans la borne. La distance restante est vérifiée avant d’ajouter le multiple suivant. Aucune racine carrée en virgule flottante n’est nécessaire.

## Version qui élimine seulement les candidats impairs

Les entiers pairs supérieurs à 2 sont composés. On peut donc marquer 2 comme vrai et n’initialiser que les impairs comme candidats. Pour un nombre premier impair `p`, son carré est impair ; avancer à partir de ce carré avec un pas de $2p$ ne visite que les multiples impairs.

```rust
fn sieve_odd(n: usize) -> Vec<usize> {
    if n < 2 {
        return Vec::new();
    }
    let len = n.checked_add(1).expect("n + 1 is too large");
    let mut is_prime = vec![false; len];
    is_prime[2] = true;
    for i in (3..=n).step_by(2) {
        is_prime[i] = true;
    }

    let mut p = 3;
    while p <= n / p {
        if is_prime[p] {
            let step = 2 * p;
            let mut multiple = p * p;
            loop {
                is_prime[multiple] = false;
                if n - multiple < step {
                    break;
                }
                multiple += step;
            }
        }
        p += 2;
    }

    (2..=n).filter(|&i| is_prime[i]).collect()
}

fn main() {
    for prime in sieve_odd(1000) {
        println!("{}", prime);
    }
}
```

Enregistrez cette version dans un autre fichier et compilez-la. Elle affiche les mêmes 168 nombres premiers, renvoie un résultat vide pour 0 et 1, et `[2]` pour 2. Ne réunissez pas les deux fonctions `main` dans un même fichier.

Cette version évite une partie du travail sur les pairs. Initialiser à faux ne garantit toutefois pas une meilleure vitesse. Le temps dépend de l’initialisation, des écritures, des accès mémoire, du compilateur et de la machine. Aucune comparaison de temps mesurés n’est présentée ici. Le tableau conserve `n + 1` éléments afin que les indices correspondent directement aux nombres.

## Complexité et bornes utilisables

Dans le modèle RAM usuel, le crible prend un temps $O(n\log\log n)$ et un espace $O(n)$ pour les marques. Ce sont des évaluations asymptotiques des opérations et du stockage, ni des temps mesurés ni une complexité en bits pour des entiers en précision arbitraire. L’exercice du crible dans le [cours d’analyse de Princeton](https://introcs.cs.princeton.edu/java/41analysis/) donne aussi cette croissance.

En Rust, [`bool`](https://doc.rust-lang.org/reference/types/boolean.html) occupe un octet et [`Vec<T>`](https://doc.rust-lang.org/std/vec/struct.Vec.html#guarantees) stocke les éléments de façon contiguë. Ce `Vec<bool>` n’est pas un tableau de bits compactés. Le nombre logique de marques est `n + 1` ; les métadonnées du vecteur, la capacité allouée et le `Vec<usize>` renvoyé nécessitent également de la mémoire.

Si `n + 1` n’est pas représentable, `checked_add` renvoie `None`, puis `expect` déclenche un panic. Dans les autres cas, il faut encore disposer de suffisamment de mémoire ; cette implémentation ne traite pas de bornes arbitrairement grandes. Pour de grands intervalles, envisagez un crible segmenté. Énumérer des nombres premiers sur un intervalle répond à un autre besoin que tester un seul grand entier.

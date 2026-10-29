---
title: 'Comment créer un programme pour énumérer les nombres premiers en Rust et des exemples de code'
slug: "RustでNombre premierを列挙する"
tags: ["Rust","Nombres Premiers","Algorithme"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "Énumérez des nombres premiers en Rust par division d’essai : petites bornes, arrêt à la racine carrée, itération du vecteur et incréments bornés."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

Cet exemple Rust conserve les nombres premiers trouvés et les utilise pour la division d’essai. `primes_up_to(max)` renvoie la liste des nombres premiers jusqu’à la borne, incluse. Il y en a 168 inférieurs ou égaux à 1000 ; 0 et 1 ne sont pas premiers. Ce n’est pas une implémentation du crible.

## Code

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

## Exécution et petites bornes

Enregistrez dans `primes.rs` et compilez avec `rustc --edition=2021 primes.rs -o primes`. Sous Windows, utilisez `primes.exe` comme nom d’exécutable. Le programme affiche 168 lignes : la première contient 2 et la dernière 997. Ces exemples ont été exécutés avec Rust 1.90.0.

`primes_up_to(0)` et `primes_up_to(1)` renvoient un vecteur vide ; `primes_up_to(2)` renvoie `[2]`, `primes_up_to(3)` renvoie `[2, 3]` et `primes_up_to(10)` renvoie `[2, 3, 5, 7]`. Le type du paramètre, `usize`, exclut les bornes négatives. Ce programme n’analyse pas l’entrée standard.

## Fonctionnement du test et de la boucle

1. Renvoyez un résultat vide si la borne est inférieure à 2. Sinon, conservez 2 et ne testez que les candidats impairs de 3 jusqu’à la borne. La borne est contrôlée avant le traitement du candidat : la borne 2 n’ajoute donc pas 3.
2. Un candidat composé `n` possède un facteur premier inférieur ou égal à sa racine carrée. Ces nombres premiers sont déjà dans la liste grâce aux candidats précédents. Si une division donne un reste nul, rejetez le candidat. Si aucun diviseur n’a été trouvé quand `p > n / p`, poursuivre la division d’essai est inutile. La division entière positive exprime la condition de la racine carrée sans calculer `p * p` ni une racine en virgule flottante.
3. `for &p in &primes` emprunte la liste, reçoit des références successives et copie chaque valeur `usize` dans `p`. Un nouveau nombre premier n’est ajouté qu’après la fin de cette boucle. Le `for p in primes_up_to(1000)` final extrait les valeurs du vecteur renvoyé et les affiche. La [documentation de Vec en Rust](https://doc.rust-lang.org/std/vec/struct.Vec.html) distingue l’itération par emprunt de celle qui consomme le vecteur possédé.
4. À l’intérieur de `n <= max`, `max - n` ne peut pas être négatif. Si la distance restante est inférieure à 2, quittez avant l’addition ; sinon, exécutez `n += 2`. Cela évite une incrémentation au-delà de la borne.

## Domaine d’application

Le programme original à borne fixe 1000 affiche lui aussi correctement 168 nombres premiers. Toutefois, remplacer seulement la borne par 0, 1 ou 2 affiche des valeurs 2 ou 3 hors intervalle, car la borne n’est pas contrôlée avant le traitement. La fonction réutilisable proposée ici gère ces cas limites.

La liste conserve un `usize` par nombre premier découvert. Les métadonnées du vecteur et la capacité allouée nécessitent aussi de la mémoire. Une borne supérieure grossière du nombre de divisions est `O(max sqrt(max))`, en comptant une division comme une opération ; ce n’est ni un temps mesuré ni une complexité en bits. Des bornes plus grandes demandent plus de temps et de stockage, sans garantie d’énumérer rapidement des nombres premiers jusqu’à des limites arbitrairement grandes. Pour de grands intervalles, consultez l’[article sur le crible d’Ératosthène](https://kenji.blog/fr/p/crible-d%C3%A9ratosth%C3%A8ne%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEnombre-premier%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). Ce n’est pas un générateur de nombres premiers cryptographiques.

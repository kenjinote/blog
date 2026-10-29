---
title: 'Wie man ein Programm zur Aufzählung von Primzahlen in Rust erstellt und Codebeispiele'
slug: "RustでPrimzahlを列挙する"
tags: ["Rust","Primzahlen","Algorithmus"]
draft: false
image: "images/img.webp"
categories: ["programming"]
description: "Primzahlen in Rust mit bekannten Primteilern auflisten: kleine Grenzen, Quadratwurzelbedingung, Vektoriteration und begrenzte Erhöhung."
date: 2022-09-09T07:08:49+09:00
lastmod: 2026-10-29
---

Dieses Rust-Beispiel speichert gefundene Primzahlen und verwendet sie für die Probedivision. `primes_up_to(max)` liefert die Liste der Primzahlen bis zur Grenze einschließlich. Bis einschließlich 1000 gibt es 168 Primzahlen; 0 und 1 sind keine Primzahlen. Dies ist keine Siebimplementierung.

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

## Ausführung und kleine Grenzen

Speichern Sie als `primes.rs` und kompilieren Sie mit `rustc --edition=2021 primes.rs -o primes`. Verwenden Sie unter Windows `primes.exe` als Namen der ausführbaren Datei. Das Programm gibt 168 Zeilen aus, beginnend mit 2 und endend mit 997. Die Beispiele wurden mit Rust 1.90.0 ausgeführt.

`primes_up_to(0)` und `primes_up_to(1)` liefern einen leeren Vektor. `primes_up_to(2)` liefert `[2]`, `primes_up_to(3)` liefert `[2, 3]` und `primes_up_to(10)` liefert `[2, 3, 5, 7]`. Der Parametertyp `usize` schließt negative Grenzen aus. Das Programm liest keine Eingaben aus der Standardeingabe ein.

## Funktionsweise von Test und Schleife

1. Bei einer Grenze unter 2 wird ein leeres Ergebnis zurückgegeben. Andernfalls wird 2 gespeichert, und nur ungerade Kandidaten von 3 bis zur Grenze werden geprüft. Die Grenze wird vor der Verarbeitung eines Kandidaten geprüft; bei der Grenze 2 wird deshalb keine 3 hinzugefügt.
2. Ein zusammengesetzter Kandidat `n` hat einen Primfaktor, der höchstens seiner Quadratwurzel entspricht. Diese Primzahlen stehen durch die früheren Kandidaten bereits in der Liste. Geht eine Division ohne Rest auf, wird der Kandidat verworfen. Wurde kein Teiler gefunden, bevor `p > n / p` gilt, sind weitere Probedivisionen unnötig. Positive Ganzzahldivision beschreibt die Quadratwurzelbedingung, ohne `p * p` oder eine Gleitkommawurzel zu berechnen.
3. `for &p in &primes` leiht die Liste aus, erhält nacheinander Referenzen und kopiert jeden `usize`-Wert nach `p`. Erst nach dieser Schleife wird eine neue Primzahl hinzugefügt. Das abschließende `for p in primes_up_to(1000)` entnimmt dem zurückgegebenen Vektor seine Werte und gibt sie aus. Die [Rust-Dokumentation zu Vec](https://doc.rust-lang.org/std/vec/struct.Vec.html) unterscheidet ausgeliehene Iteration von der Iteration, die einen Vektor im eigenen Besitz verbraucht.
4. Innerhalb von `n <= max` kann `max - n` nicht negativ sein. Bei einem Restabstand unter 2 endet die Schleife vor der Addition; andernfalls wird `n += 2` ausgeführt. So überschreitet die Erhöhung nicht die Grenze.

## Einsatzbereich

Das ursprüngliche Programm mit der festen Grenze 1000 gibt ebenfalls korrekt 168 Primzahlen aus. Wird jedoch nur die Grenze auf 0, 1 oder 2 geändert, erscheinen die Werte 2 oder 3 außerhalb des Bereichs, weil die Grenze nicht vor der Verarbeitung geprüft wird. Die hier wiederverwendbare Funktion behandelt diese Randfälle.

Die Liste speichert einen `usize` pro gefundener Primzahl. Vektormetadaten und reservierte Kapazität benötigen ebenfalls Speicher. Als grobe obere Schranke für die Divisionen lässt sich `O(max sqrt(max))` angeben, wenn eine Division als eine Operation zählt; dies ist weder gemessene Laufzeit noch Bitkomplexität. Größere Grenzen verlangen mehr Zeit und Speicher, ohne Garantie einer schnellen Auflistung bis zu beliebig großen Grenzen. Für große Intervalle siehe den [Artikel zum Sieb des Eratosthenes](https://kenji.blog/de/p/sieb-des-eratosthenes%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A61000%E4%BB%A5%E4%B8%8B%E3%81%AEprimzahl%E3%82%92%E5%88%97%E6%8C%99%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95/). Dies ist kein kryptografischer Primzahlgenerator.

---
title: "Grundwissen über Computer"
slug: "コンピュータの基本知識"
date: 2024-09-19T01:10:20+09:00
tags: ["Computer", "Grundwissen"]
draft: false
image: "img.png"
categories: ["IT & Technologie"]
---

# Grundwissen über Computer

Auf dieser Seite wird erklärt, was ein Computer ist.

## Definition eines Computers
Ein Computer ist eine Maschine, die aus den folgenden 5 Einheiten besteht:

1. Eingabegerät
2. Ausgabegerät
3. Speichergerät
4. Steuerwerk
5. Rechenwerk

Kurz gesagt ist ein Computer eine Maschine, die eine bestimmte `Verarbeitung` für eine gegebene `Eingabe` durchführt und das Ergebnis `ausgibt`.
Er kann eingegebene Daten `speichern`, `Operationen` durchführen und `ausgeben`. Die `Steuerung` ist dafür zuständig, die oben genannten 4 Einheiten zu steuern.

## Was zum Betrieb eines Computers benötigt wird
Um einen Computer zu betreiben, werden neben den Geräten (Hardware) auch Programme (Software) benötigt.

In einem Programm geben wir dem Computer Anweisungen, welche Art von Verarbeitung durchgeführt werden soll. Programme sind in einem Format geschrieben, das der Computer verstehen kann.

Ein Beispiel für ein Programm ist unten dargestellt:
Ein Programm, das die Summe von 1 bis zu einer eingegebenen ganzen Zahl berechnet.
```
#include <iostream>
using namespace std;

int main() {
    // Zuweisung des benötigten Speicherplatzes
    int n, sum = 0;
    
    // Ausgabe
    cout << "Bitte geben Sie eine ganze Zahl ein: ";
    
    // Eingabe 
    cin >> n;
    
    // Operation
    for (int i = 1; i <= n; i++) { // Operation
        sum += i;
    }
    
    // Ausgabe
    cout << "Die Summe von 1 bis " << n << " ist " << sum << "." << endl;
    
    // Ende
    return 0;
}
```

Das Programm wird durch einen Compiler in Maschinencode umgewandelt und in ein Format konvertiert, das der Computer ausführen kann.

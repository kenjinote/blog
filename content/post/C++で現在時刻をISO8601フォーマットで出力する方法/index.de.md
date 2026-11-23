---
title: "[C++20] Aktuelle Zeit mit std::chrono und std::format als UTC im ISO-8601-Format ausgeben"
date: "2023-04-15T19:35:27+09:00"
lastmod: "2026-11-23"
slug: "C++で現在時刻をISO8601フォーマットで出力する方法"
tags: ["C++", "Datum und Uhrzeit", "ISO8601"]
draft: false
image: "img.webp"
categories: ["programming"]
description: "Ein vollständiges C++20-Beispiel zur Ausgabe der aktuellen UTC-Zeit im ISO-8601-Format mit std::chrono und std::format, einschließlich Hinweisen zur Bibliotheksunterstützung."
---

### Voraussetzungen

- ISO C++ 20 Standard (/std:c++20)

### Code

Das Beispiel gibt UTC mit Sekundengenauigkeit aus, etwa `2026-11-23T00:00:00Z`.

```cpp
#include <chrono>
#include <format>
#include <iostream>
#include <string>

int main() {
    const auto now = std::chrono::floor<std::chrono::seconds>(
        std::chrono::system_clock::now());
    const std::string datetime = std::format("{:%FT%TZ}", now);
    std::cout << datetime << '\n';
}
```

> `%F` formatiert das Datum und `%T` die Uhrzeit. `T` und `Z` im Formatstring sind literale Zeichen; der `system_clock`-Zeitpunkt wird als UTC formatiert. Bei einer Zeitauflösung unter einer Sekunde können Nachkommastellen erscheinen. Die Chrono-Formatierung gehört zur C++20-Bibliothek, wird aber nicht von jeder Standardbibliothek gleich unterstützt. Prüfen Sie Compiler und Bibliothek.

### Referenzen

- [C++ standard draft: chrono formatting](https://eel.is/c++draft/time.format)
- [Microsoft C++ language conformance and feature support](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170)

---
title: "Über die Pflichtfeld-Markierung in Eingabeformularen"
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["Eingabeformular", "Webentwicklung", "UX"]
draft: false
image: "img.png"
categories: ["Blog-Betrieb"]
---

Wir haben Informationen über die "Pflicht"-Markierung in Benutzeroberflächen (Formularen) im Ausland zusammen mit UI-Richtlinienmaterialien zusammengefasst.

---

## 📌 Wichtige Pflichtmarkierungen und Best Practices

1. **Verwendung des Sternchens (\*)**

    * Es ist am weitesten verbreitet; Pflichtfelder werden mit einem "\*" versehen.
    * Jedoch ist **eine Erklärung wie " * ist ein Pflichtfeld" am Anfang des Formulars erforderlich** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * Es gibt auch Beispiele, die Farbe zur Hervorhebung verwenden (wie roten Text).

2. **"Required" oder "(required)" im Label angeben**

    * Durch das Hinzufügen des Wortes "Required" in das Label kann es Screenreadern klar angezeigt werden, was die Barrierefreiheit verbessert ([Deque][3]).

3. **Kombinierte Verwendung von ARIA-Attributen und dem HTML5-Attribut `required`**

    * Neben der visuellen Anzeige wird durch die Verwendung von `aria-required="true"` und `<input required>` auch programmatisch mitgeteilt, dass das Feld erforderlich ist ([Deque][3]).

4. **Verwendung von "(optional)" zur Kennzeichnung optionaler Felder**

    * Es gibt auch den Ansatz, optionale Felder explizit mit "(optional)" zu kennzeichnen, anstatt Pflichtfelder zu markieren, was effektiv ist, wenn beide gemischt auftreten.
    * Nielsen-Norman weist jedoch darauf hin, dass es "leichter zu beurteilen ist, wenn auch Pflichtfelder klar ausgewiesen werden" ([TPGi][4]).

---

## ✅ Zusammenfassung der UI-Richtlinienmaterialien

| Quelle                                        | Inhalt                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | Die Kombination von Sternchen und Erklärungstext wird empfohlen; nur optionale Felder anzuzeigen gilt als unfreundlich ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)**    | ・Die Zeichenfolge "Required" oder ein Bild wird im Label verwendet.<br>・Es wird deutlich gemacht, dass Hinweise allein durch Farben unzureichend sind. |
| **W3C Techniques (H90)**                   | Es gibt Beispiele für die Einbindung eines Sternchens oder "(required)" im Label und die Definition der Bedeutung am Anfang des Formulars. |
| **TPGi (Doing what's required)**           | Unter Berücksichtigung der Barrierefreiheit wird die Kombination aus Sternchen + ARIA-Attributen + Labeltext als am besten bewertet. |
| **Contensis Formular-UX-Leitfaden**        | Prägnant zusammengefasst: Eine konsistente Markierung (\* oder (optional)) ist wichtig. |

---

## ✅ Empfohlene Ansätze für die Implementierung

* Fügen Sie einen Erklärungstext am **Anfang des Formulars** hinzu:

  > Fields marked with \* are required.
  > (Oder "All fields are required" für alle, oder "unless marked optional", wenn es optionale gibt)

* **Labelzuweisung** :

    * Geschrieben als `First Name *` oder `Email (required)`.

* **ARIA-Attribute und HTML5-Attribute** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Verlassen Sie sich nicht nur auf Farben** : Bieten Sie sowohl visuelle als auch programmatische Unterstützung.

---

## 🔗 Referenzlinks (UI-Richtlinienmaterialien)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

Bei Bedarf kann ich auch spezifische HTML/CSS-Codebeispiele oder UI-Komponenten-Designvorlagen für Sketch und Figma bereitstellen. Zögern Sie nicht zu fragen!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"

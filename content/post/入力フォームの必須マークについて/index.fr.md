---
title: "À propos des Marques Obligatoires dans les Formulaires de Saisie"
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["Formulaire", "Développement Web", "UX"]
draft: false
image: "img.png"
categories: ["Gestion du Blog"]
---

Nous avons résumé les informations concernant la marque "obligatoire" sur les interfaces utilisateur (formulaires) à l'étranger, accompagnées de documents de directives UI.

---

## 📌 Principales Marques Obligatoires et Meilleures Pratiques

1. **Utilisation de l'Astérisque (\*)**

    * C'est généralement la méthode la plus répandue ; on ajoute "\*" aux champs obligatoires.
    * Cependant, **une explication telle que " * indique un champ obligatoire" au début du formulaire est indispensable** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * Il y a aussi des exemples utilisant la couleur pour souligner (comme du texte en rouge).

2. **Indiquer "Required" ou "(required)" dans l'étiquette**

    * En ajoutant le texte "Required" dans l'étiquette, on peut l'indiquer clairement aux lecteurs d'écran, ce qui améliore l'accessibilité ([Deque][3]).

3. **Utilisation combinée des attributs ARIA et de l'attribut HTML5 `required`**

    * En plus de l'affichage visuel, l'utilisation de `aria-required="true"` et `<input required>` permet d'indiquer l'obligation de manière programmatique ([Deque][3]).

4. **Utiliser "(optional)" pour indiquer les champs facultatifs**

    * Il y a aussi la méthode qui consiste à marquer explicitement les champs facultatifs par "(optional)" au lieu de marquer les obligatoires, ce qui est efficace lorsqu'il y a un mélange.
    * Toutefois, Nielsen-Norman souligne qu'il "est plus facile de juger si les champs obligatoires sont également spécifiés" ([TPGi][4]).

---

## ✅ Résumé des Documents de Directives UI

| Source                                        | Contenu                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | La combinaison de l'astérisque et du texte d'explication est recommandée ; afficher uniquement les champs facultatifs est considéré comme peu convivial ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)**    | ・Utilise la chaîne "Required" ou une image au sein de l'étiquette.<br>・Il est clairement stipulé que l'indication par la couleur seule est insuffisante. |
| **W3C Techniques (H90)**                   | Il y a des exemples d'inclusion d'un astérisque ou de "(required)" dans l'étiquette et de la définition de sa signification au début du formulaire. |
| **TPGi (Doing what's required)**           | Compte tenu de l'accessibilité, la combinaison astérisque + attributs ARIA + texte dans l'étiquette est évaluée comme optimale. |
| **Guide UX des Formulaires Contensis**     | Organisé de manière concise : un marquage cohérent (\* ou (optional)) est important. |

---

## ✅ Approches Recommandées pour l'Implémentation

* Ajouter un texte d'explication au **début du formulaire** :

  > Fields marked with \* are required.
  > (Ou "All fields are required" pour tous, ou "unless marked optional" s'il y a des champs facultatifs)

* **Attribution d'Étiquette** :

    * Écrit comme `First Name *` ou `Email (required)`.

* **Attributs ARIA et Attributs HTML5** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Ne vous fiez pas uniquement à la couleur** : Assurez une compatibilité à la fois visuelle et programmatique.

---

## 🔗 Liens de Référence (Documents de Directives UI)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

Si nécessaire, je peux également fournir des exemples spécifiques de code HTML/CSS, ou des modèles de conception de composants UI pour Sketch et Figma. N'hésitez pas à demander !

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"

---





title: "Sobre la marca obligatoria en los formularios de entrada"
date: 2025-07-14T13:47:51+09:00
tags: ["Formularios", "Desarrollo Web", "UX"]
draft: false
image: "img.png"
categories: ["Gestión del blog"]
---






He organizado la información sobre la marca "obligatorio" en las interfaces de usuario (formularios) extranjeras, junto con los documentos de directrices de UI.

---

## 📌 Principales marcas obligatorias y mejores prácticas

1. **Uso del asterisco (\*)**

    * Es el más extendido en general, y se añade un "\*" a los campos obligatorios.
    * Sin embargo, es **obligatorio incluir una explicación al principio del formulario, como "\* indica un campo obligatorio"** ([Nielsen Norman Group][1], [Universidad Estatal de California, Northridge][2]).
    * También hay ejemplos de enfatizarlo usando colores (texto rojo, etc.).

2. **Especificar "Required" o "(required)" en la etiqueta**

    * Al añadir la palabra "Required" en la etiqueta, se puede indicar claramente a los lectores de pantalla, mejorando la accesibilidad ([Deque][3]).

3. **Uso combinado de atributos ARIA y el atributo `required` de HTML5**

    * Además de la visualización, se puede transmitir de forma programática que es obligatorio mediante `aria-required="true"` o `<input required>` ([Deque][3]).

4. **Especificar campos opcionales usando "(optional)"**

    * También hay una manera de especificar los campos opcionales como "(optional)" en lugar de los campos obligatorios, lo cual es efectivo cuando hay una mezcla de ambos.
    * Sin embargo, Nielsen-Norman señala que "es más fácil juzgar si también se indica lo obligatorio" ([TPGi][4]).

---

## ✅ Resumen de documentos de directrices de UI

| Proveedor                                        | Contenido                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **NN/g: Marking Required Fields in Forms** | Se recomienda la combinación de asterisco + texto explicativo, y mostrar solo lo opcional se considera poco amigable ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)**    | ・Se usa la palabra "Required" o una imagen dentro de la etiqueta.<br>・Se afirma que la sugerencia solo por color es insuficiente.                   |
| **W3C Techniques (H90)**                   | Hay ejemplos que incluyen un asterisco o "(required)" en la etiqueta, y definen su significado al principio del formulario.                      |
| **TPGi (Doing what's required)**           | Considerando la accesibilidad, la combinación óptima es asterisco + atributo ARIA + inserción de texto en la etiqueta.                          |
| **Guía de UX de Formularios Contensis**                    | Un marcado consistente (\* o (optional)) se resume brevemente como importante.                             |

---

## ✅ Enfoques recomendados para la implementación

* Agregar texto explicativo **al principio del formulario**:

  > Fields marked with \* are required.
  > (o "All fields are required" en general, "unless marked optional" si hay opcionales)

* **Asignación de etiquetas**:

    * Se escribe como `First Name *` o `Email (required)`.

* **Atributos ARIA y HTML5**:

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **No dependa solo del color**: Responda tanto de forma visual como programática.

---

## 🔗 Enlaces de referencia (Documentos de directrices de UI)

* NN/g: *Marking Required Fields in Forms* ([Universidad Estatal de California, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

Si es necesario, también podemos proporcionar ejemplos específicos de código HTML/CSS, o plantillas de diseño de componentes de UI para Sketch o Figma. ¡No dude en consultarnos!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"

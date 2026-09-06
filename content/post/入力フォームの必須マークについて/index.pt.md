---
title: "Sobre a Marca de Obrigatório em Formulários de Entrada"
slug: "入力フォームの必須マークについて"
date: 2025-07-14T13:47:51+09:00
tags: ["Formulário", "Desenvolvimento Web", "UX"]
draft: false
image: "img.png"
categories: ["Operação do Blog"]
---

Organizamos informações sobre a marca de "obrigatório" na interface do usuário (formulários) no exterior, juntamente com materiais de diretrizes de UI.

---

## 📌 Principais Marcas de Obrigatório e Melhores Práticas

1. **Uso do Asterisco (\*)**

    * Geralmente o mais difundido, adiciona-se "\*" aos campos obrigatórios.
    * No entanto, **uma explicação como " * é um campo obrigatório" no início do formulário é obrigatória** ([Nielsen Norman Group][1], [California State University, Northridge][2]).
    * Também existem exemplos que usam cor para dar ênfase (como texto em vermelho).

2. **Especificar "Required" ou "(required)" no rótulo**

    * Ao incluir a palavra "Required" no rótulo, pode-se indicá-lo claramente para leitores de tela, melhorando a acessibilidade ([Deque][3]).

3. **Uso combinado de atributos ARIA e do atributo `required` do HTML5**

    * Além da exibição visual, usando `aria-required="true"` e `<input required>`, o campo também é comunicado como obrigatório de forma programática ([Deque][3]).

4. **Especificar campos opcionais usando "(optional)"**

    * Há também a abordagem de especificar os campos opcionais como "(optional)" em vez dos campos obrigatórios, o que é eficaz quando ambos estão misturados.
    * No entanto, a Nielsen-Norman aponta que "é mais fácil de avaliar se os campos obrigatórios também forem especificados de forma clara" ([TPGi][4]).

---

## ✅ Resumo de Materiais de Diretrizes de UI

| Fonte | Conteúdo |
| --- | --- |
| **NN/g: Marking Required Fields in Forms** | A combinação de um asterisco com um texto explicativo é recomendada; exibir apenas os opcionais é considerado pouco amigável ([Nielsen Norman Group][1]). |
| **Deque (Anatomy of Accessible Forms)** | ・A palavra "Required" ou uma imagem é usada em combinação dentro do rótulo.<br>・Afirma claramente que a indicação apenas com cores é insuficiente. |
| **W3C Techniques (H90)** | Há exemplos de inclusão de um asterisco ou "(required)" no rótulo e definição do seu significado no início do formulário. |
| **TPGi (Doing what's required)** | Considerando a acessibilidade, a combinação de asterisco + atributos ARIA + inserção de texto no rótulo é avaliada como a melhor. |
| **Guia de UX de Formulários Contensis** | Organizado de forma concisa: uma marcação consistente (\* ou (optional)) é importante. |

---

## ✅ Abordagens Recomendadas para Implementação

* Adicionar um texto explicativo no **início do formulário** :

  > Fields marked with \* are required.
  > (Ou "All fields are required" para todos de uma vez, ou "unless marked optional" se houver campos opcionais)

* **Atribuição de Rótulo** :

    * Escrito como `First Name *` ou `Email (required)`.

* **Atributos ARIA e Atributos HTML5** :

  ```html
  <label for="email">Email <abbr title="required">*</abbr></label>
  <input id="email" required aria-required="true">
  ```

* **Não confie apenas na cor** : Suporte tanto visual quanto programaticamente.

---

## 🔗 Links de Referência (Materiais de Diretrizes de UI)

* NN/g: *Marking Required Fields in Forms* ([California State University, Northridge][2], [Nielsen Norman Group][1], [Deque][3])
* Deque: *Anatomy of Accessible Forms* ([Deque][3])
* W3C Techniques: *H90 Indicating required form controls* ([W3C][5])
* TPGi: *Indicating mandatory fields accessibly* ([TPGi][4])
* Contensis: *UX Forms Guidelines* ([Contensis][6])

---

Se necessário, também posso fornecer exemplos específicos de código HTML/CSS, ou templates de design de componentes de UI para Sketch e Figma. Sinta-se à vontade para perguntar!

[1]: https://www.nngroup.com/articles/required-fields/?utm_source=chatgpt.com "Marking Required Fields in Forms - NN/g"
[2]: https://www.csun.edu/universal-design-center/web-accessibility-criteria-required-fields?utm_source=chatgpt.com "Web Accessibility Criteria - Required Fields - CSUN"
[3]: https://www.deque.com/blog/anatomy-of-accessible-forms-required-form-fields/?utm_source=chatgpt.com "The Anatomy of Accessible Forms: Required Form Fields"
[4]: https://www.tpgi.com/doing-whats-required-indicating-mandatory-fields-in-an-accessible-way/?utm_source=chatgpt.com "Doing what's required: Indicating mandatory fields in an accessible ..."
[5]: https://www.w3.org/TR/WCAG20-TECHS/H90.html?utm_source=chatgpt.com "H90: Indicating required form controls using label or legend - W3C"
[6]: https://www.contensis.com/community/blog/ux-forms-guidelines?utm_source=chatgpt.com "Build better web forms: 15 UX guidelines that work - Contensis"

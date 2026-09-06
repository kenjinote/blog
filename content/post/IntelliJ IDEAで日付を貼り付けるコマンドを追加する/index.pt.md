---
title: "Adicionar comando para inserir data no IntelliJ IDEA"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# Introdução
Ao escrever este blog, uso o IntelliJ IDEA. É conveniente porque tem boa compatibilidade com o Git e exibe uma pré-visualização de Markdown.
Toda vez que escrevo um blog, tenho que escrever `date` no cabeçalho do arquivo md. Parece que não há atalho para inserir a data, então criei um comando para inserir a data referenciando o site abaixo. Espero que seja útil.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Procedimento de configuração
1. Abra "File" > "Settings..." no menu  
   ![settings](./images/settings.png)
2. Com "Editor" > "Live Template" > "HTML/XML" selecionado, clique em "+"
3. Selecione Live Template
4. Insira "date" em Abbreviation
5. Insira "Inserir data e hora" em Description
6. Insira "$date$" em Template Text
7. Clique no botão Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Insira "date" em Name
9. Insira ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` em Expression
10. Feche a caixa de diálogo com OK
11. Pressione Define ou Change e marque "Everywhere"
12. Feche a caixa de diálogo com OK
13. Digite "date" no editor de código e pressione Enter. Quando a data "2022-09-04T05:59:04+09:00" for inserida, a configuração estará concluída!

Isso é tudo

# Conclusão
Se eu encontrar pequenos truques para o IntelliJ IDEA, gostaria de publicá-los novamente!

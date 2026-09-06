---
title: "Ajouter une commande pour insérer la date dans IntelliJ IDEA"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# Introduction
J'utilise IntelliJ IDEA lorsque j'écris ce blog. C'est pratique car sa compatibilité avec Git est bonne et il affiche un aperçu Markdown.
À chaque fois que j'écris un blog, je dois écrire `date` dans l'en-tête du fichier md. Comme il ne semble pas y avoir de raccourci pour insérer la date, j'ai créé une commande pour l'insérer en me référant au site ci-dessous. J'espère que cela vous sera utile.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Procédure de configuration
1. Ouvrez "File" > "Settings..." dans le menu  
   ![settings](./images/settings.png)
2. Avec "Editor" > "Live Template" > "HTML/XML" sélectionné, cliquez sur "+"
3. Sélectionnez Live Template
4. Entrez "date" dans Abbreviation
5. Entrez "Insérer la date et l'heure" dans Description
6. Entrez "$date$" dans Template Text
7. Cliquez sur le bouton Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Entrez "date" dans Name
9. Entrez ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` dans Expression
10. Fermez la boîte de dialogue avec OK
11. Appuyez sur Define ou Change et cochez "Everywhere"
12. Fermez la boîte de dialogue avec OK
13. Tapez "date" dans l'éditeur de code et appuyez sur Entrée. Lorsque la date "2022-09-04T05:59:04+09:00" est insérée, la configuration est terminée !

C'est tout

# Conclusion
Si je trouve d'autres petites astuces pour IntelliJ IDEA, j'aimerais les publier à nouveau !

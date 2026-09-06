---
title: "Befehl zum Einfügen des Datums in IntelliJ IDEA hinzufügen"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# Einführung
Wenn ich diesen Blog schreibe, verwende ich IntelliJ IDEA. Es ist praktisch, da es gut mit Git harmoniert und eine Markdown-Vorschau anzeigt.
Da ich jedes Mal, wenn ich einen Blog schreibe, das `date` in den md-Header schreiben muss, und es anscheinend keine Tastenkombination zum Einfügen des Datums gibt, habe ich unter Bezugnahme auf die unten stehende Website einen Befehl zum Einfügen des Datums erstellt. Ich hoffe, das ist hilfreich.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Einrichtungsschritte
1. Öffnen Sie "File" > "Settings..." im Menü  
   ![settings](./images/settings.png)
2. Klicken Sie auf "+", während "Editor" > "Live Template" > "HTML/XML" ausgewählt ist
3. Wählen Sie Live Template aus
4. Geben Sie "date" bei Abbreviation ein
5. Geben Sie "Datum und Uhrzeit einfügen" bei Description ein
6. Geben Sie "$date$" bei Template Text ein
7. Klicken Sie auf die Schaltfläche Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Geben Sie "date" bei Name ein
9. Geben Sie ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` bei Expression ein
10. Schließen Sie den Dialog mit OK
11. Drücken Sie auf Define oder Change und aktivieren Sie "Everywhere"
12. Schließen Sie den Dialog mit OK
13. Geben Sie "date" im Code-Editor ein und drücken Sie die Eingabetaste. Wenn das Datum "2022-09-04T05:59:04+09:00" eingefügt wird, ist die Einrichtung abgeschlossen!

Das war's

# Fazit
Wenn ich weitere kleine Tricks für IntelliJ IDEA finde, werde ich sie gerne wieder veröffentlichen!

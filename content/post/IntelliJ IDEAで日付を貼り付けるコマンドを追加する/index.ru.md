---
title: "Добавление команды для вставки даты в IntelliJ IDEA"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# Введение
При написании этого блога я использую IntelliJ IDEA. Это удобно, потому что он хорошо совместим с Git и отображает предварительный просмотр Markdown.
Каждый раз, когда я пишу в блог, мне приходится указывать дату в заголовке файла md. Похоже, для этого нет встроенного сочетания клавиш, поэтому я создал команду для вставки даты, опираясь на следующий сайт. Надеюсь, это будет полезно.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Процедура настройки
1. Откройте в меню "File" > "Settings..."  
   ![settings](./images/settings.png)
2. Выберите "Editor" > "Live Template" > "HTML/XML" и нажмите кнопку "+"
3. Выберите Live Template
4. Введите "date" в поле Abbreviation
5. Введите "Вставить дату и время" в поле Description
6. Введите "$date$" в поле Template Text
7. Нажмите кнопку Edit Variables  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Введите "date" в поле Name
9. Введите ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` в поле Expression
10. Нажмите OK, чтобы закрыть диалоговое окно
11. Нажмите Define или Change и отметьте галочкой "Everywhere"
12. Нажмите OK, чтобы закрыть диалоговое окно
13. В редакторе кода введите "date" и нажмите Enter. Если вставится дата "2022-09-04T05:59:04+09:00", настройка завершена!

На этом всё.

# Заключение
Если я найду другие небольшие хитрости для IntelliJ IDEA, я обязательно поделюсь ими снова!

---
title: 'Adding a command to insert a date in IntelliJ IDEA'
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT & Technology"]
---
# Introduction
I use IntelliJ IDEA when writing this blog. It works well with Git and is convenient because it shows markdown previews.
Since I have to write the date in the md header every time I write a blog post, and there doesn't seem to be a shortcut for inserting dates, I tried creating a command to insert the date, using the following site as a reference. I hope this helps.

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# Setup Procedure
1. Open "File" > "Settings..." from the menu  
   ![settings](./images/settings.png)
2. Select "Editor" > "Live Template" > "HTML/XML" and click "+"
3. Select Live Template
4. Enter "date" in Abbreviation
5. Enter "Insert date and time" in Description
6. Enter "$date$" in Template Text
7. Click Edit Variables button  
   ![edit_template_variables](./images/edit_template_variables.png)
8. Enter "date" in Name
9. Enter ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")`` in Expression
10. Click OK to close the dialog
11. Click Define or Change and check "Everywhere"
12. Click OK to close the dialog
13. Type "date" in the code editor and press Enter. If the date "2022-09-04T05:59:04+09:00" is inserted, the setup is complete!

That's all.

# Conclusion
I will continue to share more IntelliJ IDEA tips if I find them!

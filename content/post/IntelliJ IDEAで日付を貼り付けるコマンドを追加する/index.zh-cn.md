---
title: '在IntelliJ IDEA中添加插入日期的命令'
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・科技"]
---
# 简介
我写这个博客的时候，使用的是IntelliJ IDEA。它和Git的兼容性很好，而且能显示Markdown的预览，非常方便。
每次写博客时都必须在md的头部写入date，但似乎没有插入日期的快捷键，因此我参考了以下网站，
制作了插入日期的命令。希望能对您有所帮助。

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# 设置步骤
1. 打开菜单的“File”>“Settings...”  
   ![settings](./images/settings.png)
2. 在选择“Editor”>“Live Template”>“HTML/XML”的状态下点击“+”
3. 选择Live Template
4. 在Abbreviation中输入“date”
5. 在Description中输入“插入日期时间”
6. 在Template Text中输入“$date$”
7. 点击Edit Variables按钮  
   ![edit_template_variables](./images/edit_template_variables.png)
8. 在Name中输入“date”
9. 在Expression中输入``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")``
10. 点击OK关闭对话框
11. 点击Define或Change并勾选“Everywhere”
12. 点击OK关闭对话框
13. 在代码编辑器中输入“date”并按Enter，如果插入了“2022-09-04T05:59:04+09:00”这样的日期，设置就完成了！

以上

# 结语
如果发现了IntelliJ IDEA的小技巧，我还会继续分享的！

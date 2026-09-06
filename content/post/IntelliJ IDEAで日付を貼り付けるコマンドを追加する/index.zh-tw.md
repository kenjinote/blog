---
title: "在 IntelliJ IDEA 中新增插入日期的指令"
slug: "IntelliJ IDEAで日付を貼り付けるコマンドを追加する"
date: 2022-09-04T05:59:04+09:00
tags: ["IntelliJ IDEA"]
draft: false
image: "images/IntelliJ_logo.png"
categories: ["IT・テクノロジー"]
---
# 前言
寫這個部落格時，我使用的是 IntelliJ IDEA。它不僅與 Git 的相容性很好，還能顯示 Markdown 的預覽，非常方便。
每次寫部落格時，都必須在 md 檔案的標頭中寫入 date，但似乎沒有插入日期的快捷鍵，因此我參考了下方的網站，建立了一個用來插入日期的指令。希望能對大家有所幫助。

[Is there a shortcut for inserting date/time in IntelliJ IDEA?](https://stackoverflow.com/questions/8714779/is-there-a-shortcut-for-inserting-date-time-in-intellij-idea)

# 設定步驟
1. 開啟選單中的「File」>「Settings...」  
   ![settings](./images/settings.png)
2. 在選取「Editor」>「Live Template」>「HTML/XML」的狀態下，點擊「+」
3. 選擇 Live Template
4. 在 Abbreviation 中輸入「date」
5. 在 Description 中輸入「插入日期和時間」
6. 在 Template Text 中輸入「$date$」
7. 點擊 Edit Variables 按鈕  
   ![edit_template_variables](./images/edit_template_variables.png)
8. 在 Name 中輸入「date」
9. 在 Expression 中輸入 ``date("yyyy-MM-dd'T'HH:mm:ss'+09:00'")``
10. 點擊 OK 關閉對話方塊
11. 按下 Define 或 Change 並勾選「Everywhere」
12. 點擊 OK 關閉對話方塊
13. 在程式碼編輯器中輸入「date」並按下 Enter，若成功插入日期「2022-09-04T05:59:04+09:00」，即代表設定完成！

以上

# 結語
如果再發現 IntelliJ IDEA 的小技巧，我會再繼續發布分享！

---
title: '【免費下載】支援國定假日自動顯示的Excel日曆範本'
slug: "Excelの日曆範本（休日対応版）"
date: 2024-05-01T00:15:57+09:00
lastmod: 2026-11-23
tags: ["Excel", "日曆", "範本", "假日"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '免費提供只要輸入年份與月份，即可自動顯示該月份日本國定假日的實用Excel日曆範本。歡迎下載使用，以提升您的行程管理與工作效率。'
---

## 我製作了Excel的日曆範本（支援假日版）！

我製作了一個Excel範本，只要輸入年份和月份，就會顯示該月份日曆上的假日。

歡迎下載使用。
[日曆.xlsx](/downloads/excel-japan-holidays-calendar.xlsx)

## 相容性與資料來源

變更年份時，此範本會透過 Excel 的 `WEBSERVICE` 函數，從第三方 ExcelAPI 服務取得日本國定假日。使用時需要網際網路連線，資料查詢與更新也取決於該服務是否正常運作。Microsoft 說明指出，此函數依賴 Windows 功能，因此在 Excel for Mac 中不會傳回結果。請參閱 Microsoft 的 [WEBSERVICE 函數說明](https://support.microsoft.com/en-us/excel/functions/webservice-function)及[假日清單 API 文件](https://excelapi.org/en/docs/datetime/holiday-list/)。

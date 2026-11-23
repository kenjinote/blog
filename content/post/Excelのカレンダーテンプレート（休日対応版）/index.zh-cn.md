---
title: '【免费下载】支持节假日自动显示的Excel日历模板'
slug: "Excelの日历模板（休日対応版）"
date: 2024-05-01T00:15:57+09:00
lastmod: 2026-11-23
tags: ["Excel", "日历", "模板", "节假日"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: '我们免费提供一款实用的Excel日历模板，只需输入年份和月份，即可自动显示当月日本的节假日。请务必下载使用，以提高日程管理和工作效率。'
---

## 制作了Excel日历模板（支持节假日版）！

我制作了一个Excel模板，输入年份和月份后，即可显示该月日历上的节假日。

请下载使用。
[日历.xlsx](/downloads/excel-japan-holidays-calendar.xlsx)

## 兼容性与数据来源

更改年份时，此模板会通过 Excel 的 `WEBSERVICE` 函数从第三方 ExcelAPI 服务获取日本节假日。使用时需要联网，能否获取数据及数据更新取决于该服务是否可用。Microsoft 说明此函数依赖 Windows 功能，因此在 Excel for Mac 中不会返回结果。请参阅 Microsoft 的 [WEBSERVICE 函数说明](https://support.microsoft.com/en-us/excel/functions/webservice-function)和[节假日列表 API 文档](https://excelapi.org/en/docs/datetime/holiday-list/)。

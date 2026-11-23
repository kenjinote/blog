---
title: '[Free Download] Excel Calendar Template with Automatic Holiday Display'
slug: "ExcelのCalendarTemplate（休日対応版）"
date: 2024-05-01T00:15:57+09:00
lastmod: 2026-11-23
tags: ["Excel", "Calendar", "Template", "Holidays"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: 'We distribute for free a convenient Excel calendar template that automatically reflects Japanese holidays for that month simply by entering the year and month. Please download and use it for schedule management and business efficiency.'
---

## I created an Excel calendar template (with holiday support)!

I made an Excel template that automatically displays the holidays for a given month when you enter the year and month.

Please download and use it.
[Calendar.xlsx](カレンダー.xlsx)

## Compatibility and data source

This template retrieves Japanese holidays from the third-party ExcelAPI service with Excel’s `WEBSERVICE` function when you change the year. It needs an internet connection, and retrieval and updates depend on that service being available. Microsoft states that this function relies on Windows features and does not return results in Excel for Mac. See Microsoft’s [WEBSERVICE function documentation](https://support.microsoft.com/en-us/excel/functions/webservice-function) and the [holiday-list API documentation](https://excelapi.org/en/docs/datetime/holiday-list/).

---
title: '簡單解說使用 paint.net 為圖片特定區域打馬賽克的方法'
slug: "paint.netで圖片の特定個所にモザイクをかける方法"
tags: ["paint.net", "馬賽克", "影像編輯", "隱私"]
draft: false
image: "img.webp"
categories: ["ai-technology"]
description: "說明如何在paint.net選取範圍套用Pixelate效果，並調整Cell Size與縮放方式。馬賽克無法保證安全遮蔽資訊，文中也介紹較安全的處理方式。"
date: "2023-04-11T16:33:10+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---


我將介紹如何使用 paint.net 在圖片的特定區域加上馬賽克。

在將圖片上傳到網路上時，有時候會想要在圖片的特定區域加上馬賽克。使用 paint.net，您可以快速地處理圖片。

## 步驟

#### 1. 使用 paint.net 開啟您想要進行馬賽克處理的圖片
#### 2. 使用選取工具，選擇您想要加上馬賽克的部分（可複選）

![img_2.png](img_2.webp)

#### 3. 選擇選單＞效果＞扭曲＞馬賽克

![img_1.png](img_1.webp)

- Cell Size 控制放大後像素的大小。數值越大，方塊越大；但這不代表資訊已安全隱藏。
- 若要呈現方形像素區塊，請將[Scale Down]設為`Multisample Bilinear`，將[Scale Up]設為`Nearest Neighbor`。

點擊 `OK` 關閉對話框。

#### 4. 圖片將會被加上馬賽克，接著請儲存圖片。

![img.png](img.webp)

## 隱私注意

若必須可靠地隱藏個人資料等資訊，不要只依賴馬賽克或模糊效果。請用不透明的純色完全遮住，再匯出成不含圖層或編輯紀錄的PNG或JPEG，並檢查匯出的檔案。可編輯原檔請另行安全保存。

以上。

## 參考資料

- [paint.net: Pixelate effect](https://paint.net/doc/latest/EffectsDistortMenu.html)
- [paint.net: Roadmap and change log](https://paint.net/roadmap.html)
- [UK Information Commissioner’s Office: Securely disclosing documents](https://ico.org.uk/media2/pbwchh24/disclosing-documents-to-the-public-securely-all-1-0-0.pdf)

---
title: "WinGet का उपयोग करके कमांड लाइन से ऐप इंस्टॉल करें"
slug: "WinGet を使ってコマンドでアプリをインストールする"
date: 2022-10-05T12:15:20+09:00
tags: ["WinGet"]
draft: false
image: "img.png"
categories: ["उपकरण और विकास पर्यावरण"]
---
## पूर्वापेक्षाएँ
Windows 11 होना चाहिए

## प्रक्रिया
1. Microsoft Store से `ऐप इंस्टॉलर` इंस्टॉल करें
   https://www.microsoft.com/store/productId/9NBLGGH4NNS1
2. कमांड प्रॉम्प्ट में ऐप इंस्टॉल करें
    ```powershell
    winget install Google.Chrome
    ```
## मुख्य ऐप्स जिन्हें इंस्टॉल किया जा सकता है
- Google Chrome (कमांड `winget install Google.Chrome`)
- Microsoft Edge (कमांड `winget install Microsoft.Edge`)
- Microsoft Teams (कमांड `winget install Microsoft.Teams`)
- Microsoft Office (कमांड `winget install Microsoft.Office`)
- Visual Studio Code (कमांड `winget install vscode`)
- Slack (कमांड `winget install SlackTechnologies.Slack`)
- Discord (कमांड `winget install Discord.Discord`)
- Docker Desktop (कमांड `winget install Docker.DockerDesktop`)
- Git (कमांड `winget install Git`)
- 7zip (कमांड `winget install 7zip`)
- VLC (कमांड `winget install VideoLAN.VLC`)

## संदर्भ
[एप्लिकेशन इंस्टॉल और प्रबंधित करने के लिए winget टूल का उपयोग करें](https://learn.microsoft.com/hi-in/windows/package-manager/winget/)

### अतिरिक्त बात
मैंने सोचा था कि मैं Paint.Net भी इंस्टॉल कर सकता हूं, लेकिन मैं इसे इंस्टॉल नहीं कर सका।

https://forums.getpaint.net/topic/118574-please-add-paintnet-to-the-available-packages-for-windows-package-manager-winget/

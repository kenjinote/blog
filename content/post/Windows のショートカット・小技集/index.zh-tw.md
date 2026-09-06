---
title: "Windows 的快速鍵與小技巧集"
slug: "Windows 的快速鍵與小技巧集"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "小技巧", "快速鍵"]
draft: false
image: "img.png"
categories: ["PC・小工具"]
---
這是一些在 Windows 中常用的小技巧。希望剛開始使用 Windows 的使用者能閱讀這篇文章。
預設環境為 Windows 11，但許多技巧在 Windows 10 中也適用。

## 關閉視窗
- 視窗處於活動狀態時按下 `Alt + F4`
- 視窗處於活動狀態時按下 `Ctrl + W`。關閉分頁或視窗（僅限支援的應用程式）
- 雙擊視窗標題列左側的圖示
- 點擊視窗標題列的 `×`

## 顯示桌面
- `Win + D`。按 2 次可恢復原來的視窗狀態。當您只想短暫顯示桌面時非常方便。
- `Win + M`。最小化所有應用程式。按 2 次無法恢復。

## 語音輸入
- `Win + H`。開始語音輸入。要結束語音輸入，請按下 `Esc` 或再次按下 `Win + H`。

## 在檔案總管中顯示傳統的右鍵選單
- 按下 `Shift + F10` 或應用程式鍵。應用程式鍵位於鍵盤的右下角。

## 選擇範圍並擷取螢幕畫面
- 按下 `Win + Shift + S` 可選擇範圍並擷取螢幕畫面。
- 按下 `Win + Print Screen` 或單獨按下 `Print Screen` 可擷取全螢幕。
  (如果加上 `Win`，擷取的圖片將儲存在 `C:\Users\使用者名稱\Pictures\Screenshots` 中。)
- 按下 `Alt + Print Screen` 可擷取目前的活動視窗。

## 啟動釘選在工作列上的應用程式
- 按下 `Win + 數字鍵` 可啟動釘選在工作列上的應用程式。  
  例如，按下 `Win + 1` 將啟動工作列最左側的應用程式。
- 按下 `Win + T` 可將焦點移至工作列上的圖示，連續多次按下 `Win + T`，
  或使用 `←` 或 `→` 移動選擇，然後按下 `Enter` 鍵啟動選定的應用程式。

## 放大/縮小
- 按下 `Win + +` 可啟動 Windows 放大鏡。此外，按 `Win + + 或 -` 可放大/縮小螢幕。
- 在記事本或瀏覽器中，按下 `Ctrl + + 或 -` 可放大/縮小（僅限支援的應用程式）。

## 鎖定 Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Space` 或 `Enter`

## 關閉 Windows
- 在按下 `Win + M` 或 `Win + D` 顯示桌面時，或者按下 `Win + T` 或 `Win + B` 啟動工作列時，按下 `Alt + F4`，將顯示如下對話方塊，確認已選擇「關機」，然後按下 `Enter`
  也可以透過 `Win + R` → `Alt + F4` → `Alt + F4` 執行。
  ![img_20.png](img_20.png)
- 依序按下 `Win + X` → `U` → `U` 即可關機。
- 在命令提示字元或 `Win + R` 開啟的「執行」中輸入 `shutdown /s /t 0` 即可關機。若加上 `/f` 則會強制關機。

## 重新啟動 Windows
- 在按下 `Win + M` 或 `Win + D` 顯示桌面時，或者按下 `Win + T` 或 `Win + B` 啟動工作列時，按下 `Alt + F4`，將顯示如下對話方塊，按 1 次 `↓` 選擇「重新啟動」，然後按下 `Enter`
  也可以透過 `Win + R` → `Alt + F4` → `Alt + F4` 執行。
  ![img_21.png](img_21.png)
- 依序按下 `Win + X` → `U` → `R` 即可重新啟動。
- 輸入 `shutdown /r /t 0` 即可重新啟動。若加上 `/f` 則會強制重新啟動。

## 睡眠 Windows
- 在按下 `Win + M` 或 `Win + D` 顯示桌面時，或者按下 `Win + T` 或 `Win + B` 啟動工作列時，按下 `Alt + F4`，將顯示如下對話方塊，按 1 次 `↑` 選擇「睡眠」，然後按下 `Enter`
  也可以透過 `Win + R` → `Alt + F4` → `Alt + F4` 執行。
  ![img_23.png](img_23.png)
- 透過 `Win + R` → 或在命令提示字元中輸入 `rundll32.exe powrprof.dll,SetSuspendState` 即可進入休眠狀態。

## 登出 Windows
- 在按下 `Win + M` 或 `Win + D` 顯示桌面時，或者按下 `Win + T` 或 `Win + B` 啟動工作列時，按下 `Alt + F4`，將顯示如下對話方塊，按 2 次 `↑` 選擇「登出」，然後按下 `Enter`
  也可以透過 `Win + R` → `Alt + F4` → `Alt + F4` 執行。
  ![img_22.png](img_22.png)
- 依序按下 `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → 按 2 次 `Tab` 或 2 次 `↓` → `Enter` 或 `Space`
- 輸入 `logoff` 即可登出。

## 使用鍵盤移動視窗
- `Win + ←`：向左移動
- `Win + →`：向右移動
- `Win + ↑`：向上移動/最大化
- `Win + ↓`：向下移動/最小化
- `Win + Shift + ← 或 →`：在多顯示器之間移動
- `Win + Alt + ← 或 → 或 ↑ 或 ↓`：在不最大化或最小化的情況下移動視窗
- 在未最小化的狀態下，按下 `Alt + Space` 後按 `M`，然後使用方向鍵移動。  
  ※因為視窗會跟隨游標，即使視窗顯示在螢幕外也可以將其移回。

## 在工作管理員中結束處理程序
![img_24.png](img_24.png)
1. 按下 `Ctrl + Shift + Esc` 可啟動工作管理員。
2. 按下 `Ctrl + Tab` 可切換分頁。
3. 在 `詳細資料` 分頁中按下 `Tab`，接著使用鍵盤英數輸入搜尋處理程序的前綴。
4. 當選取處理程序名稱後，按下 `Delete` 鍵，再按 `Enter` 鍵即可結束處理程序。

## 使用命令指定處理程序名稱並結束
- 輸入 `taskkill /f /im 處理程序名稱` 即可結束處理程序。
  例如，輸入 `taskkill /f /im explorer.exe` 即可結束檔案總管。

## 從工作列圖示啟動多個相同的程式
- 在工作列上按住 `Shift` 鍵並點擊左鍵，即可啟動多個相同的程式。（僅限支援多開的應用程式）

## 以系統管理員權限啟動程式
- 按住 `Ctrl + Shift` 啟動程式即可獲得系統管理員權限。

## 啟動檔案總管
- 按下 `Win + E` 即可啟動檔案總管。
- 按下 `Win + R` 顯示「執行」，輸入 `explorer` 並按下 `Enter`。
- 按下 `Ctrl + Shift + N` 可建立新資料夾。

## 在檔案總管目前開啟的位置開啟命令提示字元
- 在 Windows 11 中，可從右鍵選單的「終端機」啟動命令提示字元。
- 此外，在網址列中輸入 `cmd` 並按下 `Enter` 鍵即可啟動命令提示字元。

## 顯示剪貼簿記錄
- 按下 `Win + V` 即可顯示剪貼簿記錄。
  選取以前複製的文字或圖片即可再次複製。

## 執行
![img_28.png](img_28.png)
- 按下 `Win + R` 即可啟動「執行」。

以下介紹幾個可在「執行」或命令提示字元中執行的命令。

## 開啟 Edge
![img_18.png](img_18.png)
- 輸入 `msedge` 並按下 `Enter`

## 開啟 Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- 輸入 `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` 並按下 `Enter`

## 開啟終端機
![img_19.png](img_19.png)
- 輸入 `wt` 並按下 `Enter`

## 開啟控制台
![img_15.png](img_15.png)
- 輸入 `control` 並按下 `Enter`
- 也可以輸入 `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}` 開啟。

## 啟動記事本
![img_4.png](img_4.png)
- 輸入 `notepad` 並按下 `Enter`  

## 啟動小算盤
![img_5.png](img_5.png)
- 輸入 `calc` 並按下 `Enter`

## 啟動小畫家
![img_6.png](img_6.png)
- 輸入 `mspaint` 並按下 `Enter`  

## 啟動 PowerShell
![img_7.png](img_7.png)
- 輸入 `powershell` 並按下 `Enter`  

## 啟動 Visual Studio Code
![img_8.png](img_8.png)
- 輸入 `code` 並按下 `Enter`

## 啟動 Excel
![img_9.png](img_9.png)
- 輸入 `excel` 並按下 `Enter`  
  ※僅限安裝了 Excel 的情況。

## 開啟 Word
![img_10.png](img_10.png)
- 輸入 `winword` 並按下 `Enter`  
  ※僅限安裝了 Word 的情況。

## 開啟 PowerPoint
![img_11.png](img_11.png)
- 輸入 `powerpnt` 並按下 `Enter`  
  ※僅限安裝了 PowerPoint 的情況。

## 開啟系統設定
![img_1.png](img_1.png)
- 輸入 `msconfig` 並按下 `Enter`  

## 開啟系統內容
![img_2.png](img_2.png)
- 輸入 `sysdm.cpl` 並按下 `Enter`

## 開啟 Windows 關於
![img_27.png](img_27.png)
- 輸入 `winver` 並按下 `Enter`

## 開啟螢幕小鍵盤
![img_14.png](img_14.png)
- 輸入 `osk` 並按下 `Enter`

## 開啟寫字板
![img_12.png](img_12.png)
- 輸入 `wordpad` 或 `write` 並按下 `Enter`

## 開啟登錄編輯程式
![img_13.png](img_13.png)
- 輸入 `regedit` 並按下 `Enter`

## 開啟程式和功能
- 輸入 `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` 並按下 `Enter`

## 開啟鍵盤內容
- 輸入 `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` 並按下 `Enter`

## 開啟滑鼠內容
![img_16.png](img_16.png)
- 輸入 `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` 並按下 `Enter`

## 開啟聲音
![img_3.png](img_3.png)
- 輸入 `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` 並按下 `Enter`

## 開啟使用者帳戶
- 輸入 `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` 並按下 `Enter`

## 複製標準訊息方塊中的字串
![img_26.png](img_26.png)
- 按下 `Ctrl + C` 即可複製標準訊息方塊中的字串。
  複製上述的訊息方塊時，會將以下內容複製到剪貼簿：
```
[Window Title]
寫字板

[Main Instruction]
您要儲存變更到 文件 嗎?

[儲存(S)] [不要儲存(N)] [取消]
```

## 將命令提示字元的輸出儲存到剪貼簿
在命令的後方加上 ` | clip` (管線符號加 clip)，如 `echo "hello" | clip`，即可將標準輸出複製到剪貼簿。

## 以文字輸出資料夾階層
在命令提示字元中使用 `tree` 命令，可以樹狀結構輸出資料夾階層。

輸出範例
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(以下省略)
```

## 參考資料
- [Windows 的鍵盤快速鍵](https://support.microsoft.com/zh-tw/windows/windows-%E7%9A%84%E9%8D%B5%E7%9B%A4%E5%BF%AB%E9%80%9F%E9%8D%B5-dcc61a57-8ff0-cffe-9796-cb9706c75eec)

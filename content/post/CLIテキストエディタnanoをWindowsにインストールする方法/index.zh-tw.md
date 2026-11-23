---
title: '在 Windows 使用 nano 命令列文字編輯器：WSL 與 MSYS2'
slug: "CLI文字編輯器nanoをWindowsに安裝する方法"
date: 2024-03-31T18:09:32+09:00
lastmod: "2026-11-23"
tags: ["nano", "文字編輯器"]
draft: false
image: "img_1.webp"
categories: ["tools-development-environment"]
description: '介紹在 Windows 使用 GNU nano 的現行方式：透過 WSL 安裝 Linux 環境，或透過 MSYS2 安裝 Windows 開發工具，並說明基本快速鍵。'
---


在 Windows 使用 GNU nano 有幾種方式。舊下載網站提供的獨立 `nano.exe` 可能難以確認來源與維護狀態，因此本文介紹兩種持續維護的發行管道。

## 方法一：在 WSL 使用

如果也需要 Linux 命令列工具，請選擇 WSL。在 Windows 11 或 Windows 10 2004 版（組建 19041）以上，以系統管理員身分開啟 PowerShell 並執行：

```powershell
wsl --install
```

重新啟動後開啟 Ubuntu，並在 Linux 終端機安裝 nano：

```bash
sudo apt update
sudo apt install nano
nano --version
```

執行 `nano 檔名` 即可開啟檔案。WSL 中的 Windows C: 磁碟機位於 `/mnt/c/`，例如 `nano /mnt/c/Users/使用者名稱/notes.txt`。安裝和檔案存取方式請參閱 [Microsoft 的 WSL 安裝指南](https://learn.microsoft.com/zh-tw/windows/wsl/install)。

## 方法二：透過 MSYS2 使用

如果不需要完整 Linux 發行版，只想搭配 Windows 開發工具使用 Unix 風格命令列，請選擇 [MSYS2](https://www.msys2.org/)。依照[官方安裝指南](https://www.msys2.org/docs/installer/)安裝後，開啟「MSYS2 MSYS」終端機。 圖形安裝程式需要 64 位元 Windows 10 1809 以上版本或 Windows Server 2019；各套件需求可能不同（請參閱[支援的 Windows 版本](https://www.msys2.org/docs/windows_support/)）。先更新套件資料庫和已安裝套件。若更新要求重新啟動終端機，請重新開啟並完成更新，再安裝 nano。

```bash
pacman -Suy
pacman -S nano
nano --version
```

套件名稱與安裝命令可在 [MSYS2 nano 套件頁面](https://packages.msys2.org/packages/nano?variant=x86_64)查詢。請在 MSYS2 終端機內執行 nano。若要從一般命令提示字元或 PowerShell 使用，還需要額外設定 PATH 和執行環境；不建議未經評估便將 MSYS2 的 `/usr/bin` 加入 Windows PATH。

## 基本操作

執行 `nano notes.txt` 等命令即可啟動。畫面底部會顯示快速鍵說明：`^` 代表 Ctrl，`M-` 代表 Meta（通常是 Alt）。按 `Ctrl+O` 寫入檔案，以 Enter 確認顯示的檔名，再按 `Ctrl+X` 結束。目前版本也可用 `Ctrl+S` 儲存目前緩衝區。詳情請參閱 [GNU nano 官方快速鍵表](https://www.nano-editor.org/dist/latest/cheatsheet.html)。

nano 支援國際化和 UTF-8，但日文輸入與顯示也取決於終端機、字型、地區設定與輸入法。如果在 WSL 或 MSYS2 中出現亂碼或無法輸入日文，請檢查終端機的 UTF-8 和輸入法設定。

## 參考資料

- [GNU nano](https://www.nano-editor.org/)
- [GNU nano 官方快速鍵表](https://www.nano-editor.org/dist/latest/cheatsheet.html)
- [Microsoft Learn：安裝 WSL](https://learn.microsoft.com/zh-tw/windows/wsl/install)
- [MSYS2 官方安裝指南](https://www.msys2.org/docs/installer/)
- [支援的 Windows 版本](https://www.msys2.org/docs/windows_support/)
- [MSYS2 nano 套件](https://packages.msys2.org/packages/nano?variant=x86_64)

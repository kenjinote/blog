---
title: "為 msix 加上自簽憑證以便安裝"
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自己証明書", "インストール"]
draft: false
image: "img.png"
categories: ["IT・テクノロジー"]
---

# 為 msix 加上自簽憑證以便安裝

在 Windows 上發布應用程式時，使用 **MSIX 套件** 會很方便，因為它統一了安裝和更新機制。然而，MSIX 有一個限制，即「必須有已簽署的憑證」。
當您想要測試發布由企業或個人開發的應用程式時，可能會遇到「購買商業程式碼簽署憑證太過小題大作」的情況。

這時 **自簽憑證 (Self-Signed Certificate)** 就能派上用場。在本文中，我們將總結為 MSIX 加上自簽憑證並允許在本地環境中安裝的步驟。

---

## 1. 建立自簽憑證

首先，以系統管理員模式啟動 PowerShell 並執行以下命令。

```powershell
// 建立自簽憑證
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

這裡建立的是用於「程式碼簽署」的憑證。

* 使用 `-FriendlyName` 給它一個容易理解的名稱，以便日後尋找。
* 您可以使用 `-NotAfter` 調整到期日。這次我們將其設定為 10 年。

---

## 2. 匯出 PFX 檔案

將建立的憑證匯出為 PFX 格式，以便可以與 `signtool` 一起使用。

```powershell
// 建立 pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

此時設定的密碼（範例中為 `password`）將在稍後的簽署操作中需要。

---

## 3. 將自簽憑證安裝到受信任的根憑證授權單位

就這樣，Windows 並不信任建立的憑證。要安裝它，您需要從 `certmgr.msc` 將其匯入到 **[受信任的根憑證授權單位] -> [憑證]** 。

如果匯入匯出的憑證（ `.cer` 或 `.pfx` ），它將在目標 PC 上被視為受信任的憑證。
這可以防止即使您簽署了 MSIX 也會出現「不受信任的憑證」警告。

---

## 4. 簽署安裝程式 (MSIX)

最後，使用建立的 PFX 憑證簽署 MSIX。 `signtool` 包含在 Visual Studio 和 Windows SDK 中。

```powershell
// 簽署安裝程式
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` 指定簽章演算法。
* 使用 `/f` 指定 PFX 檔案，並使用 `/p` 傳遞密碼。
* 最後，指定 MSIX 檔案的路徑。
* 如果未設定 signtool 的路徑，請指定完整路徑。在我的環境中，它位於以下位置。

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

這樣就完成了簽署，並完成了一個可以在目標 PC 上安裝的 MSIX。

---

## 總結

* 使用 **New-SelfSignedCertificate** 建立自簽憑證 
* 使用 **Export-PfxCertificate** 匯出 PFX 
* 將憑證安裝到 **受信任的根憑證授權單位** 
* 使用 **signtool** 簽署 MSIX 

透過遵循此流程，您可以在本地環境中檢查操作並進行測試發布，而無需購買商業憑證。
當然，憑證授權單位核發的憑證對於實際的商業發布是必不可少的，但這種方法在開發和驗證階段非常方便。

---

👉 這次我們以 installer.msix 為例，但您也可以將相同的程序應用於您自己開發的應用程式。

---

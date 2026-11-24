---
title: "安全診斷 GitHub Copilot 憑證錯誤"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の解決方法"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "安全調查憑證錯誤並檢查 Proxy 與 ESET，不降低 TLS 防護。"
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 安全診斷 GitHub Copilot 憑證錯誤

僅憑此錯誤無法判定原因是 ESET。GitHub 表示，這類錯誤常與檢查 TLS 流量的 Proxy 或自訂憑證有關。

## 以下日誌記錄於 2024 年 4 月 21 日。授權相關文字反映當時情況；目前設定請參考 GitHub 最新文件。

請在另一個網路測試同一個 IDE，確認問題是否與 Proxy 或 VPN 有關。若企業 Proxy 會檢查 TLS，請管理員檢查憑證鏈，並將組織正式發行的 CA 憑證安裝到作業系統信任存放區。使用 ESET 時，請更新產品並依照官方憑證修復指引處理。只有確認特定應用程式的檢查造成問題且符合組織政策時，才考慮個別規則。

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## 請勿持續關閉 ESET SSL/TLS 檢查，也不要永久忽略憑證錯誤。ESET 說明，停用會降低對加密流量威脅的檢查；GitHub 也警告忽略憑證錯誤可能帶來安全風險。

記錄的錯誤

## 連線檢查

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

透過 Proxy 測試時，請依 GitHub 文件新增 `-x http://主機:連接埠`。

## ESET 說明

安全檢查

> 分享日誌前，請移除認證資料、Proxy 使用者名稱與密碼，以及個人資訊。

## 參考資料

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)

---
title: "GitHub Copilotの証明書エラーを安全に診断する"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の対処方法"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "証明書エラーの原因をプロキシやESETも含めて切り分け、安全な対処方法を紹介します。"
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# GitHub Copilotの証明書エラーを安全に診断する

このエラーだけではESETが原因とは断定できません。GitHubは、TLS通信を検査するプロキシやカスタム証明書がよくある原因と説明しています。

## 次のログは2024年4月21日の記録です。ライセンスに関する文言も当時のもので、現在のネットワーク設定はGitHubの最新資料を確認してください。

別のネットワークでも同じIDEを試し、プロキシやVPNに依存するか確認します。社内でTLS検査を行う場合は、管理者に証明書チェーンを確認してもらい、組織が配布したCA証明書をOSの信頼ストアに登録してください。ESET利用時は製品を更新し、公式の証明書修復手順を確認します。原因が特定アプリの検査と確認できた場合のみ、組織の方針に沿ってアプリ別ルールを検討してください。

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## ESETのSSL/TLS検査を常時無効にする方法や、証明書エラーを無視する設定は勧めません。ESETは無効化すると暗号化通信の脅威検査が低下すると説明し、GitHubも証明書検証を無視する方法にセキュリティ上のリスクがあると警告しています。

記録したエラー

## 接続確認

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

プロキシ経由では、GitHubの公式例に従って`-x http://ホスト:ポート`を追加します。

## ESETについて

安全な確認方法

> 診断ログを共有する前に、認証情報、プロキシのユーザー名・パスワード、個人情報を削除してください。

## 参考資料

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)

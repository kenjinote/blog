---
title: "安全排查 GitHub Copilot 证书错误"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合の处理方法"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "安全排查证书错误，检查代理和 ESET，同时不削弱 TLS 保护。"
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# 安全排查 GitHub Copilot 证书错误

仅凭此错误无法断定原因是 ESET。GitHub 说明，此类错误通常与检查 TLS 流量的代理或自定义证书有关。

## 以下日志记录于 2024 年 4 月 21 日。许可证相关文字反映当时情况；当前网络设置请查看 GitHub 最新文档。

尝试在另一个网络中使用同一 IDE，确认问题是否与代理或 VPN 有关。若企业代理会检查 TLS，请让管理员验证证书链，并将组织正式签发的 CA 证书安装到操作系统信任存储中。使用 ESET 时，请更新产品并遵循其证书修复说明。只有确认特定应用的检查导致问题且符合组织政策时，才考虑设置应用规则。

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## 不要一直关闭 ESET SSL/TLS 检查，也不要永久忽略证书错误。ESET 说明关闭检查会降低对加密流量威胁的扫描；GitHub 也警告，忽略证书错误可能带来安全风险。

记录的错误

## 连通性检查

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

通过代理测试时，请按 GitHub 文档添加 `-x http://主机名:端口`。

## 关于 ESET

安全检查

> 分享日志前，请删除凭据、代理用户名和密码以及个人信息。

## 参考资料

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)

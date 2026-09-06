---
title: '使用自签名证书实现 MSIX 的安装'
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自签名证书", "安装"]
draft: false
image: "img.png"
categories: ["IT・技术"]
---

# 使用自签名证书实现 MSIX 的安装

在 Windows 上分发应用时，使用 **MSIX 包** 可以统一安装和更新的机制，非常方便。但是，MSIX 有一个限制，即“必须使用经过签名的证书”。
当我们想要测试分发企业或个人开发的应用时，可能会觉得“购买商用代码签名证书太过夸张”吧。

这时，**自签名证书（Self-Signed Certificate）** 就能派上用场了。本文将总结为 MSIX 添加自签名证书，使其能够在本地环境中进行安装的步骤。

---

## 1. 创建自签名证书

首先，以管理员身份启动 PowerShell，并执行以下命令。

```powershell
// 创建自签名证书
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

此处创建的是“用于代码签名”的证书。

* 使用 `-FriendlyName` 赋予一个容易理解的名称，以后会更容易查找。
* 使用 `-NotAfter` 可以调整有效期。本次设置为 10 年。

---

## 2. 导出 PFX 文件

将创建的证书导出为 PFX 格式，以便在 `signtool` 中使用。

```powershell
// 创建 pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

此时设置的密码（示例中为 `password`），在后续的签名操作中会用到。

---

## 3. 将自签名证书安装到受信任的根证书颁发机构

创建的证书按原样是不会被 Windows 信任的。要安装它，需要从 `certmgr.msc` 导入到 **[受信任的根证书颁发机构] → [证书]** 中。

导入导出的证书（`.cer` 或 `.pfx`）后，在目标 PC 上就会被视为受信任的证书。
这样一来，即使对 MSIX 进行了签名，也不会出现“不受信任的证书”的警告了。

---

## 4. 为安装程序 (MSIX) 添加签名

最后，使用创建的 PFX 证书对 MSIX 进行签名。`signtool` 包含在 Visual Studio 和 Windows SDK 中。

```powershell
// 为安装程序添加签名
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` 指定了签名算法。
* `/f` 指定 PFX 文件，`/p` 传递密码。
* 最后请指定 MSIX 文件的路径。
* 如果没有配置 signtool 的环境变量路径，请指定完整路径。在我的环境中，它位于以下位置。

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

至此，签名完成，可以在目标 PC 上安装的 MSIX 就准备好了。

---

## 总结

* 使用 **New-SelfSignedCertificate** 创建自签名证书
* 使用 **Export-PfxCertificate** 导出 PFX
* 将证书安装到 **受信任的根证书颁发机构**
* 使用 **signtool** 对 MSIX 进行签名

掌握了这个流程，就可以在不购买商用证书的情况下，在本地环境中进行运行确认和测试分发了。
当然，在实际的商用分发中，证书颁发机构签发的证书是必不可少的，但在开发和验证阶段，这种方法非常方便。

---

👉 本次以 installer.msix 为例，但同样的步骤也适用于自研应用。

---

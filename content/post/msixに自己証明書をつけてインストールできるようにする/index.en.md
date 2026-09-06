---
title: 'Installing an MSIX with a Self-Signed Certificate'
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "self-signed certificate", "installation"]
draft: false
image: "img.png"
categories: ["IT & Technology"]
---

# Installing an MSIX with a Self-Signed Certificate

When distributing apps on Windows, using **MSIX packages** is convenient because it unifies the installation and update mechanisms. However, MSIX has a restriction that it requires a "must be signed" certificate.
There may be situations where you want to test-distribute an app developed for a company or individually, but "purchasing a commercial code signing certificate is too much."

This is where a **Self-Signed Certificate** comes in handy. In this article, we will summarize the steps to attach a self-signed certificate to an MSIX and make it installable in a local environment.

---

## 1. Create a Self-Signed Certificate

First, launch PowerShell in administrator mode and run the following command.

```powershell
// Create a self-signed certificate
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

This creates a certificate for "code signing".

* Giving it a descriptive name with `-FriendlyName` makes it easier to find later.
* You can adjust the expiration date with `-NotAfter`. Here it's set to 10 years.

---

## 2. Export the PFX File

Export the created certificate in PFX format so it can be used with `signtool`.

```powershell
// Create pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

The password set here (e.g., `password`) will be required later for signing operations.

---

## 3. Install the Self-Signed Certificate to Trusted Root Certification Authorities

The created certificate won't be trusted by Windows as is. To install it, you need to import it into **[Trusted Root Certification Authorities] -> [Certificates]** from `certmgr.msc`.

If you import the exported certificate (`.cer` or `.pfx`), it will be treated as a trusted certificate on the target PC.
This prevents the "untrusted certificate" warning when signing an MSIX.

---

## 4. Sign the Installer (MSIX)

Finally, use the created PFX certificate to sign the MSIX. `signtool` is included with Visual Studio and the Windows SDK.

```powershell
// Sign the installer
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` specifies the signature algorithm.
* `/f` specifies the PFX file, and `/p` passes the password.
* Finally, specify the path to the MSIX file.
* If signtool is not in your path, specify the full path. In my environment, it was in the following location:

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

This completes the signing, and the installable MSIX for the target PC is ready.

---

## Summary

* Create a self-signed certificate with **New-SelfSignedCertificate**
* Export the PFX with **Export-PfxCertificate**
* Install the certificate in **Trusted Root Certification Authorities**
* Sign the MSIX with **signtool**

By following this flow, you can test operations and distribute locally without buying a commercial certificate.
Of course, a certificate issued by a Certificate Authority is essential for actual commercial distribution, but this method is very convenient during the development and verification stages.

---

👉 In this example, we used installer.msix, but the same procedure applies to your own custom apps.

---

---
title: "Permettre l'installation de msix avec un certificat auto-signé"
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自己証明書", "インストール"]
draft: false
image: "img.png"
categories: ["IT・テクノロジー"]
---

# Permettre l'installation de msix avec un certificat auto-signé

Lors de la distribution d'applications sous Windows, l'utilisation d'un **package MSIX** est pratique car elle unifie les mécanismes d'installation et de mise à jour. Cependant, MSIX a la restriction qu'"un certificat signé est toujours requis".
Lorsque vous souhaitez distribuer pour test une application développée par une entreprise ou un particulier, il peut y avoir des situations où "l'achat d'un certificat de signature de code commercial est exagéré".

C'est là qu'un **certificat auto-signé (Self-Signed Certificate)** s'avère utile. Dans cet article, nous résumerons les étapes pour joindre un certificat auto-signé à MSIX et permettre son installation dans un environnement local.

---

## 1. Créer un certificat auto-signé

Tout d'abord, démarrez PowerShell en mode administrateur et exécutez la commande suivante.

```powershell
// Créer un certificat auto-signé
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

Ce qui est créé ici est un certificat pour la "signature de code".

* Lui donner un nom facile à comprendre avec `-FriendlyName` facilite sa recherche ultérieure.
* Vous pouvez ajuster la date d'expiration avec `-NotAfter`. Cette fois, elle est fixée à 10 ans.

---

## 2. Exporter le fichier PFX

Exportez le certificat créé au format PFX afin qu'il puisse être utilisé avec `signtool`.

```powershell
// Créer pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

Le mot de passe défini à ce moment-là (dans l'exemple, `password`) sera requis pour l'opération de signature ultérieure.

---

## 3. Installer le certificat auto-signé dans les Autorités de certification racines de confiance

Le certificat créé n'est pas approuvé par Windows tel quel. Pour l'installer, vous devez l'importer de `certmgr.msc` vers **[Autorités de certification racines de confiance] -> [Certificats]** .

Si vous importez le certificat exporté ( `.cer` ou `.pfx` ), il sera traité comme un certificat de confiance sur le PC cible.
Cela empêche l'avertissement de "certificat non approuvé" d'apparaître même si vous signez le MSIX.

---

## 4. Signer le programme d'installation (MSIX)

Enfin, utilisez le certificat PFX créé pour signer le MSIX. `signtool` est inclus dans Visual Studio et le SDK Windows.

```powershell
// Signer le programme d'installation
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` spécifie l'algorithme de signature.
* Spécifiez le fichier PFX avec `/f` et transmettez le mot de passe avec `/p`.
* Enfin, spécifiez le chemin d'accès au fichier MSIX.
* Si le chemin d'accès à signtool n'est pas défini, spécifiez le chemin complet. Dans mon environnement, il se trouvait à l'emplacement suivant.

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

Cela conclut la signature et complète un MSIX qui peut être installé sur le PC cible.

---

## Résumé

* Créer un certificat auto-signé avec **New-SelfSignedCertificate** 
* Exporter le PFX avec **Export-PfxCertificate** 
* Installer le certificat dans les **Autorités de certification racines de confiance** 
* Signer le MSIX avec **signtool** 

En suivant ce flux, vous pouvez vérifier le fonctionnement et distribuer pour test dans l'environnement local sans acheter de certificat commercial.
Bien sûr, un certificat émis par une autorité de certification est essentiel pour la distribution commerciale réelle, mais cette méthode est très pratique dans les étapes de développement et de vérification.

---

👉 Cette fois, nous avons utilisé installer.msix comme exemple, mais vous pouvez appliquer la même procédure à votre propre application.

---

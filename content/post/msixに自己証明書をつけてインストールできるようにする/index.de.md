---
title: "Zulassen der msix-Installation mit einem selbstsignierten Zertifikat"
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自己証明書", "インストール"]
draft: false
image: "img.png"
categories: ["IT・テクノロジー"]
---

# Zulassen der msix-Installation mit einem selbstsignierten Zertifikat

Beim Verteilen von Apps unter Windows ist die Verwendung eines **MSIX-Pakets** praktisch, da Installations- und Aktualisierungsmechanismen vereinheitlicht werden. MSIX hat jedoch die Einschränkung, dass "immer ein signiertes Zertifikat erforderlich ist".
Wenn Sie eine von einem Unternehmen oder einer Einzelperson entwickelte App zum Testen verteilen möchten, kann es Situationen geben, in denen "der Kauf eines kommerziellen Code-Signing-Zertifikats übertrieben ist".

Hier ist ein **selbstsigniertes Zertifikat (Self-Signed Certificate)** nützlich. In diesem Artikel fassen wir die Schritte zusammen, um ein selbstsigniertes Zertifikat an MSIX anzuhängen und die Installation in einer lokalen Umgebung zuzulassen.

---

## 1. Ein selbstsigniertes Zertifikat erstellen

Starten Sie zunächst PowerShell im Administratormodus und führen Sie den folgenden Befehl aus.

```powershell
// Selbstsigniertes Zertifikat erstellen
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

Was hier erstellt wird, ist ein Zertifikat für "Code Signing".

* Ihm mit `-FriendlyName` einen leicht verständlichen Namen zu geben, erleichtert das spätere Auffinden.
* Sie können das Ablaufdatum mit `-NotAfter` anpassen. Diesmal ist es auf 10 Jahre eingestellt.

---

## 2. PFX-Datei exportieren

Exportieren Sie das erstellte Zertifikat im PFX-Format, damit es mit `signtool` verwendet werden kann.

```powershell
// pfx erstellen
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

Das zu diesem Zeitpunkt festgelegte Passwort (im Beispiel `password`) wird für den späteren Signaturvorgang benötigt.

---

## 3. Selbstsigniertes Zertifikat in vertrauenswürdigen Stammzertifizierungsstellen installieren

Das erstellte Zertifikat wird von Windows nicht ohne Weiteres als vertrauenswürdig eingestuft. Um es zu installieren, müssen Sie es aus `certmgr.msc` nach **[Vertrauenswürdige Stammzertifizierungsstellen] -> [Zertifikate]** importieren.

Wenn Sie das exportierte Zertifikat ( `.cer` oder `.pfx` ) importieren, wird es auf dem Ziel-PC als vertrauenswürdiges Zertifikat behandelt.
Dadurch wird verhindert, dass die Warnung "nicht vertrauenswürdiges Zertifikat" angezeigt wird, selbst wenn Sie das MSIX signieren.

---

## 4. Installationsprogramm (MSIX) signieren

Verwenden Sie schließlich das erstellte PFX-Zertifikat, um das MSIX zu signieren. `signtool` ist in Visual Studio und im Windows SDK enthalten.

```powershell
// Installationsprogramm signieren
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` gibt den Signaturalgorithmus an.
* Geben Sie die PFX-Datei mit `/f` an und übergeben Sie das Passwort mit `/p`.
* Geben Sie schließlich den Pfad zur MSIX-Datei an.
* Wenn der Pfad zu signtool nicht festgelegt ist, geben Sie den vollständigen Pfad an. In meiner Umgebung befand es sich am folgenden Speicherort.

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

Damit ist die Signatur abgeschlossen und ein MSIX, das auf dem Ziel-PC installiert werden kann, ist fertiggestellt.

---

## Zusammenfassung

* Erstellen Sie ein selbstsigniertes Zertifikat mit **New-SelfSignedCertificate** 
* Exportieren Sie PFX mit **Export-PfxCertificate** 
* Installieren Sie das Zertifikat in **Vertrauenswürdige Stammzertifizierungsstellen** 
* Signieren Sie MSIX mit **signtool** 

Indem Sie diesem Ablauf folgen, können Sie den Betrieb überprüfen und in der lokalen Umgebung zu Testzwecken verteilen, ohne ein kommerzielles Zertifikat kaufen zu müssen.
Natürlich ist ein von einer Zertifizierungsstelle ausgestelltes Zertifikat für den tatsächlichen kommerziellen Vertrieb unerlässlich, aber diese Methode ist in der Entwicklungs- und Überprüfungsphase sehr praktisch.

---

👉 Diesmal haben wir installer.msix als Beispiel verwendet, aber Sie können das gleiche Verfahren auf Ihre eigene App anwenden.

---

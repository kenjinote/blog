---

title: "Habilitar la instalación de msix con un certificado autofirmado"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "certificado autofirmado", "instalación"]
draft: false
image: "img.png"
categories: ["IT / Tecnología"]
---


# Habilitar la instalación de msix con un certificado autofirmado

Al distribuir aplicaciones en Windows, el uso del **paquete MSIX** es conveniente ya que unifica los mecanismos de instalación y actualización. Sin embargo, MSIX tiene la restricción de requerir un "certificado firmado obligatoriamente".
En ocasiones, cuando se desea distribuir una aplicación desarrollada por una empresa o un individuo con fines de prueba, "comprar un certificado de firma de código comercial puede resultar excesivo".

Ahí es donde resulta útil el **certificado autofirmado (Self-Signed Certificate)**. En este artículo, resumiremos los pasos para adjuntar un certificado autofirmado a un MSIX para permitir su instalación en un entorno local.

---

## 1. Crear un certificado autofirmado

Primero, inicie PowerShell en modo administrador y ejecute el siguiente comando.

```powershell
// Crear certificado autofirmado
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

Lo que se crea aquí es un certificado para "firma de código".

* Asignar un nombre fácil de entender con `-FriendlyName` facilita su búsqueda posterior.
* La fecha de vencimiento se puede ajustar con `-NotAfter`. En esta ocasión, está configurada para 10 años.

---

## 2. Exportar el archivo PFX

Exporte el certificado creado en formato PFX para poder utilizarlo con `signtool`.

```powershell
// Crear pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

La contraseña configurada en este momento (en el ejemplo, `password`) será necesaria para la posterior operación de firma.

---

## 3. Instalar el certificado autofirmado en las entidades de certificación raíz de confianza

El certificado creado no es confiable para Windows por defecto. Para instalarlo, debe importarse desde `certmgr.msc` en **[Entidades de certificación raíz de confianza] → [Certificados]**.

Si importa el certificado exportado (`.cer` o `.pfx`), se tratará como un certificado de confianza en la PC de destino.
Con esto, no aparecerá la advertencia de "certificado no confiable" al firmar el MSIX.

---

## 4. Firmar el instalador (MSIX)

Finalmente, utilice el certificado PFX creado para firmar el MSIX. `signtool` está incluido en Visual Studio o Windows SDK.

```powershell
// Firmar el instalador
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` especifica el algoritmo de firma.
* `/f` especifica el archivo PFX y `/p` proporciona la contraseña.
* Finalmente, especifique la ruta del archivo MSIX.
* Si la ruta de signtool no está configurada, especifique la ruta completa. En mi entorno, se encontraba en la siguiente ubicación:

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

Con esto, la firma se ha completado y el MSIX instalable en la PC de destino está listo.

---

## Resumen

* Crear un certificado autofirmado con **New-SelfSignedCertificate**
* Exportar el PFX con **Export-PfxCertificate**
* Instalar el certificado en las **Entidades de certificación raíz de confianza**
* Firmar el MSIX con **signtool**

Si comprende este flujo, podrá realizar pruebas de funcionamiento y distribuciones de prueba en un entorno local sin comprar un certificado comercial.
Por supuesto, para la distribución comercial real, un certificado emitido por una autoridad de certificación es obligatorio, pero este método es muy útil en las etapas de desarrollo y verificación.

---

👉 En esta ocasión usamos installer.msix como ejemplo, pero el mismo procedimiento se puede aplicar a aplicaciones de desarrollo propio.

---

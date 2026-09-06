---
title: "Tornar possível instalar o msix com um certificado autoassinado"
slug: "msixに自己証明書をつけてインストールできるようにする"
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自己証明書", "インストール"]
draft: false
image: "img.png"
categories: ["IT・テクノロジー"]
---

# Tornar possível instalar o msix com um certificado autoassinado

Ao distribuir aplicativos no Windows, usar um **pacote MSIX** é conveniente porque unifica os mecanismos de instalação e atualização. No entanto, o MSIX tem a restrição de que "um certificado assinado é sempre necessário".
Quando você deseja distribuir para teste um aplicativo desenvolvido por uma empresa ou indivíduo, pode haver situações em que "comprar um certificado de assinatura de código comercial é um exagero".

É aí que um **certificado autoassinado (Self-Signed Certificate)** é útil. Neste artigo, resumiremos as etapas para adicionar um certificado autoassinado ao MSIX e permitir que ele seja instalado em um ambiente local.

---

## 1. Criar um certificado autoassinado

Primeiro, inicie o PowerShell no modo de administrador e execute o seguinte comando.

```powershell
// Criar certificado autoassinado
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

O que é criado aqui é um certificado para "assinatura de código".

* Dar a ele um nome fácil de entender com `-FriendlyName` facilita a localização posterior.
* Você pode ajustar a data de expiração com `-NotAfter`. Desta vez, está definido para 10 anos.

---

## 2. Exportar o arquivo PFX

Exporte o certificado criado no formato PFX para que possa ser usado com `signtool`.

```powershell
// Criar pfx
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

A senha definida neste momento (no exemplo, `password`) será necessária para a operação de assinatura posterior.

---

## 3. Instalar o certificado autoassinado em Autoridades de Certificação Raiz Confiáveis

O certificado criado não é confiável para o Windows como está. Para instá-lo, você precisa importá-lo de `certmgr.msc` para **[Autoridades de Certificação Raiz Confiáveis] -> [Certificados]** .

Se você importar o certificado exportado ( `.cer` ou `.pfx` ), ele será tratado como um certificado confiável no PC de destino.
Isso evita que o aviso de "certificado não confiável" apareça mesmo se você assinar o MSIX.

---

## 4. Assinar o instalador (MSIX)

Finalmente, use o certificado PFX criado para assinar o MSIX. O `signtool` está incluído no Visual Studio e no Windows SDK.

```powershell
// Assinar o instalador
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` especifica o algoritmo de assinatura.
* Especifique o arquivo PFX com `/f` e passe a senha com `/p`.
* Finalmente, especifique o caminho para o arquivo MSIX.
* Se o caminho para signtool não estiver definido, especifique o caminho completo. No meu ambiente, ele estava localizado no seguinte local.

```
"C:\Program Files (x86)\Microsoft Visual Studio\Shared\NuGetPackages\microsoft.windows.sdk.buildtools\10.0.26100.1742\bin\10.0.26100.0\x64\signtool.exe"
```

Isso conclui a assinatura e completa um MSIX que pode ser instalado no PC de destino.

---

## Resumo

* Crie um certificado autoassinado com **New-SelfSignedCertificate** 
* Exporte o PFX com **Export-PfxCertificate** 
* Instale o certificado nas **Autoridades de Certificação Raiz Confiáveis** 
* Assine o MSIX com **signtool** 

Ao seguir este fluxo, você pode verificar a operação e distribuir para teste no ambiente local sem comprar um certificado comercial.
Claro, um certificado emitido por uma autoridade de certificação é essencial para distribuição comercial real, mas esse método é muito conveniente nos estágios de desenvolvimento e verificação.

---

👉 Desta vez, usamos installer.msix como exemplo, mas você pode aplicar o mesmo procedimento ao seu próprio aplicativo.

---

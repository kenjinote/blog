---
title: 'msixに自己証明書をつけてインストールできるようにする'
date: 2025-08-30T04:18:04+09:00
tags: ["msix", "自己証明書", "インストール"]
draft: false
image: "img.png"
---

# msixに自己証明書をつけてインストールできるようにする

Windows でアプリを配布する際、**MSIX パッケージ**を利用すると、インストールや更新の仕組みが統一され便利です。しかし、MSIX には「必ず署名された証明書」が必要という制約があります。
企業や個人で開発したアプリをテスト配布したいときに、「商用コードサイニング証明書を購入するのは大げさすぎる」という場面もあるでしょう。

そこで役立つのが **自己証明書（Self-Signed Certificate）** です。この記事では、MSIX に自己証明書をつけてローカル環境でインストールできるようにする手順をまとめます。

---

## 1. 自己証明書を作成する

まず PowerShell を管理者モードで起動し、以下のコマンドを実行します。

```powershell
// 自己証明書の作成
New-SelfSignedCertificate -Type CodeSigningCert -Subject "CN=035A9AAC-915B-4CE1-AE39-1A101BED42F5" -CertStoreLocation Cert:\CurrentUser\My -NotAfter (Get-Date).AddYears(10) -KeyUsage DigitalSignature -FriendlyName "kenjinote"
```

ここで作成されるのは「コード署名用」の証明書です。

* `-FriendlyName` でわかりやすい名前を付けておくと後から探しやすいです。
* `-NotAfter` で有効期限を調整できます。今回は 10 年に設定しています。

---

## 2. PFX ファイルをエクスポートする

作成した証明書を PFX 形式でエクスポートして、`signtool` で利用できるようにします。

```powershell
// pfxの作成
$cert = Get-ChildItem Cert:\CurrentUser\My | Where-Object { $_.FriendlyName -eq "kenjinote" }
$password = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "D:\pfx\cert.pfx" -Password $password
```

このとき設定したパスワード（例では `password`）は、後の署名操作で必要になります。

---

## 3. 自己証明書を信頼できるルート証明機関にインストールする

作成した証明書は、そのままでは Windows に信頼されません。インストールするには、`certmgr.msc` から **\[信頼されたルート証明機関] → \[証明書]** にインポートする必要があります。

エクスポートした証明書（`.cer` や `.pfx`）をインポートすれば、対象 PC 上では信頼された証明書として扱われます。
これにより、MSIX を署名しても「信頼されていない証明書」という警告が出なくなります。

---

## 4. インストーラ（MSIX）に署名をつける

最後に、作成した PFX 証明書を使って MSIX に署名します。`signtool` は Visual Studio や Windows SDK に含まれています。

```powershell
// インストーラに署名をつける
signtool sign /fd SHA256 /f "D:\pfx\cert.pfx" /p "password" "C:\installer\installer.msix"
```

* `/fd SHA256` は署名アルゴリズムを指定しています。
* `/f` で PFX ファイルを指定し、`/p` でパスワードを渡します。
* 最後に MSIX ファイルのパスを指定してください。

これで署名が完了し、対象 PC でインストール可能な MSIX が完成します。

---

## まとめ

* **New-SelfSignedCertificate** で自己証明書を作成する
* **Export-PfxCertificate** で PFX をエクスポートする
* **信頼されたルート証明機関** に証明書をインストールする
* **signtool** で MSIX に署名する

この流れを押さえれば、商用証明書を買わずにローカル環境で動作確認やテスト配布が可能になります。
もちろん実際の商用配布では認証局発行の証明書が必須ですが、開発・検証段階ではこの手法がとても便利です。

---

👉 今回は installer.msix を例にしましたが、同じ手順で自作アプリにも適用できます。

---

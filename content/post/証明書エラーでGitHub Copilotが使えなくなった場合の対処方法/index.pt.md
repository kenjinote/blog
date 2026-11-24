---
title: "Diagnosticar erros de certificado do GitHub Copilot com segurança"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のSolução"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Investigue erros de certificado e verifique proxy e ESET com segurança, sem enfraquecer a proteção TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Diagnosticar erros de certificado do GitHub Copilot com segurança

Este erro, por si só, não prova que o ESET seja a causa. Segundo o GitHub, ele costuma envolver proxy que inspeciona TLS ou certificado personalizado.

## O log abaixo foi registrado em 21 de abril de 2024. O texto sobre a licença é daquele incidente; consulte a documentação atual do GitHub para as configurações vigentes.

Teste o mesmo IDE em outra rede para verificar se o problema depende do proxy ou VPN. Se um proxy corporativo inspecionar TLS, peça ao administrador que verifique a cadeia e instale no repositório de confiança do sistema o certificado CA oficial da organização. Se usar ESET, atualize-o e siga as instruções de reparo de certificados. Considere uma regra por aplicativo somente se a inspeção desse aplicativo for confirmada como causa e a política permitir.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## Não deixe a inspeção SSL/TLS do ESET desativada nem ignore permanentemente erros de certificado. A ESET informa que desativá-la reduz a verificação de ameaças no tráfego criptografado; o GitHub alerta que ignorar erros pode criar riscos de segurança.

Erro registrado

## Verificação de conectividade

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Para testar por proxy, siga a sintaxe documentada pelo GitHub e adicione `-x http://HOST:PORTA`.

## Sobre o ESET

Verificações seguras

> Antes de compartilhar logs, remova credenciais, usuário e senha do proxy e dados pessoais.

## Referências

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)

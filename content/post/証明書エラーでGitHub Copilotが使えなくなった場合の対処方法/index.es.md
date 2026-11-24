---
title: "Diagnosticar errores de certificado de GitHub Copilot de forma segura"
slug: "証明書エラーでGitHub Copilotが使えなくなった場合のMétodo de resolución"
tags: ["GitHub Copilot", "certificates"]
draft: false
image: "img.webp"
categories: ["tools-development-environment"]
description: "Investiga errores de certificado de forma segura y revisa el proxy y ESET sin debilitar la protección TLS."
date: "2024-04-21T18:47:26+09:00"
lastmod: "2026-11-24T00:00:00+09:00"
---
# Diagnosticar errores de certificado de GitHub Copilot de forma segura

Este error por sí solo no demuestra que ESET sea la causa. GitHub indica que suele estar relacionado con proxies que inspeccionan TLS o con certificados personalizados.

## El registro siguiente se guardó el 21 de abril de 2024. El texto sobre la licencia corresponde a aquel incidente; consulta la documentación actual de GitHub para conocer la configuración vigente.

Prueba el mismo IDE en otra red para comprobar si el problema depende del proxy o la VPN. Si un proxy corporativo inspecciona TLS, pide al administrador que verifique la cadena e instale en el almacén de confianza del sistema el certificado CA oficial de la organización. Si usas ESET, actualízalo y sigue sus instrucciones de reparación de certificados. Considera una regla por aplicación solo si se confirma que esa inspección causa el problema y la política lo permite.

```text
[ERROR] [ghostText] [2024-04-21T04:06:46.900Z] Error on ghost text request: (FetchError) unable to verify the first certificate
[ERROR] [certificates] [2024-04-21T04:06:46.901Z] Your current Copilot license doesn't support proxy connections with custom certificates. Please visit https://gh.io/copilot-network-errors to learn more. Original cause: {"type":"system","_name":"FetchError","code":"UNABLE_TO_VERIFY_LEAF_SIGNATURE"}
```

## No dejes desactivada la inspección SSL/TLS de ESET ni ignores permanentemente los errores de certificado. ESET advierte que desactivarla reduce el análisis del tráfico cifrado, y GitHub señala que ignorar errores de certificado puede crear riesgos de seguridad.

Error registrado

## Comprobación de conectividad

```powershell
curl.exe --verbose -i -L https://copilot-proxy.githubusercontent.com/_ping
```

Para probar mediante un proxy, sigue la sintaxis documentada por GitHub y añade `-x http://HOST:PUERTO`.

## Acerca de ESET

Comprobaciones seguras

> Antes de compartir registros, elimina credenciales, usuarios y contraseñas del proxy y datos personales.

## Referencias

- [GitHub Docs: Troubleshooting network errors](https://docs.github.com/en/copilot/how-tos/troubleshoot-copilot/troubleshoot-network-errors)
- [GitHub Docs: Copilot network settings](https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/network-settings)
- [GitHub Docs: Configure network settings for JetBrains IDEs](https://docs.github.com/en/copilot/how-tos/copilot-in-your-ide/set-up-copilot/configure-network-settings?tool=jetbrains)
- [ESET: Manage SSL/TLS protocol filtering](https://support.eset.com/en/kb3126-disable-ssl-filtering-in-eset-windows-products)

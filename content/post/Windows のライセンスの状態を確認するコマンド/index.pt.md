---
title: 'Como verificar o status de ativação da licença do Windows! Verifique facilmente com um único comando'
slug: "Windows のLicençaの状態を確認するComando"
date: "2025-04-14T00:41:45+09:00"
lastmod: "2026-11-25"
tags: ["Windows", "Licença", "Prompt de Comando"]
draft: false
image: "img_1.webp"
categories: ["pc-gadgets"]
description: 'Veja como consultar o canal da licença e o status de ativação do Windows com os comandos slmgr integrados (/dli, /dlv e /xpr) e por que a ativação não comprova o direito de uso da licença.'
---

# 【Windows】Como verificar o status da licença (OK com 1 comando)

Você já se perguntou se a sua licença do Windows está autenticada corretamente?

Para esses momentos, uma forma conveniente é o **método de verificar as informações da licença com um único comando** . Você pode verificar facilmente o status atual da sua licença simplesmente executando os passos abaixo.

## Comando para verificar o status da licença

Você pode exibir as informações da sua licença usando uma ferramenta de script embutida no Windows. O comando a ser usado está aqui:

```
slmgr /dli
```

Quando você executa este comando, algumas informações sobre a sua licença serão exibidas em uma janela.

## Como executar

1. Pesquise “cmd” no menu Iniciar e abra o Prompt de Comando. Não é necessário ter privilégios de administrador para `/dli`, `/dlv` ou `/xpr`.

2. Digite o seguinte no Prompt de Comando e pressione Enter:

   ```
   slmgr /dli
   ```

3. Após esperar alguns segundos, informações da licença como as seguintes serão exibidas.

   ![Janela de status da licença do Windows](img.webp)

## Principais informações exibidas

* Parte da chave do produto
* Canal da licença (como Retail ou OEM)
* Status da licença (os campos variam conforme a edição e o canal)

## E se você quiser saber informações mais detalhadas?

Também existem comandos como os seguintes:

* `slmgr /dlv` : Exibe informações mais detalhadas da licença
* `slmgr /xpr`: Exibe a data de expiração da ativação

`/xpr` mostra a data de expiração da ativação e é mais útil para clientes KMS; ativações Retail e MAK geralmente são permanentes. O `slmgr` não valida se a licença do Windows foi obtida legalmente. No Windows 11, também é possível verificar o status em Configurações > Sistema > Ativação.

## Resumo

O status da licença do Windows pode ser facilmente verificado com um único comando.

* **Verificação simples** : `slmgr /dli`
* **Verificação detalhada** : `slmgr /dlv`
* **Verificação da data de expiração** : `slmgr /xpr`

Se o status não for o esperado, consulte as Configurações de Ativação do Windows ou fale com o vendedor ou administrador da organização.

## Referências

- [Slmgr.vbs options for obtaining volume activation information](https://learn.microsoft.com/en-us/windows-server/get-started/activation-slmgr-vbs-options)
- [Activate Windows](https://support.microsoft.com/en-us/windows/activation/activate-windows)

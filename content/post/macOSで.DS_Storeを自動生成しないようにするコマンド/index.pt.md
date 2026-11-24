---
title: "Controlar a leitura de .DS_Store em compartilhamentos SMB no macOS"
slug: "macOSで.DS_Storeを自動生成しないようにするComando"
date: 2022-09-12T16:03:42+09:00
lastmod: "2026-11-24T00:00:00+09:00"
tags: ["macOS"]
draft: false
image: "img.webp"
categories: ["pc-gadgets"]
description: "Siga as instruções da Apple para desativar ou reativar a leitura de arquivos .DS_Store em compartilhamentos SMB no macOS. Isso não impede sua criação; saia da sessão e entre novamente após alterar a opção."
---
A Apple documenta esta preferência como uma forma de agilizar a navegação SMB: ela instrui o macOS a **não ler arquivos `.DS_Store` em compartilhamentos SMB**. Isso não impede a criação de novos arquivos nem exclui os existentes. A exibição e a ordenação no Finder podem mudar.

### Desativar a leitura em compartilhamentos SMB

Execute este comando no Terminal:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool TRUE
```

Encerre a sessão da conta do macOS e inicie-a novamente para aplicar a alteração. O Finder usará informações básicas em vez dos metadados de `.DS_Store` ao exibir as pastas.

### Reativar a leitura

Defina o valor como `FALSE` para restaurar o comportamento padrão:

```bash
defaults write com.apple.desktopservices DSDontWriteNetworkStores -bool FALSE
```

Depois, saia da sessão e entre novamente. A Apple apresenta essa opção como um ajuste de navegação SMB e informa que o artigo se destina a administradores de empresas e instituições de ensino. Consulte o [Suporte da Apple](https://support.apple.com/en-us/102064).

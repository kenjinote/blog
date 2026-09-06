---
title: "LoadIcon não precisa chamar DestroyIcon"
slug: "LoadIcon-nao-precisa-chamar-DestroyIcon"
date: 2024-04-19T01:55:17+09:00
tags: ["ícone", "LoadIcon", "DestroyIcon", "Programação Windows"]
draft: false
categories: ["Programação"]
---

# Sobre a necessidade de chamar DestroyIcon

É necessário chamar DestroyIcon nos seguintes casos:
 
- CreateIconFromResourceEx (se chamado sem a flag LR_SHARED)
- CreateIconIndirect 
- CopyIcon

Quando criado pelas funções acima.

- LoadIcon
- LoadImage (se usar a flag LR_SHARED)
- CopyImage (se usar a flag LR_COPYRETURNORG e o parâmetro hImage for um ícone compartilhado)
- CreateIconFromResource
- CreateIconFromResourceEx (se usar a flag LR_SHARED)

Ícones criados e carregados nos casos acima não devem chamar DestroyIcon.

### Referência
- [Função DestroyIcon (winuser.h)](https://learn.microsoft.com/pt-br/windows/win32/api/winuser/nf-winuser-destroyicon)

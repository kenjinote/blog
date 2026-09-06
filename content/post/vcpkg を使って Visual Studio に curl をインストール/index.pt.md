---
title: "【Para Iniciantes】Guia para Instalar libcurl (com suporte a OpenSSL) no Visual Studio usando vcpkg"
slug: "vcpkg を使って Visual Studio に curl をインストール"
date: 2025-07-07T21:46:08+09:00
tags: ["vcpkg", "curl", "Visual Studio", "C++"]
draft: false
image: "img.png"
categories: ["Ferramentas e Ambiente de Desenvolvimento"]
---

## Se você for usar libcurl (com suporte a OpenSSL) no Visual Studio, a instalação do vcpkg é fácil e recomendada

Quando se quer lidar com comunicação HTTP em C++, libcurl é frequentemente usado. Mas a compilação e o ajuste de dependências são surpreendentemente difíceis, não é mesmo?

O que é útil em momentos como esse é a ferramenta de gerenciamento de bibliotecas C++ da Microsoft, ** "vcpkg" ** .
Desta vez, introduziremos as etapas desde a introdução de libcurl (compatível com OpenSSL) usando cpkg até torná-lo fácil de usar no Visual Studio.

---

### Instalação do vcpkg (apenas para quem ainda não instalou)

Primeiro, vamos instalar o cpkg. Execute as etapas a seguir no PowerShell.

`powershell
git clone https://github.com/microsoft/vcpkg
cd vcpkg
.ootstrap-vcpkg.bat
`

※Se você ainda não tem o Git instalado, instale-o a partir do [Site oficial do Git](https://git-scm.com/).

---

### Instalação de libcurl (compatível com OpenSSL)

Em seguida, use vcpkg para instalar o libcurl. Para especificar a versão de 64 bits compatível com OpenSSL, execute o comando a seguir.

`powershell
vcpkg install curl[ssl] --triplet x64-windows
`

Ao executar este comando, as dependências necessárias (como OpenSSL) também são configuradas automaticamente.

---

### Configuração de integração com o Visual Studio

Para facilitar o uso de bibliotecas instaladas com vcpkg a partir do seu projeto do Visual Studio, defina as configurações de integração com o comando a seguir.

`powershell
vcpkg integrate install
`

Depois de configurado, #include <curl/curl.h> ficará automaticamente disponível nos seus projetos do Visual Studio e você não precisará mais definir caminhos de bibliotecas ou configurações de vinculador manualmente.

---

## Conclusão

Com isso, a preparação para instalar libcurl (compatível com OpenSSL) no Visual Studio está concluída.

* Ao usar vcpkg, você pode gerenciar dependências difíceis de uma só vez
* Instale facilmente libcurl com cpkg install curl[ssl] --triplet x64-windows
* A integração automática com o Visual Studio é possível com cpkg integrate install

Agora, basta incluir o cabeçalho no seu projeto e usar a API libcurl para iniciar o desenvolvimento.
Aproveite o útil vcpkg e aumente rapidamente a eficiência do seu desenvolvimento.

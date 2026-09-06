---
title: "Como instalar o Gemini CLI no Windows"
slug: "Como instalar o Gemini CLI no Windows"
date: 2025-07-13T23:49:56+09:00
tags: ["Gemini", "CLI", "Windows", "instalação", "desenvolvimento"]
draft: false
image: "img.png"
categories: ["PC・Gadgets"]
---

# [Para iniciantes] Como instalar o Gemini CLI no Windows

O "Gemini CLI" permite que você use a IA generativa do Google, "Gemini", a partir da linha de comando.
Neste artigo, explicaremos as etapas para instalar o Gemini CLI em um ambiente Windows da forma mais simples possível.

---

## 1. Preparação: Instalar o Node.js e npm

Primeiro, como o Gemini CLI é executado em um ambiente chamado "Node.js", você precisa instalar o seguinte:

* **Node.js** 
* **npm (Ferramenta de gerenciamento de pacotes incluída no Node.js)** 
* **npx (Ferramenta de execução de comandos incluída no npm)** 

Faça o download da versão do Node.js para Windows no site oficial abaixo (a versão LTS é recomendada):

👉 [Site Oficial do Node.js](https://nodejs.org/)

Após a conclusão da instalação, verifique se foi instalado corretamente com os seguintes comandos:

```powershell
node -v
npm -v
```

---

## 2. Inicie o PowerShell

Para usar o Gemini CLI no Windows, geralmente é usado o PowerShell.
Digite "PowerShell" no menu Iniciar para abri-lo.

---

## 3. Instale o Gemini CLI

Copie e cole o seguinte comando no PowerShell para executá-lo:

```bash
npx @google/gemini-cli
```

Este comando executa temporariamente o pacote Gemini CLI publicado pelo Google.
Você pode ser solicitado a realizar a configuração inicial e o login, se necessário.

* Observação: pode levar alguns minutos na primeira vez. Se ocorrer um erro, verifique novamente o Node.js e o seu ambiente de rede.

---

## 4. Instalação completa! O que fazer a seguir

O Gemini CLI agora está instalado no seu Windows.
A partir de agora, você poderá usar o Gemini na linha de comando para várias operações, como geração de texto e preenchimento de código.

Se você quiser verificar a documentação oficial ou a ajuda, também pode usar comandos como este:

```bash
npx @google/gemini-cli --help
```

---

## Resumo

Vamos revisar as etapas para instalar o Gemini CLI no Windows:

1. Instalar o Node.js e o npm
2. Iniciar o PowerShell
3. Executar `npx @google/gemini-cli`

E você está pronto!
Se quiser usar a IA generativa localmente, experimente estas etapas como referência.

---
title: "Tentando instalar o Qt Extension Pack no Visual Studio Code"
slug: "Visual Studio Code に Qt Extension Pack を入れてみた"
date: 2024-09-13T00:53:53+09:00
tags: ["Visual Studio Code", "Qt Extension Pack"]
draft: false
image: "img_1.png"
categories: ["ツール・開発環境"]
---

# Iniciando o desenvolvimento Qt no VSCode: Como instalar o Qt Extension Pack

Olá, aqui é o Kenji.
Desta vez, apresentarei "como configurar o ambiente de desenvolvimento Qt no Visual Studio Code (doravante VSCode)".

Recentemente, além do Qt Creator oficial, há um número crescente de pessoas que desejam desenvolver aplicativos Qt usando o VSCode, que é leve e altamente extensível.
Para essas pessoas, recomendo o **"Qt Extension Pack"** .
Basta instalar este pacote de extensões e você terá as principais extensões relacionadas ao Qt de uma só vez.

---

## Público-alvo

* Aqueles que desejam iniciar o desenvolvimento de aplicativos GUI usando Qt
* Aqueles que desejam desenvolver no VSCode em vez do Qt Creator
* Aqueles que têm preguiça de procurar extensões uma por uma

---

## Pré-requisitos

* O VSCode deve estar instalado
  ([Você pode baixá-lo gratuitamente no site oficial](https://code.visualstudio.com/))
* A própria biblioteca Qt deve estar instalada ([Site oficial do Qt](https://www.qt.io/))

---

## O que é o Qt Extension Pack?

O Qt Extension Pack é um pacote de extensões para o VSCode.
Ao instalá-lo, os seguintes recursos são adicionados automaticamente:

* Suporte para arquivos `.ui` (Qt Designer)
* Destaque de sintaxe para arquivos `.pro` e `.qrc`
* Conclusão de código C++, compilação e suporte a depuração para Qt
* Qt Resource Browser (referência de recursos)

---

## Instruções de Instalação

### 1. Abra o VSCode

Primeiro, inicie o VSCode.

### 2. Abra a visualização de Extensões

Clique na barra de atividades no lado esquerdo (ícone de blocos quadrados) para exibir as "Extensões".

Ou você pode pressionar o atalho
`Ctrl + Shift + X`.

### 3. Pesquise por "Qt Extension Pack"

Digite a seguinte palavra-chave na barra de pesquisa:

```
Qt Extension Pack
```

![img.png](img.png)

### 4. Clique no botão de Instalação

Quando o pacote de destino for exibido, clique no botão "Instalar".
Isso instalará várias extensões de uma só vez, como as seguintes:

* Qt Language Support
* QML Support
* Qt Designer Integration
* CMake Tools (essencial para desenvolvimento Qt compatível com CMake)

---

## Configuração adicional do projeto (Exemplo CMake + Qt)

Se você usar o Qt baseado no CMake, recomendamos combiná-lo com as seguintes extensões:

* [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
* [CMake Language Support](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)

Além disso, se você incluir a seguinte descrição em CMakeLists.txt, a integração com o Qt será tranquila:

```cmake
find_package(Qt6 REQUIRED COMPONENTS Widgets)
target_link_libraries(MyApp PRIVATE Qt6::Widgets)
```

---

## Bônus: Como abro os arquivos .ui?

Os arquivos `.ui` podem ser editados no Qt Designer.
No VSCode, você poderá clicar com o botão direito do mouse no arquivo `.ui` → selecionar `Open with Qt Designer` (o Qt Designer deve estar incluído na variável de ambiente `PATH`).

---

## Resumo

| Passo | Conteúdo                          |
| -- | --------------------------- |
| 1  | Iniciar o VSCode                    |
| 2  | Abrir o painel de extensões                  |
| 3  | Pesquisar por "Qt Extension Pack" |
| 4  | Clicar no botão de Instalação              |

Construir um ambiente Qt no VSCode tornou-se muito mais fácil do que antes.
Ele tem recursos suficientes como uma alternativa ao Qt Creator e é recomendado para quem quer trabalhar com leveza.

---

## Coleção de links recomendados

* [Site oficial do Qt](https://www.qt.io/)
* [Qt Extension Pack - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TheQtCompany.qt)
* [Site oficial do VSCode](https://code.visualstudio.com/)
* [Extensão CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)

---

## Por fim

No futuro, planejo prosseguir com o desenvolvimento utilizando ferramentas de UI do Qt e QML neste ambiente.
Na próxima vez, explicarei **como compilar e executar um aplicativo Hello World em Qt a partir do VSCode** .

Até logo!

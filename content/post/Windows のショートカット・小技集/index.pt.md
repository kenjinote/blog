---
title: "Atalhos e Dicas do Windows"
slug: "Windows のショートカット・小技集"
date: 2022-09-18T23:49:29+09:00
tags: ["Windows", "Dicas", "Atalhos"]
draft: false
image: "img.png"
categories: ["PC e Gadgets"]
---
Esta é uma coleção de pequenas dicas e atalhos úteis para o uso diário do Windows. Espero que seja útil para iniciantes.
Embora seja focado no Windows 11, a maioria também deve funcionar no Windows 10.

## Fechar janela
- `Alt + F4` com a janela ativa
- `Ctrl + W` com a janela ativa. Fecha a aba ou janela (apenas em aplicativos suportados)
- Dê um duplo clique no ícone à esquerda da barra de título da janela
- Clique no `×` na barra de título da janela

## Mostrar a área de trabalho
- `Win + D`. Pressione duas vezes para restaurar o estado original da janela. Muito útil quando você quer mostrar a área de trabalho por um instante.
- `Win + M`. Minimiza todos os aplicativos. Pressionar duas vezes não restaura.

## Digitação por voz
- `Win + H`. Inicia a digitação por voz. Para sair, pressione `Esc` ou `Win + H` novamente.

## Mostrar o menu de contexto clássico no Explorer
- Pressione `Shift + F10` ou a tecla de aplicativo. A tecla de aplicativo é a que fica no canto inferior direito do teclado.

## Capturar uma área da tela
- Você pode capturar uma área selecionada com `Win + Shift + S`.
- Você pode capturar a tela inteira com `Win + Print Screen` ou apenas `Print Screen`.
(Se você adicionar o `Win`, a imagem capturada será salva em `C:\Users\NomeDoUsuario\Pictures\Screenshots`.)
- Você pode capturar a janela atual com `Alt + Print Screen`.

## Iniciar aplicativos fixados na barra de tarefas
- Você pode iniciar os aplicativos fixados na barra de tarefas com `Win + Tecla numérica`.
  Por exemplo, pressionar `Win + 1` iniciará o primeiro aplicativo da esquerda na barra de tarefas.
- `Win + T` move o foco para os ícones da barra de tarefas. Pressionar `Win + T` várias vezes, ou usar `←` ou `→`, moverá a seleção, e pressionar `Enter` iniciará o aplicativo selecionado.

## Ampliar/Reduzir
- `Win + +` inicia a Lupa do Windows. Você pode ampliar/reduzir a tela usando `Win + + ou -`.
- Você pode ampliar/reduzir no Bloco de Notas ou navegadores com `Ctrl + + ou -` (apenas em aplicativos suportados).

## Bloquear o Windows
- `Win + L`
- `Ctrl + Alt + Del` → `Espaço` ou `Enter`

## Desligar o Windows
- Com a área de trabalho visível (usando `Win + M` ou `Win + D`) ou a barra de tarefas ativa (`Win + T` ou `Win + B`), pressione `Alt + F4`. Uma caixa de diálogo como a mostrada abaixo aparecerá; certifique-se de que "Desligar" esteja selecionado e pressione `Enter`.
  Também pode ser feito com `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_20.png](img_20.png)
- Você pode desligar usando `Win + X` → `U` → `U`.
- No Prompt de Comando ou em "Executar" (`Win + R`), digite `shutdown /s /t 0` para desligar. Adicionar `/f` forçará o desligamento.

## Reiniciar o Windows
- Com a área de trabalho visível (usando `Win + M` ou `Win + D`) ou a barra de tarefas ativa (`Win + T` ou `Win + B`), pressione `Alt + F4`. Uma caixa de diálogo aparecerá; pressione `↓` uma vez para selecionar "Reiniciar" e pressione `Enter`.
　Também pode ser feito com `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_21.png](img_21.png)
- Você pode reiniciar usando `Win + X` → `U` → `R`.
- Você pode reiniciar com `shutdown /r /t 0`. Adicionar `/f` forçará a reinicialização.

## Suspender (Dormir) o Windows
- Com a área de trabalho visível (usando `Win + M` ou `Win + D`) ou a barra de tarefas ativa (`Win + T` ou `Win + B`), pressione `Alt + F4`. Uma caixa de diálogo aparecerá; pressione `↑` uma vez para selecionar "Suspender" e pressione `Enter`.
  Também pode ser feito com `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_23.png](img_23.png)
- Em `Win + R` ou no Prompt de Comando, digite `rundll32.exe powrprof.dll,SetSuspendState` para hibernar.

## Sair do Windows (Logoff)
- Com a área de trabalho visível (usando `Win + M` ou `Win + D`) ou a barra de tarefas ativa (`Win + T` ou `Win + B`), pressione `Alt + F4`. Uma caixa de diálogo aparecerá; pressione `↑` duas vezes para selecionar "Sair" e pressione `Enter`.
  Também pode ser feito com `Win + R` → `Alt + F4` → `Alt + F4`.
  ![img_22.png](img_22.png)
- `Win + X` → `U` → `I`
- `Ctrl + Alt + Del` → 2 vezes `Tab` ou 2 vezes `↓` → `Enter` ou `Espaço`
- Você pode sair (fazer logoff) digitando `logoff`.

## Mover janelas com o teclado
- `Win + ←`: Mover para a esquerda
- `Win + →`: Mover para a direita
- `Win + ↑`: Mover para cima/Maximizar
- `Win + ↓`: Mover para baixo/Minimizar
- `Win + Shift + ← ou →`: Mover entre múltiplos monitores
- `Win + Alt + ← ou → ou ↑ ou ↓`: Mover a janela sem maximizar ou minimizar
- Com a janela não minimizada, pressione `Alt + Espaço` seguido de `M`, e então use as teclas de seta para mover.  
※ Como a janela segue o cursor do mouse, você pode resgatá-la mesmo se ela estiver fora da tela visível.

## Encerrar processos com o Gerenciador de Tarefas
![img_24.png](img_24.png)
1. Você pode abrir o Gerenciador de Tarefas com `Ctrl + Shift + Esc`.
2. Alterne entre as abas usando `Ctrl + Tab`.
3. Na aba `Detalhes`, após pressionar `Tab`, você pode buscar o processo digitando letras iniciais no teclado.
4. Com o nome do processo selecionado, pressione a tecla `Delete` seguida de `Enter` para encerrá-lo.

## Encerrar processos por nome via comando
- Você pode encerrar um processo usando `taskkill /f /im NomeDoProcesso`.
Por exemplo, `taskkill /f /im explorer.exe` encerrará o Explorer.

## Iniciar várias instâncias do mesmo programa a partir da barra de tarefas
- Segure `Shift` e clique com o botão esquerdo do mouse em um ícone na barra de tarefas para abrir outra instância do mesmo programa (apenas para aplicativos que suportam múltiplas instâncias).

## Executar programas como Administrador
- Segure `Ctrl + Shift` ao clicar em um programa para executá-lo com privilégios de Administrador.

## Abrir o Explorador de Arquivos (Explorer)
- Pressione `Win + E` para abrir o Explorador de Arquivos.
- Pressione `Win + R` para abrir "Executar", digite `explorer` e pressione `Enter`.
- Pressione `Ctrl + Shift + N` para criar uma nova pasta.

## Abrir o Prompt de Comando no local atual no Explorer
- No Windows 11, você pode abrir o Prompt de Comando selecionando "Abrir no Terminal" no menu do botão direito.
- Alternativamente, digite `cmd` na barra de endereços do Explorer e pressione `Enter` para abrir o Prompt de Comando.

## Mostrar histórico da área de clipboard (área de transferência)
- `Win + V` mostra o histórico da área de transferência.
Você pode selecionar textos ou imagens copiados anteriormente para copiá-los novamente.

## Executar (Arquivo)
![img_28.png](img_28.png)
- `Win + R` abre a caixa de diálogo "Executar".

Abaixo estão alguns comandos que podem ser usados em "Executar" ou no Prompt de Comando.

## Abrir o Edge
![img_18.png](img_18.png)
- Digite `msedge` e pressione `Enter`

## Abrir o Internet Explorer 11 (IE11)
![img_25.png](img_25.png)
- Digite `powershell.exe -Command "(New-Object -ComObject InternetExplorer.Application).Visible = $true"` e pressione `Enter`

## Abrir o Terminal
![img_19.png](img_19.png)
- Digite `wt` e pressione `Enter`

## Abrir o Painel de Controle
![img_15.png](img_15.png)
- Digite `control` e pressione `Enter`
- Também pode ser aberto com `explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}`.

## Iniciar o Bloco de Notas
![img_4.png](img_4.png)
- Digite `notepad` e pressione `Enter`  

## Iniciar a Calculadora
![img_5.png](img_5.png)
- Digite `calc` e pressione `Enter`

## Iniciar o Paint
![img_6.png](img_6.png)
- Digite `mspaint` e pressione `Enter`  

## Iniciar o PowerShell
![img_7.png](img_7.png)
- Digite `powershell` e pressione `Enter`  

## Iniciar o Visual Studio Code
![img_8.png](img_8.png)
- Digite `code` e pressione `Enter`

## Iniciar o Excel
![img_9.png](img_9.png)
- Digite `excel` e pressione `Enter`  
※ Apenas se o Excel estiver instalado.

## Abrir o Word
![img_10.png](img_10.png)
- Digite `winword` e pressione `Enter`  
※ Apenas se o Word estiver instalado.

## Abrir o PowerPoint
![img_11.png](img_11.png)
- Digite `powerpnt` e pressione `Enter`  
  ※ Apenas se o PowerPoint estiver instalado.

## Abrir a Configuração do Sistema
![img_1.png](img_1.png)
- Digite `msconfig` e pressione `Enter`  

## Abrir as Propriedades do Sistema
![img_2.png](img_2.png)
- Digite `sysdm.cpl` e pressione `Enter`

## Abrir informações sobre o Windows
![img_27.png](img_27.png)
- Digite `winver` e pressione `Enter`

## Abrir o Teclado Virtual
![img_14.png](img_14.png)
- Digite `osk` e pressione `Enter`

## Abrir o WordPad
![img_12.png](img_12.png)
- Digite `wordpad` ou `write` e pressione `Enter`

## Abrir o Editor do Registro
![img_13.png](img_13.png)
- Digite `regedit` e pressione `Enter`

## Abrir Programas e Recursos
- Digite `explorer.exe shell:::{7b81be6a-ce2b-4676-a29e-eb907a5126c5}` e pressione `Enter`

## Abrir Propriedades do Teclado
- Digite `explorer.exe shell:::{725BE8F7-668E-4C7B-8F90-46BDB0936430}` e pressione `Enter`

## Abrir Propriedades do Mouse
![img_16.png](img_16.png)
- Digite `explorer.exe shell:::{6C8EEC18-8D75-41B2-A177-8831D59D2D50}` e pressione `Enter`

## Abrir Configurações de Som
![img_3.png](img_3.png)
- Digite `explorer.exe shell:::{F2DDFC82-8F12-4CDD-B7DC-D4FE1425AA4D}` e pressione `Enter`

## Abrir Contas de Usuário
- Digite `explorer.exe shell:::{60632754-c523-4b62-b45c-4172da012619}` e pressione `Enter`

## Copiar o texto de caixas de mensagem padrão
![img_26.png](img_26.png)
- Você pode copiar o texto de uma caixa de mensagem padrão com `Ctrl + C`.
Se você copiar a caixa de mensagem acima, o seguinte será copiado para a área de transferência:
```
[Window Title]
WordPad

[Main Instruction]
Deseja salvar as alterações em Documento?

[Salvar (S)] [Não Salvar (N)] [Cancelar]
```

## Armazenar a saída do Prompt de Comando na área de transferência
Adicionar ` | clip` (pipe+clip) ao final de um comando, como `echo "hello" | clip`, copia a saída padrão para a área de transferência.

## Saída de texto da hierarquia de pastas
No Prompt de Comando, você pode gerar a hierarquia de pastas em formato de árvore usando o comando `tree`.

Exemplo de saída:
```
C:.
├─.idea
│  └─libraries
├─binaryeditorbz
├─blog
│  ├─archetypes
│  ├─content
│  ├─data
│  ├─layouts
│  ├─static
│  └─themes
│      └─PaperMod
│          ├─.git
│          │  ├─branches
│          │  ├─hooks
│          │  ├─info
│          │  ├─logs
│          │  │  └─refs
│          │  │      ├─heads
│          │  │      └─remotes
│          │  │          └─origin
│          │  ├─objects
│          │  │  ├─info
│          │  │  └─pack
│          │  └─refs
│          │      ├─heads
│          │      ├─remotes
│          │      │  └─origin
│          │      └─tags
│          ├─.github
│          │  ├─ISSUE_TEMPLATE
│          │  └─workflows
│          ├─assets
│          │  ├─css
│          │  │  ├─common
│          │  │  ├─core
│          │  │  ├─extended
│          │  │  ├─hljs
│          │  │  └─includes
│          │  └─js
│          ├─i18n
│          ├─images
│          └─layouts
│              ├─partials
│              │  └─templates
│              ├─shortcodes
│              └─_default
│                  └─_markup
(omitido)
```

## Referências
- [Atalhos de teclado no Windows](https://support.microsoft.com/ja-jp/windows/windows-%E3%81%AE%E3%82%AD%E3%83%BC%E3%83%9C%E3%83%BC%E3%83%89-%E3%82%B7%E3%83%A7%E3%83%BC%E3%83%88%E3%82%AB%E3%83%83%E3%83%88-dcc61a57-8ff0-cffe-9796-cb9706c75eec)

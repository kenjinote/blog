---
title: "Windows 11: verificar a Inicialização Rápida quando a escala muda"

slug: "Múltiplos Monitoresで毎回起動時にDPIの設定がリセットされてしまうときの対処法"
date: 2024-04-29T19:42:20+09:00
lastmod: "2026-11-24T00:00:00+09:00"

tags: ["Vários monitores", "DPI", "Painel de controle"]
draft: false
image: "img.webp"
categories: ["it-technology"]
description: "Etapa de diagnóstico cautelosa no Windows 11: desative temporariamente a Inicialização Rápida, teste desligar e ligar e restaure a opção se não ajudar."
---
A Inicialização Rápida salva a sessão do kernel e o estado dos drivers em um arquivo de hibernação durante o desligamento para acelerar a próxima inicialização. Desativá-la pode deixar a inicialização mais lenta. A documentação da Microsoft não a identifica como causa da redefinição de escala em vários monitores; use estas etapas como teste temporário, não como solução comprovada.

## Alterar a configuração temporariamente

1. Abra o Painel de Controle e selecione **Opções de Energia**.
2. Abra **Escolher a função dos botões de energia**.
3. Clique em **Alterar configurações não disponíveis no momento** (pode exigir acesso de administrador).
4. Desmarque **Ligar inicialização rápida (recomendado)** e clique em **Salvar alterações**.
5. Escolha **Desligar**, ligue o PC novamente e verifique se a escala foi mantida. Faça o teste desligando e ligando; **Reiniciar** não usa a Inicialização Rápida.

Se não ajudar, volte à mesma tela e reative a opção. Os nomes dos menus podem variar conforme o idioma do Windows e as atualizações.

## Referências da Microsoft

- [Shut down, sleep, or hibernate your PC — Microsoft Support](https://support.microsoft.com/en-us/windows/experience/power-battery/shut-down-sleep-or-hibernate-your-pc)
- [System power states — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states)
- [Distinguishing Fast Startup from Wake-from-Hibernation — Microsoft Learn](https://learn.microsoft.com/en-us/windows-hardware/drivers/kernel/distinguishing-fast-startup-from-wake-from-hibernation)

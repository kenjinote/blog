---
title: "Copilot ou IA local? Decida com base em dados e medições"
slug: "hybrid-ai-development-workflow"
date: "2026-09-11T21:00:00+09:00"
lastmod: "2026-11-23T12:00:00+09:00"
description: "Escolha ferramentas na nuvem como GitHub Copilot ou modelos locais conforme políticas de dados, qualidade, latência, custo e hardware."
image: "img/eyecatch.jpg"
categories: ["programming", "ai", "productivity"]
tags: ["GitHub Copilot", "Local AI", "Workflow", "Privacy"]
---

# [Copilot ou IA local? Decida com base em dados e medições](https://kenji.blog/p/hybrid-ai-development-workflow/)

Assistentes de programação vão da conclusão no IDE a edições feitas por agentes. Não presuma que a nuvem é mais capaz e o local mais seguro. Verifique os dados enviados, os termos aplicáveis, a qualidade nas tarefas, a latência e o custo operacional.

Este guia usa documentação oficial conferida em 23 de novembro de 2026. Produtos, modelos, configurações e políticas mudam; reveja os links e as regras da organização antes de adotar uma solução.

## Nuvem e inferência local têm fluxos de dados diferentes

Dependendo do modelo e do recurso do IDE, serviços na nuvem como o GitHub Copilot podem enviar prompts, trechos de código e contexto relevante do repositório. A política atual do GitHub diz que dados de interação de planos individuais do Copilot podem ser usados para treinar e aprimorar modelos, com opção de desativação nas configurações pessoais. Também diz que dados de clientes Business e Enterprise não são usados para treinamento sem autorização do cliente. Confira plano, hospedagem do modelo, recurso e políticas do administrador.

- [Políticas do GitHub Copilot para assinantes individuais](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies)
- [Hospedagem de modelos e tratamento de dados do GitHub Copilot](https://docs.github.com/en/copilot/reference/ai-models/model-hosting)

Na inferência local, o modelo roda no dispositivo e as entradas podem permanecer nele. Escolher um modelo local não garante uma configuração totalmente offline. Verifique telemetria e sincronização da extensão, ferramentas externas e tráfego de rede ao baixar modelos. O Continue explica como preparar a extensão e o modelo previamente e desativar telemetria anônima para uso offline.

- [Usar Continue sem conexão à Internet](https://docs.continue.dev/guides/running-continue-without-internet)

O Ollama oferece uma API local em `http://localhost:11434` e uma API hospedada na nuvem em `https://ollama.com/api`, que exige uma chave. Usar Ollama não significa automaticamente que a inferência seja local. Confira o endpoint configurado. Se disponibilizar um servidor local na rede, projete controles de acesso à parte.

- [Endpoints e uso da API Ollama](https://docs.ollama.com/api/introduction)

## Escolha o caminho conforme a tarefa e a classificação dos dados

Comece pela classificação de dados e pela política de IA da organização. Defina quais códigos, registros, projetos e credenciais podem sair do ambiente aprovado. Nunca coloque segredos em prompts, mesmo com modelo local; substitua-os por valores de teste. Para serviços na nuvem, verifique também o uso para treinamento por plano, retenção, monitoramento de abuso, região, controles administrativos e transferência aos provedores dos modelos.

- Autocompletar rotineiro, comentários ou rascunhos de testes: confira qualidade, latência, integração ao IDE e dados enviados; use recurso de nuvem aprovado ou modelo local pequeno.
- Resumir ou editar código interno: confira escopo da entrada, verificação dos resultados, contrato e retenção; use nuvem aprovada pela organização ou ambiente local controlado.
- Código confidencial ou regulamentado: confira transmissão externa, registros, perímetro de rede e auditoria; exija ambiente local isolado que atenda à política e tenha aprovação organizacional.
- Projetos extensos ou depuração difícil: avalie qualidade, contexto, permissões de ferramentas e custo; use nuvem ou modelo hospedado internamente que cumpra os requisitos.
- Trabalho sem Internet: prepare downloads, tráfego da extensão, atualizações e correções; valide a configuração offline.

Esses exemplos não são uma classificação de desempenho. Servem para reduzir as opções conforme as regras da organização e testes de tarefas.

## Meça qualidade, latência e custo nas mesmas tarefas

Crie um conjunto pequeno de testes com critérios de sucesso, falhas e método de pontuação. Dê aos candidatos o mesmo código e instruções e registre ID do modelo, extensão, data e configurações. Compare precisão, testes aprovados, consistência com o projeto existente, recusas seguras e tempo de correção. Faça várias tentativas, pois as respostas variam. Um desenvolvedor deve revisar o código importante e executar seus testes.

Meça separadamente o tempo até a primeira saída e até a conclusão total. Inclua uso na nuvem, assinaturas, novas tentativas e revisão, além de compra, eletricidade e manutenção do hardware local. Velocidade e qualidade locais dependem de tamanho do modelo, quantização, contexto, GPU/memória e ajustes do IDE. Não decida apenas pelo número de parâmetros ou uma estimativa de VRAM: teste no seu hardware.

## Passos mínimos para testar um modelo local

Instale Ollama. No catálogo, confira licença, tamanho do download e recursos; baixe a tag exata desejada:

```sh
ollama pull <model-name:tag>
```

O formato atual de configuração do Continue pode registrar Ollama assim. Substitua `<MODEL_ID>` pelo ID baixado exibido por `ollama list`.

```yaml
name: Local coding model
version: 0.0.1
schema: v1
models:
  - name: Local model
    provider: ollama
    model: <MODEL_ID>
    apiBase: http://localhost:11434
    roles:
      - chat
```

Chamadas a ferramentas, entradas de imagem e limites de contexto variam por modelo. Teste o funcionamento real mesmo que o IDE detecte os recursos automaticamente. Comece com permissões mínimas. Agentes que editam arquivos ou executam comandos devem exigir revisão e aprovação humana. Considere instruções maliciosas em código de fontes externas.

- [API Ollama](https://docs.ollama.com/api/introduction)
- [Configuração Ollama no Continue](https://docs.continue.dev/customize/model-providers/top-level/ollama)
- [Biblioteca de modelos Ollama](https://ollama.com/library)

## Comece pequeno e reavalie quando as condições mudarem

Escolha uma tarefa de baixo risco e compare um recurso de nuvem aprovado com um modelo local no mesmo conjunto de testes. Analise qualidade, tempo de correção, latência, custo e destino dos dados; defina regras por tarefa com a equipe. Reveja a política e os testes se o modelo, plano, extensão ou contrato mudar.

A segurança não depende apenas de ser nuvem ou local. Entenda o caminho de processamento, minimize as entradas e teste em um ambiente aprovado.

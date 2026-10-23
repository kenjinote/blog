---
title: "A diferença essencial entre XSS e CSRF e defesas modernas"
description: "Como as duas maiores vulnerabilidades de aplicações Web são exploradas."
slug: cross-site-scripting-xss-csrf-security
categories:
  - software-development
  - security
tags:
  - tech
  - security
  - xss
  - csrf
  - web-security
image: eyecatch.jpg
date: 2026-09-27T23:49:42+09:00
lastmod: 2026-10-24T02:00:00+09:00
---

## Introdução

Em aplicações Web modernas, a segurança não é apenas uma funcionalidade adicional, mas um dos elementos mais importantes que formam a base do sistema. Entre eles, **XSS (Cross-Site Scripting)** e **CSRF (Cross-Site Request Forgery)** são vulnerabilidades graves com um longo histórico e que ainda são encontradas em muitas aplicações Web. Eles são frequentemente confundidos, mas tanto seus mecanismos de ataque quanto as medidas de defesa contra eles são fundamentalmente diferentes.

Neste artigo, desvendaremos as diferenças essenciais entre XSS e CSRF, como os invasores exploram essas vulnerabilidades e as defesas modernas que os desenvolvedores devem implementar, com explicações detalhadas incluindo a evolução histórica.

---

## 1. As profundezas do XSS (Cross-Site Scripting)

O XSS é um método de ataque onde um invasor injeta scripts maliciosos (principalmente JavaScript) em uma página Web, fazendo com que o script seja executado nos navegadores de outros usuários que visitam essa página. A essência deste ataque reside no fato de que "dados não confiáveis são interpretados como código executável sem passar por processamento adequado".

### 3 tipos principais de XSS

O XSS pode ser classificado pela forma como os dados são armazenados ou refletidos e pelo local onde ocorre a interpretação insegura. As categorias não são mutuamente exclusivas: dados armazenados ou refletidos também podem ser processados de modo inseguro no cliente.

#### 1. Stored XSS (XSS Armazenado)
O XSS armazenado pode afetar vários visitantes. O script do invasor fica armazenado no servidor, por exemplo, em um banco de dados ou sistema de arquivos. Quando um usuário visita uma página que contém esses dados, o script é enviado ao navegador e executado. A gravidade depende dos privilégios e do contexto de execução.
*   **Locais típicos de ocorrência:** Seções de comentários, fóruns de discussão, perfis de usuários, recursos de avaliação, etc.
*   **Ameaça:** O escopo do impacto é muito amplo, e todos os usuários que abrirem a página podem ser vítimas.

#### 2. Reflected XSS (XSS Refletido)
O Reflected XSS ocorre quando um script malicioso não é salvo no servidor, mas é enviado como parte de uma requisição (como parâmetros de URL ou dados de formulário) e é incluído "refletido" como está na resposta do servidor.
*   **Locais típicos de ocorrência:** Páginas de resultados de busca, exibição de mensagens de erro, transferência de dados entre etapas, etc.
*   **Método de ataque:** Os invasores realizam o ataque fazendo com que os usuários cliquem em URLs que contêm parâmetros maliciosos (usando e-mails de phishing ou redes sociais).

#### 3. DOM-based XSS
O XSS baseado em DOM ocorre quando o JavaScript do cliente processa dados não confiáveis por meio de um sink inseguro. Os dados também podem ter passado por um servidor; o ponto determinante é que o processamento inseguro ocorre no cliente.
*   **Mecanismo:** Ocorre quando o JavaScript da aplicação lê dados de fontes que o invasor pode controlar, como `window.location` ou `document.referrer`, e os passa diretamente para pontos de execução (sinks) perigosos, como `innerHTML` ou `eval()`.
*   **Ameaça:** Muitas vezes não deixa rastros nos logs do servidor, tornando difícil a detecção por WAFs (Web Application Firewalls) e afins.

### Danos causados pelo XSS e técnicas de execução de scripts em contexto

Quando o XSS é bem-sucedido, o script do invasor é executado no navegador do usuário com a mesma origem (privilégios) do site. Isso leva aos seguintes danos graves:

1.  **Sequestro de sessão (Session Hijacking):** Se um cookie de autenticação não tiver `HttpOnly`, o invasor poderá roubar seu ID de sessão por meio de `document.cookie`. Mesmo com `HttpOnly`, o XSS ainda pode enviar requisições autenticadas em nome do usuário.
2.  **Execução de ações não autorizadas:** Faz com que qualquer operação dentro da aplicação (mudança de senha, transferência de dinheiro, envio de mensagens, etc.) seja executada em segundo plano com as permissões do usuário.
3.  **Phishing:** Renderiza um formulário de login falso no DOM para roubar as credenciais do usuário diretamente.
4.  **Distribuição de malware:** Redireciona o navegador do usuário para kits de exploração, infectando o PC com malware.

### Defesas modernas contra XSS

Para prevenir o XSS, uma abordagem de Defesa em Profundidade (Defense in Depth) é essencial.

#### 1. Tratamento de escape (Output Encoding) de acordo com o contexto
A medida mais fundamental e importante é o processamento de escape (codificação) que converte a entrada do usuário em strings inofensivas ao emiti-la em uma página da Web. O importante é escolher o método de escape apropriado de acordo com o **contexto (corpo HTML, atributos HTML, dentro de JavaScript, dentro de CSS, dentro de URL, etc.)** onde os dados são gerados. Muitos frameworks da web modernos (React, Vue, Angular, etc.) realizam escape de HTML por padrão, mas ainda requerem atenção.

#### 2. Introdução de CSP (Content Security Policy)
O CSP é um mecanismo de defesa muito poderoso contra XSS, definindo no cabeçalho HTTP uma lista branca (whitelist) de recursos que o navegador está autorizado a carregar e executar.
```http
Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com;
```
Com isso, mesmo que um invasor consiga injetar um script inline `<script>alert(1)</script>`, sua execução será bloqueada pelo CSP.

#### 3. Utilização do atributo Cookie HttpOnly
Ao adicionar o atributo `HttpOnly` a cookies que armazenam IDs de sessão, etc., esses cookies não poderão ser acessados a partir do JavaScript (ex: `document.cookie`). Isso não impede que o XSS em si ocorra, mas é uma medida de mitigação importante que reduz significativamente o risco de sequestro de sessão por meio de XSS.

---

## 2. A essência do CSRF (Cross-Site Request Forgery)

CSRF é um ataque no qual um invasor induz um usuário a visitar um site armadilha, forçando-o a enviar requisições não intencionais a outro site onde o usuário já está autenticado (logado).

Enquanto o XSS "executa scripts maliciosos dentro do navegador", o CSRF é fundamentalmente diferente no sentido de que "explora o comportamento padrão do navegador (envio automático de cookies) para enviar requisições maliciosas".

### Mecanismo do CSRF: Exploração do "envio automático de cookies"

O navegador anexa cookies automaticamente quando suas condições de envio são atendidas, inclusive em algumas requisições acionadas por imagens ou formulários de outro site. Porém, `SameSite`, `Secure`, Domain, Path e as restrições do navegador podem impedir o envio.

**Cenário de ataque:**

Este exemplo didático pressupõe uma aplicação vulnerável: o cookie de autenticação permite envio entre sites com `SameSite=None; Secure`, e não há validação de tokens CSRF nem verificações de Origin. `bank.example` e `attacker.invalid` são domínios reservados de sites distintos.
1.  O usuário faz login no site do banco (`bank.example`) e recebe um cookie de sessão.
2.  O usuário navega para o site armadilha do invasor (`attacker.invalid`) em outra guia.
3.  O site armadilha possui um formulário oculto e um script de envio automático configurado como este:
    ```html
    <form action="https://bank.example/transfer" method="POST" id="csrf-form">
        <input type="hidden" name="toAccount" value="ATTACKER_ACCOUNT">
        <input type="hidden" name="amount" value="1000000">
    </form>
    <script>document.getElementById('csrf-form').submit();</script>
    ```
4.  O navegador envia uma requisição POST para `bank.example`. Neste momento, **o cookie de sessão do site do banco é adicionado automaticamente.**
5.  O servidor do banco o processa como uma solicitação de um usuário legítimo, pois contém um cookie de sessão válido, e a transferência fraudulenta é executada.

### Evolução histórica das defesas contra CSRF e práticas mais recentes

Para evitar o CSRF, é necessário verificar se a requisição "foi enviada da página legítima pretendida".

#### 1. Tokens CSRF (Anti-CSRF Tokens): Defesa tradicional e confiável
A defesa mais confiável e amplamente utilizada há mais tempo é o Token CSRF (Padrão Synchronizer Token).
*   O servidor gera um token aleatório e imprevisível para cada sessão e o salva no lado do servidor (como na sessão).
*   Incorpore este token como um campo oculto (hidden) no formulário HTML enviado ao cliente.
*   Ao enviar o formulário, o servidor compara o token enviado com o token armazenado no servidor e processa a solicitação apenas se eles corresponderem.
Os invasores podem forçar o envio de requisições a partir do site armadilha, mas não podem ler a página do site de destino para obter o token correto (devido à Política de Mesma Origem (Same-Origin Policy)), portanto, o ataque falha.

#### 2. Padrão Double Submit Cookie
Esta é uma técnica frequentemente usada em APIs que não possuem estado (sessões) no lado do servidor.
*   O servidor gera um token aleatório e o envia ao cliente como um cookie.
*   O JavaScript do cliente lê o valor desse cookie e o define no cabeçalho da requisição (ex: `X-CSRF-Token`) para enviá-lo.
*   O servidor verifica se o valor do token no cookie e o valor do token no cabeçalho correspondem.
Os passos acima descrevem uma simples comparação de igualdade. Não é recomendável depender apenas dela quando um invasor pode injetar cookies. Prefira a proteção integrada do framework. Ao usar Double Submit, valide um token Signed Double Submit autenticado por HMAC com um segredo do servidor e vinculado à sessão autenticada atual. APIs com cabeçalhos personalizados também devem evitar permitir CORS com credenciais para origens não confiáveis.

#### 3. Atributo SameSite Cookie: Defesa poderosa por navegadores modernos
O atributo `SameSite` controla o envio de cookies entre sites e é uma camada de defesa. Em aplicações de uso geral, combine-o com tokens CSRF ou validação de Origin, em vez de tratá-lo como substituto.

*   `SameSite=Strict`: O cookie não será enviado em nenhuma requisição de origem cruzada, incluindo navegações de nível superior, como cliques em links. É o mais seguro, mas pode afetar a experiência do usuário (UX), como não manter o status de login ao clicar em um link de outro site.
*   `SameSite=Lax`: Os cookies não são enviados em requisições entre sites, como carregamento de imagens ou requisições POST, mas são enviados em navegações de nível superior por meio de cliques em links (requisições GET). É o comportamento padrão em muitos navegadores atuais. Isso pode evitar a maioria das vulnerabilidades CSRF por envios de formulários POST maliciosos.
*   `SameSite=None`: Remove a restrição de SameSite ao envio entre sites e exige `Secure`. As demais condições de envio e restrições do navegador continuam valendo.

SameSite distingue sites, não origens: subdomínios irmãos do mesmo domínio registrável podem ser considerados do mesmo site. Lax também não protege um endpoint que altera estado por GET. Use métodos HTTP adequados para mudanças de estado e validação CSRF no servidor. Como o comportamento Lax padrão pode ter exceções, configure explicitamente os atributos necessários.

---

## Correlação entre XSS e CSRF e Resumo

A figura abaixo mostra a diferença no fluxo de ataques.

```mermaid
graph TD
    subgraph Ataque XSS
        A["Invasor"] -- "Injeção de script malicioso" --> B["Servidor Web"]
        B -- "Página com o script" --> C["Navegador da vítima"]
        C -- "Roubo do ID de sessão (sem HttpOnly)" --> A
    end

    subgraph Ataque CSRF
        D["Vítima"] -- "Login" --> E["Servidor Web"]
        D -- "Visualização" --> F["Site armadilha do invasor"]
        F -- "Requisição forçada (com Cookie)" --> E
    end
```

XSS e CSRF são vulnerabilidades diferentes, mas **se o XSS existir, a maioria das defesas contra CSRF será invalidada**. Isso porque os scripts executados por XSS estão sendo executados em páginas legítimas, tornando possível ler tokens CSRF e enviar requisições da mesma origem.

Portanto, para garantir a segurança de uma aplicação Web, é necessária a construção de uma base sólida: primeiro, conter completamente o XSS (com escapes adequados e CSP), e então implementar as defesas contra CSRF (Cookies SameSite e tokens CSRF).

É importante que os desenvolvedores não confiem cegamente nos recursos de segurança fornecidos por frameworks, mas que entendam os mecanismos essenciais dessas vulnerabilidades e projetem a defesa em camadas adequadas.

## Referências

- [OWASP: XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP: CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

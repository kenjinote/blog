---
title: "OAuth 2.0 e OIDC: autenticação, autorização e validação de tokens"
description: "Autenticação e autorização, papéis de OAuth 2.0 e OIDC, código de autorização com PKCE e validação do token de ID com fórmulas e exemplos de JavaScript e Python."
slug: "oauth2-oidc-authentication-authorization-difference"
date: "2026-09-22T08:00:00+09:00"
lastmod: "2026-10-27"
image: "eyecatch.jpg"
categories:
    - "security"
tags:
    - "oauth2"
    - "oidc"
    - "authentication"
    - "authorization"
    - "iam"

---

OAuth 2.0 é um framework de autorização que concede acesso limitado a aplicações. OpenID Connect (OIDC) acrescenta um mecanismo para comunicar ao cliente o resultado da autenticação do usuário final.

Este artigo distingue autenticação e autorização, as finalidades dos tokens, código de autorização com PKCE e validação do token de ID. O código ilustra operações específicas; não implementa um login completo. Em produção, use uma biblioteca OIDC e uma configuração do provedor adequadas aos seus requisitos.

## 1. Autenticação e autorização

### Autenticação / AuthN

A autenticação verifica a identidade de um usuário ou sistema com base nas evidências apresentadas. Uma analogia é a conferência do crachá de um funcionário na recepção de uma empresa.

### Autorização / AuthZ

A autorização determina quais operações uma entidade pode realizar e quais recursos pode acessar. Confirmar que alguém é funcionário não significa permitir que entre em todas as salas de servidores.

| Item | Autenticação | Autorização |
| --- | --- | --- |
| Pergunta | Quem é? | O que é permitido? |
| Sigla | AuthN | AuthZ |
| Mecanismo tratado aqui | OIDC comunica o resultado da autenticação | OAuth 2.0 concede acesso limitado |
| Exemplo de token | Token de ID do OIDC | Token de acesso do OAuth 2.0 |

Nem todo mecanismo de autenticação emite um token de ID. OAuth 2.0 também não define todo o controle de acesso de uma aplicação. Depois de receber um token, a API ainda precisa verificar as permissões exigidas pelo recurso e pela operação específicos.

OAuth 2.0, por si só, não padroniza como o cliente verifica o resultado da autenticação do usuário final. Receber um token de acesso não basta para estabelecer um login: use um protocolo, como OIDC, que permita validar esse resultado.

## 2. Papéis e concessões do OAuth 2.0

### 2.1 Acesso limitado

OAuth 2.0 permite que um cliente obtenha um token de acesso em nome do proprietário do recurso ou em seu próprio nome. Delegar acesso sem entregar a senha do usuário ao cliente é uma característica importante do fluxo de código de autorização.

### 2.2 Quatro papéis

1. **Proprietário do recurso (Resource Owner)**: entidade capaz de autorizar o acesso a um recurso protegido. Não precisa ser uma pessoa.
2. **Cliente (Client)**: aplicação que utiliza recursos protegidos.
3. **Servidor de autorização (Authorization Server)**: servidor que verifica a autorização, a autenticação do cliente e outras condições do fluxo aplicável, e emite tokens.
4. **Servidor de recursos (Resource Server)**: servidor que valida tokens e permissões e fornece recursos protegidos.

### 2.3 Principais tipos de concessão

#### Código de autorização (Authorization Code Grant)

A resposta de autorização retorna um código de curta duração, que é trocado por um token de acesso no endpoint de tokens. Tanto **clientes confidenciais**, capazes de proteger credenciais em um servidor, quanto **clientes públicos**, como SPAs e aplicativos nativos, podem usar esse fluxo com PKCE. Inserir um segredo do cliente em código distribuído ou no navegador não permite mantê-lo em sigilo.

#### Concessão implícita (Implicit Grant)

Essa concessão retorna um token de acesso diretamente na resposta de autorização. Há riscos de vazamento, injeção e reutilização de tokens. A RFC 9700 estabelece que os clientes NÃO DEVERIAM utilizá-la (SHOULD NOT), a menos que os riscos especificados sejam mitigados. Em uma configuração nova, escolha código de autorização com PKCE. Não interprete essa recomendação como uma proibição idêntica para todos os tipos de resposta do OIDC.

#### Credenciais de senha do proprietário do recurso (ROPC)

Nessa concessão, o cliente recebe diretamente a senha do usuário. Embora a RFC 6749 a descreva, as orientações de segurança atualizadas da RFC 9700 determinam que ela **NÃO DEVE ser usada (MUST NOT)**. A migração de sistemas legados não deve ser apresentada como uma exceção recomendada.

#### Credenciais do cliente (Client Credentials Grant)

Um cliente confidencial se autentica para obter um token. Ele pode acessar recursos sob seu controle ou recursos de outro proprietário mediante um acordo prévio com o servidor de autorização. Esse fluxo costuma atender à comunicação entre sistemas sem interação do usuário final; o cliente não se torna necessariamente o proprietário do recurso.

### 2.4 Código de autorização e PKCE

PKCE (Proof Key for Code Exchange) vincula o cliente que inicia uma solicitação de autorização ao cliente que troca o código por tokens, ajudando a proteger contra interceptação e injeção de códigos. É obrigatório para clientes públicos e também recomendado para clientes confidenciais. Não substitui a autenticação exigida de um cliente confidencial.

A cada transação de autorização, o cliente gera um novo `code_verifier` secreto. A RFC 7636 especifica de 43 a 128 caracteres formados por letras, dígitos e `-._~`, e recomenda pelo menos 256 bits de entropia. Codificar 32 bytes obtidos de um gerador criptograficamente seguro em Base64url sem preenchimento produz 43 caracteres.

Com `S256`, o desafio é calculado pela fórmula abaixo. O preenchimento `=` no final da codificação Base64url é omitido.

$$
\text{code\_challenge}=\operatorname{BASE64URL}\!\left(\operatorname{SHA256}\!\left(\operatorname{ASCII}(\text{code\_verifier})\right)\right)
$$

A solicitação de autorização envia `code_challenge` e `code_challenge_method=S256`; a solicitação de token envia o `code_verifier` guardado para a mesma transação. O servidor o verifica com o método e o desafio registrados junto ao código. Não mude para `plain` porque `S256` falhou.

#### Visão geral do fluxo

```mermaid
sequenceDiagram
    autonumber
    participant U as "Usuário / navegador"
    participant C as "Cliente"
    participant AS as "Servidor de autorização / OP do OIDC"
    participant RS as "Servidor de recursos"
    Note over C: "Guardar verifier e state por transação; também nonce no OIDC"
    C->>U: "Redirecionar ao endpoint de autorização"
    U->>AS: "Solicitação: challenge e S256; openid e nonce no OIDC"
    AS-->>U: "Solicitar autenticação e consentimento conforme necessário"
    U->>AS: "Realizar autenticação e autorização"
    AS-->>U: "Redirecionar ao redirect_uri registrado com code e state"
    U->>C: "Callback: code e state"
    Note over C: "Verificar transação, state e emissor esperado"
    C->>AS: "Trocar code com verifier e a autenticação do cliente exigida"
    Note over AS: "Validar código, vínculos e PKCE"
    AS-->>C: "Token de acesso; também token de ID no OIDC"
    Note over C: "No OIDC, validar token de ID e nonce"
    C->>RS: "Chamar a API com o token de acesso"
    RS-->>C: "Validar token e permissões, e retornar o recurso"
```

O diagrama resume um fluxo bem-sucedido. Proteja as comunicações com TLS. A implementação também precisa tratar a validação dos redirecionamentos, o uso único dos códigos, as respostas de erro, a expiração da transação e a defesa contra ataques de confusão de servidores (mix-up) ao usar vários servidores de autorização.

#### Geração dos parâmetros PKCE (JavaScript / Web Crypto API)

Estas funções para o navegador exigem um contexto seguro, como HTTPS. `generatePkce()` apenas retorna parâmetros: não envia a solicitação de autorização nem armazena a transação. Não exponha o verifier em logs ou URLs; vincule-o à transação iniciada naquele navegador e descarte-o após a troca ou a expiração.

```javascript
function base64url(bytes) {
    return btoa(String.fromCharCode(...bytes))
        .replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
}

function generateCodeVerifier() {
    const bytes = new Uint8Array(32);
    crypto.getRandomValues(bytes);
    return base64url(bytes);
}

async function generateCodeChallenge(codeVerifier) {
    if (typeof codeVerifier !== 'string' ||
        codeVerifier.length < 43 || codeVerifier.length > 128 ||
        /[^A-Za-z0-9._~-]/.test(codeVerifier)) {
        throw new TypeError('Invalid PKCE verifier');
    }
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await crypto.subtle.digest('SHA-256', data);
    return base64url(new Uint8Array(digest));
}

async function generatePkce() {
    const code_verifier = generateCodeVerifier();
    return {
        code_verifier,
        code_challenge: await generateCodeChallenge(code_verifier),
        code_challenge_method: 'S256'
    };
}
```

O código usa todos os bits dos 32 bytes aleatórios. O exemplo anterior concatenava apenas os dois últimos dígitos hexadecimais de cada um de 28 inteiros aleatórios de 32 bits: obtinha 896 bits, mas preservava somente 224. Esse truncamento foi corrigido.

## 3. OIDC e tokens de ID

### 3.1 Uma camada de autenticação sobre OAuth

No OIDC, o cliente (Relying Party) solicita autenticação com o escopo `openid`, e o OpenID Provider (OP) retorna o resultado em um token de ID. O usuário não precisa digitar uma senha a cada vez: o OP pode usar uma sessão existente ou outro método de autenticação.

### 3.2 Separar as finalidades dos tokens

- **Token de acesso**: credencial para acessar um servidor de recursos. Pode ser um JWT ou uma string opaca; OAuth 2.0 não impõe um único formato. O cliente deve seguir os requisitos da API, sem presumir uma estrutura interna.
- **Token de ID**: JWT que representa um resultado de autenticação destinado ao cliente. Antes de usá-lo, valide sua assinatura, suas declarações e seu vínculo com a solicitação de autenticação. Apenas decodificá-lo não basta; ele também não deve ser enviado como substituto de um token de acesso à API.

### 3.3 Estrutura de JWT e assinaturas

Esta seção explica **JWS Compact Serialization** para um JWT assinado e não criptografado, composto por três partes separadas por pontos. Um JWT também pode ser criptografado como JWE ou ter uma estrutura aninhada: nem sempre tem três partes.

1. **Header (cabeçalho)**: campos como o algoritmo de assinatura `alg` e o identificador de chave `kid`.
2. **Payload (carga útil)**: declarações sobre emissor, destinatários, expiração, sujeito e outros dados.
3. **Signature (assinatura)**: assinatura ou MAC gerado pelo algoritmo especificado. O RS256, usado aqui, emprega uma assinatura digital RSA.

O cabeçalho e a carga útil estão apenas codificados em Base64url. A assinatura não oculta seu conteúdo. Veja também [as diferenças entre criptografia, hash e assinatura]({{< relref "post/modern-cryptography-public-key-hash-signature/index.pt.md" >}}).

#### Principais declarações obrigatórias do token de ID

- `iss`: identificador do emissor do OP. Deve coincidir exatamente com o emissor esperado.
- `sub`: identificador do usuário único e nunca reatribuído dentro daquele emissor. Ao usar vários OPs, combine-o com `iss` para identificar o usuário.
- `aud`: destinatário ou destinatários previstos. Verifique se inclui o `client_id` do cliente e não aceite destinatários adicionais que não sejam confiáveis.
- `exp`: instante de expiração. O horário atual deve ser anterior a ele.
- `iat`: instante de emissão. A política do cliente define a idade aceitável do token e outras restrições.

Se a solicitação de autenticação enviou um `nonce`, exija essa declaração e confira seu valor. Solicitar declarações adicionais ou `max_age` também exige as validações correspondentes.

#### Entrada da assinatura RS256

Considere `H` como o cabeçalho protegido em UTF-8, `P` como a carga útil em UTF-8 e `B64u` como a codificação Base64url sem preenchimento. A entrada da assinatura é a seguinte sequência de bytes; `||` indica concatenação.

$$
M=\operatorname{ASCII}\!\left(\operatorname{B64u}(H)\,||\,\texttt{.}\,||\,\operatorname{B64u}(P)\right),\qquad S=\operatorname{Sign}_{\mathrm{RS256}}(sk,M)
$$

RS256 usa RSASSA-PKCS1-v1_5 com SHA-256. O cálculo do hash faz parte do algoritmo de assinatura; a equação não acrescenta outro hash externo. A terceira parte do token é `B64u(S)`. Verifique a assinatura com uma chave pública do OP confiável e o algoritmo especificado, sem descrever a verificação de assinaturas em geral como uma descriptografia com chave pública.

Não deixe um token ainda não verificado decidir quais algoritmos são permitidos ou de onde obter as chaves. Use um JWKS confiável obtido de uma configuração ou de um processo Discovery do OP devidamente verificados, e trate a rotação e o cache das chaves. `kid` serve para selecionar uma chave dentro desse conjunto confiável; não obtenha chaves de uma URL arbitrária indicada pelo token.

#### Exemplo parcial de validação em Python

A função PyJWT abaixo atende a uma configuração limitada: **RS256, sem criptografia, um único destinatário representado como string e um nonce já enviado na solicitação**. Quem chama a função fornece `signing_key`, uma chave pública do JWKS do OP confiável. As declarações obrigatórias precisam existir, além de ter valores válidos. Se `azp` estiver presente, esta configuração exige que coincida com `client_id`.

Esta função não conclui um login. Quem a chama deve validar e gerenciar a relação entre o callback e a transação inicial, state, a troca do código, o emissor esperado e o uso único do nonce. Destinatários múltiplos, criptografia, requisitos adicionais de autenticação, `max_age` e `acr` ficam fora deste exemplo.

```python
import hmac
import math
import jwt


def verify_id_token(id_token, signing_key, *, issuer, client_id, expected_nonce):
    if not isinstance(expected_nonce, str) or not expected_nonce:
        raise ValueError('A nonce from the stored transaction is required')
    claims = jwt.decode(
        id_token,
        signing_key,
        algorithms=['RS256'],
        audience=client_id,
        issuer=issuer,
        options={
            'require': ['iss', 'sub', 'aud', 'exp', 'iat', 'nonce'],
            'strict_aud': True,
        },
    )
    for name in ('exp', 'iat'):
        value = claims[name]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or (isinstance(value, float) and not math.isfinite(value))):
            raise jwt.InvalidTokenError('Invalid NumericDate')
    subject = claims['sub']
    if (not isinstance(subject, str) or not subject or not subject.isascii()
            or len(subject) > 255):
        raise jwt.InvalidTokenError('Invalid subject')
    nonce = claims['nonce']
    if (not isinstance(nonce, str) or not hmac.compare_digest(
            nonce.encode('utf-8'), expected_nonce.encode('utf-8'))):
        raise jwt.InvalidTokenError('Nonce mismatch')
    if 'azp' in claims and claims['azp'] != client_id:
        raise jwt.InvalidTokenError('Authorized party mismatch')
    return claims
```

A função retorna as declarações validadas dentro desse escopo. Não anuncie uma autenticação bem-sucedida apenas porque a assinatura é válida, nem vincule contas usando um nome ou endereço de e-mail não verificado.

## 4. Considerações de segurança

### 4.1 state, nonce, PKCE e CSRF

Ao usar `state`, vincule de forma segura um valor imprevisível à transação iniciada no navegador. No callback, confira o valor, a expiração e se ele ainda não foi usado; em seguida, marque-o como utilizado. A igualdade entre strings não evita, por si só, todas as formas de [CSRF]({{< relref "post/cross-site-scripting-xss-csrf-security/index.pt.md" >}}).

A RFC 9700 também descreve a possibilidade de confiar na proteção CSRF do PKCE após confirmar seu suporte pelo servidor, além do uso de nonce do OIDC. Essas proteções continuam exigindo um vínculo por transação e validação correta. `state`, `nonce` e PKCE têm papéis diferentes; valores constantes ou comparações omitidas não fornecem a proteção pretendida. Vários servidores de autorização também exigem uma defesa contra ataques mix-up.

### 4.2 Expiração e tokens de atualização

Uma duração curta do token de acesso é uma forma de limitar o tempo de uso de um token roubado. Um valor como 15 minutos é um exemplo de projeto, não um requisito universal. Ao verificar `exp` em um JWT assinado, a condição de expiração é:

$$
T_{\mathrm{now}}<T_{\mathrm{exp}},\qquad T_{\mathrm{exp}}=T_{\mathrm{iat}}+D_{\mathrm{lifetime}}\ \text{somente se definido assim}\ T_{\mathrm{now}}<T_{\mathrm{iat}}+D_{\mathrm{lifetime}}
$$

Essa condição verifica apenas a expiração: não demonstra a validade completa do token nem a permissão de acesso. Também é preciso verificar o algoritmo, a chave, o emissor, os destinatários e, quando aplicável, `nbf`, o estado de revogação e o vínculo com a solicitação de autenticação. Gerencie explicitamente qualquer tolerância à diferença entre relógios.

A emissão de tokens de atualização é opcional. Sem eles, o cliente pode precisar de uma nova transação de autorização. A RFC 9700 exige restrição ao remetente (sender constraints) ou rotação para tokens de atualização emitidos a clientes públicos. Essa restrição vincula criptograficamente o token ao cliente que o apresenta. Revogar um token de atualização não invalida necessariamente, de imediato, os tokens de acesso já emitidos.

### 4.3 Escolher o fluxo e a implementação

Para aplicações web, SPAs e aplicativos nativos com interação do usuário, comece com código de autorização e PKCE. Escolha uma configuração compatível com o tipo de cliente, o armazenamento dos tokens, o suporte do provedor e o modelo de ameaças. Não imponha o mesmo fluxo a todos os casos, como o uso de credenciais do cliente para M2M.

## Conclusão

Use os tokens de acesso do OAuth 2.0 para acessar recursos e valide os tokens de ID do OIDC como resultados de autenticação destinados ao cliente. Confira o vínculo do código com PKCE, a assinatura, as declarações obrigatórias, o nonce e a relação entre o callback e a transação inicial.

## Referências

- [RFC 6749: OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749.html) (papéis, tokens e credenciais do cliente; veja a RFC 9700 para as orientações de segurança atualizadas)
- [RFC 7636: PKCE](https://www.rfc-editor.org/rfc/rfc7636.html) (seção 4, seção 7.1 e apêndice B)
- [RFC 9700: boas práticas de segurança para OAuth 2.0](https://www.rfc-editor.org/rfc/rfc9700.html) (seções 2.1, 2.2.2 e 2.4)
- [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) (seções 2, 3.1.3.7 e 5.7)
- [RFC 7515: JWS](https://www.rfc-editor.org/rfc/rfc7515.html) (seções 3.1 e 5.1)
- [API do PyJWT](https://pyjwt.readthedocs.io/en/stable/api.html) (algoritmos permitidos, declarações obrigatórias e validação dos destinatários)

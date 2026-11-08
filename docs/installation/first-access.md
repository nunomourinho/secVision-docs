# O primeiro acesso

Primeiro início de sessão com a conta inicial, alteração da palavra-passe e ativação do segundo fator com uma aplicação autenticadora, e o procedimento nos inícios de sessão seguintes.

```{video} 06-primeiro-acesso
```

Com a plataforma instalada, esta página descreve o primeiro início de sessão: a alteração da palavra-passe inicial e a ativação do segundo fator de autenticação. A plataforma exige estes dois passos antes de apresentar qualquer conteúdo.

## Requisitos de segurança

A palavra-passe inicial é igual em todas as instalações e consta do manual, pelo que deve ser alterada no primeiro acesso.

O segundo fator acrescenta à palavra-passe um elemento que só o utilizador possui (o telemóvel ou uma chave de segurança). Desta forma, o conhecimento da palavra-passe, por si só, não permite o acesso.

**Motivos dos dois passos obrigatórios**

- A palavra-passe inicial, ChangeMe123!, é igual em todas as instalações e é pública.
- O segundo fator acrescenta à palavra-passe um elemento que só o utilizador possui: o telemóvel ou uma chave de segurança.
- Sem o segundo fator, a palavra-passe não é suficiente para iniciar sessão.

## Início de sessão com a conta inicial

No browser, abra o endereço indicado pelo instalador. No laboratório, o endereço é localhost, porta 8080; num servidor, utilize o nome ou o endereço do servidor, a partir de qualquer computador da rede. Na página de entrada, introduza o utilizador **admin** e a palavra-passe inicial.

```{figure} /_static/img/06-primeiro-acesso/01.jpg
:alt: A página de entrada

A página de entrada.
```

## Nova palavra-passe

A plataforma solicita de imediato uma nova palavra-passe. A lista de regras apresentada exige pelo menos doze caracteres, maiúsculas e minúsculas, um número e um símbolo. Cada regra fica a verde quando é cumprida.

Introduza a palavra-passe duas vezes, para evitar erros, e guarde-a num cofre de palavras-passe. Não é possível reutilizar as três últimas palavras-passe.

```{figure} /_static/img/06-primeiro-acesso/02.jpg
:alt: Definir a palavra-passe nova

Definição da nova palavra-passe.
```

Quando todas as regras estiverem a verde, o botão fica ativo. Defina a palavra-passe e continue.

```{figure} /_static/img/06-primeiro-acesso/03.jpg
:alt: Confirmar

Confirmação.
```

## Segundo fator

Estão disponíveis duas opções:

- **Aplicação autenticadora** no telemóvel: Google Authenticator, Microsoft Authenticator ou equivalente. É a opção mais comum e não tem custos.
- **Chave de segurança física**, como uma YubiKey, ou o Windows Hello.

Este exemplo utiliza a aplicação autenticadora.

```{figure} /_static/img/06-primeiro-acesso/04.jpg
:alt: Escolher o segundo fator

Escolha do segundo fator.
```

É apresentado um código QR. No telemóvel, abra a aplicação autenticadora, selecione a opção para adicionar uma conta e aponte a câmara para o código. O mesmo segredo é apresentado em texto, para os casos em que a câmara não consiga ler o código.

Este segredo associa o telemóvel à conta e não deve ser partilhado. É apresentado neste manual porque se trata de uma instalação de laboratório, que será eliminada.

```{figure} /_static/img/06-primeiro-acesso/05.jpg
:alt: Ler o código QR com o telemóvel

Leitura do código QR com o telemóvel.
```

A aplicação apresenta um código de seis dígitos, renovado a cada trinta segundos. Introduza o código apresentado nesse momento e confirme. Nesta gravação, o código foi calculado a partir do mesmo segredo, pelo mesmo método utilizado pela aplicação do telemóvel.

Se o código for recusado, a causa mais provável é a hora do telemóvel estar incorreta, uma vez que estes códigos dependem do relógio. Ative o acerto automático da hora e introduza o código seguinte.

```{figure} /_static/img/06-primeiro-acesso/06.jpg
:alt: O código de seis dígitos

O código de seis dígitos.
```

## Painel inicial

Após a confirmação, é apresentado o painel da plataforma. Numa instalação nova, o painel está vazio; os dados surgem após a importação do inventário e a configuração da organização.

```{figure} /_static/img/06-primeiro-acesso/07.jpg
:alt: Dentro da plataforma

O painel da plataforma.
```

## Inícios de sessão seguintes

Para verificar um início de sessão normal, termine a sessão no botão do canto e inicie sessão novamente com a nova palavra-passe.

```{figure} /_static/img/06-primeiro-acesso/08.jpg
:alt: Sair e voltar a entrar

Terminar sessão e iniciar novamente.
```

Após a palavra-passe, a plataforma solicita o código da aplicação autenticadora. Este procedimento aplica-se a todos os inícios de sessão.

Em caso de perda do telemóvel, um administrador pode repor o segundo fator da conta; no início de sessão seguinte, o utilizador volta a ativá-lo.

```{figure} /_static/img/06-primeiro-acesso/09.jpg
:alt: A palavra-passe e o código

A palavra-passe e o código.
```

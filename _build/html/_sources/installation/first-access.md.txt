# O primeiro acesso

Entrar pela primeira vez com a conta inicial, trocar a palavra-passe e ativar o segundo fator com uma aplicação autenticadora — e o que muda nas entradas seguintes.

```{video} 06-primeiro-acesso
```

A plataforma está instalada. Nesta página entramos pela primeira vez. Vamos trocar a palavra-passe inicial e ativar o segundo fator de autenticação — dois passos que a plataforma exige antes de mostrar o que quer que seja.

## Porquê

Porquê? A palavra-passe inicial é a mesma em todas as instalações, e está escrita no manual. Por isso a primeira coisa a fazer é trocá-la.

E o segundo fator junta à palavra-passe uma coisa que só a pessoa tem: o telemóvel, ou uma chave de segurança. Assim, quem descobrir a palavra-passe, sozinha, não consegue entrar.

**Porquê dois passos obrigatórios**

- A palavra-passe inicial, ChangeMe123!, é igual em todas as instalações — toda a gente a conhece.
- O segundo fator junta à palavra-passe algo que só o utilizador tem: o telemóvel ou uma chave de segurança.
- Quem descobrir a palavra-passe, sem o segundo fator, não entra.

## Entrar com a conta inicial

No browser, abrimos o endereço que o instalador indicou — aqui, no laboratório, localhost, porta 8080; num servidor, é o nome ou o endereço dele, a partir de qualquer computador da rede. Aparece a página de entrada. Escrevemos o utilizador, admin, e a palavra-passe inicial.

```{figure} /_static/img/06-primeiro-acesso/01.jpg
:alt: A página de entrada

A página de entrada.
```

## A palavra-passe nova

Em vez de entrar, a plataforma pede logo uma palavra-passe nova. Repare na lista de regras por baixo: pelo menos doze caracteres, maiúsculas e minúsculas, um número e um símbolo. Cada regra fica verde quando é cumprida.

Escreve-se a palavra-passe duas vezes, para evitar enganos. Guarde-a já num cofre de palavras-passe. A plataforma também não deixa repetir as últimas três que usou.

```{figure} /_static/img/06-primeiro-acesso/02.jpg
:alt: Definir a palavra-passe nova

Definir a palavra-passe nova.
```

Com todas as regras a verde, o botão fica ativo. Definimos a palavra-passe e continuamos.

```{figure} /_static/img/06-primeiro-acesso/03.jpg
:alt: Confirmar

Confirmar.
```

## O segundo fator

Agora o segundo fator. Há duas opções. Uma aplicação autenticadora no telemóvel — o Google Authenticator, o Microsoft Authenticator ou outra. Ou uma chave de segurança física, como uma YubiKey, ou o Windows Hello.

A aplicação no telemóvel é a mais comum e não custa nada. É essa que escolhemos.

```{figure} /_static/img/06-primeiro-acesso/04.jpg
:alt: Escolher o segundo fator

Escolher o segundo fator.
```

Aparece um código QR. No telemóvel, abre-se a aplicação autenticadora, escolhe-se acrescentar uma conta, e aponta-se a câmara para este quadrado. Por baixo está o mesmo segredo em texto, para o caso de a câmara não o conseguir ler.

Este segredo é o que liga o telemóvel à conta, por isso nunca se partilha. Mostramo-lo aqui sem receio porque esta instalação é de laboratório e vai ser apagada.

```{figure} /_static/img/06-primeiro-acesso/05.jpg
:alt: Ler o código QR com o telemóvel

Ler o código QR com o telemóvel.
```

A aplicação mostra agora um código de seis dígitos, que muda a cada trinta segundos. Escrevemos o código que estiver no ecrã nesse momento e confirmamos. Nesta gravação, o código foi calculado a partir do mesmo segredo, tal como a aplicação do telemóvel o calcula.

Se o código for recusado, o mais provável é a hora do telemóvel estar errada — estes códigos dependem do relógio. Acerte a hora automaticamente, e tente o código seguinte.

```{figure} /_static/img/06-primeiro-acesso/06.jpg
:alt: O código de seis dígitos

O código de seis dígitos.
```

## Dentro

Entrámos. Este é o painel da plataforma. Ainda está vazio — normal, numa instalação acabada de fazer: os dados chegam quando se importa o inventário e se configura a organização.

```{figure} /_static/img/06-primeiro-acesso/07.jpg
:alt: Dentro da plataforma

Dentro da plataforma.
```

## As entradas seguintes

Vejamos agora como é uma entrada normal. Saímos, no botão do canto, e voltamos a entrar, desta vez com a palavra-passe nova.

```{figure} /_static/img/06-primeiro-acesso/08.jpg
:alt: Sair e voltar a entrar

Sair e voltar a entrar.
```

Depois da palavra-passe, a plataforma pede o código da aplicação autenticadora. É assim em todas as entradas: palavra-passe, e logo a seguir o código do telemóvel.

Se perder o telemóvel, não tente contornar: um administrador pode repor o segundo fator da sua conta, e da próxima vez que entrar ativa-o de novo.

```{figure} /_static/img/06-primeiro-acesso/09.jpg
:alt: A palavra-passe e o código

A palavra-passe e o código.
```

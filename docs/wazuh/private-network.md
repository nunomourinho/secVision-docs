# A rede privada para os agentes do Wazuh

Porque há servidores que o Wazuh não vê (zonas isoladas, DMZ), como uma rede privada gerida pelo Headscale lhes dá um caminho de saída sem abrir portas, e como o SecVision se liga a ela: o endereço, a autoridade certificadora, a chave de API, o ponto de entrada do Wazuh e a política da rede.

```{video} 509-rede-vpn-ligar-o-headscale
```

Há servidores que o Wazuh não consegue ver, porque estão numa zona isolada da rede e a firewall não os deixa chegar ao gestor. Esta página descreve a solução do SecVision, uma rede privada gerida pelo Headscale, e o ecrã onde se liga o SecVision a essa rede. A página seguinte, [Ligar um servidor da DMZ](connect-a-server.md), mostra como se liga o primeiro servidor.

## Acesso

**Proteger** > **Rede VPN** > **Estado e ligação**

O ecrã só é visível para o administrador do SecVision.

```{figure} /_static/capturas/vpn-ligacao/menu.jpg
:alt: Menu lateral: Proteger > Rede VPN > Estado e ligação

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

Uma DMZ é uma zona da rede onde ficam os servidores mais expostos, e que está isolada de propósito: de lá, só se sai para onde a firewall deixar. O agente do Wazuh liga-se sempre de dentro para fora, ao gestor, nas portas 1514 e 1515. Se a firewall não deixa chegar ao gestor, o servidor fica em GAP, sem ninguém a vê-lo.

A saída habitual seria abrir portas da DMZ para a rede interna, que é o risco que uma DMZ existe para evitar. Em vez disso, o servidor recebe um caminho de saída para um único sítio, que já alcança: o Headscale.

**O problema**

- Uma DMZ é uma zona isolada: de lá só se sai para onde a firewall deixa.
- O agente do Wazuh liga-se de dentro para fora, ao gestor, nas portas 1514 e 1515.
- Se a firewall não deixa chegar ao gestor, o servidor fica em GAP.
- Abrir portas para o interior é o risco que a DMZ existe para evitar.

## A solução, em quatro peças

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/01.jpg
:alt: As quatro peças da rede privada: o servidor, o Headscale, o ponto de entrada e o SecVision

As quatro peças da rede privada.
```

1. **O servidor:** tem o agente do Wazuh e um programa pequeno, o `secvision-agente`. Só falam com o Headscale, de dentro para fora.
2. **O Headscale:** fica na DMZ e junta os servidores numa rede privada. Nunca inicia uma ligação para dentro.
3. **O ponto de entrada:** o HAProxy, a face do Wazuh. Tem o cliente da rede privada e só aceita as portas 1514 e 1515.
4. **O SecVision:** gere as chaves, as validades e os bloqueios. Não faz parte da rede privada.

Os servidores não se veem uns aos outros: só chegam ao ponto de entrada, e só nas duas portas do Wazuh. Se um for comprometido, não tem por onde saltar para os outros.

## Informação a solicitar

Antes de abrir o ecrã, são necessários os elementos da instalação do Headscale e do ponto de entrada, que o guia de instalação da rede privada (`documentacao/rede-vpn-instalacao.md`, incluído na instalação do SecVision) descreve.

**Responsáveis**

| Elemento | A quem pedir |
|---|---|
| Endereço do Headscale, nome que os servidores usam para o alcançar, autoridade certificadora, chave de API | Administrador da rede ou da infraestrutura |
| Endereço do ponto de entrada na rede privada | Administrador do servidor HAProxy |
| Endereço do depósito de instaladores | Administrador do Headscale |

## A ligação ao Headscale

**Proteger** > **Rede VPN** > **Estado e ligação**

O primeiro bloco indica onde está o Headscale e como o SecVision lhe fala.

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/02.jpg
:alt: Proteger > Rede VPN > Estado e ligação

Ecrã **Proteger** > **Rede VPN** > **Estado e ligação**.
```

1. **URL do Headscale:** o endereço que o SecVision usa para falar com o Headscale. Neste laboratório é um endereço local; em produção seria o nome do servidor na DMZ.
2. **URL que os servidores usam:** pode ser diferente do primeiro, porque a DMZ e a rede do SecVision veem o Headscale por nomes diferentes. É este endereço que vai dentro do comando de instalação.
3. **Autoridade certificadora (PEM):** só é necessária quando o certificado do Headscale é de uma autoridade interna. É um certificado, não é um segredo.
4. **Chave de API:** dá ao SecVision autorização para gerir a rede. Fica cifrada e nunca volta a aparecer no ecrã. Deixar o campo vazio, ao guardar, mantém a chave que existe.

## O ponto de entrada

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/03.jpg
:alt: Estado e ligação > O ponto de entrada

Ecrã **Estado e ligação**, bloco do ponto de entrada.
```

1. **Nome do hub** e **Endereço do hub na VPN:** o nome do ponto de entrada e o endereço que o Headscale lhe atribuiu quando ele se juntou à rede. É para este endereço que cada servidor envia os dados.
2. **Validade do acesso de uma máquina nova (dias):** passado esse prazo, o SecVision bloqueia a máquina, a não ser que alguém a renove. Vazio significa sem validade.
3. **URL do depósito de instaladores:** o endereço de onde os servidores descarregam os instaladores, porque na DMZ não há Internet.

## Guardar e testar a ligação

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/04.jpg
:alt: Guardar e testar a ligação

Ecrã **Estado e ligação**, após **Guardar e testar a ligação**.
```

1. Clique em **Guardar e testar a ligação**.
2. O SecVision faz duas verificações a sério: se o Headscale responde com um certificado de confiança e se aceita a chave de API. É a prova de que o SecVision consegue gerir a rede, antes de qualquer servidor se ligar.

```{figure} /_static/capturas/vpn-ligacao/resultado-1.jpg
:alt: O resultado do teste de ligação

O resultado: o Headscale responde e aceita a chave de API.
```

## A política

**Proteger** > **Rede VPN** > **Política**

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/05.jpg
:alt: Proteger > Rede VPN > Política

Ecrã **Proteger** > **Rede VPN** > **Política**.
```

A política são as regras da rede, e é o SecVision que as escreve, a partir de uma lista declarada, e não o administrador à mão. Diz uma coisa só: os servidores podem chegar ao ponto de entrada, nas portas 1514 e 1515. Tudo o que não está escrito, o Headscale recusa.

Os testes de isolamento ainda estão por correr enquanto não há servidores na rede. Quando houver, o Headscale confirma que um servidor não chega a outro e que o ponto de entrada não os procura a eles. O SecVision também deteta se alguém alterou a política por fora e mostra a diferença antes de a repor.

## A lista de máquinas

**Proteger** > **Rede VPN** > **Máquinas**

```{figure} /_static/img/509-rede-vpn-ligar-o-headscale/06.jpg
:alt: Proteger > Rede VPN > Máquinas

Ecrã **Proteger** > **Rede VPN** > **Máquinas**.
```

Por agora só lá está o ponto de entrada, ligado e ativo. Cada servidor que se juntar à rede aparece nesta lista, com o seu estado, e é daqui que se bloqueia, se renova a validade ou se revoga o acesso, como descreve a página [Gerir as máquinas da rede privada](manage-machines.md).

## Resumo

O SecVision guarda a ligação ao Headscale, com a chave de API cifrada, escreve a política da rede e deteta se alguém a alterou por fora.

O SecVision não faz parte da rede privada e não vê o que os servidores enviam ao Wazuh.

**Funcionalidades e limitações**

- Guarda a ligação ao Headscale, com a chave de API cifrada, e testa-a com o Headscale a sério.
- Escreve a política da rede e deteta se alguém a alterou por fora.
- Não faz parte da rede privada e não vê o tráfego dos servidores.
- No ambiente de testes a tarefa diária que bloqueia os acessos vencidos está desligada, pelo que o ecrã pode mostrar o aviso de que nunca correu; em produção corre todos os dias.

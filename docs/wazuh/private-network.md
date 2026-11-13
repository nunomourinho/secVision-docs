# Montar a rede privada para os agentes do Wazuh

Porque há servidores que o Wazuh não vê (zonas isoladas, DMZ), e como o SecVision monta sozinho a rede privada que lhes dá um caminho de saída sem abrir portas: instala o Headscale e o ponto de entrada do Wazuh por SSH, gera os certificados e as chaves, e publica os instaladores. Só se escrevem endereços e uma palavra-passe, uma vez.

```{video} 509-montar-a-rede-privada
```

Há servidores que o Wazuh não consegue ver, porque estão numa zona isolada da rede e a firewall não os deixa chegar ao gestor. Esta página descreve a solução do SecVision, uma rede privada gerida pelo Headscale, e o assistente que a monta do princípio ao fim, a partir do ecrã. A página seguinte, [Adicionar um servidor da DMZ ao Wazuh](connect-a-server.md), mostra como se liga cada servidor.

## Acesso

**Proteger** > **Rede VPN** > **Montar a rede**

O assistente só é visível para o administrador do SecVision.

## Conceito

Uma DMZ é uma zona da rede onde ficam os servidores mais expostos, e que está isolada de propósito: de lá, só se sai para onde a firewall deixar. O agente do Wazuh liga-se sempre de dentro para fora, ao gestor, nas portas 1514 e 1515. Se a firewall não deixa chegar ao gestor, o servidor fica em GAP, sem ninguém a vê-lo.

A saída habitual seria abrir portas da DMZ para a rede interna, que é o risco que uma DMZ existe para evitar. Em vez disso, o servidor recebe um caminho de saída para um único sítio, que já alcança: o Headscale.

**O problema**

- Uma DMZ é uma zona isolada: de lá só se sai para onde a firewall deixa.
- O agente do Wazuh liga-se de dentro para fora, ao gestor, nas portas 1514 e 1515.
- Se a firewall não deixa chegar ao gestor, o servidor fica em GAP.
- Abrir portas para o interior é o risco que a DMZ existe para evitar.

## A solução, em três peças

```{figure} /_static/img/509-montar-a-rede-privada/01.jpg
:alt: As três peças da rede privada: o Headscale, o ponto de entrada e o SecVision

As três peças da rede privada.
```

1. **O Headscale:** fica num servidor da DMZ e junta os servidores numa rede privada. Nunca inicia uma ligação para dentro.
2. **O ponto de entrada:** o HAProxy, a face do Wazuh. Tem o cliente da rede privada e só aceita as portas 1514 e 1515.
3. **O SecVision:** instala, configura e gere as outras duas, por SSH e pelo seu ecrã. Não faz parte da rede.

Os servidores não se veem uns aos outros: só chegam ao ponto de entrada, e só nas duas portas do Wazuh. Se um for comprometido, não tem por onde saltar para os outros.

## O que se escreve, e o que não se escreve

O SecVision gera, guarda e leva aos servidores tudo o que é secreto ou técnico: a sua própria autoridade de certificação, os certificados dos servidores, a chave de API do Headscale, o token do depósito, as chaves de registo e as impressões digitais. **Nada disto se copia nem se cola.**

O que se escreve, e só se escreve uma vez, é:

- o endereço de cada servidor (o do Headscale, o do ponto de entrada e o do gestor do Wazuh);
- a palavra-passe de um administrador de cada um dos dois servidores, que só serve para esta instalação e nunca fica guardada.

## Informação a solicitar

Antes de abrir o assistente, são necessários dois servidores de uma zona isolada e o endereço do gestor do Wazuh. Os servidores não precisam de Internet: o SecVision leva consigo o que for preciso.

**Responsáveis**

| Elemento | A quem pedir |
|---|---|
| Servidor da DMZ para o Headscale: endereço, acesso por SSH e palavra-passe de um administrador | Administrador da infraestrutura |
| Servidor do ponto de entrada (HAProxy): endereço, acesso por SSH e palavra-passe de um administrador | Administrador do servidor HAProxy |
| Endereço do gestor do Wazuh, visto a partir do ponto de entrada | Administrador do Wazuh |

## Os quatro passos

```{figure} /_static/img/509-montar-a-rede-privada/02.jpg
:alt: Proteger > Rede VPN > Montar a rede

Ecrã **Proteger** > **Rede VPN** > **Montar a rede**.
```

O assistente tem quatro passos, todos no mesmo ecrã: o servidor do Headscale, os instaladores, o ponto de entrada do Wazuh, e adicionar servidores. Cada passo fica verde quando está feito, e um passo feito pode refazer-se.

## Passo 1: o servidor do Headscale

```{figure} /_static/img/509-montar-a-rede-privada/03.jpg
:alt: Passo 1: o endereço do servidor e a impressão digital

Passo 1: o endereço do servidor da DMZ e a impressão digital que o SecVision mostra.
```

1. **Endereço do servidor da DMZ:** o servidor onde o Headscale vai ficar. Só precisa de acesso por SSH.
2. Carregue em **Verificar o servidor**. O SecVision mostra a **impressão digital** do servidor, que é a identidade dele: confirme-a uma vez. A partir daí, a ligação só é aceite com este servidor, e não com outro que se faça passar por ele.
3. **Palavra-passe:** a de um administrador do servidor. É usada uma só vez e nunca fica guardada.
4. Carregue em **Instalar o Headscale**.

```{figure} /_static/img/509-montar-a-rede-privada/04.jpg
:alt: A instalação, passo a passo

A instalação, com cada passo a ficar verde.
```

O SecVision cria a sua própria autoridade de certificação e emite os certificados do servidor, escolhe os pacotes certos para a máquina, envia-os, instala o Headscale e o depósito de instaladores, e cria a chave de API, que fica cifrada na base de dados do SecVision. Cada passo vai ficando verde à medida que acaba; se um falhar, diz-se qual e porquê, com um botão **Repetir**.

## Passo 2: os instaladores

```{figure} /_static/img/509-montar-a-rede-privada/05.jpg
:alt: Passo 2: publicar os instaladores

Passo 2: os instaladores, publicados e conferidos.
```

Carregue em **Publicar os instaladores**. O SecVision envia ao depósito o programa que se instala em cada servidor, o `secvision-agente`, e o pacote do agente do Wazuh. Volta a ler o que ficou lá, confirma que chegou intacto e regista-o. Já não se registam nomes, endereços nem somas de verificação à mão.

## Passo 3: o ponto de entrada do Wazuh

```{figure} /_static/img/509-montar-a-rede-privada/06.jpg
:alt: Passo 3: o endereço do servidor do HAProxy

Passo 3: o servidor onde está o HAProxy.
```

1. **Endereço do servidor do HAProxy**, **Verificar o servidor** (confirme a impressão digital) e a **palavra-passe** de um administrador, como no passo 1.
2. **Endereço do gestor Wazuh (visto a partir deste servidor):** é para ele que o HAProxy vai passar o que chegar nas portas do Wazuh.

```{figure} /_static/img/509-montar-a-rede-privada/07.jpg
:alt: O endereço do gestor do Wazuh e a autorização para reiniciar o HAProxy

O endereço do gestor e a autorização para reiniciar o HAProxy.
```

3. Marque a **autorização para reiniciar o HAProxy**. Se ele já estiver a servir outras coisas nesse servidor, ficariam sem serviço por instantes; por isso o SecVision só avança depois de a dar.
4. Carregue em **Instalar o ponto de entrada**.

```{figure} /_static/img/509-montar-a-rede-privada/08.jpg
:alt: O ponto de entrada está na rede privada

O ponto de entrada já está na rede privada.
```

O SecVision cria uma chave de registo de uso único, junta o servidor à rede privada, abre as portas do Wazuh só nela, e descobre sozinho o endereço que o Headscale lhe deu, que antes se escrevia à mão.

## Resumo

O SecVision instalou o Headscale e o depósito, criou os certificados e as chaves, publicou os instaladores e instalou o ponto de entrada, tudo a partir do ecrã. Em todo o processo escrevem-se três endereços e uma palavra-passe por servidor; nenhuma chave, certificado ou impressão digital é copiada e colada.

**Funcionalidades e limitações**

- Os dois servidores precisam de um Linux com systemd, de acesso por SSH, de `curl` e de `openssl`. O servidor do Headscale tem de ser Debian ou Ubuntu (o pacote do Headscale é um `.deb`); o do ponto de entrada precisa do `haproxy` já instalado.
- A palavra-passe nunca é guardada. Para refazer um passo (por exemplo, para levar um certificado novo a um servidor), o SecVision pede-a outra vez.
- A chave da autoridade de certificação do SecVision é o segredo mais valioso da rede: está cifrada na base de dados e vai na cópia de segurança.
- Já tem um Headscale instalado à mão? Continua a funcionar: use **Estado e ligação** (avançado) para indicar o endereço e a chave de API, e **Convites** > **Avançado** para o comando de cada servidor.
- Não está provado em produção, e o instalador do agente para Windows ainda não foi provado numa máquina real.

A página [Quando algo falha na rede privada](network-health.md) mostra o painel que vigia a rede depois de montada.

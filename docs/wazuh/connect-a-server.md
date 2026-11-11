# Ligar um servidor da DMZ ao Wazuh

O percurso completo de um servidor que não chega ao gestor do Wazuh: publicar os instaladores no depósito, registá-los no SecVision, gerar o comando de instalação, corrê-lo no servidor e confirmar que ele aparece na rede privada, no SecVision e no painel do Wazuh.

```{video} 510-ligar-um-servidor-da-dmz
```

Esta página liga um servidor de uma zona isolada ao Wazuh, do princípio ao fim. O servidor não tem Internet, não chega ao gestor, e ninguém vai abrir portas na firewall. Todos os passos foram feitos a sério, num laboratório, e o resultado vê-se no SecVision e no painel do Wazuh. Pressupõe a ligação do SecVision ao Headscale descrita em [A rede privada para os agentes do Wazuh](private-network.md).

## Acesso

**Proteger** > **Rede VPN** > **Convites**

```{figure} /_static/capturas/vpn-convites/menu.jpg
:alt: Menu lateral: Proteger > Rede VPN > Convites

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Os quatro passos

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/01.jpg
:alt: Os quatro passos para ligar um servidor da DMZ

Os quatro passos.
```

1. **Publicar:** o executável do agente e o pacote do Wazuh vão para o depósito, que o servidor alcança.
2. **Registar:** no SecVision, declara-se onde estão os ficheiros e qual é a impressão digital de cada um.
3. **Gerar:** o SecVision cria uma chave de registo de uso único e um comando para este servidor.
4. **Instalar:** cola-se o comando no servidor; o agente junta-se à rede privada e instala o agente do Wazuh.

O servidor só precisa de chegar ao Headscale e ao depósito, que estão na própria DMZ. Tudo o resto passa pela rede privada.

## Informação a solicitar

Antes de começar, são necessários o executável `secvision-agente` e o pacote oficial do agente do Wazuh, na mesma versão do gestor, e o acesso de um administrador ao servidor.

**Responsáveis**

| Elemento | A quem pedir |
|---|---|
| Token do depósito (para carregar ficheiros) | Administrador do Headscale |
| Nome do servidor, tal como o Wazuh o vai mostrar | Responsável do servidor |
| Sessão de administrador (com `sudo`) no servidor | Administrador do servidor |

## 1. Publicar no depósito

Na máquina do administrador, o executável do agente e o pacote do Wazuh estão prontos. Os dois ficheiros vão para o depósito do Headscale, um servidor de ficheiros pequeno, só com HTTPS, que a DMZ alcança. Para carregar ficheiros é preciso o token do depósito; para os descarregar, não.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/02.jpg
:alt: A máquina do administrador: o executável e o pacote do agente

A máquina do administrador, com o executável e o pacote do agente do Wazuh.
```

O guião `bin/vpn-publicar.sh` envia o ficheiro, volta a descarregá-lo e compara. Se o que está no depósito não for o que foi enviado, falha. No fim escreve três coisas: o nome, o endereço e a impressão digital (o sha256 do ficheiro), que se vão precisar no SecVision.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/03.jpg
:alt: bin/vpn-publicar.sh a publicar o executável do agente

O guião `bin/vpn-publicar.sh` a publicar o executável.
```

Repete-se para o pacote do Wazuh. O depósito não é de confiança absoluta: quem o alterasse não conseguiria que o servidor instalasse um ficheiro diferente, porque o agente confere a impressão digital antes de instalar.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/04.jpg
:alt: bin/vpn-publicar.sh a publicar o pacote do agente do Wazuh

O mesmo guião a publicar o pacote do agente do Wazuh.
```

## 2. Registar os ficheiros no SecVision

**Proteger** > **Rede VPN** > **Convites**

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/05.jpg
:alt: Proteger > Rede VPN > Convites: registar o executável

Ecrã **Proteger** > **Rede VPN** > **Convites**, secção **Registar um ficheiro do depósito**.
```

1. Em **O que é**, escolha **Executável secvision-agente**.
2. Em **URL no depósito**, indique o endereço pelo qual os servidores veem o ficheiro. É o nome do depósito dentro da DMZ, e não o endereço local do administrador.
3. Em **sha256**, cole a impressão digital que o guião escreveu. É esta que o SecVision põe no comando e que o servidor vai exigir.
4. Clique em **Registar**.

O pacote do Wazuh regista-se da mesma maneira, escolhendo **Pacote do agente Wazuh (.deb)**: o sistema fica implícito e indica-se a arquitetura, **amd64**. Fica a lista com os dois ficheiros, cada um com a sua impressão digital.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/06.jpg
:alt: Registar o pacote do agente do Wazuh

Registo do pacote do agente do Wazuh.
```

## 3. Gerar o comando de instalação

Na secção **Instalar numa máquina**, indica-se o nome do servidor e, se necessário, a validade do acesso e o tempo que a chave de registo vive.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/07.jpg
:alt: Instalar numa máquina: o nome do servidor

Secção **Instalar numa máquina**.
```

1. **Nome da máquina:** `portal-dmz-01`. É o nome que o Wazuh vai mostrar.
2. **Validade do acesso (dias, opcional):** vazio usa o valor por omissão do ecrã **Estado e ligação**.
3. **O token vive (minutos):** a chave de registo vale 60 minutos e uma só vez.
4. Clique em **Gerar o comando de instalação**.

Ao gerar, o SecVision pede ao Headscale uma chave de registo de uso único. Essa chave não fica guardada no SecVision: aparece agora, uma vez, dentro do comando.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/08.jpg
:alt: O comando de instalação gerado pelo SecVision

O comando de instalação.
```

O comando descarrega o `secvision-agente` do depósito e executa-o com o token. O token leva tudo o que o agente precisa: onde está o Headscale, a autoridade certificadora, a chave de uso único, o endereço do ponto de entrada e os dois ficheiros com as suas impressões digitais. Quem tiver este comando durante uma hora pode ligar um servidor com este nome, por isso copia-se e cola-se logo, e não se guarda num documento.

## 4. Instalar no servidor

No servidor, o `portal-dmz-01` (um Debian 12), abre-se o terminal com a sessão de um administrador da máquina.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/09.jpg
:alt: O servidor portal-dmz-01, um Debian 12

O servidor da DMZ.
```

Este servidor não chega à Internet: o pedido a `packages.wazuh.com` falha, e o código de saída diferente de zero confirma-o. É por isso que os instaladores estão no depósito.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/10.jpg
:alt: O servidor não resolve nomes da Internet

Sem Internet: o pedido falha.
```

O que o servidor alcança é o Headscale, na própria DMZ, que responde que está bem. É a única porta de saída deste servidor, e a única de que a instalação precisa.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/11.jpg
:alt: O servidor alcança o Headscale

O Headscale responde.
```

Cola-se o comando que o SecVision gerou. O comando descarrega o executável do depósito, torna-o executável e corre-o com o `sudo`, porque instalar serviços exige privilégios de administrador.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/12.jpg
:alt: O comando colado no terminal do servidor

O comando colado no terminal.
```

Primeiro, o agente instala-se como serviço e guarda o token, só legível pelo administrador. Depois entra na rede privada, usando a chave de uso único. A partir deste momento, as portas 1514 e 1515, locais a este servidor, levam ao ponto de entrada do Wazuh pela rede privada. O agente do Wazuh não precisa de saber que existe uma rede privada: fala com o endereço local.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/13.jpg
:alt: O agente junta-se à rede privada

O agente junta-se à rede privada.
```

Depois descarrega o pacote do Wazuh do depósito e confere a impressão digital. Só se for exatamente a que o SecVision declarou é que o instala.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/14.jpg
:alt: O pacote é conferido e instalado

O pacote é conferido e instalado.
```

O agente do Wazuh fica configurado para falar só com o endereço local, com os comandos remotos bloqueados e a configuração protegida contra alterações. É a instalação de confiança zero descrita em [Instalar os agentes do Wazuh](installing-agents.md). No fim, o instalador verifica que o agente está a correr e ligado ao gestor pela rede privada; se falhar alguma verificação, diz qual.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/15.jpg
:alt: A configuração endurecida do agente

A configuração endurecida do agente.
```

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/16.jpg
:alt: A instalação terminou

A instalação terminou.
```

Confirma-se no servidor: os dois serviços estão ativos, o da ligação e o do Wazuh, e as portas 1514 e 1515 estão à escuta apenas no endereço local.

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/17.jpg
:alt: Os dois serviços ativos e as portas locais

Os dois serviços ativos e as portas locais.
```

## O resultado no SecVision

**Proteger** > **Rede VPN** > **Máquinas**

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/18.jpg
:alt: Proteger > Rede VPN > Máquinas

Ecrã **Proteger** > **Rede VPN** > **Máquinas**.
```

A lista já mostra o `portal-dmz-01`:

1. **Ligação:** ligado, o Headscale vê-o.
2. **Agente Wazuh:** o Wazuh recebe os dados dele pela rede privada.
3. **Acesso até:** o acesso tem validade, de um ano, a contar da instalação.

## O resultado no Wazuh

**Wazuh** > **Endpoints** > **Agents**

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/19.jpg
:alt: Wazuh > Endpoints > Agents

Ecrã **Wazuh** > **Endpoints** > **Agents**.
```

No painel do Wazuh, o mesmo servidor aparece como agente ativo. Para o Wazuh é um agente como os outros; a diferença é apenas o caminho que os dados fazem até lá.

## Aplicar a política com testes

**Proteger** > **Rede VPN** > **Política**

```{figure} /_static/img/510-ligar-um-servidor-da-dmz/20.jpg
:alt: Proteger > Rede VPN > Política

Ecrã **Proteger** > **Rede VPN** > **Política**.
```

Agora que há um servidor na rede, a política já pode correr os testes de isolamento. No ecrã **Política**, clique em **Aplicar a política desejada** e confirme: o Headscale só a aceita se os testes passarem.

## Resumo

O SecVision gera um comando para cada servidor, com uma chave de registo de uso único. Quem o corre é uma pessoa, com a sessão de administrador do servidor.

O SecVision não entra no servidor: não executa o comando por si.

**Funcionalidades e limitações**

- O servidor precisa de um Linux com systemd e do pacote `lsb-release`, de que o pacote do Wazuh depende. Se faltar, o agente diz-o antes de instalar, porque sem Internet o servidor não o consegue ir buscar.
- O servidor só precisa de alcançar o Headscale (443) e o depósito (8080).
- O instalador para Windows existe mas ainda não foi provado numa máquina real: antes de o usar em produção, faça um piloto com um único servidor.
- Os servidores antigos, que não correm o cliente da rede privada, ligam-se por uma ponte: uma máquina moderna da mesma rede, instalada com a opção **Esta máquina é uma ponte** da secção **Instalar numa máquina**. Não está coberta por um vídeo.

# Gerir as máquinas da rede privada

Depois de um servidor estar ligado, o que o administrador pode decidir: bloquear (e desbloquear) o acesso, vendo o Wazuh perder e recuperar o agente, fixar a validade do acesso, recolher provas do que o Wazuh já guardou, e revogar um servidor da rede.

```{video} 511-gerir-as-maquinas-da-rede-vpn
```

Com os servidores ligados, o trabalho do administrador é decidir quem continua na rede. Esta página descreve as quatro decisões que o SecVision oferece e, para cada uma, o efeito que se vê no Wazuh. Pressupõe um ou mais servidores ligados, como descreve [Ligar um servidor da DMZ ao Wazuh](connect-a-server.md).

## Acesso

**Proteger** > **Rede VPN** > **Máquinas**

O ecrã é visível para o operador e para o administrador. As ações que alteram a rede exigem o administrador.

```{figure} /_static/capturas/vpn-maquinas-ligadas/menu.jpg
:alt: Menu lateral: Proteger > Rede VPN > Máquinas

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/01.jpg
:alt: As quatro decisões: bloquear, validade, provas e revogar

As quatro decisões.
```

1. **Bloquear:** corta o caminho ao ponto de entrada. O servidor continua na lista e pode voltar.
2. **Validade:** o acesso acaba numa data. Passada, o SecVision bloqueia sozinho, e avisa antes.
3. **Provas:** lê do Wazuh o que ele já guarda daquele servidor, com impressão digital.
4. **Revogar:** apaga o servidor da rede. Só volta com um convite novo.

Em nenhum destes casos o SecVision entra no servidor. Tudo se decide na rede privada ou lê-se do Wazuh, e é por isso que funciona mesmo com os comandos remotos bloqueados.

## Informação a solicitar

**Responsáveis**

| Decisão | Quem decide |
|---|---|
| Bloquear ou desbloquear por suspeita ou manutenção | Responsável de cibersegurança, com o responsável do servidor |
| Fixar a validade de um acesso temporário (um prestador) | Responsável de cibersegurança |
| Recolher provas para um incidente ou uma auditoria | Responsável de cibersegurança |
| Revogar um servidor desativado ou comprometido | Responsável de cibersegurança |

## A lista

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/02.jpg
:alt: Proteger > Rede VPN > Máquinas

Ecrã **Proteger** > **Rede VPN** > **Máquinas**.
```

Na lista de máquinas aparecem o ponto de entrada e os servidores ligados. Cada servidor tem à direita as ações: **Provas**, **Bloquear**, **Validade**, **Sistema** e **Revogar**. A lista é lida do Headscale a cada pedido, por isso mostra a verdade de agora, e não a de ontem.

## Bloquear

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/03.jpg
:alt: O servidor bloqueado na lista de máquinas

O servidor bloqueado.
```

1. Na linha do servidor, clique em **Bloquear**.
2. O SecVision confirma: «Máquina bloqueada: deixou de chegar ao hub».

Bloquear muda a etiqueta do servidor na rede para uma que não tem nenhuma regra de acesso. O Headscale corta as ligações que ele tinha abertas, e ele deixa de chegar ao ponto de entrada. É imediato e não apaga nada: o servidor continua na lista, com o estado bloqueado, à espera de uma decisão.

## O Wazuh perde o servidor

**Wazuh** > **Endpoints** > **Agents**

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/04.jpg
:alt: Wazuh > Endpoints > Agents: o agente desligado

Ecrã **Wazuh** > **Endpoints** > **Agents**, com o agente desligado.
```

No painel do Wazuh o agente ainda aparece ativo logo a seguir ao bloqueio, porque o Wazuh só dá por falta de um agente quando deixa de receber os seus sinais de vida, e por omissão espera dez minutos (`agents_disconnection_time`). No vídeo, a espera é acelerada. Passado esse tempo, o agente passa a **Disconnected**. Do ponto de vista do Wazuh, o servidor deixou de existir; do ponto de vista do administrador, foi uma decisão, e não uma avaria.

## Desbloquear

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/05.jpg
:alt: O servidor desbloqueado na lista de máquinas

O servidor desbloqueado.
```

Para desfazer, clique em **Desbloquear**. A etiqueta volta ao que era e o caminho reabre. Ninguém tem de ir ao servidor.

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/06.jpg
:alt: Wazuh > Endpoints > Agents: o agente ativo outra vez

O Wazuh volta a ver o servidor.
```

O agente, que nunca deixou de tentar ligar-se, volta a ligar-se sozinho, e o painel do Wazuh mostra-o ativo outra vez.

## Validade do acesso

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/07.jpg
:alt: Validade do acesso do servidor

A validade do acesso.
```

1. Clique em **Validade**.
2. Em **O acesso vale até**, indique a data. Neste exemplo, o fim de junho.
3. Clique em **Guardar**. **Tirar a validade** deixa a máquina sem prazo.

O Headscale não faz expirar as máquinas etiquetadas, e por isso é o SecVision que guarda a data e bloqueia a máquina quando ela passa. Avisa alguns dias antes (o número define-se em **Estado e ligação**), para que ninguém seja apanhado de surpresa.

## Recolher provas

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/08.jpg
:alt: Recolher provas do servidor

Recolher provas.
```

1. Clique em **Provas**.
2. Em **O que recolher**, escolha **Alertas do agente**, **Pacotes instalados** ou **Estado do agente e da ligação**.
3. Em **Janela (horas)**, indique a janela dos alertas.
4. Clique em **Recolher**.

As provas servem para um incidente ou para uma auditoria: o que o Wazuh sabe deste servidor. O SecVision só lê: não corre nada no servidor, porque o agente foi instalado com os comandos remotos bloqueados. O que se recolhe é o que o Wazuh já tinha.

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/09.jpg
:alt: Provas recolhidas, com a impressão digital

As provas recolhidas.
```

Cada recolha fica guardada com a sua impressão digital (sha256), o nome do servidor e a hora. Se alguém alterar o ficheiro depois, o SecVision recusa entregá-lo, porque a impressão digital já não bate certo.

## Revogar

```{figure} /_static/img/511-gerir-as-maquinas-da-rede-vpn/10.jpg
:alt: Revogar a máquina: confirmação com o nome

Revogar a máquina.
```

1. Clique em **Revogar**.
2. Escreva o nome da máquina para confirmar. É uma decisão definitiva.
3. Clique em **Revogar**.

Revogar apaga o servidor da rede. O servidor revogado só volta com um convite novo, e a chave de registo antiga já não serve. Na lista fica marcado como revogado, e o registo de quem o revogou, e quando, fica na trilha de auditoria.

## Resumo

Se há uma suspeita ou uma manutenção, bloqueia-se. Se o acesso é temporário, fixa-se a validade. Em caso de incidente ou de auditoria, recolhem-se as provas primeiro. E se o servidor foi desativado ou comprometido, revoga-se.

**Funcionalidades e limitações**

- Bloqueia e desbloqueia sem tocar no servidor, e a decisão vê-se no Wazuh passados dez minutos.
- Fixa a validade do acesso e bloqueia sozinho quando ela passa.
- Recolhe provas do que o Wazuh já guarda (estado, pacotes, alertas), com impressão digital.
- Revoga, com confirmação pelo nome, deixando o registo na trilha de auditoria.
- Não executa nada nos servidores: um servidor comprometido não é o sítio certo para executar ordens.

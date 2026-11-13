# Instalar os agentes do Wazuh

Função do agente numa máquina e motivo da instalação endurecida; o gerador de scripts do SecVision (gestor, portas, versão e políticas de confiança zero), a fila dos sistemas em GAP e o assistente do próprio Wazuh, em comparação; e a apresentação da máquina após a instalação.

```{video} 502-instalar-os-agentes
```

A página anterior apresenta as máquinas monitorizadas e as máquinas em GAP. Esta página descreve a correção de um GAP através da instalação do agente do Wazuh, com o script gerado pelo SecVision, e as opções disponibilizadas pelo próprio Wazuh.

## Acesso

**Proteger** > **SOC** > **Wazuh Agent Builder**

```{figure} /_static/capturas/wazuh-agentes/menu.jpg
:alt: Menu lateral: Proteger > SOC > Wazuh Agent Builder

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

O agente é executado com privilégios elevados em todas as máquinas. Estes privilégios permitem-lhe ler os registos e o inventário, mas tornam-no um risco se estiver mal configurado.

Por omissão, o gestor pode ordenar ao agente a execução de comandos, a alteração da configuração ou a atualização automática, pelo que o comprometimento do gestor compromete todas as máquinas. A instalação de confiança zero elimina este risco: o agente apenas envia dados, não recebe ordens e comunica exclusivamente com o gestor.

**Motivo da instalação endurecida**

- O agente é executado com privilégios elevados em cada máquina e constitui um ponto de entrada se estiver mal configurado.
- Por omissão, o gestor pode ordenar ao agente a execução de comandos e a atualização automática.
- Confiança zero: o agente apenas envia dados, não recebe ordens e comunica exclusivamente com o gestor.

## Gerador de scripts

No Wazuh Agent Builder, é indicada a localização do gestor e a versão do agente. A versão tem de ser igual ou anterior à do gestor, uma vez que um agente mais recente não estabelece ligação. O gestor deste ambiente está na versão 4.14.10. A configuração é guardada automaticamente.

```{figure} /_static/capturas/wazuh-agentes/builder-1.jpg
:alt: Proteger > SOC > Wazuh Agent Builder

Ecrã **Proteger** > **SOC** > **Wazuh Agent Builder**.
```

No ecrã, encontra os seguintes elementos:

1. **Endereço do gestor:** Neste exemplo, um endereço ilustrativo.
2. **Portas:** 1514 para os eventos e 1515 para o registo do agente.
3. **Versão do agente:** Introduza «4.14.10» neste campo.
4. **Aviso de versão:** A versão deve ser igual ou anterior à do gestor.

**Wazuh Agent Builder** > **Políticas Zero-Trust**

As políticas de confiança zero são apresentadas com o respetivo efeito: bloqueio dos comandos remotos, desativação das atualizações pelo gestor e das respostas ativas, restrição das permissões dos ficheiros do agente e firewall do agente, que restringe a comunicação ao gestor.

É gerado um script por sistema operativo: Windows, versões antigas do Windows Server e Linux. O script transfere o pacote oficial do Wazuh, instala-o e aplica as políticas selecionadas.

```{figure} /_static/capturas/wazuh-agentes/zerotrust-1.jpg
:alt: Wazuh Agent Builder > Políticas Zero-Trust

Ecrã **Wazuh Agent Builder** > **Políticas Zero-Trust** (1 de 3).
```

1. **Bloqueio de comandos remotos:** O gestor não pode ordenar a execução de comandos.

```{figure} /_static/capturas/wazuh-agentes/zerotrust-2.jpg
:alt: Wazuh Agent Builder > Políticas Zero-Trust

Ecrã **Wazuh Agent Builder** > **Políticas Zero-Trust** (2 de 3).
```

1. **Firewall do agente:** Restringe a comunicação ao gestor.
2. Clique em **Linux — Debian/Ubuntu/RHEL (.sh)**.

```{figure} /_static/capturas/wazuh-agentes/zerotrust-3.jpg
:alt: Wazuh Agent Builder > Políticas Zero-Trust

Ecrã **Wazuh Agent Builder** > **Políticas Zero-Trust** (3 de 3).
```

1. **Script:** Um script por sistema operativo.

## Perfis de agente

As limitações do agente deixaram de ser um conjunto único para todas as máquinas: há **perfis**, escolhidos por máquina. Em **Proteger** > **SOC** > **Wazuh Agent Builder**, o seletor **Perfil do agente** escolhe o perfil que se edita, e **Novo perfil** e **Duplicar** criam outros.

| Perfil | O que limita |
|---|---|
| **Predefinido** | O que o Agent Builder já tinha: comandos remotos, atualização pelo gestor, resposta ativa, permissões dos ficheiros e firewall do agente. |
| **Desbloqueado** | Nada: o gestor pode dar ordens ao agente. É uma decisão a justificar. |
| **Bloqueado (zero-trust)** | Tudo. |

Cada perfil pode ter um **grupo** do Wazuh. O perfil de cada instalação fica registado, para se saber mais tarde porque é que uma máquina aceita ordens do gestor e outra não. Um perfil em uso não se elimina, e o predefinido também não.

Na fila de integração e em **Rede VPN**, cada máquina escolhe o seu perfil, e **Personalizar só para esta máquina** muda as limitações dessa instalação sem mexer no perfil.

## Fila de integração

**Proteger** > **Instalar agente Wazuh**

A fila de integração apresenta os sistemas incluídos no âmbito sem agente, ordenados pela criticidade, pela exposição e pelos dias em GAP. Neste ambiente, são três máquinas Windows.

O botão **Iniciar Integração** abre o script correspondente ao sistema operativo indicado no catálogo, com os valores do gerador. Este script é entregue ao administrador da máquina, que o executa com as respetivas credenciais; a plataforma não instala o agente.

```{figure} /_static/capturas/wazuh-agentes/fila-1.jpg
:alt: Proteger > Instalar agente Wazuh

Ecrã **Proteger** > **Instalar agente Wazuh** (1 de 3).
```

```{figure} /_static/capturas/wazuh-agentes/fila-2.jpg
:alt: Proteger > Instalar agente Wazuh

Ecrã **Proteger** > **Instalar agente Wazuh** (2 de 3).
```

1. **Ordenação:** Criticidade, exposição e dias em GAP.
2. Clique em **Iniciar Integração**.

```{figure} /_static/capturas/wazuh-agentes/fila-3.jpg
:alt: Proteger > Instalar agente Wazuh

Ecrã **Proteger** > **Instalar agente Wazuh** (3 de 3).
```

1. **Sistema operativo:** Selecionado a partir do catálogo.

### O separador Rede VPN

Quando a rede privada está montada (ver [a rede privada](private-network.md)), **Iniciar Integração** tem um terceiro separador, **Rede VPN**, que gera um comando único para o servidor, com o perfil escolhido, em vez de um script para correr à mão.

O SecVision lê o sistema operativo que o catálogo conhece e propõe o **Sistema do servidor** certo: **Linux**, **Windows Server 2016 ou mais recente** ou **Antigo** (Windows Server 2012 R2 e anteriores, que vão pela ponte). É só uma sugestão, e a escolha é do administrador. Quando o agente aparece no Wazuh com o nome esperado, o SecVision liga-o sozinho ao sistema do catálogo (esta verificação corre de dez em dez minutos, e nunca substitui uma ligação feita por uma pessoa).

Ver [Instalar o agente num Windows Server](install-on-windows.md) e [Servidores Windows antigos](legacy-servers.md).

## Assistente do Wazuh

**Wazuh** > **Endpoints** > **Deploy new agent**

O painel do Wazuh dispõe também de um assistente: após a seleção do pacote (neste exemplo, Debian) e do endereço do gestor, é apresentado o comando de instalação, com a mesma versão.

A diferença reside na configuração aplicada. O comando do Wazuh instala o agente com a configuração de origem; o script do SecVision instala o mesmo pacote oficial e aplica o endurecimento. Ambos são funcionais, mas apenas o segundo elimina os riscos da configuração por omissão.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-1.jpg
:alt: Wazuh > Endpoints > Deploy new agent

Ecrã **Wazuh** > **Endpoints** > **Deploy new agent** (1 de 3).
```

1. Clique em **DEB amd64**.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-2.jpg
:alt: Wazuh > Endpoints > Deploy new agent

Ecrã **Wazuh** > **Endpoints** > **Deploy new agent** (2 de 3).
```

1. Introduza «10.0.0.50» no campo **Server address**.

```{figure} /_static/capturas/wazuh-agentes/wazuh_deploy-3.jpg
:alt: Wazuh > Endpoints > Deploy new agent

Ecrã **Wazuh** > **Endpoints** > **Deploy new agent** (3 de 3).
```

1. **Comando de instalação:** Gerado pelo próprio Wazuh.

**Wazuh** > **Endpoints** > **Agents**

Após a execução do script, a máquina é apresentada como ativa na lista de agentes do Wazuh. Os agentes deste ambiente de testes foram instalados com o mesmo pacote oficial, um por máquina Linux do catálogo.

O último passo é efetuado no SecVision: a associação do agente ao sistema do catálogo, que retira o sistema do estado GAP e é descrita numa página própria.

```{figure} /_static/capturas/wazuh-agentes/wazuh_agentes-1.jpg
:alt: Wazuh > Endpoints > Agents

Ecrã **Wazuh** > **Endpoints** > **Agents**.
```

1. **Agente instalado:** Apresentado na lista após a instalação.

## Resumo

A plataforma gera o script adequado a cada máquina e define a ordem de instalação.

A plataforma não instala agentes, uma vez que uma ferramenta de gestão com credenciais de administrador em todas as máquinas constituiria, em si mesma, o maior risco da organização.

**Funcionalidades e limitações**

- Gera o script de cada sistema operativo, com o gestor, a versão e o perfil do agente, e o comando único da rede privada.
- Ordena os sistemas em GAP pela criticidade, pela exposição e pelos dias sem monitorização.
- Não instala agentes: o script é executado por um operador, com as credenciais da máquina.

# O Explorer — inventário de uma máquina

O inventário recolhido pelo agente (software, processos, rede e contas) e as vulnerabilidades do software instalado, apresentados no Explorer do SecVision e no painel do Wazuh, em paralelo, para a mesma máquina do ambiente de testes.

```{video} 503-o-explorer
```

Com o agente instalado, a máquina passa a reportar o seu inventário: software, processos, rede e contas. Esta página apresenta o inventário de uma máquina, no SecVision e no Wazuh.

## Acesso

**Detetar** > **SOC** > **Wazuh Explorer**

```{figure} /_static/capturas/wazuh-explorer/menu.jpg
:alt: Menu lateral: Detetar > SOC > Wazuh Explorer

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

O agente recolhe periodicamente o estado da máquina: software instalado e respetiva versão, processos em execução, interfaces de rede e contas existentes.

O Wazuh cruza esse software com as bases públicas de vulnerabilidades (CVE), o que permite responder a uma questão habitual em auditoria: as máquinas com software vulnerável e o software em causa.

**O inventário e a sua importância**

- O agente recolhe periodicamente o estado da máquina: software, processos, interfaces, portas e contas.
- O Wazuh cruza o software com as bases de vulnerabilidades conhecidas (CVE).
- O conhecimento do software instalado é o primeiro passo de qualquer correção.

## No SecVision

No Wazuh Explorer, após a seleção do agente (neste exemplo, a base de dados 003), os dados de todos os separadores são carregados em simultâneo. Junto ao agente é apresentado o sistema do catálogo associado, com ligação direta.

```{figure} /_static/capturas/wazuh-explorer/agente-1.jpg
:alt: Detetar > SOC > Wazuh Explorer

Ecrã **Detetar** > **SOC** > **Wazuh Explorer** (1 de 2).
```

1. Selecione o agente **003** na lista de agentes.
2. Clique em **Visão Geral**.

```{figure} /_static/capturas/wazuh-explorer/agente-2.jpg
:alt: Detetar > SOC > Wazuh Explorer

Ecrã **Detetar** > **SOC** > **Wazuh Explorer** (2 de 2).
```

1. **Sistema do catálogo:** Sistema associado ao agente.

**Wazuh Explorer** > **Software**

O separador do software apresenta todos os pacotes instalados, com a versão e o fabricante, e permite a pesquisa por nome. Neste exemplo, o openssl desta máquina está na versão 3.0.9, uma versão antiga com vulnerabilidades conhecidas.

Esta versão foi instalada deliberadamente no ambiente de testes, para disponibilizar vulnerabilidades reais para demonstração. Numa instituição, este separador permite identificar pacotes desatualizados deste tipo.

```{figure} /_static/capturas/wazuh-explorer/software-1.jpg
:alt: Wazuh Explorer > Software

Ecrã **Wazuh Explorer** > **Software** (1 de 5).
```

1. Clique em **Software**.

```{figure} /_static/capturas/wazuh-explorer/software-2.jpg
:alt: Wazuh Explorer > Software

Ecrã **Wazuh Explorer** > **Software** (2 de 5).
```

1. Introduza «openssl» no campo **Pesquisar...**.
2. **openssl 3.0.9-1:** Versão instalada.
3. Clique em **Pesquisar...**.

```{figure} /_static/capturas/wazuh-explorer/software-3.jpg
:alt: Wazuh Explorer > Software

Ecrã **Wazuh Explorer** > **Software** (3 de 5).
```

```{figure} /_static/capturas/wazuh-explorer/software-4.jpg
:alt: Wazuh Explorer > Software

Ecrã **Wazuh Explorer** > **Software** (4 de 5).
```

```{figure} /_static/capturas/wazuh-explorer/software-5.jpg
:alt: Wazuh Explorer > Software

Ecrã **Wazuh Explorer** > **Software** (5 de 5).
```

**Wazuh Explorer** > **Processos · Rede · Utilizadores**

Estes separadores apresentam os processos em execução, as interfaces e os endereços de rede e as contas da máquina. Uma conta desconhecida ou um processo indevido podem ser detetados neste ecrã antes de originarem um incidente.

```{figure} /_static/capturas/wazuh-explorer/maquina-1.jpg
:alt: Wazuh Explorer > Processos · Rede · Utilizadores

Ecrã **Wazuh Explorer** > **Processos · Rede · Utilizadores** (1 de 4).
```

1. Clique em **Processos**.

```{figure} /_static/capturas/wazuh-explorer/maquina-2.jpg
:alt: Wazuh Explorer > Processos · Rede · Utilizadores

Ecrã **Wazuh Explorer** > **Processos · Rede · Utilizadores** (2 de 4).
```

1. Clique em **Rede e Tráfego**.

```{figure} /_static/capturas/wazuh-explorer/maquina-3.jpg
:alt: Wazuh Explorer > Processos · Rede · Utilizadores

Ecrã **Wazuh Explorer** > **Processos · Rede · Utilizadores** (3 de 4).
```

1. Clique em **Utilizadores**.

```{figure} /_static/capturas/wazuh-explorer/maquina-4.jpg
:alt: Wazuh Explorer > Processos · Rede · Utilizadores

Ecrã **Wazuh Explorer** > **Processos · Rede · Utilizadores** (4 de 4).
```

**Wazuh Explorer** > **Vulnerabilidades**

As vulnerabilidades são contabilizadas por gravidade (críticas, altas, médias e baixas), cada uma com o CVE, o pacote afetado e a pontuação de gravidade (CVSS).

Estes dados provêm do Indexer do Wazuh, pelo que exigem o respetivo endereço e credenciais na configuração. Sem o Indexer, a plataforma recorre à API antiga do gestor, que nas versões recentes já não disponibiliza estes dados.

```{figure} /_static/capturas/wazuh-explorer/vulns-1.jpg
:alt: Wazuh Explorer > Vulnerabilidades

Ecrã **Wazuh Explorer** > **Vulnerabilidades** (1 de 2).
```

1. Clique em **Vulnerabilidades**.

```{figure} /_static/capturas/wazuh-explorer/vulns-2.jpg
:alt: Wazuh Explorer > Vulnerabilidades

Ecrã **Wazuh Explorer** > **Vulnerabilidades** (2 de 2).
```

1. **Vulnerabilidades por gravidade:** Obtidas do Indexer.

## No Wazuh

**Wazuh** > **Endpoints** > **base-de-dados-003**

No painel do Wazuh, a mesma máquina tem uma página própria, com o inventário do sistema, os eventos e o mapa das técnicas de ataque e, em baixo, as vulnerabilidades por gravidade.

Os valores coincidem com os apresentados pelo SecVision, por provirem da mesma origem. O SecVision não guarda uma cópia: consulta o Wazuh sempre que o ecrã é aberto.

```{figure} /_static/capturas/wazuh-explorer/wazuh_agente-1.jpg
:alt: Wazuh > Endpoints > base-de-dados-003

Ecrã **Wazuh** > **Endpoints** > **base-de-dados-003** (1 de 2).
```

1. **Agente no painel do Wazuh:** O mesmo agente apresentado no SecVision.

```{figure} /_static/capturas/wazuh-explorer/wazuh_agente-2.jpg
:alt: Wazuh > Endpoints > base-de-dados-003

Ecrã **Wazuh** > **Endpoints** > **base-de-dados-003** (2 de 2).
```

1. **Vulnerabilidades:** Os mesmos valores apresentados no SecVision.

**Wazuh** > **Vulnerability Detection** > **Inventory**

O inventário de vulnerabilidades do Wazuh destina-se ao tratamento individual das vulnerabilidades pela equipa do centro de operações.

```{figure} /_static/capturas/wazuh-explorer/wazuh_vuln-1.jpg
:alt: Wazuh > Vulnerability Detection > Inventory

Ecrã **Wazuh** > **Vulnerability Detection** > **Inventory**.
```

## Resumo

O Explorer reúne, para cada máquina, a informação do Wazuh e a informação do catálogo.

A plataforma não corrige vulnerabilidades: a atualização do openssl desta máquina compete ao respetivo administrador. A plataforma fornece a lista que permite planear essa correção.

**Funcionalidades e limitações**

- Apresenta, por máquina, o inventário e as vulnerabilidades, em conjunto com o sistema do catálogo.
- Não guarda cópia: consulta o Wazuh sempre que o ecrã é aberto.
- Não corrige vulnerabilidades: a atualização do software compete ao administrador da máquina.

# O Explorer — uma máquina por dentro

O inventário que o agente recolhe — software, processos, rede, contas — e as vulnerabilidades do software instalado, vistos no Explorer do SecVision e no painel do Wazuh, lado a lado, para a mesma máquina do ambiente de testes.

```{video} 503-o-explorer
```

Com o agente instalado, a máquina passa a contar o que tem: o software, os processos, a rede, as contas. Nesta página vemos uma máquina por dentro, no SecVision e no Wazuh.

## Onde fica no menu

**Menu:** Detetar › Soc › Wazuh Explorer

```{figure} /_static/capturas/wazuh-explorer/menu.jpg
:alt: Menu lateral: Detetar › Soc › Wazuh Explorer

O caminho no menu lateral: Detetar › Soc › Wazuh Explorer.
```

1. No menu lateral, abra **Detetar**.
2. Dentro dele, abra **Soc**.
3. Clique em **Wazuh Explorer**: abre o ecrã desta página.

## O conceito

O agente tira uma fotografia da máquina de tempos a tempos: que software está instalado e em que versão, que processos correm, que interfaces de rede e que contas existem.

E o Wazuh cruza esse software com as bases públicas de vulnerabilidades, as CVE. É daqui que vem a resposta à pergunta que um auditor faz sempre: que máquinas têm software vulnerável, e qual.

**O inventário, e porque importa**

- O agente fotografa a máquina de tempos a tempos: software, processos, interfaces, portas, contas.
- O Wazuh cruza o software com as bases de vulnerabilidades conhecidas (CVE).
- Saber o que está instalado é o primeiro passo de qualquer correção: não se corrige o que não se vê.

## No SecVision

**Menu:** Detetar › SOC › Wazuh Explorer

No Wazuh Explorer escolhe-se o agente, aqui a base de dados 003, e os dados de todos os separadores carregam de uma vez. Ao lado do agente aparece o sistema do catálogo a que está associado, e um clique leva até ele.

```{figure} /_static/capturas/wazuh-explorer/agente-1.jpg
:alt: Detetar › SOC › Wazuh Explorer

O ecrã em Detetar › SOC › Wazuh Explorer (1 de 2).
```

1. Escolha **003** em **agente-sem-sistema (ID: 004) — active — 172.20.0.7**.
2. Clique em **Visão Geral**.

```{figure} /_static/capturas/wazuh-explorer/agente-2.jpg
:alt: Detetar › SOC › Wazuh Explorer

O ecrã em Detetar › SOC › Wazuh Explorer (2 de 2).
```

1. **O sistema do catálogo**

**Menu:** Wazuh Explorer › Software

No separador do software, todos os pacotes instalados, com a versão e o fabricante. Pesquisa-se pelo nome: o openssl desta máquina está na versão 3.0.9, uma versão antiga, com vulnerabilidades conhecidas.

Esta versão foi plantada de propósito no ambiente de testes, para haver vulnerabilidades a sério para mostrar. Numa instituição, é exatamente o tipo de pacote esquecido que este separador encontra.

```{figure} /_static/capturas/wazuh-explorer/software-1.jpg
:alt: Wazuh Explorer › Software

O ecrã em Wazuh Explorer › Software (1 de 5).
```

1. Clique em **Software**.

```{figure} /_static/capturas/wazuh-explorer/software-2.jpg
:alt: Wazuh Explorer › Software

O ecrã em Wazuh Explorer › Software (2 de 5).
```

1. Escreva «openssl» no campo **Pesquisar...**.
2. **openssl 3.0.9-1 — a versão instalada**
3. Clique em **Pesquisar...**.

```{figure} /_static/capturas/wazuh-explorer/software-3.jpg
:alt: Wazuh Explorer › Software

O ecrã em Wazuh Explorer › Software (3 de 5).
```

```{figure} /_static/capturas/wazuh-explorer/software-4.jpg
:alt: Wazuh Explorer › Software

O ecrã em Wazuh Explorer › Software (4 de 5).
```

```{figure} /_static/capturas/wazuh-explorer/software-5.jpg
:alt: Wazuh Explorer › Software

O ecrã em Wazuh Explorer › Software (5 de 5).
```

**Menu:** Wazuh Explorer › Processos · Rede · Utilizadores

Os processos que estão a correr, as interfaces e os endereços de rede, e as contas da máquina. Uma conta que ninguém conhece, ou um processo que não devia lá estar, vê-se aqui antes de se ver num incidente.

```{figure} /_static/capturas/wazuh-explorer/maquina-1.jpg
:alt: Wazuh Explorer › Processos · Rede · Utilizadores

O ecrã em Wazuh Explorer › Processos · Rede · Utilizadores (1 de 4).
```

1. Clique em **Processos**.

```{figure} /_static/capturas/wazuh-explorer/maquina-2.jpg
:alt: Wazuh Explorer › Processos · Rede · Utilizadores

O ecrã em Wazuh Explorer › Processos · Rede · Utilizadores (2 de 4).
```

1. Clique em **Rede e Tráfego**.

```{figure} /_static/capturas/wazuh-explorer/maquina-3.jpg
:alt: Wazuh Explorer › Processos · Rede · Utilizadores

O ecrã em Wazuh Explorer › Processos · Rede · Utilizadores (3 de 4).
```

1. Clique em **Utilizadores**.

```{figure} /_static/capturas/wazuh-explorer/maquina-4.jpg
:alt: Wazuh Explorer › Processos · Rede · Utilizadores

O ecrã em Wazuh Explorer › Processos · Rede · Utilizadores (4 de 4).
```

**Menu:** Wazuh Explorer › Vulnerabilidades

E as vulnerabilidades, contadas por gravidade: críticas, altas, médias e baixas, cada uma com a CVE, o pacote afetado e a pontuação de gravidade, o CVSS.

Estas vêm do Indexer do Wazuh, e por isso pedem a morada e as credenciais dele na configuração. Sem o Indexer, a plataforma recorre à API antiga do gestor, que nas versões recentes já não as tem.

```{figure} /_static/capturas/wazuh-explorer/vulns-1.jpg
:alt: Wazuh Explorer › Vulnerabilidades

O ecrã em Wazuh Explorer › Vulnerabilidades (1 de 2).
```

1. Clique em **Vulnerabilidades**.

```{figure} /_static/capturas/wazuh-explorer/vulns-2.jpg
:alt: Wazuh Explorer › Vulnerabilidades

O ecrã em Wazuh Explorer › Vulnerabilidades (2 de 2).
```

1. **Por gravidade, do Indexer**

## No Wazuh

**Menu:** Wazuh › Endpoints › base-de-dados-003

No painel do Wazuh, a mesma máquina tem a sua página: o inventário do sistema, os eventos, o mapa das técnicas de ataque. E, em baixo, as vulnerabilidades por gravidade.

Os números são os mesmos que o SecVision mostrou, porque vêm do mesmo sítio. O SecVision não tem uma cópia a envelhecer: pergunta ao Wazuh cada vez que se abre o ecrã.

```{figure} /_static/capturas/wazuh-explorer/wazuh_agente-1.jpg
:alt: Wazuh › Endpoints › base-de-dados-003

O ecrã em Wazuh › Endpoints › base-de-dados-003 (1 de 2).
```

1. **O mesmo agente, no painel do Wazuh**

```{figure} /_static/capturas/wazuh-explorer/wazuh_agente-2.jpg
:alt: Wazuh › Endpoints › base-de-dados-003

O ecrã em Wazuh › Endpoints › base-de-dados-003 (2 de 2).
```

1. **Os mesmos números**

**Menu:** Wazuh › Vulnerability Detection › Inventory

E o inventário de vulnerabilidades do Wazuh, para quem as trata uma a uma no dia a dia do centro de operações.

```{figure} /_static/capturas/wazuh-explorer/wazuh_vuln-1.jpg
:alt: Wazuh › Vulnerability Detection › Inventory

O ecrã em Wazuh › Vulnerability Detection › Inventory.
```

## Resumo

O Explorer junta, para cada máquina, o que o Wazuh sabe e o que o catálogo sabe.

E não corrige nada: atualizar o openssl desta máquina é trabalho de quem a administra. O que a plataforma dá é a lista certa, para isso acontecer.

**O que a plataforma faz — e o que não faz**

- Mostra, por máquina, o inventário e as vulnerabilidades, ao lado do sistema do catálogo.
- Não guarda cópia: lê o Wazuh quando se abre o ecrã.
- Não corrige nada: a atualização do software é trabalho de quem administra a máquina.

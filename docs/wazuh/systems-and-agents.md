# Associar os sistemas aos agentes

Necessidade de associação entre o catálogo e o Wazuh; associação e desassociação de um agente a um sistema e respetivo efeito no estado (Monitorizado ou GAP) e na fila de integração; e o efeito no Wazuh, onde os agentes não são alterados, uma vez que a associação pertence ao catálogo.

```{video} 504-sistemas-e-agentes
```

O catálogo do SecVision identifica os sistemas da organização, e o Wazuh identifica as máquinas monitorizadas. Esta página descreve a associação entre ambos e os respetivos efeitos.

## Acesso

**Identificar** > **Inventário** > **Catálogo de Segurança**

```{figure} /_static/capturas/wazuh-sistemas/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Catálogo de Segurança

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

Um sistema com agente associado está monitorizado; sem agente, está em GAP. A proporção do âmbito com agente corresponde à cobertura de monitorização, um dos indicadores do painel.

A associação é relevante nos dois sentidos. Um agente não associado a nenhum sistema corresponde a uma máquina desconhecida do catálogo, sem dono nem criticidade atribuídos, o que constitui igualmente uma lacuna.

**Relevância da associação**

- Um sistema com agente associado está Monitorizado; sem agente, está em GAP.
- A cobertura de monitorização corresponde à proporção do âmbito com agente: é um indicador e uma evidência para o auditor.
- Um agente sem sistema corresponde a uma máquina desconhecida do catálogo, o que constitui igualmente uma lacuna.

## No SecVision

**Identificar** > **Catálogo de Segurança**

No catálogo de segurança, a coluna **Wazuh** apresenta o agente de cada sistema. O nome do agente abre a máquina no Explorer.

```{figure} /_static/capturas/wazuh-sistemas/catalogo-1.jpg
:alt: Identificar > Catálogo de Segurança

Ecrã **Identificar** > **Catálogo de Segurança**.
```

1. **Coluna Wazuh:** Agente de cada sistema.

## Desassociação

**Catálogo de Segurança** > **Agente Wazuh**

A associação é gerida nas ações de cada sistema. Neste exemplo, o servidor 002 está associado ao agente com o mesmo nome e a associação é removida, como sucede quando uma máquina é substituída ou reinstalada.

O sistema passa de imediato a GAP, com a data desse momento, a partir da qual são contados os dias em GAP.

```{figure} /_static/capturas/wazuh-sistemas/desassociar-1.jpg
:alt: Catálogo de Segurança > Agente Wazuh

Ecrã **Catálogo de Segurança** > **Agente Wazuh** (1 de 3).
```

1. Clique no ícone de ações do sistema.

```{figure} /_static/capturas/wazuh-sistemas/desassociar-2.jpg
:alt: Catálogo de Segurança > Agente Wazuh

Ecrã **Catálogo de Segurança** > **Agente Wazuh** (2 de 3).
```

1. **Associação atual:** servidor-002 ↔ agente servidor-002.
2. Clique em **Remover associação**.

```{figure} /_static/capturas/wazuh-sistemas/desassociar-3.jpg
:alt: Catálogo de Segurança > Agente Wazuh

Ecrã **Catálogo de Segurança** > **Agente Wazuh** (3 de 3).
```

**Proteger** > **Instalar agente Wazuh**

Na fila de integração, o número de sistemas desprotegidos passa de três para quatro: o servidor 002 é apresentado com zero dias em GAP, a aguardar agente.

```{figure} /_static/capturas/wazuh-sistemas/gap-1.jpg
:alt: Proteger > Instalar agente Wazuh

Ecrã **Proteger** > **Instalar agente Wazuh**.
```

No ecrã, encontra os seguintes elementos:

1. **Sistemas sem monitorização:** Mais um sistema na fila.
2. **Dias em GAP:** Contagem iniciada no momento da desassociação.

## No Wazuh

**Wazuh** > **Endpoints** > **Agents**

No Wazuh, não ocorre qualquer alteração: o agente do servidor 002 continua ativo e a enviar dados. A associação pertence ao catálogo e não ao Wazuh, pelo que a desassociação não desativa nem elimina nada na máquina.

Este ecrã apresenta também a lacuna inversa: o agente sem sistema, ativo no Wazuh e sem registo no catálogo. Este agente deve ser associado a um sistema existente, ou deve ser registado o sistema em falta.

```{figure} /_static/capturas/wazuh-sistemas/wazuh-1.jpg
:alt: Wazuh > Endpoints > Agents

Ecrã **Wazuh** > **Endpoints** > **Agents**.
```

No ecrã, encontra os seguintes elementos:

1. **Agente do servidor 002:** Mantém-se ativo no Wazuh.
2. **Agente sem sistema:** Agente sem registo no catálogo.

## Associação

**Catálogo de Segurança** > **Associar agente Wazuh**

A associação é efetuada na mesma ação. A janela apresenta apenas os agentes ainda sem sistema, para impedir a associação do mesmo agente a dois sistemas.

```{figure} /_static/capturas/wazuh-sistemas/associar-1.jpg
:alt: Catálogo de Segurança > Associar agente Wazuh

Ecrã **Catálogo de Segurança** > **Associar agente Wazuh** (1 de 5).
```

```{figure} /_static/capturas/wazuh-sistemas/associar-2.jpg
:alt: Catálogo de Segurança > Associar agente Wazuh

Ecrã **Catálogo de Segurança** > **Associar agente Wazuh** (2 de 5).
```

1. Clique no ícone de ações do sistema.

```{figure} /_static/capturas/wazuh-sistemas/associar-3.jpg
:alt: Catálogo de Segurança > Associar agente Wazuh

Ecrã **Catálogo de Segurança** > **Associar agente Wazuh** (3 de 5).
```

1. **Agentes disponíveis:** Apenas os agentes ainda sem sistema.
2. Selecione **servidor-002**.

```{figure} /_static/capturas/wazuh-sistemas/associar-4.jpg
:alt: Catálogo de Segurança > Associar agente Wazuh

Ecrã **Catálogo de Segurança** > **Associar agente Wazuh** (4 de 5).
```

1. Clique em **Associar Agente**.

```{figure} /_static/capturas/wazuh-sistemas/associar-5.jpg
:alt: Catálogo de Segurança > Associar agente Wazuh

Ecrã **Catálogo de Segurança** > **Associar agente Wazuh** (5 de 5).
```

**Identificar** > **Catálogo de Segurança**

O servidor 002 volta a estar monitorizado, com o agente indicado na coluna **Wazuh**.

A associação de um agente que já tem sistema é recusada: cada agente corresponde a um único sistema.

```{figure} /_static/capturas/wazuh-sistemas/resultado-1.jpg
:alt: Identificar > Catálogo de Segurança

Ecrã **Identificar** > **Catálogo de Segurança**.
```

1. **Estado:** Monitorizado.

## Resumo

A associação determina o estado de cada sistema, os dias em GAP, a fila de integração e a cobertura de monitorização.

A associação não altera o Wazuh. Para retirar uma máquina da monitorização, é necessário desinstalar o agente; a desassociação altera apenas a informação do catálogo.

**Funcionalidades e limitações**

- Associa cada sistema ao respetivo agente e determina o estado, os dias em GAP e a cobertura.
- Apresenta os agentes por associar, que correspondem a máquinas fora do catálogo.
- Não altera os agentes: a associação e a desassociação afetam apenas o catálogo.

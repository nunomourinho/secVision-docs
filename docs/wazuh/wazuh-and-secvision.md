# O Wazuh e o SecVision

Componentes do Wazuh (agentes, gestor e Indexer) e respetiva utilização pelo SecVision: credenciais, ligação, agentes com os nomes das máquinas, estado do servidor e associação do catálogo de sistemas à monitorização. As gravações foram feitas num Wazuh real, o do ambiente de testes.

```{video} 501-o-wazuh-e-o-secvision
```

Esta é a primeira página do módulo sobre o Wazuh. Descreve o Wazuh, o seu funcionamento interno e a utilização que o SecVision lhe dá: os dados lidos, os ecrãs utilizados e as operações que nunca são executadas automaticamente.

## Acesso

**Detetar** > **SOC** > **Wazuh Explorer**

```{figure} /_static/capturas/wazuh-ligacao/menu.jpg
:alt: Menu lateral: Detetar > SOC > Wazuh Explorer

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Conceito

O Wazuh é uma plataforma de monitorização de segurança de código aberto. Cada máquina executa um agente: um programa que lê os registos do sistema, inventaria o software instalado e monitoriza a configuração.

Os agentes enviam os dados para o gestor, que aplica milhares de regras e determina o que constitui um alerta. Os resultados são guardados no Indexer, uma base de dados de pesquisa: alertas, arquivo de todos os eventos, inventário de cada máquina e vulnerabilidades conhecidas do software instalado.

**Componentes do Wazuh**

Agentes
: programa instalado em cada máquina: registos, inventário de software e configuração

Gestor
: recebe os dados, aplica as regras e determina o que constitui um alerta

Indexer
: guarda os alertas, o arquivo, o inventário e as vulnerabilidades

Painel
: interface do próprio Wazuh, destinada às equipas do centro de operações

```{figure} /_static/img/501-o-wazuh-e-o-secvision/01.jpg
:alt: O que é o Wazuh

Componentes do Wazuh.
```

O SecVision não substitui o Wazuh. Lê a informação do Wazuh e apresenta-a em conjunto com o catálogo: máquinas monitorizadas, software instalado e vulnerabilidades. Esta combinação transforma uma lista de sistemas numa visão do risco.

O SecVision escreve no Wazuh apenas as regras de falso positivo e de deteção, sempre por decisão de um administrador, com cópia de segurança prévia, validação e reversão automática se o gestor não as aceitar. Cada uma destas funcionalidades tem uma página própria neste módulo.

**Utilização do Wazuh pelo SecVision**

- Leitura: agentes, inventário, vulnerabilidades e estado do servidor.
- Associação de cada sistema do catálogo ao respetivo agente; os sistemas sem agente ficam em GAP.
- Pesquisa por software e por CVE, para os relatórios de recomendações.
- Escrita de regras de falso positivo e de deteção, apenas por decisão de um administrador.

## Ligação

A ligação é configurada no Wazuh Explorer, no SecVision, e exige dois endereços: o da API do gestor, utilizado para consultar os agentes e aplicar regras, e o do Indexer, onde se encontram as vulnerabilidades. Cada endereço tem um utilizador e uma palavra-passe próprios.

As palavras-passe são guardadas encriptadas na base de dados e não voltam a ser apresentadas; o campo indica apenas a sua existência. O utilizador da API necessita de permissão de leitura dos agentes e das regras e, para a aplicação de regras, de permissão de escrita e de reinício do gestor.

```{figure} /_static/capturas/wazuh-ligacao/credenciais-1.jpg
:alt: Detetar > SOC > Wazuh Explorer

Ecrã **Detetar** > **SOC** > **Wazuh Explorer** (1 de 2).
```

1. Separador **Configuração da API Wazuh:** Apresenta os campos da ligação.

```{figure} /_static/capturas/wazuh-ligacao/credenciais-2.jpg
:alt: Detetar > SOC > Wazuh Explorer

Ecrã **Detetar** > **SOC** > **Wazuh Explorer** (2 de 2).
```

No ecrã, encontra os seguintes elementos:

1. **API do gestor:** Endereço, utilizador e palavra-passe.
2. **Indexer:** Endereço, utilizador e palavra-passe, para as vulnerabilidades.
3. **Palavra-passe:** Guardada encriptada e não apresentada novamente.

## Agentes

**Wazuh Explorer** > **Ligar ao Wazuh**

O botão **Ligar ao Wazuh** obtém a lista dos agentes. No separador **Explorador API**, é possível consultar diretamente a API do gestor. Neste ambiente de testes, cada máquina Linux do catálogo tem um agente com o respetivo nome (servidor 002, base de dados 003, equipamento de rede 005 e serviço 007) e o sistema operativo correspondente.

Existe também, deliberadamente, um agente sem máquina associada: o agente sem sistema. Representa uma máquina ligada ao Wazuh mas não registada no catálogo, que a plataforma apresenta separadamente.

```{figure} /_static/capturas/wazuh-ligacao/agentes-1.jpg
:alt: Wazuh Explorer > Ligar ao Wazuh

Ecrã **Wazuh Explorer** > **Ligar ao Wazuh** (1 de 5).
```

1. Clique em **Ligar ao Wazuh**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-2.jpg
:alt: Wazuh Explorer > Ligar ao Wazuh

Ecrã **Wazuh Explorer** > **Ligar ao Wazuh** (2 de 5).
```

1. Clique em **Explorador API**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-3.jpg
:alt: Wazuh Explorer > Ligar ao Wazuh

Ecrã **Wazuh Explorer** > **Ligar ao Wazuh** (3 de 5).
```

1. Introduza «/agents?select=name,status,os.name» no campo **/agents?limit=10**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-4.jpg
:alt: Wazuh Explorer > Ligar ao Wazuh

Ecrã **Wazuh Explorer** > **Ligar ao Wazuh** (4 de 5).
```

1. **Agentes:** Um agente por máquina, com o respetivo nome.

```{figure} /_static/capturas/wazuh-ligacao/agentes_wazuh-1.jpg
:alt: Wazuh Explorer > Ligar ao Wazuh

Ecrã **Wazuh Explorer** > **Ligar ao Wazuh** (5 de 5).
```

**Wazuh** > **Endpoints** > **Agents**

No painel do Wazuh, são apresentados os mesmos agentes, com o mesmo nome, endereço e sistema operativo, todos ativos. A base de dados 003 é um Debian 12, conforme indicado no catálogo do SecVision.

O SecVision não guarda uma cópia destes dados: consulta o Wazuh em cada pedido, pelo que a informação é idêntica nos dois sistemas.

```{figure} /_static/capturas/wazuh-ligacao/agentes_wazuh-1.jpg
:alt: Wazuh > Endpoints > Agents

Ecrã **Wazuh** > **Endpoints** > **Agents**.
```

No ecrã, encontra os seguintes elementos:

1. **Agentes no painel do Wazuh:** Os mesmos agentes apresentados no SecVision.
2. **base-de-dados-003:** Debian 12.

## Servidor

**Wazuh Explorer** > **Servidor Wazuh**

O separador do servidor apresenta a versão do gestor e o estado de cada serviço. Neste exemplo, o indicador de saúde está a vermelho: seis dos dezasseis serviços estão parados. Um serviço parado é o primeiro elemento a verificar quando os alertas deixam de ser recebidos.

Os seis serviços parados correspondem a funções não utilizadas nesta instalação: envio de alertas por correio, syslog, integrações, relatórios, cluster e monitorização sem agente. Em **Configurar monitorização**, estes serviços são excluídos da contagem, e o indicador passa a verde. Esta lista é verificada pela plataforma quando aplica uma regra e o gestor é reiniciado.

**Como excluir serviços da monitorização:** Siga os passos indicados nas capturas seguintes.

```{figure} /_static/capturas/wazuh-ligacao/servidor-1.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (1 de 12).
```

1. Clique em **Servidor Wazuh**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-2.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (2 de 12).
```

```{figure} /_static/capturas/wazuh-ligacao/servidor-3.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (3 de 12).
```

1. Clique em **Configurar monitorização**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-4.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (4 de 12).
```

1. Clique em **wazuh-agentlessd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-5.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (5 de 12).
```

1. Clique em **wazuh-csyslogd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-6.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (6 de 12).
```

1. Clique em **wazuh-integratord**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-7.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (7 de 12).
```

1. Clique em **wazuh-maild**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-8.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (8 de 12).
```

1. Clique em **wazuh-reportd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-9.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (9 de 12).
```

1. Clique em **wazuh-clusterd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-10.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (10 de 12).
```

1. Clique em **Guardar**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-11.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (11 de 12).
```

```{figure} /_static/capturas/wazuh-ligacao/servidor-12.jpg
:alt: Wazuh Explorer > Servidor Wazuh

Ecrã **Wazuh Explorer** > **Servidor Wazuh** (12 de 12).
```

## Catálogo

**Identificar** > **Sistemas**

O catálogo de sistemas apresenta o resultado: as máquinas com agente estão monitorizadas, com o nome do agente indicado. As máquinas Windows deste ambiente não têm agente e estão em GAP (incluídas no âmbito, mas sem monitorização).

A associação é feita neste ecrã, sistema a sistema, e pode ser desfeita. A desassociação de um agente coloca o sistema em GAP com a data desse momento, a partir da qual são contados os dias em GAP na fila de integração.

```{figure} /_static/capturas/wazuh-ligacao/sistemas-1.jpg
:alt: Identificar > Sistemas

Ecrã **Identificar** > **Sistemas** (1 de 2).
```

```{figure} /_static/capturas/wazuh-ligacao/sistemas-2.jpg
:alt: Identificar > Sistemas

Ecrã **Identificar** > **Sistemas** (2 de 2).
```

No ecrã, encontra os seguintes elementos:

1. **Agente:** Agente associado a cada sistema.
2. **Estado:** Monitorizado ou GAP.

## Ambiente de testes

Todos os dados apresentados são reais. O ambiente de testes dispõe de um Wazuh próprio, instalado automaticamente na criação do ambiente, sempre na versão mais recente publicada. Os agentes são máquinas reais, com software e vulnerabilidades reais.

O ambiente de testes comunica exclusivamente com este Wazuh. Se for introduzido o endereço do Wazuh de produção, a plataforma recusa a ligação antes de a estabelecer, para que uma regra de ensaio nunca reinicie o gestor de produção.

**O Wazuh do ambiente de testes**

- Um Wazuh real, em Docker, sempre na versão mais recente publicada.
- Um agente por cada máquina Linux do catálogo, com o nome e o sistema indicados no catálogo.
- O ambiente de testes comunica exclusivamente com este Wazuh; a ligação ao de produção é recusada.

## Resumo

No âmbito da conformidade, esta funcionalidade responde à medida de registos e monitorização do Anexo IV: a plataforma demonstra, com dados, os sistemas monitorizados e os não monitorizados.

A plataforma não instala agentes (gera os scripts, executados por um operador) e não substitui o painel do Wazuh nem o trabalho de análise diária dos alertas.

**Funcionalidades e limitações**

- No Anexo IV, responde à medida de registos e monitorização (T.RAR): identifica os sistemas monitorizados e os não monitorizados.
- Não instala agentes: gera os scripts, executados por um operador.
- Não substitui o painel do Wazuh nem o trabalho de análise dos alertas.

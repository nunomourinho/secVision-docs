# O Wazuh e o SecVision

O que é o Wazuh — agentes, gestor, Indexer — e o que o SecVision faz com ele: as credenciais, a ligação, os agentes com os nomes das máquinas, o estado do servidor, e o catálogo de sistemas ligado à monitorização. Gravado num Wazuh a sério, o do ambiente de testes.

```{video} 501-o-wazuh-e-o-secvision
```

Este é o primeiro página do módulo sobre o Wazuh. Vamos ver o que é, como funciona por dentro, e o que o SecVision faz com ele: que dados lê, que ecrãs usa, e o que nunca faz sozinho.

## Onde fica no menu

**Menu:** Detetar › Soc › Wazuh Explorer

```{figure} /_static/capturas/wazuh-ligacao/menu.jpg
:alt: Menu lateral: Detetar › Soc › Wazuh Explorer

O caminho no menu lateral: Detetar › Soc › Wazuh Explorer.
```

1. No menu lateral, abra **Detetar**.
2. Dentro dele, abra **Soc**.
3. Clique em **Wazuh Explorer**: abre o ecrã desta página.

## O conceito

O Wazuh é uma plataforma de monitorização de segurança, de código aberto. Em cada máquina corre um agente: um programa pequeno que lê os registos do sistema, faz o inventário do software instalado e vigia a configuração.

Os agentes enviam tudo para o gestor. O gestor aplica milhares de regras, e é ele que decide o que é um alerta. O que sai fica no Indexer, uma base de dados de pesquisa: os alertas, os arquivos de todos os eventos, o inventário de cada máquina e as vulnerabilidades conhecidas do software que lá está.

**O que é o Wazuh**

Agentes
: um programa pequeno em cada máquina — registos, inventário de software, configuração

Gestor
: recebe tudo, aplica as regras e decide o que é um alerta

Indexer
: guarda os alertas, os arquivos, o inventário e as vulnerabilidades

Painel
: o ecrã do próprio Wazuh, para quem trabalha no centro de operações

```{figure} /_static/img/501-o-wazuh-e-o-secvision/01.jpg
:alt: O que é o Wazuh

O que é o Wazuh.
```

O SecVision não substitui o Wazuh. Lê o que ele sabe e põe-no ao lado do catálogo: que máquinas estão monitorizadas, que software têm, que vulnerabilidades. É isso que transforma uma lista de sistemas numa visão do risco.

E há uma coisa que escreve: as regras de falso positivo e de deteção. Escreve-as só quando um administrador manda, com cópia de segurança antes, validação, e reversão automática se o gestor não as aceitar. Cada uma destas partes tem o seu página neste módulo.

**O que o SecVision faz com o Wazuh**

- Lê: os agentes, o inventário, as vulnerabilidades e o estado do servidor.
- Liga cada sistema do catálogo ao seu agente — e o que não tem agente fica em GAP.
- Pesquisa por software e por CVE, para os relatórios de recomendações.
- Escreve regras de falso positivo e de deteção, só quando um administrador manda.

## A ligação

**Menu:** Detetar › SOC › Wazuh Explorer

A ligação faz-se no Wazuh Explorer, do lado do SecVision. Pede duas moradas: a da API do gestor, por onde se pergunta pelos agentes e se aplicam regras, e a do Indexer, onde estão as vulnerabilidades. Cada uma com o seu utilizador e palavra-passe.

As palavras-passe ficam cifradas na base de dados, e nunca voltam ao ecrã: o campo mostra só que existe uma. O utilizador da API precisa de poder ler os agentes e as regras; para aplicar regras, também de as escrever e de reiniciar o gestor.

```{figure} /_static/capturas/wazuh-ligacao/credenciais-1.jpg
:alt: Detetar › SOC › Wazuh Explorer

O ecrã em Detetar › SOC › Wazuh Explorer (1 de 2).
```

1. Clique em **Configuração da API Wazuh**.

```{figure} /_static/capturas/wazuh-ligacao/credenciais-2.jpg
:alt: Detetar › SOC › Wazuh Explorer

O ecrã em Detetar › SOC › Wazuh Explorer (2 de 2).
```

1. **API do gestor**
2. **Indexer — as vulnerabilidades**
3. **Cifrada — nunca volta ao ecrã**

## Os agentes

**Menu:** Wazuh Explorer › Ligar ao Wazuh

Ligar ao Wazuh traz a lista dos agentes. No separador Explorador API pode perguntar-se à API do gestor diretamente, e a resposta mostra-os todos: neste ambiente de testes, cada máquina Linux do catálogo tem um agente com o nome dela, o servidor 002, a base de dados 003, o equipamento de rede 005 e o serviço 007, e o sistema operativo que cada uma corre.

E há um agente sem máquina nenhuma, de propósito: o agente sem sistema. É o caso de uma máquina que alguém ligou ao Wazuh e que ninguém registou no catálogo, e a plataforma tem de o mostrar à parte.

```{figure} /_static/capturas/wazuh-ligacao/agentes-1.jpg
:alt: Wazuh Explorer › Ligar ao Wazuh

O ecrã em Wazuh Explorer › Ligar ao Wazuh (1 de 5).
```

1. Clique em **Ligar ao Wazuh**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-2.jpg
:alt: Wazuh Explorer › Ligar ao Wazuh

O ecrã em Wazuh Explorer › Ligar ao Wazuh (2 de 5).
```

1. Clique em **Explorador API**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-3.jpg
:alt: Wazuh Explorer › Ligar ao Wazuh

O ecrã em Wazuh Explorer › Ligar ao Wazuh (3 de 5).
```

1. Escreva «/agents?select=name,status,os.name» no campo **/agents?limit=10**.

```{figure} /_static/capturas/wazuh-ligacao/agentes-4.jpg
:alt: Wazuh Explorer › Ligar ao Wazuh

O ecrã em Wazuh Explorer › Ligar ao Wazuh (4 de 5).
```

1. **Um agente por máquina, com o nome dela**

```{figure} /_static/capturas/wazuh-ligacao/agentes_wazuh-1.jpg
:alt: Wazuh Explorer › Ligar ao Wazuh

O ecrã em Wazuh Explorer › Ligar ao Wazuh (5 de 5).
```

1. **Os mesmos agentes, no painel do Wazuh**
2. **base-de-dados-003 — Debian 12**

**Menu:** Wazuh › Endpoints › Agents

E do lado do Wazuh, no painel dele, os mesmos agentes: o mesmo nome, o mesmo endereço, o mesmo sistema operativo, e ativos. A base de dados 003 é um Debian 12, tal como o catálogo do SecVision diz.

O SecVision não guarda uma cópia destes dados: pergunta ao Wazuh de cada vez. O que um mostra, o outro mostra também.

```{figure} /_static/capturas/wazuh-ligacao/agentes_wazuh-1.jpg
:alt: Wazuh › Endpoints › Agents

O ecrã em Wazuh › Endpoints › Agents.
```

1. **Os mesmos agentes, no painel do Wazuh**
2. **base-de-dados-003 — Debian 12**

## O servidor

**Menu:** Wazuh Explorer › Servidor Wazuh

O separador do servidor mostra a versão do gestor e o estado de cada um dos seus serviços. Aqui a saúde está a vermelho: seis dos dezasseis serviços estão parados. Um serviço parado é o primeiro sítio onde olhar quando os alertas deixam de chegar.

Mas estes seis são funções que esta instalação não usa: o envio de alertas por correio, o syslog, as integrações, os relatórios, o cluster e a monitorização sem agente. Em Configurar monitorização tiram-se da conta, e a saúde passa a verde. É esta lista que a plataforma confirma quando aplica uma regra e o gestor reinicia.

```{figure} /_static/capturas/wazuh-ligacao/servidor-1.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (1 de 12).
```

1. Clique em **Servidor Wazuh**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-2.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (2 de 12).
```

```{figure} /_static/capturas/wazuh-ligacao/servidor-3.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (3 de 12).
```

1. Clique em **Configurar monitorização**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-4.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (4 de 12).
```

1. Clique em **wazuh-agentlessd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-5.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (5 de 12).
```

1. Clique em **wazuh-csyslogd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-6.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (6 de 12).
```

1. Clique em **wazuh-integratord**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-7.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (7 de 12).
```

1. Clique em **wazuh-maild**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-8.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (8 de 12).
```

1. Clique em **wazuh-reportd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-9.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (9 de 12).
```

1. Clique em **wazuh-clusterd**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-10.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (10 de 12).
```

1. Clique em **Guardar**.

```{figure} /_static/capturas/wazuh-ligacao/servidor-11.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (11 de 12).
```

```{figure} /_static/capturas/wazuh-ligacao/servidor-12.jpg
:alt: Wazuh Explorer › Servidor Wazuh

O ecrã em Wazuh Explorer › Servidor Wazuh (12 de 12).
```

## O catálogo

**Menu:** Identificar › Sistemas

No catálogo de sistemas vê-se o resultado. As máquinas com agente estão monitorizadas, com o nome do agente ao lado. As máquinas Windows deste ambiente não têm agente, e estão em GAP: em âmbito, mas sem monitorização.

A associação faz-se aqui, sistema a sistema, ou desfaz-se. Desassociar um agente põe o sistema em GAP com a data desse momento, e é essa data que conta os dias em GAP na fila de integração.

```{figure} /_static/capturas/wazuh-ligacao/sistemas-1.jpg
:alt: Identificar › Sistemas

O ecrã em Identificar › Sistemas (1 de 2).
```

```{figure} /_static/capturas/wazuh-ligacao/sistemas-2.jpg
:alt: Identificar › Sistemas

O ecrã em Identificar › Sistemas (2 de 2).
```

1. **O agente de cada sistema**
2. **Monitorizado ou GAP**

## O ambiente de testes

Tudo o que vimos é real. O ambiente de testes tem um Wazuh próprio, instalado sozinho quando se cria o ambiente, sempre na última versão publicada. Os agentes são máquinas a sério, com software a sério, e vulnerabilidades a sério.

E o ambiente de testes fala com este Wazuh e com mais nenhum. Se alguém lá escrever a morada do Wazuh de produção, a plataforma recusa antes de abrir a ligação, para uma regra de ensaio nunca reiniciar o gestor verdadeiro.

**O Wazuh do ambiente de testes**

- Um Wazuh a sério, em Docker, sempre na última versão publicada.
- Um agente por cada máquina Linux do catálogo, com o nome e o sistema que o catálogo diz.
- O ambiente de testes fala com este Wazuh e com mais nenhum: o de produção é recusado.

## Resumo

Na conformidade, isto serve a medida de registos e monitorização do Anexo IV: a plataforma mostra, com factos, que sistemas estão monitorizados e quais não estão.

E com honestidade, o que não faz: não instala agentes, gera os scripts e quem os corre é uma pessoa; e não substitui o painel do Wazuh, nem quem analisa os alertas no dia a dia.

**O que a plataforma faz — e o que não faz**

- No Anexo IV, serve a medida de registos e monitorização (T.RAR): mostra o que está monitorizado e o que não está.
- Não instala agentes: gera os scripts, e quem os corre é uma pessoa.
- Não substitui o painel do Wazuh, nem o trabalho de quem analisa os alertas.

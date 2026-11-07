# Fechar os GAP e ver o que está exposto

A fila de integração dos sistemas em GAP e o gerador dos scripts do agente de monitorização; e a superfície exposta, por fora e por dentro, com as vulnerabilidades em exploração e os equipamentos fora do catálogo.

```{video} 332-agentes-e-superficie
```

No página do catálogo vimos os sistemas em GAP: em âmbito, mas sem monitorização. Nesta página vemos como se fecham, e como se descobre o que está exposto, por fora e por dentro.

## Onde fica no menu

**Menu:** Proteger › Instalar agente wazuh › Instalar agente Wazuh

```{figure} /_static/capturas/agentes-superficie/menu.jpg
:alt: Menu lateral: Proteger › Instalar agente wazuh › Instalar agente Wazuh

O caminho no menu lateral: Proteger › Instalar agente wazuh › Instalar agente Wazuh.
```

1. No menu lateral, abra **Proteger**.
2. Dentro dele, abra **Instalar agente wazuh**.
3. Clique em **Instalar agente Wazuh**: abre o ecrã desta página.

## A fila

**Menu:** Proteger › Instalar agente Wazuh

No menu Proteger, Instalar agente Wazuh — o Wazuh é a plataforma de monitorização de segurança de código aberto que o SecVision usa. A fila de integração não se ordena à mão: primeiro a criticidade, depois a exposição, depois os dias em GAP. Um sistema crítico exposto à Internet vem antes de um operacional interno.

```{figure} /_static/capturas/agentes-superficie/abrir-1.jpg
:alt: Proteger › Instalar agente Wazuh

O ecrã em Proteger › Instalar agente Wazuh.
```

1. **Criticidade, exposição, dias em GAP**

## O script

**Menu:** Proteger › SOC › Wazuh Agent Builder

O gerador de scripts pede onde está o gestor, os portos e a versão do agente, e as políticas de confiança zero — cada uma com o efeito escrito ao lado. Sai um script por sistema operativo.

A plataforma não instala nada sozinha: gera o script, e quem o corre é uma pessoa, com as credenciais da máquina. Instalado o agente e confirmada a ligação, o sistema passa a monitorizado, e a cobertura sobe.

```{figure} /_static/capturas/agentes-superficie/builder-1.jpg
:alt: Proteger › SOC › Wazuh Agent Builder

O ecrã em Proteger › SOC › Wazuh Agent Builder (1 de 2).
```

```{figure} /_static/capturas/agentes-superficie/builder-2.jpg
:alt: Proteger › SOC › Wazuh Agent Builder

O ecrã em Proteger › SOC › Wazuh Agent Builder (2 de 2).
```

## A superfície

**Menu:** Identificar › Inventário › Superfície Int. e Ext.

A superfície interna mostra o que o varrimento da rede encontrou. Neste ambiente de testes ainda não se varreu nenhuma rede, e o ecrã diz onde se faz: no Inventário de Redes, com o botão do varrimento. Numa instalação real, as portas aparecem classificadas por risco: Telnet, FTP ou VNC são críticos; o acesso remoto ao ambiente de trabalho ou as bases de dados abertas são elevados.

E nos dois ecrãs aparecem os equipamentos fora do catálogo: endereços que respondem e não estão associados a nenhum sistema do catálogo. O botão Catalogar devolve-os ao catálogo, em vez de os deixar numa lista à parte.

```{figure} /_static/capturas/agentes-superficie/superficie-1.jpg
:alt: Identificar › Inventário › Superfície Int. e Ext.

O ecrã em Identificar › Inventário › Superfície Int. e Ext (1 de 2).
```

```{figure} /_static/capturas/agentes-superficie/superficie-2.jpg
:alt: Identificar › Inventário › Superfície Int. e Ext.

O ecrã em Identificar › Inventário › Superfície Int. e Ext (2 de 2).
```

## Resumo

É aqui que o risco ganha factos: quando um sistema tem uma vulnerabilidade em exploração, a probabilidade sugerida no registo de risco sobe ao topo da escala.

E uma nota sobre o ambiente de testes: tem um Wazuh próprio, com um agente em cada máquina Linux do catálogo, e fala com esse e com mais nenhum. O de produção é recusado, para um ensaio nunca lhe tocar. O módulo sobre o Wazuh mostra-o por dentro.

**O que a plataforma faz — e o que não faz**

- No Anexo IV: proteção perimetral (T.PPL), antivírus (T.PPT), registos (T.RAR) — e o inventário dos ativos acessíveis pela Internet.
- A probabilidade sugerida no registo de risco sobe ao topo quando um sistema tem uma vulnerabilidade em exploração.
- No ambiente de testes, a plataforma fala com um Wazuh próprio, de testes, e recusa o de produção.

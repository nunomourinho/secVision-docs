# Correção dos GAP e superfície exposta

A fila de integração dos sistemas em GAP e o gerador de scripts do agente de monitorização; a superfície exposta, externa e interna, com as vulnerabilidades em exploração e os equipamentos fora do catálogo.

```{video} 332-agentes-e-superficie
```

A página do catálogo apresenta os sistemas em GAP: incluídos no âmbito, mas sem monitorização. Esta página descreve a correção dessas lacunas e a identificação da superfície exposta, externa e interna.

## Acesso

**Proteger** > **Instalar agente Wazuh**

```{figure} /_static/capturas/agentes-superficie/menu.jpg
:alt: Menu lateral: Proteger > Instalar agente Wazuh

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Fila de integração

O Wazuh é a plataforma de monitorização de segurança de código aberto utilizada pelo SecVision. A fila de integração é ordenada automaticamente pela criticidade, pela exposição e pelos dias em GAP: um sistema crítico exposto à Internet precede um sistema operacional interno.

```{figure} /_static/capturas/agentes-superficie/abrir-1.jpg
:alt: Proteger > Instalar agente Wazuh

Ecrã **Proteger** > **Instalar agente Wazuh**.
```

1. **Ordenação:** Criticidade, exposição e dias em GAP.

## Gerador de scripts

**Proteger** > **SOC** > **Wazuh Agent Builder**

O gerador de scripts solicita a localização do gestor, as portas, a versão do agente e as políticas de confiança zero, cada uma com o respetivo efeito descrito. É gerado um script por sistema operativo.

A plataforma não instala o agente: gera o script, que é executado por um operador com as credenciais da máquina. Após a instalação do agente e a confirmação da ligação, o sistema passa a monitorizado e a cobertura aumenta.

```{figure} /_static/capturas/agentes-superficie/builder-1.jpg
:alt: Proteger > SOC > Wazuh Agent Builder

Ecrã **Proteger** > **SOC** > **Wazuh Agent Builder** (1 de 2).
```

```{figure} /_static/capturas/agentes-superficie/builder-2.jpg
:alt: Proteger > SOC > Wazuh Agent Builder

Ecrã **Proteger** > **SOC** > **Wazuh Agent Builder** (2 de 2).
```

## Superfície exposta

**Identificar** > **Inventário** > **Superfície Int. e Ext.**

A superfície interna apresenta os resultados do varrimento da rede. Neste ambiente de testes, nenhuma rede foi ainda varrida, e o ecrã indica o local onde o varrimento é iniciado: o Inventário de Redes, com o botão do varrimento. Numa instalação real, as portas são classificadas por risco: Telnet, FTP ou VNC são críticas; o acesso remoto ao ambiente de trabalho ou as bases de dados expostas são elevados.

Os dois ecrãs apresentam também os equipamentos fora do catálogo: endereços ativos não associados a nenhum sistema do catálogo. O botão **Catalogar** integra-os no catálogo.

```{figure} /_static/capturas/agentes-superficie/superficie-1.jpg
:alt: Identificar > Inventário > Superfície Int. e Ext.

Ecrã **Identificar** > **Inventário** > **Superfície Int. e Ext.** (1 de 2).
```

```{figure} /_static/capturas/agentes-superficie/superficie-2.jpg
:alt: Identificar > Inventário > Superfície Int. e Ext.

Ecrã **Identificar** > **Inventário** > **Superfície Int. e Ext.** (2 de 2).
```

## Resumo

Estes dados fundamentam a apreciação do risco: quando um sistema tem uma vulnerabilidade em exploração, a probabilidade sugerida no registo de risco passa para o nível máximo da escala.

O ambiente de testes dispõe de um Wazuh próprio, com um agente em cada máquina Linux do catálogo, e comunica exclusivamente com este. A ligação ao Wazuh de produção é recusada, para impedir que um ensaio o afete. O módulo sobre o Wazuh descreve-o em detalhe.

**Funcionalidades e limitações**

- No Anexo IV: proteção perimetral (T.PPL), antivírus (T.PPT), registos (T.RAR) e inventário dos ativos acessíveis pela Internet.
- A probabilidade sugerida no registo de risco passa para o nível máximo quando um sistema tem uma vulnerabilidade em exploração.
- No ambiente de testes, a plataforma comunica com um Wazuh de testes próprio e recusa a ligação ao de produção.

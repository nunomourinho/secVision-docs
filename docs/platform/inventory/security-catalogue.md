# O catálogo de segurança e a cobertura

Os sistemas operados pela instituição, com o nível de criticidade (N1 a N4), a inclusão no âmbito e o estado de monitorização, e a taxa de cobertura resultante, apresentada no ponto de situação.

```{video} 313-catalogo-de-seguranca
```

O inventário identifica os equipamentos existentes. O catálogo de segurança identifica os sistemas operados pela instituição, o respetivo nível de criticidade e o estado da monitorização de segurança, a partir dos quais é calculada a cobertura.

## Acesso

**Identificar** > **Inventário** > **Catálogo de Segurança**

```{figure} /_static/capturas/catalogo/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Catálogo de Segurança

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Níveis

Cada sistema tem um nível: N1 crítico, N2 estratégico, N3 operacional e N4 secundário. A cobertura considera os três primeiros níveis; o N4 está excluído por omissão.

Cada sistema está monitorizado ou em GAP (incluído no âmbito, mas sem monitorização de segurança ativa). Os dias em GAP são calculados desde a transição, no momento da consulta, e não são gravados.

**Os quatro níveis**

| Nível | Significado | Incluído na cobertura |
|---|---|---|
| N1 | crítico: a sua falha interrompe a missão | sim |
| N2 | estratégico | sim |
| N3 | operacional | sim |
| N4 | secundário | não, por omissão |

```{tip}
A exclusão do N4 é configurada em **Administração** > **Cobertura**. Um sistema em GAP é um sistema incluído no âmbito sem monitorização ativa.
```

## Catálogo

```{figure} /_static/capturas/catalogo/abrir-1.jpg
:alt: Identificar > Inventário > Catálogo de Segurança

Ecrã **Identificar** > **Inventário** > **Catálogo de Segurança**.
```

No ecrã, encontra os seguintes filtros, a par do filtro por rede:

1. **Nível:** De N1 a N4.
2. **Estado:** Monitorizado ou GAP.
3. **Ativo de informação:** Sistemas com ou sem ativo de informação associado.

Um sistema sem ativo de informação associado é apresentado a âmbar. Esta indicação não significa risco nulo, mas sim que o risco da informação que suporta ainda não foi apreciado. Este tema é descrito na página seguinte.

## Ponto de situação

**Identificar** > **Inventário** > **Visão Geral**

A Visão Geral apresenta o resumo desta fase em quatro indicadores: sistemas no âmbito, sistemas monitorizados, sistemas em GAP e taxa de cobertura global. São também apresentadas a cobertura por camada (N1 a N4) e os sistemas em GAP por sistema operativo e por tipo.

Esta informação permite, por exemplo, identificar que os sistemas em GAP são servidores do mesmo tipo, que podem ser corrigidos da mesma forma. Enquanto existirem sistemas em GAP, é apresentado um aviso com ligação ao ecrã de instalação do agente de monitorização.

```{figure} /_static/capturas/catalogo/dashboard-1.jpg
:alt: Identificar > Inventário > Visão Geral

Ecrã **Identificar** > **Inventário** > **Visão Geral** (1 de 2).
```

1. **Aviso de sistemas em GAP:** Ligação direta ao instalador do agente.

```{figure} /_static/capturas/catalogo/dashboard-2.jpg
:alt: Identificar > Inventário > Visão Geral

Ecrã **Identificar** > **Inventário** > **Visão Geral** (2 de 2).
```

## Resumo

O nível de cada sistema é uma decisão de negócio e não técnica, pelo que deve ser definido com a direção e os donos dos serviços. A identificação dos sistemas monitorizados deve ser solicitada à equipa de informática.

A taxa de cobertura indica sempre, em rodapé, os níveis excluídos, uma vez que uma taxa sem o denominador visível não é adequada para apresentação.

**Informação a solicitar e funcionalidades**

- Direção e donos dos serviços: nível de cada sistema, uma decisão de negócio e não técnica.
- Equipa de informática: sistemas com monitorização de segurança ativa.
- A taxa indica sempre os níveis excluídos: uma taxa sem o denominador visível não é adequada para apresentação.

# Consultar o parque

O inventário de ativos e as respetivas fontes, os filtros, o abate de um equipamento sem eliminação de dados e o inventário de redes.

```{video} 312-ver-o-parque
```

Após a importação, o parque deve ser verificado. Esta página descreve o inventário de ativos, a origem de cada equipamento, o abate de equipamentos retirados e o inventário de redes.

## Acesso

**Identificar** > **Inventário** > **Inventário de Ativos**

```{figure} /_static/capturas/parque/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Inventário de Ativos

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Inventário de ativos

Os separadores do topo apresentam cada fonte: o navegador do Active Directory, o do DNS e o gestor do DHCP. Existem ainda dois separadores do diretório: o estado atual do servidor e o registo da última leitura, incluindo os equipamentos removidos do domínio.

Os separadores diferem no momento de referência: o primeiro apresenta a última importação, o segundo o diretório no momento da consulta e o terceiro as alterações desde a última leitura. Este último permite identificar os equipamentos retirados do parque.

```{figure} /_static/capturas/parque/abrir-1.jpg
:alt: Identificar > Inventário > Inventário de Ativos

Ecrã **Identificar** > **Inventário** > **Inventário de Ativos** (1 de 3).
```

No ecrã, encontra os seguintes elementos:

1. **Separadores das fontes:** Cada fonte é apresentada num separador próprio.
2. Separador **Diretório (registo):** Apresenta o registo da última leitura do diretório.

```{figure} /_static/capturas/parque/abrir-2.jpg
:alt: Identificar > Inventário > Inventário de Ativos

Ecrã **Identificar** > **Inventário** > **Inventário de Ativos** (2 de 3).
```

1. Filtro **Todos:** Apresenta todos os registos.

```{figure} /_static/capturas/parque/abrir-3.jpg
:alt: Identificar > Inventário > Inventário de Ativos

Ecrã **Identificar** > **Inventário** > **Inventário de Ativos** (3 de 3).
```

```{figure} /_static/capturas/parque/filtros-1.jpg
:alt: Filtros — e a baixa de um equipamento

Filtros e abate de um equipamento.
```

No ecrã, encontra os seguintes elementos:

1. **Procurar:** Pesquisa por nome, sistema operativo, estado, fonte, rede e tempo desde a última deteção do equipamento.
2. Filtro **Baixa:** Apresenta apenas os equipamentos em serviço, inclui os abatidos ou apresenta apenas estes.

O abate de um equipamento não elimina dados: o registo, as ligações e os instantâneos datados são mantidos. Os endereços de um equipamento abatido deixam de ser considerados da instituição; se forem detetados noutro equipamento, a plataforma emite um novo alerta.

## Redes

**Identificar** > **Inventário** > **Inventário de Redes**

O Inventário de Redes regista cada rede: VLAN, nome, intervalo de endereços e notas. A Ficha da organização obtém deste inventário as gamas de endereços IP, e o varrimento da rede, descrito na página da superfície interna, utiliza-o como ponto de partida.

```{figure} /_static/capturas/parque/redes-1.jpg
:alt: Identificar > Inventário > Inventário de Redes

Ecrã **Identificar** > **Inventário** > **Inventário de Redes**.
```

1. **Gamas de endereços:** Intervalos de endereços de cada rede.

## Resumo

Solicite à equipa de informática o mapa das redes e a lista dos equipamentos retirados. A plataforma guarda a evidência de cada abate, e o número total de equipamentos dos indicadores não se altera com um abate, uma vez que constitui evidência datada.

**Informação a solicitar e funcionalidades**

- Equipa de informática: redes, com VLAN e intervalos, e equipamentos retirados do parque.
- O inventário reflete as fontes: as correções são feitas na origem, seguidas de nova importação.
- O abate preserva a evidência; o número total de equipamentos dos indicadores não se altera.

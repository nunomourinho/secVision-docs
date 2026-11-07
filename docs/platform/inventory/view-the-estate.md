# Ver o parque

O inventário de ativos e as suas fontes, os filtros, a baixa de um equipamento sem apagar nada, e o inventário de redes.

```{video} 312-ver-o-parque
```

Com o parque importado, é altura de o conferir. Nesta página vemos o inventário de ativos, as fontes de onde cada equipamento veio, como se dá baixa de um equipamento que saiu, e o inventário de redes.

## Onde fica no menu

**Menu:** Identificar › Inventário › Inventário de Ativos

```{figure} /_static/capturas/parque/menu.jpg
:alt: Menu lateral: Identificar › Inventário › Inventário de Ativos

O caminho no menu lateral: Identificar › Inventário › Inventário de Ativos.
```

1. No menu lateral, abra **Identificar**.
2. Dentro dele, abra **Inventário**.
3. Clique em **Inventário de Ativos**: abre o ecrã desta página.

## O inventário

**Menu:** Identificar › Inventário › Inventário de Ativos

No menu Identificar, Inventário, Inventário de Ativos. Os separadores do topo mostram cada fonte: o navegador do Active Directory, o do DNS, o gestor do DHCP. E dois separadores do diretório: o que o servidor diz agora, e o que ficou registado da última leitura — incluindo o que desapareceu do domínio.

A diferença entre eles é o tempo. Um mostra a última importação; outro, o diretório neste momento; o terceiro, o que mudou desde a última leitura. É neste que se dá por uma máquina que saiu do parque.

```{figure} /_static/capturas/parque/abrir-1.jpg
:alt: Identificar › Inventário › Inventário de Ativos

O ecrã em Identificar › Inventário › Inventário de Ativos (1 de 3).
```

1. **Cada fonte, no seu separador**
2. Clique em **Diretório (registo)**.

```{figure} /_static/capturas/parque/abrir-2.jpg
:alt: Identificar › Inventário › Inventário de Ativos

O ecrã em Identificar › Inventário › Inventário de Ativos (2 de 3).
```

1. Clique em **Todos**.

```{figure} /_static/capturas/parque/abrir-3.jpg
:alt: Identificar › Inventário › Inventário de Ativos

O ecrã em Identificar › Inventário › Inventário de Ativos (3 de 3).
```

Os filtros procuram por nome, sistema operativo, estado, fonte, rede, e há quanto tempo não se vê o equipamento. O filtro Baixa escolhe entre ver só o que está em serviço, incluir os abatidos, ou só esses.

Dar baixa não apaga nada: a linha fica, as ligações ficam, os instantâneos datados ficam. E os endereços de um equipamento abatido deixam de ser tratados como sendo da instituição: se aparecerem noutras mãos, a plataforma volta a avisar.

```{figure} /_static/capturas/parque/filtros-1.jpg
:alt: Filtros — e a baixa de um equipamento

Filtros — e a baixa de um equipamento.
```

1. **Procurar**
2. **Baixa — em serviço, abatidos, ou todos**

## As redes

**Menu:** Identificar › Inventário › Inventário de Redes

O Inventário de Redes regista cada rede: a VLAN, o nome, o intervalo de endereços e notas. É daqui que a Ficha da organização vai buscar as gamas de endereços IP, e é daqui que parte o varrimento da rede, que vemos mais à frente, na superfície interna.

```{figure} /_static/capturas/parque/redes-1.jpg
:alt: Identificar › Inventário › Inventário de Redes

O ecrã em Identificar › Inventário › Inventário de Redes.
```

1. **As gamas de endereços**

## Resumo

Peça à informática o mapa das redes, e a lista dos equipamentos que saíram. A plataforma guarda a prova de cada baixa; e o número total de equipamentos dos indicadores não muda com uma baixa, porque é prova datada.

**O que pedir a quem — e o que a plataforma faz**

- À informática: as redes, com VLAN e intervalos, e os equipamentos que saíram do parque.
- O inventário é um espelho das fontes: corrige-se na origem e reimporta-se.
- A baixa guarda a prova; o número total de equipamentos dos indicadores não muda.

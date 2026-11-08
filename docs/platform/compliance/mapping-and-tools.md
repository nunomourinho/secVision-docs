# Mapeamento entre referenciais e cobertura por ferramenta

Contabilização de um controlo cumprido numa norma para outra norma, por herança através de mapeamento confirmado, e identificação das ferramentas que cobrem cada controlo, numa leitura inversa às tabelas das normas.

```{video} 321-mapeamento-e-ferramentas
```

Com várias normas no âmbito, o mesmo requisito repete-se; por exemplo, a gestão de acessos consta do Anexo IV, do QNRCS e da ISO 27001. Esta página descreve como um controlo implementado uma vez é contabilizado em várias normas, e as ferramentas que suportam cada controlo.

## Acesso

**Governar** > **GRC — Conformidade** > **Mapeamento entre referenciais**

```{figure} /_static/capturas/mapeamento-ferramentas/menu.jpg
:alt: Menu lateral: Governar > GRC — Conformidade > Mapeamento entre referenciais

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Herança de conformidade

Um controlo é considerado implementado se existir um mapeamento confirmado, com cobertura total, para um controlo de outra norma que seja aplicável e esteja implementado.

Esta regra é restritiva: os mapeamentos propostos, as coberturas parciais e as cadeias de dois níveis não geram herança. O estado declarado prevalece sempre sobre a herança.

**Herança de conformidade**

- Um controlo é considerado implementado se existir um mapeamento confirmado, com cobertura total, para um controlo aplicável e implementado noutra norma.
- Não geram herança: mapeamentos propostos ou rejeitados, coberturas parciais e origens não aplicáveis.
- Não existe transitividade: um mapeamento de A para B e de B para C não torna C implementado.
- O estado declarado prevalece sempre; a herança preenche apenas os estados em branco.

## Mapeamento

Os cruzamentos incluídos nas normas são apresentados como propostas por confirmar. Cada proposta pode ser confirmada ou rejeitada, e podem ser adicionados novos mapeamentos, com cobertura total ou parcial.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-1.jpg
:alt: Governar > GRC — Conformidade > Mapeamento entre referenciais

Ecrã **Governar** > **GRC — Conformidade** > **Mapeamento entre referenciais** (1 de 3).
```

1. Separador **Lado a lado:** Apresenta as duas normas em paralelo.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-2.jpg
:alt: Governar > GRC — Conformidade > Mapeamento entre referenciais

Ecrã **Governar** > **GRC — Conformidade** > **Mapeamento entre referenciais** (2 de 3).
```

1. Separador **Referências externas:** Contabiliza as remissões para legislação ainda não incluída na plataforma.

```{figure} /_static/capturas/mapeamento-ferramentas/abrir-3.jpg
:alt: Governar > GRC — Conformidade > Mapeamento entre referenciais

Ecrã **Governar** > **GRC — Conformidade** > **Mapeamento entre referenciais** (3 de 3).
```

## Cobertura por ferramenta

**Governar** > **GRC — Conformidade** > **Cobertura por ferramenta**

Este ecrã apresenta, numa leitura inversa, as tabelas incluídas nas normas: cada controlo indica as ferramentas que o cobrem, e o ecrã agrupa essa informação por ferramenta, com as normas e os controlos cobertos e a percentagem sobre os controlos declarados aplicáveis.

A lista pode ser filtrada por tipo e por licença (código aberto ou comercial) e exportada como relatório para Word ou folha de cálculo, o que é útil antes de uma aquisição.

```{figure} /_static/capturas/mapeamento-ferramentas/ferramentas-1.jpg
:alt: Governar > GRC — Conformidade > Cobertura por ferramenta

Ecrã **Governar** > **GRC — Conformidade** > **Cobertura por ferramenta** (1 de 2).
```

1. Seletor **Universo:** Define as normas de referência da medição: normas no âmbito, normas fora do âmbito ou todas.

```{figure} /_static/capturas/mapeamento-ferramentas/ferramentas-2.jpg
:alt: Governar > GRC — Conformidade > Cobertura por ferramenta

Ecrã **Governar** > **GRC — Conformidade** > **Cobertura por ferramenta** (2 de 2).
```

## Resumo

A plataforma propõe mapeamentos, mas apenas os confirmados são considerados. A herança é calculada no momento da consulta e não é gravada. Relativamente às ferramentas, a plataforma apresenta a cobertura indicada pelas normas e não recomenda marcas.

**Funcionalidades e limitações**

- Propõe os mapeamentos incluídos nas normas; apenas os confirmados são considerados.
- Calcula a herança no momento da consulta, sem a gravar.
- Apresenta a cobertura de cada ferramenta; não recomenda marcas nem substitui uma análise de mercado.

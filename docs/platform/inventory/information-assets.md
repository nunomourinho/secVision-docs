# Ativos de informação

Do servidor à informação: cada ativo com tipo, classificação, confidencialidade, integridade e disponibilidade, dono e sistemas de suporte, e a árvore de contenção.

```{video} 314-ativos-de-informacao
```

Um servidor é um bem; a apreciação de risco incide sobre a informação que suporta (dados dos estudantes, matrículas, vencimentos). Esta página descreve o registo dos ativos de informação, cujo conceito é apresentado em {doc}`/fundamentals/information-and-assets`.

## Acesso

**Identificar** > **Inventário** > **Ativos de informação**

```{figure} /_static/capturas/ativos-informacao/menu.jpg
:alt: Menu lateral: Identificar > Inventário > Ativos de informação

Caminho de acesso no menu lateral. Os números indicam a ordem dos cliques.
```

## Campos

Cada ativo tem um tipo, uma classificação e três valores: confidencialidade, integridade e disponibilidade. Tem também um dono, o responsável do serviço, e os sistemas de suporte; por exemplo, um serviço de correio pode depender de três servidores.

Pode ainda ter um tipo de catálogo: o código MONARC equivalente (um método público de análise de risco), que disponibiliza modelos de ameaças e vulnerabilidades.

**Campos de um ativo**

| Campo | Descrição |
|---|---|
| Tipo | processo, base de dados, aplicação, suporte, pessoa-chave, serviço |
| Classificação | público, interno, confidencial, restrito; no Grupo A, de acordo com o processo de classificação (O.PCF) |
| C, I, A | valor da confidencialidade, da integridade e da disponibilidade |
| Dono | responsável pelo ativo: o responsável do serviço, e não a equipa de informática |
| Sistemas | sistemas do catálogo que suportam o ativo (podem ser vários) |
| Tipo do catálogo | código MONARC equivalente, com modelos de risco |

## Configuração do ecrã

A lista pode ser filtrada por tipo, classificação e grupo. O número de riscos de cada ativo é apresentado na respetiva linha e abre o registo de risco já filtrado.

```{figure} /_static/capturas/ativos-informacao/abrir-1.jpg
:alt: Identificar > Inventário > Ativos de informação

Ecrã **Identificar** > **Inventário** > **Ativos de informação**.
```

Cada ativo tem os botões **Editar**, **Apreciar riscos** e **Contenção**. No ecrã, encontra os seguintes elementos:

1. Botão **Apreciar riscos:** Abre o registo de risco do ativo.
2. Botão **Contenção:** Define os contentores do ativo.

## Árvore de contenção

O separador **Árvore de contenção** apresenta a hierarquia de contenção: campus, edifício, sala, servidor. Um equipamento pode pertencer a vários contentores em simultâneo; por exemplo, uma sala e um circuito elétrico.

Em cada nó, um emblema indica o número de riscos dos contentores superiores ainda não propagados até esse nó. Por exemplo, se a sala tiver risco de inundação, os servidores nela instalados herdam esse risco. A pesquisa não oculta ramos: expande o caminho até ao elemento procurado.

```{figure} /_static/capturas/ativos-informacao/arvore-1.jpg
:alt: A árvore de contenção

A árvore de contenção (1 de 2).
```

1. Separador **Árvore de contenção:** Apresenta a hierarquia de contenção.

```{figure} /_static/capturas/ativos-informacao/arvore-2.jpg
:alt: A árvore de contenção

A árvore de contenção (2 de 2).
```

## Resumo

Solicite a cada responsável de serviço a informação utilizada e o valor das três propriedades, e à equipa de informática os sistemas de suporte. Um sistema sem ativo associado é apresentado a âmbar no catálogo até à apreciação do risco da informação que suporta.

**Informação a solicitar e funcionalidades**

- Responsáveis de serviço: informação utilizada e valor de C, I e A.
- Equipa de informática: sistemas de suporte de cada ativo.
- Um sistema sem ativo associado é apresentado a âmbar no catálogo: risco por apreciar, e não risco nulo.
